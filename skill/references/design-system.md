# Design System Reference

Copy this CSS verbatim into every deck's `<style>` block.

---

## Design Tokens

```css
:root {
  --bg: #f5f5f7;
  --text: #1d1d1f;
  --text-muted: #6e6e73;
  --accent: #0a84ff;
  --accent-purple: #5e5ce6;
  --card-bg: rgba(255,255,255,0.58);
  --card-border: rgba(255,255,255,0.68);
  --shadow-sm: 0 2px 12px rgba(15,23,42,0.04);
  --shadow-md: 0 8px 32px rgba(15,23,42,0.06), 0 1px 4px rgba(15,23,42,0.04);
  --shadow-lg: 0 20px 60px rgba(15,23,42,0.08), 0 2px 8px rgba(15,23,42,0.05);
  --green: #10b981;
  --red: #ef4444;
  --orange: #f59e0b;
  --chart-blue: #0a84ff;
  --chart-purple: #5e5ce6;
  --chart-cyan: #64d2ff;
  --chart-grid: rgba(29,29,31,0.08);
  --chart-axis: rgba(29,29,31,0.24);
}
```

To use a custom brand color, swap `--accent` and keep `--accent-purple` as complement.

---

## Base Reset & Font

```css
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif;
  -webkit-font-smoothing: antialiased;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}
```

---

## Radial Gradient Background (always on body::before)

```css
body::before {
  content:''; position:fixed; inset:0; pointer-events:none; z-index:0;
  background:
    radial-gradient(ellipse 90% 75% at 8% -15%, rgba(10,132,255,0.05) 0%, transparent 70%),
    radial-gradient(ellipse 65% 55% at 94% 96%, rgba(94,92,230,0.04) 0%, transparent 65%),
    linear-gradient(180deg, rgba(255,255,255,0.6) 0%, rgba(245,245,247,0.85) 100%);
}
```

Adjust halo colors to match `--accent` if user sets a custom brand color.

---

## Typography

```css
h1 {
  font-size: clamp(48px, 6.5vw, 82px); font-weight: 750;
  letter-spacing: -0.045em; line-height: 1.04; margin-bottom: 20px;
}
h2 {
  font-size: clamp(36px, 4.8vw, 62px); font-weight: 740;
  letter-spacing: -0.038em; line-height: 1.08; margin-bottom: 16px;
}
h3 {
  font-size: clamp(24px, 2.8vw, 42px); font-weight: 700;
  letter-spacing: -0.025em; line-height: 1.14; margin-bottom: 14px;
}
.lead {
  font-size: clamp(18px, 2vw, 23px); font-weight: 500;
  color: var(--text-muted); line-height: 1.54;
  max-width: 720px; margin-bottom: 32px;
}
.eyebrow {
  display:inline-flex; align-items:center;
  padding:6px 16px; border-radius:999px;
  font-size:12px; font-weight:600; letter-spacing:0.02em;
  margin-bottom:20px;
  background:rgba(10,132,255,0.1); color:var(--accent);
}
.gradient-text {
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent-purple) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.card-title { font-size:20px; font-weight:700; margin-bottom:10px; color:var(--text); }
.card-text  { font-size:15px; color:var(--text-muted); line-height:1.62; }
```

### Pill Tags (colored variants)

```css
/* Base pill shape — add color class below */
.pill { display:inline-flex; padding:5px 14px; border-radius:999px; font-size:12px; font-weight:600; }
.pill-blue   { background:rgba(10,132,255,0.1);  color:#0a84ff; }
.pill-green  { background:rgba(16,185,129,0.1);  color:#10b981; }
.pill-red    { background:rgba(239,68,68,0.1);   color:#ef4444; }
.pill-orange { background:rgba(245,158,11,0.1);  color:#f59e0b; }
.pill-purple { background:rgba(94,92,230,0.1);   color:#5e5ce6; }
```

### Large number display (for stat cards)

```css
.big-num {
  font-size: clamp(36px, 3.6vw, 52px); font-weight: 800;
  letter-spacing: -0.04em; line-height: 1;
}
```

---

## Glass Card

```css
.card {
  background: var(--card-bg);
  backdrop-filter: saturate(115%) blur(32px);
  -webkit-backdrop-filter: saturate(115%) blur(32px);
  border: 1px solid var(--card-border);
  border-radius: 36px; padding: 28px 32px;
  box-shadow: var(--shadow-md);
  transition: all 0.35s cubic-bezier(0.2,0.7,0.2,1);
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
  border-color: rgba(10,132,255,0.18);
}
```

### Card accent variants

```css
.card-blue   { border-color:rgba(10,132,255,0.24); background:rgba(10,132,255,0.04); }
.card-purple { border-color:rgba(94,92,230,0.20);  background:rgba(94,92,230,0.04); }
.card-green  {
  border-color: color-mix(in srgb, var(--green) 20%, transparent);
  background:   color-mix(in srgb, var(--green) 3%, transparent);
}
```

### Inner chart card (lighter, for nested visuals)

```css
.chart-card {
  background: rgba(255,255,255,0.62);
  backdrop-filter: saturate(118%) blur(24px);
  -webkit-backdrop-filter: saturate(118%) blur(24px);
  border: 1px solid rgba(255,255,255,0.74);
  border-radius: 28px; padding: 18px;
  box-shadow: var(--shadow-sm);
}
.chart-head  { display:flex; justify-content:space-between; align-items:end; margin-bottom:10px; }
.chart-title { font-size:16px; font-weight:700; letter-spacing:-.01em; }
.chart-sub   { font-size:12px; color:var(--text-muted); }
svg.chart    { width:100%; height:auto; display:block; }
```

---

## Stats Banner

```css
.stats-row {
  display:flex; gap:0;
  background:var(--card-bg);
  backdrop-filter:saturate(115%) blur(32px);
  -webkit-backdrop-filter:saturate(115%) blur(32px);
  border:1px solid var(--card-border); border-radius:28px;
  box-shadow:var(--shadow-md); overflow:hidden;
  width:fit-content; margin:0 auto 48px;
}
.stat-item {
  padding:22px 42px; border-right:1px solid rgba(0,0,0,0.05);
  display:flex; flex-direction:column; gap:6px;
}
.stat-item:last-child { border-right:none; }
.stat-label { font-size:12px; font-weight:600; letter-spacing:0.06em; text-transform:uppercase; color:var(--text-muted); }
.stat-value { font-size:20px; font-weight:700; color:var(--text); }
```

---

## Fixed Chrome (Nav, Progress Bar, Counter, Hint)

```css
/* Right-side navigation dots */
.nav {
  position:fixed; right:28px; top:50%; transform:translateY(-50%);
  display:flex; flex-direction:column; gap:12px; z-index:100;
  background:var(--card-bg); backdrop-filter:saturate(115%) blur(24px);
  -webkit-backdrop-filter:saturate(115%) blur(24px);
  border:1px solid var(--card-border); border-radius:32px;
  padding:14px 12px; box-shadow:var(--shadow-md);
}
.nav-dot {
  width:8px; height:8px; border-radius:50%;
  background:rgba(0,0,0,0.16); cursor:pointer;
  transition:all 0.3s cubic-bezier(0.2,0.7,0.2,1);
}
.nav-dot.active { background:var(--accent); height:26px; }
.nav-dot:hover:not(.active) { background:rgba(0,0,0,0.28); }

/* Top progress bar */
.progress {
  position:fixed; top:0; left:0; height:2px;
  background:linear-gradient(90deg,var(--accent),var(--accent-purple));
  z-index:200; transition:width 0.4s cubic-bezier(0.2,0.7,0.2,1);
}

/* Slide counter (bottom right) */
.slide-counter {
  position:fixed; bottom:24px; right:24px; z-index:100;
  font-size:11px; font-weight:600; color:rgba(0,0,0,0.4);
  font-family:'SF Pro Display',-apple-system,sans-serif;
  background:rgba(255,255,255,0.72);
  backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(0,0,0,0.07); border-radius:999px; padding:5px 12px;
}

/* Keyboard hint (bottom center, fades out after first slide) */
.hint {
  position:fixed; bottom:24px; left:50%; transform:translateX(-50%);
  font-size:11px; color:rgba(0,0,0,0.35);
  display:flex; gap:6px; align-items:center; z-index:100;
  background:rgba(255,255,255,0.65); border:1px solid rgba(0,0,0,0.07);
  border-radius:999px; padding:5px 14px; backdrop-filter:blur(10px);
  transition:opacity .5s; pointer-events:none;
}
.key {
  display:inline-flex; align-items:center; justify-content:center;
  width:20px; height:20px; border:1px solid rgba(0,0,0,0.15);
  border-radius:5px; font-size:9px;
  background:rgba(255,255,255,0.75); color:rgba(0,0,0,0.5);
}
```

---

## Responsive Breakpoint

Always add this at the end of your `<style>` block:

```css
@media (max-width:960px) {
  section { padding:64px 20px; }
  .grid-2, .grid-chart, .compare-grid { grid-template-columns:1fr; }
  .stats-row { flex-direction:column; }
  .stat-item { border-right:none; border-bottom:1px solid rgba(0,0,0,0.05); }
  .stat-item:last-child { border-bottom:none; }
}
```
