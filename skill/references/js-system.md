# JavaScript System Reference

Two scripts for every deck: navigation (slide switching) and edit mode (text editing).
Copy both verbatim into the HTML, after the closing `</div><!-- /deck -->`.

---

## Document Skeleton

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DECK TITLE</title>
  <style>
    /* paste design-system.md CSS here */
    /* paste slide-templates.md CSS snippets here */
    /* paste chart-templates.md animation CSS if using charts */
    /* paste slide deck container CSS from SKILL.md */
  </style>
</head>
<body>

<!-- Fixed chrome -->
<div class="progress" id="progress"></div>
<div class="slide-counter" id="counter">1 / N</div>
<div class="hint" id="hint">
  <span class="key">←</span><span class="key">→</span>
  <span style="margin:0 4px">或</span>
  <span class="key">↑</span><span class="key">↓</span>
  <span style="margin:0 6px">翻页 · 空格下一页</span>
</div>

<!-- Slide deck -->
<div class="deck">
  <section id="hero" data-index="0">…</section>
  <section data-index="1">…</section>
  <!-- more slides -->
</div>

<div class="nav" id="nav"></div>

<!-- Edit mode UI -->
<button class="edit-toggle" id="editToggle" title="切换到编辑模式">⚙</button>
<div class="edit-overlay" id="editOverlay"></div>
<div class="edit-sidebar" id="editSidebar">
  <div class="edit-header">
    <h3>✏️ 编辑模式</h3>
    <button class="edit-close" id="editClose">✕</button>
  </div>
  <div class="edit-body" id="editBody"></div>
  <div class="edit-footer">
    <span class="edit-save-status" id="saveStatus">✓ 自动保存</span>
    <button class="edit-btn edit-btn-primary" id="downloadFile">⬇ 下载 HTML</button>
  </div>
</div>

<script>/* Navigation JS — paste Script 1 here */</script>
<script>/* Edit mode JS — paste Script 2 here */</script>
</body>
</html>
```

---

## Script 1: Navigation System

```javascript
const sections   = Array.from(document.querySelectorAll('[data-index]'));
const total      = sections.length;
const navEl      = document.getElementById('nav');
const progressEl = document.getElementById('progress');
const counterEl  = document.getElementById('counter');
const hintEl     = document.getElementById('hint');
let   current    = 0, locked = false;

// Build nav dots
sections.forEach((_, i) => {
  const d = document.createElement('div');
  d.className = 'nav-dot' + (i === 0 ? ' active' : '');
  d.addEventListener('click', () => goTo(i));
  navEl.appendChild(d);
});
sections[0].classList.add('active');

function updateUI() {
  navEl.querySelectorAll('.nav-dot').forEach((d,i) => d.classList.toggle('active', i===current));
  counterEl.textContent = `${current+1} / ${total}`;
  progressEl.style.width = `${((current+1)/total)*100}%`;
}

function animateIn(idx) {
  const els = sections[idx].querySelectorAll('[data-in]');
  els.forEach(el => el.classList.remove('visible'));
  requestAnimationFrame(() => {
    els.forEach((el,i) => setTimeout(() => el.classList.add('visible'), 80+i*65));
  });
}

function goTo(n) {
  if (n<0||n>=total||n===current||locked) return;
  locked = true;
  const prev=current, dir=n>current?1:-1;
  current = n;
  sections[prev].classList.remove('active');
  if (dir>0) sections[prev].classList.add('prev');
  sections[current].classList.remove('prev');
  sections[current].classList.add('active');
  animateIn(current); updateUI();
  if (current>0) hintEl.style.opacity='0';
  setTimeout(() => { sections[prev].classList.remove('prev'); locked=false; }, 700);
}

// Keyboard
document.addEventListener('keydown', e => {
  if (['ArrowDown','ArrowRight',' '].includes(e.key)) { e.preventDefault(); goTo(current+1); }
  if (['ArrowUp','ArrowLeft'].includes(e.key))        { e.preventDefault(); goTo(current-1); }
});

// Mouse wheel
let wt=null;
document.addEventListener('wheel', e => {
  e.preventDefault();
  if (wt||Math.abs(e.deltaY)<8) return;
  goTo(current+(e.deltaY>0?1:-1));
  wt=setTimeout(()=>{wt=null;},700);
},{passive:false});

// Touch
let tx=0,ty=0;
document.addEventListener('touchstart',e=>{tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
document.addEventListener('touchend',e=>{
  const dy=e.changedTouches[0].clientY-ty, dx=e.changedTouches[0].clientX-tx;
  if(Math.abs(dy)>Math.abs(dx)&&Math.abs(dy)>40) goTo(current+(dy<0?1:-1));
},{passive:true});

updateUI(); animateIn(0);
```

---

## Script 2: Edit Mode

**Important**: customize `SLIDE_FIELDS` to match the actual sections in the deck.
Every slide should have at least its title and lead text in the fields array.

```javascript
(function() {
  'use strict';
  const STORAGE_KEY = 'deck_edits_v1'; // change per deck to avoid collisions

  // ── Customize SLIDE_FIELDS per deck ──────────────────────────────────────
  // One entry per slide. `sel` is a CSS selector for the DOM element.
  // type: 'text' for single-line, 'textarea' for multi-line
  const SLIDE_FIELDS = [
    { name: '封面 (Slide 1)', fields: [
      { label: '主标题',   sel: '#hero h1',    type: 'text' },
      { label: '副标题',   sel: '#hero .lead', type: 'textarea' },
      { label: '标签',     sel: '#hero .eyebrow', type: 'text' },
    ]},
    { name: 'Slide 2', fields: [
      { label: '标题',     sel: '[data-index="1"] h2', type: 'text' },
      { label: '描述',     sel: '[data-index="1"] .lead', type: 'textarea' },
    ]},
    // ADD MORE SLIDES HERE — one entry per section[data-index]
  ];

  const COLOR_FIELDS = [
    { key:'accent',  cssVar:'--accent',       label:'主题色 (蓝)',  default:'#0a84ff' },
    { key:'purple',  cssVar:'--accent-purple', label:'强调色 (紫)', default:'#5e5ce6' },
    { key:'green',   cssVar:'--green',          label:'成功色 (绿)', default:'#10b981' },
    { key:'bg',      cssVar:'--bg',             label:'背景色',      default:'#f5f5f7' },
  ];
  // ── End customization ─────────────────────────────────────────────────────

  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY)||'{}');

  // Restore saved color overrides on load
  COLOR_FIELDS.forEach(f => {
    if (saved['color_'+f.key]) document.documentElement.style.setProperty(f.cssVar, saved['color_'+f.key]);
  });
  // Restore saved text overrides on load
  Object.entries(saved).forEach(([k,v]) => {
    if (!k.startsWith('color_')) {
      const el = document.querySelector(k);
      if (el) el.innerHTML = v;
    }
  });

  const toggleBtn   = document.getElementById('editToggle');
  const overlay     = document.getElementById('editOverlay');
  const sidebar     = document.getElementById('editSidebar');
  const bodyEl      = document.getElementById('editBody');
  const closeBtn    = document.getElementById('editClose');
  const saveStatus  = document.getElementById('saveStatus');
  const downloadBtn = document.getElementById('downloadFile');

  function openEdit()  {
    toggleBtn.classList.add('active'); overlay.classList.add('show');
    sidebar.classList.add('open'); document.body.classList.add('edit-mode-active');
    renderFields();
  }
  function closeEdit() {
    toggleBtn.classList.remove('active'); overlay.classList.remove('show');
    sidebar.classList.remove('open'); document.body.classList.remove('edit-mode-active');
  }
  toggleBtn.addEventListener('click', () => sidebar.classList.contains('open') ? closeEdit() : openEdit());
  overlay.addEventListener('click', closeEdit);
  closeBtn.addEventListener('click', closeEdit);

  function showSaved() { saveStatus.classList.add('show'); setTimeout(()=>saveStatus.classList.remove('show'),1500); }

  function renderFields() {
    bodyEl.innerHTML = '';

    // Color group
    const cg = makeGroup('🎨 主题色彩', true);
    COLOR_FIELDS.forEach(f => {
      const row = document.createElement('div'); row.className='edit-field';
      row.innerHTML = `<div class="edit-label">${f.label}</div>
        <input type="color" class="edit-input" style="height:36px;padding:2px 4px;cursor:pointer"
               value="${saved['color_'+f.key]||f.default}">`;
      row.querySelector('input').addEventListener('input', e => {
        document.documentElement.style.setProperty(f.cssVar, e.target.value);
        saved['color_'+f.key] = e.target.value;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
        showSaved();
      });
      cg.body.appendChild(row);
    });
    bodyEl.appendChild(cg.el);

    // Slide text fields
    SLIDE_FIELDS.forEach((slide, si) => {
      const sg = makeGroup(`Slide ${si+1}: ${slide.name}`, si===0);
      slide.fields.forEach(f => {
        const el = document.querySelector(f.sel);
        if (!el) return;
        const row = document.createElement('div'); row.className='edit-field';
        row.innerHTML = `<div class="edit-label">${f.label}</div>${
          f.type==='textarea'
            ? `<textarea class="edit-textarea">${el.innerHTML}</textarea>`
            : `<input class="edit-input" type="text" value="${el.innerHTML.replace(/"/g,'&quot;')}">`
        }`;
        const input = row.querySelector('input,textarea');
        input.addEventListener('input', () => {
          el.innerHTML = input.value;
          saved[f.sel] = input.value;
          localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
          showSaved();
        });
        sg.body.appendChild(row);
      });
      bodyEl.appendChild(sg.el);
    });
  }

  function makeGroup(title, open=false) {
    const el = document.createElement('div');
    el.className = 'edit-group' + (open ? '' : ' collapsed');
    el.innerHTML = `<div class="edit-group-header">${title}<span class="edit-group-arrow">▼</span></div>
                    <div class="edit-group-body"></div>`;
    el.querySelector('.edit-group-header').addEventListener('click', () => el.classList.toggle('collapsed'));
    return { el, body: el.querySelector('.edit-group-body') };
  }

  downloadBtn.addEventListener('click', () => {
    const blob = new Blob([document.documentElement.outerHTML], {type:'text/html'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'presentation.html';
    a.click();
  });
})();
```

---

## Edit Mode CSS (include in `<style>` block)

```css
.edit-toggle { position:fixed; right:0; top:50%; transform:translateY(-50%); z-index:500; width:40px; height:40px; border:none; cursor:pointer; background:var(--accent); color:#fff; font-size:18px; border-radius:10px 0 0 10px; box-shadow:-2px 2px 12px rgba(0,0,0,0.15); transition:all 0.3s ease; display:flex; align-items:center; justify-content:center; opacity:0.5; }
.edit-toggle:hover { opacity:1; width:44px; }
.edit-toggle.active { right:420px; opacity:1; }
.edit-overlay { position:fixed; inset:0; z-index:400; background:rgba(0,0,0,0.3); opacity:0; pointer-events:none; transition:opacity 0.35s ease; }
.edit-overlay.show { opacity:1; pointer-events:auto; }
.edit-sidebar { position:fixed; top:0; right:-420px; width:420px; height:100vh; z-index:450; background:#fff; box-shadow:-4px 0 40px rgba(0,0,0,0.12); transition:right 0.35s cubic-bezier(0.22,1,0.36,1); display:flex; flex-direction:column; color:#1d1d1f; font-family:-apple-system,sans-serif; }
.edit-sidebar.open { right:0; }
.edit-header { display:flex; align-items:center; justify-content:space-between; padding:18px 24px; border-bottom:1px solid #e5e5e7; flex-shrink:0; }
.edit-header h3 { font-size:16px; font-weight:700; margin:0; letter-spacing:-0.01em; }
.edit-close { width:32px; height:32px; border:none; background:#f5f5f7; border-radius:8px; cursor:pointer; font-size:16px; display:flex; align-items:center; justify-content:center; color:#666; transition:all 0.2s; }
.edit-close:hover { background:#e5e5e7; }
.edit-body { flex:1; overflow-y:auto; padding:16px 24px 24px; }
.edit-body::-webkit-scrollbar { width:4px; }
.edit-body::-webkit-scrollbar-thumb { background:#d2d2d7; border-radius:2px; }
.edit-group { margin-bottom:20px; border:1px solid #e5e5e7; border-radius:12px; overflow:hidden; }
.edit-group-header { display:flex; align-items:center; justify-content:space-between; padding:12px 16px; background:#fafafa; cursor:pointer; user-select:none; font-size:13px; font-weight:600; letter-spacing:0.02em; }
.edit-group-header:hover { background:#f0f0f2; }
.edit-group-arrow { font-size:10px; color:#999; transition:transform 0.2s; }
.edit-group.collapsed .edit-group-arrow { transform:rotate(-90deg); }
.edit-group-body { padding:12px 16px 16px; }
.edit-group.collapsed .edit-group-body { display:none; }
.edit-field { margin-bottom:12px; }
.edit-field:last-child { margin-bottom:0; }
.edit-label { font-size:11px; font-weight:600; color:#6e6e73; letter-spacing:0.03em; margin-bottom:4px; text-transform:uppercase; }
.edit-input, .edit-textarea { width:100%; padding:8px 10px; border:1px solid #d2d2d7; border-radius:8px; font-size:13px; font-family:inherit; color:#1d1d1f; background:#fff; transition:border-color 0.2s; }
.edit-input:focus, .edit-textarea:focus { outline:none; border-color:var(--accent); box-shadow:0 0 0 3px rgba(10,132,255,0.12); }
.edit-textarea { resize:vertical; min-height:48px; line-height:1.5; }
.edit-footer { padding:16px 24px; border-top:1px solid #e5e5e7; flex-shrink:0; display:flex; gap:10px; align-items:center; }
.edit-btn { flex:1; padding:10px 16px; border:none; border-radius:10px; font-size:13px; font-weight:600; cursor:pointer; transition:all 0.2s; display:flex; align-items:center; justify-content:center; gap:6px; }
.edit-btn-primary { background:var(--accent); color:#fff; }
.edit-btn-primary:hover { opacity:0.85; }
.edit-save-status { font-size:11px; color:var(--green); flex-shrink:0; opacity:0; transition:opacity 0.3s; }
.edit-save-status.show { opacity:1; }
.edit-mode-active [data-editable]:hover { outline:2px dashed var(--accent); outline-offset:2px; cursor:pointer; background:rgba(10,132,255,0.03); border-radius:4px; }
```
