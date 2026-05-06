# Chart Templates Reference

All charts are inline SVG. Always wrap in `.chart-card`.
Charts animate only when `section.active` (JS handles this via `animation-play-state`).

---

## Required Animation CSS

Include these keyframes in the deck's `<style>` block whenever any chart is present:

```css
/* Line chart draw */
.line-main {
  fill:none; stroke:url(#lineGrad); stroke-width:4;
  stroke-linecap:round; stroke-linejoin:round;
  stroke-dasharray:1200; stroke-dashoffset:1200;
  animation: drawLine 1.2s cubic-bezier(.2,.7,.2,1) forwards;
}
@keyframes drawLine { to { stroke-dashoffset:0; } }

/* Data point pop-in */
.point {
  fill:#fff; stroke:var(--accent); stroke-width:3; r:5;
  transform-origin:center;
  animation: pop .45s ease both;
}
@keyframes pop { from { transform:scale(.2); opacity:0; } to { transform:scale(1); opacity:1; } }

/* Bar chart grow from bottom */
.bar { transform-origin:bottom; transform:scaleY(0); animation: grow .9s cubic-bezier(.2,.7,.2,1) forwards; }
@keyframes grow { to { transform:scaleY(1); } }

/* Animated dashed flow line */
.flow-line { stroke:rgba(10,132,255,.5); stroke-width:2; fill:none; stroke-dasharray:8 8; animation: flow 1.6s linear infinite; }
@keyframes flow { to { stroke-dashoffset:-32; } }

/* Donut ring segments */
@keyframes ringDraw1 { from {stroke-dasharray:0 440;} to {stroke-dasharray:206 440;} }
@keyframes ringDraw2 { from {stroke-dasharray:0 440;} to {stroke-dasharray:145 440;} }
@keyframes ringDraw3 { from {stroke-dasharray:0 440;} to {stroke-dasharray:88 440;} }

/* SVG helper classes */
.axis  { stroke:var(--chart-axis); stroke-width:1; }
.grid  { stroke:var(--chart-grid);  stroke-width:1; }
.flow-node { fill:rgba(255,255,255,.7); stroke:rgba(10,132,255,.28); stroke-width:1.2; }
```

---

## Chart 1 — Animated Line Chart

Use for: trends over time, before/after comparison as series.

**Stroke-dasharray tip**: set `stroke-dasharray` and initial `stroke-dashoffset` to the
approximate path length (measure or estimate; 1200 works for most 600-wide SVGs).

```html
<svg class="chart" viewBox="0 0 600 280">
  <defs>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="var(--accent)"/>
      <stop offset="100%" stop-color="var(--accent-purple)"/>
    </linearGradient>
    <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="rgba(10,132,255,0.15)"/>
      <stop offset="100%" stop-color="rgba(10,132,255,0)"/>
    </linearGradient>
  </defs>

  <!-- Grid lines -->
  <line class="grid" x1="50" y1="40"  x2="560" y2="40"/>
  <line class="grid" x1="50" y1="100" x2="560" y2="100"/>
  <line class="grid" x1="50" y1="160" x2="560" y2="160"/>
  <line class="grid" x1="50" y1="220" x2="560" y2="220"/>

  <!-- Axes -->
  <line class="axis" x1="50" y1="40"  x2="50"  y2="240"/>
  <line class="axis" x1="50" y1="240" x2="560" y2="240"/>

  <!-- Area fill (optional, adds depth) -->
  <path fill="url(#areaGrad)" opacity="0.6"
        d="M80,200 L180,155 L280,120 L380,85 L480,55 L480,240 L80,240 Z"/>

  <!-- Main line — adjust d= points to match your data -->
  <path class="line-main" d="M80,200 L180,155 L280,120 L380,85 L480,55"/>

  <!-- Data points — stagger animation-delay -->
  <circle class="point" cx="80"  cy="200" style="animation-delay:.9s"/>
  <circle class="point" cx="180" cy="155" style="animation-delay:1.0s"/>
  <circle class="point" cx="280" cy="120" style="animation-delay:1.1s"/>
  <circle class="point" cx="380" cy="85"  style="animation-delay:1.2s"/>
  <circle class="point" cx="480" cy="55"  style="animation-delay:1.3s"/>

  <!-- Value labels above points -->
  <text x="80"  y="188" font-size="13" font-weight="600" fill="var(--text)" text-anchor="middle">2.1</text>
  <text x="480" y="43"  font-size="13" font-weight="600" fill="var(--accent)" text-anchor="middle">5.8</text>

  <!-- X-axis labels -->
  <text x="80"  y="260" font-size="12" fill="var(--text-muted)" text-anchor="middle">Jan</text>
  <text x="180" y="260" font-size="12" fill="var(--text-muted)" text-anchor="middle">Feb</text>
  <text x="280" y="260" font-size="12" fill="var(--text-muted)" text-anchor="middle">Mar</text>
  <text x="380" y="260" font-size="12" fill="var(--text-muted)" text-anchor="middle">Apr</text>
  <text x="480" y="260" font-size="12" fill="var(--text-muted)" text-anchor="middle">May</text>

  <!-- Y-axis labels -->
  <text x="42" y="44"  font-size="11" fill="var(--text-muted)" text-anchor="end">6</text>
  <text x="42" y="164" font-size="11" fill="var(--text-muted)" text-anchor="end">3</text>
  <text x="42" y="244" font-size="11" fill="var(--text-muted)" text-anchor="end">0</text>
</svg>
```

**Coordinate math**: SVG y=0 is top. For a chart range [0, maxVal]:
`y = topPadding + (1 - value/maxVal) * chartHeight`
Example: max=6, chartHeight=180 (40→220), value=5.8 → y = 40 + (1-5.8/6)*180 ≈ 46

---

## Chart 2 — Bar Chart (Before / After comparison)

Use for: metric comparison, before/after optimization.
Each row = one metric. Rows spaced 115px apart (y, y+115, y+230).

```html
<svg class="chart" viewBox="0 0 680 380">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a84ff"/>
      <stop offset="100%" stop-color="#5e5ce6"/>
    </linearGradient>
  </defs>

  <!-- Grid -->
  <line class="grid" x1="180" y1="42"  x2="640" y2="42"/>
  <line class="grid" x1="180" y1="157" x2="640" y2="157"/>
  <line class="grid" x1="180" y1="272" x2="640" y2="272"/>

  <!-- ══ Row 1: Metric A ══ -->
  <rect x="30" y="20" width="130" height="32" rx="16" fill="rgba(10,132,255,0.08)"/>
  <text x="95" y="41" font-size="14" font-weight="600" fill="#0a84ff" text-anchor="middle">Metric A</text>

  <rect class="bar" x="185" y="60" width="120" height="38" fill="#e5e7eb" rx="6" style="animation-delay:.1s"/>
  <text x="245" y="84" font-size="16" font-weight="700" fill="#6e6e73" text-anchor="middle">Before</text>
  <text x="185" y="114" font-size="11" fill="#9ca3af" text-anchor="middle">优化前</text>

  <rect class="bar" x="324" y="35" width="120" height="63" fill="url(#barGrad)" rx="6" style="animation-delay:.2s"/>
  <text x="384" y="73" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">After</text>
  <text x="324" y="114" font-size="11" fill="#0a84ff" text-anchor="middle">优化后</text>

  <!-- Delta badge -->
  <rect x="472" y="40" width="72" height="28" rx="14" fill="rgba(16,185,129,0.12)"/>
  <text x="508" y="59" font-size="14" font-weight="700" fill="#10b981" text-anchor="middle">+XX%</text>

  <!-- ══ Row 2: Metric B (y + 115) ══ -->
  <rect x="30" y="135" width="130" height="32" rx="16" fill="rgba(94,92,230,0.08)"/>
  <text x="95" y="156" font-size="14" font-weight="600" fill="#5e5ce6" text-anchor="middle">Metric B</text>

  <rect class="bar" x="185" y="175" width="120" height="38" fill="#e5e7eb" rx="6" style="animation-delay:.3s"/>
  <text x="245" y="199" font-size="16" font-weight="700" fill="#6e6e73" text-anchor="middle">Before</text>
  <text x="185" y="229" font-size="11" fill="#9ca3af" text-anchor="middle">优化前</text>

  <rect class="bar" x="324" y="150" width="120" height="63" fill="url(#barGrad)" rx="6" style="animation-delay:.4s"/>
  <text x="384" y="188" font-size="18" font-weight="700" fill="#ffffff" text-anchor="middle">After</text>
  <text x="324" y="229" font-size="11" fill="#5e5ce6" text-anchor="middle">优化后</text>

  <rect x="472" y="155" width="72" height="28" rx="14" fill="rgba(16,185,129,0.12)"/>
  <text x="508" y="174" font-size="14" font-weight="700" fill="#10b981" text-anchor="middle">+XX%</text>

  <!-- ══ Row 3: Metric C (y + 230) — add if needed ══ -->
</svg>
```

---

## Chart 3 — Donut / Ring Chart

Use for: category share, strategy weight distribution, composition.

**Arc length formula** (for r=70, circumference ≈ 440):
`arc = percentage * 4.4`  (e.g., 47% → 206.8 ≈ 207)

**Dashoffset** for each segment = negative sum of all previous arc lengths.

```html
<!-- Wrap in a flex container with a legend below -->
<div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:10px">
  <svg viewBox="0 0 280 280" style="display:block;width:180px;height:180px">
    <defs>
      <linearGradient id="dg1"><stop offset="0%" stop-color="#0a84ff"/><stop offset="100%" stop-color="#0a84ff"/></linearGradient>
      <linearGradient id="dg2"><stop offset="0%" stop-color="#5e5ce6"/><stop offset="100%" stop-color="#5e5ce6"/></linearGradient>
      <linearGradient id="dg3"><stop offset="0%" stop-color="#64d2ff"/><stop offset="100%" stop-color="#64d2ff"/></linearGradient>
    </defs>
    <!-- Track (grey background ring) -->
    <circle cx="140" cy="140" r="70" fill="none" stroke="#f0f0f0" stroke-width="28"/>

    <!-- Segment 1: 47% → arc=207, offset=0 -->
    <circle cx="140" cy="140" r="70" fill="none" stroke="url(#dg1)" stroke-width="28"
            stroke-dasharray="207 440" stroke-dashoffset="0"
            transform="rotate(-90 140 140)" stroke-linecap="round"
            style="animation:ringDraw1 1s ease forwards"/>

    <!-- Segment 2: 33% → arc=145, offset=-207 -->
    <circle cx="140" cy="140" r="70" fill="none" stroke="url(#dg2)" stroke-width="28"
            stroke-dasharray="145 440" stroke-dashoffset="-207"
            transform="rotate(-90 140 140)" stroke-linecap="round"
            style="animation:ringDraw2 1.1s ease forwards;animation-delay:.2s;stroke-dasharray:0 440"/>

    <!-- Segment 3: 20% → arc=88, offset=-(207+145)=-352 -->
    <circle cx="140" cy="140" r="70" fill="none" stroke="url(#dg3)" stroke-width="28"
            stroke-dasharray="88 440" stroke-dashoffset="-352"
            transform="rotate(-90 140 140)" stroke-linecap="round"
            style="animation:ringDraw3 1.2s ease forwards;animation-delay:.4s;stroke-dasharray:0 440"/>

    <!-- Center label -->
    <text x="140" y="133" font-size="32" font-weight="800" fill="#0a84ff" text-anchor="middle">100%</text>
    <text x="140" y="158" font-size="13" fill="#6e6e73" text-anchor="middle">Total</text>
  </svg>
  <div style="font-size:12px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;color:var(--text-muted)">Distribution Label</div>
</div>

<!-- Legend cells (place in a flex:1 grid beside the donut) -->
<div style="flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
  <div style="text-align:center;padding:22px 16px;border-radius:28px;background:rgba(10,132,255,0.05);border:1px solid rgba(10,132,255,0.14)">
    <div class="big-num" style="color:var(--accent);margin-bottom:10px">47%</div>
    <div style="font-size:14px;font-weight:700;color:var(--accent);margin-bottom:4px">Category A</div>
    <div style="font-size:13px;color:var(--text-muted);line-height:1.5">Description</div>
  </div>
  <div style="text-align:center;padding:22px 16px;border-radius:28px;background:rgba(94,92,230,0.05);border:1px solid rgba(94,92,230,0.14)">
    <div class="big-num" style="color:var(--accent-purple);margin-bottom:10px">33%</div>
    <div style="font-size:14px;font-weight:700;color:var(--accent-purple);margin-bottom:4px">Category B</div>
    <div style="font-size:13px;color:var(--text-muted);line-height:1.5">Description</div>
  </div>
  <div style="text-align:center;padding:22px 16px;border-radius:28px;background:rgba(100,210,255,0.06);border:1px solid rgba(100,210,255,0.28)">
    <div class="big-num" style="color:#64d2ff;margin-bottom:10px">20%</div>
    <div style="font-size:14px;font-weight:700;color:#64d2ff;margin-bottom:4px">Category C</div>
    <div style="font-size:13px;color:var(--text-muted);line-height:1.5">Description</div>
  </div>
</div>
```

---

## Chart 4 — Animated Flow Diagram

Use for: system architecture, data pipeline, process with arrows.

```html
<svg class="chart" viewBox="0 0 600 200" style="overflow:visible">
  <!-- Nodes: use <rect class="flow-node" .../> -->
  <rect class="flow-node" x="20"  y="80" width="120" height="44" rx="22"/>
  <text x="80"  y="107" font-size="14" font-weight="600" fill="var(--text)" text-anchor="middle">Input</text>

  <rect class="flow-node" x="240" y="80" width="120" height="44" rx="22"/>
  <text x="300" y="107" font-size="14" font-weight="600" fill="var(--text)" text-anchor="middle">Process</text>

  <rect class="flow-node" x="460" y="80" width="120" height="44" rx="22"/>
  <text x="520" y="107" font-size="14" font-weight="600" fill="var(--text)" text-anchor="middle">Output</text>

  <!-- Animated dashed connector lines -->
  <path class="flow-line" d="M140,102 L240,102"/>
  <path class="flow-line" d="M360,102 L460,102" style="animation-delay:.3s"/>

  <!-- Arrowheads -->
  <polygon points="238,96 248,102 238,108" fill="rgba(10,132,255,0.5)"/>
  <polygon points="458,96 468,102 458,108" fill="rgba(10,132,255,0.5)"/>
</svg>
```
