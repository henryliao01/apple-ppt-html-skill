# Slide Layout Templates

Seven reusable layout templates. Pick the best fit per slide.
All templates use `data-in` on key elements for stagger animation.

---

## Template A — Hero (centered, text focus)

Best for: opening slide, section divider, closing CTA.

```html
<section id="hero" data-index="0">
  <div class="container" style="text-align:center">
    <span class="eyebrow" data-in>CATEGORY · TOPIC</span>
    <h1 data-in>Main Title<br><span class="gradient-text">Highlighted Line</span></h1>
    <p class="lead" data-in style="margin:0 auto 32px">
      Supporting description. Keep to 1–2 lines.
    </p>
    <div class="stats-row" data-in>
      <div class="stat-item">
        <span class="stat-label">METRIC A</span>
        <span class="stat-value">Value</span>
      </div>
      <div class="stat-item">
        <span class="stat-label">METRIC B</span>
        <span class="stat-value" style="color:var(--accent)">Value</span>
      </div>
      <div class="stat-item">
        <span class="stat-label">METRIC C</span>
        <span class="stat-value">Value</span>
      </div>
    </div>
  </div>
</section>
```

---

## Template B — 2-Column Grid

Best for: problem/solution, before/after, dual-topic, text + visual.
Adjust column ratio: `1fr 1fr` (equal), `1.2fr 1fr` (left heavier), `1fr 1.4fr` (right heavier).

```html
<section data-index="N">
  <div class="container">
    <span class="eyebrow" data-in>Section Tag</span>
    <h2 data-in>Section Title</h2>
    <p class="lead" data-in>Brief description of this section.</p>
    <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:stretch">
      <!-- Left: single large card -->
      <div class="card card-blue" data-in style="padding:36px">
        <h3 class="card-title">Left Title</h3>
        <p class="card-text">Left content goes here.</p>
      </div>
      <!-- Right: stacked cards -->
      <div style="display:flex;flex-direction:column;gap:16px">
        <div class="card" data-in style="flex:1;padding:28px">
          <h3 class="card-title">Top Right</h3>
          <p class="card-text">Content.</p>
        </div>
        <div class="card" data-in style="flex:1;padding:28px">
          <h3 class="card-title">Bottom Right</h3>
          <p class="card-text">Content.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

**Equal-height rule**: always `align-items:stretch` on the grid parent. For stacked right-side cards, give each `flex:1` so they share the height evenly.

---

## Template C — 4-Card Grid (overview / features)

Best for: 4 parallel items of equal weight (strategies, pillars, steps).

```html
<section data-index="N">
  <div class="container">
    <span class="eyebrow" data-in>Overview</span>
    <h2 data-in>Four Key Directions</h2>
    <p class="lead" data-in>Description.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px">
      <div class="card" style="text-align:center;padding:48px 32px" data-in>
        <div style="font-size:72px;font-weight:800;letter-spacing:-0.05em;line-height:1;color:var(--accent);margin-bottom:20px">01</div>
        <h3 class="card-title">Card Title</h3>
        <p class="card-text">Description of this item.</p>
        <span class="pill pill-blue" style="margin-top:16px">Tag</span>
      </div>
      <div class="card" style="text-align:center;padding:48px 32px" data-in>
        <div style="font-size:72px;font-weight:800;letter-spacing:-0.05em;line-height:1;color:var(--accent-purple);margin-bottom:20px">02</div>
        <h3 class="card-title">Card Title</h3>
        <p class="card-text">Description of this item.</p>
        <span class="pill pill-purple" style="margin-top:16px">Tag</span>
      </div>
      <div class="card" style="text-align:center;padding:48px 32px" data-in>
        <div style="font-size:72px;font-weight:800;letter-spacing:-0.05em;line-height:1;color:var(--green);margin-bottom:20px">03</div>
        <h3 class="card-title">Card Title</h3>
        <p class="card-text">Description of this item.</p>
        <span class="pill pill-green" style="margin-top:16px">Tag</span>
      </div>
      <div class="card" style="text-align:center;padding:48px 32px" data-in>
        <div style="font-size:72px;font-weight:800;letter-spacing:-0.05em;line-height:1;color:var(--orange);margin-bottom:20px">04</div>
        <h3 class="card-title">Card Title</h3>
        <p class="card-text">Description of this item.</p>
        <span class="pill pill-orange" style="margin-top:16px">Tag</span>
      </div>
    </div>
  </div>
</section>
```

---

## Template D — Chart + Insight Cards

Best for: data analysis, metrics, trend visualization.
Left: SVG chart. Right: 2–3 stacked metric callout cards.

```html
<section data-index="N">
  <div class="container" style="max-width:1280px">
    <span class="eyebrow" data-in>Analytics</span>
    <h2 data-in>Metrics Overview</h2>
    <p class="lead" data-in style="max-width:860px">Summary insight.</p>
    <div data-in style="display:grid;grid-template-columns:1.4fr 1fr;gap:20px;align-items:stretch">
      <!-- Left: chart -->
      <div class="chart-card" style="display:flex;flex-direction:column">
        <div class="chart-head">
          <div class="chart-title">Chart Title</div>
          <div class="chart-sub">Subtitle / period</div>
        </div>
        <!-- INSERT SVG CHART HERE from chart-templates.md -->
      </div>
      <!-- Right: metric cards -->
      <div style="display:flex;flex-direction:column;gap:16px">
        <div class="chart-card" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:28px">
          <div style="font-size:13px;color:var(--text-muted);margin-bottom:8px">Metric Label</div>
          <div class="big-num" style="color:var(--accent)">42.8%</div>
          <div style="font-size:14px;color:var(--green);margin-top:8px;font-weight:600">↑ +18% vs prior period</div>
        </div>
        <div class="chart-card" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:24px">
          <div style="font-size:14px;font-weight:700;color:var(--accent);margin-bottom:12px">Key Inflection</div>
          <div style="font-size:14px;color:var(--text-muted);line-height:1.7">Point 1: detail</div>
          <div style="font-size:14px;color:var(--text-muted);line-height:1.7">Point 2: detail</div>
        </div>
        <div class="chart-card" style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:28px">
          <div style="font-size:13px;color:var(--text-muted);margin-bottom:8px">Target Metric</div>
          <div class="big-num" style="color:var(--green)">5.8x</div>
          <div style="font-size:14px;color:var(--green);margin-top:8px;font-weight:600">↑ +107% improvement potential</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Template E — Process Pipeline (horizontal steps)

Best for: workflow, steps, funnel stages, sequence.

```html
<section data-index="N">
  <div class="container">
    <span class="eyebrow" data-in>Workflow</span>
    <h2 data-in>Process Title</h2>
    <p class="lead" data-in>Description of the flow.</p>
    <div data-in style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:32px">
      <div class="card" style="padding:28px 24px;text-align:center;position:relative">
        <div style="font-size:32px;margin-bottom:12px">🔍</div>
        <span class="pill pill-blue" style="margin-bottom:12px">Step 01</span>
        <div style="font-size:16px;font-weight:700;margin-bottom:8px">Step Title</div>
        <div style="font-size:14px;color:var(--text-muted);line-height:1.5">Description.</div>
        <div style="position:absolute;right:-14px;top:50%;transform:translateY(-50%);font-size:18px;color:rgba(0,0,0,0.15)">→</div>
      </div>
      <!-- Repeat for each step; remove the arrow → on the last card -->
    </div>
    <!-- Optional: output/result card below -->
    <div class="card card-blue" data-in style="padding:32px 40px">
      <div style="font-size:24px;font-weight:750;color:var(--accent);margin-bottom:12px">Output / Result</div>
      <p class="card-text">What the process produces.</p>
    </div>
  </div>
</section>
```

---

## Template F — Insight Cards with Tags

Best for: findings, recommendations, evidence list, key messages.
Scale to 2–6 items by adjusting grid columns.

```html
<section data-index="N">
  <div class="container">
    <span class="eyebrow" data-in>Findings</span>
    <h2 data-in>Key Insights</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
      <div class="card" data-in style="padding:32px">
        <div style="display:flex;align-items:flex-start;gap:16px">
          <div style="flex-shrink:0;width:44px;height:44px;border-radius:14px;background:rgba(10,132,255,0.1);display:flex;align-items:center;justify-content:center;font-size:22px">💡</div>
          <div>
            <div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap">
              <span class="pill pill-blue">Insight</span>
              <span class="pill pill-green">High Impact</span>
            </div>
            <div style="font-size:18px;font-weight:700;color:var(--text);margin-bottom:8px">Insight Title</div>
            <div style="font-size:15px;color:var(--text-muted);line-height:1.62">Body text explaining the insight.</div>
          </div>
        </div>
      </div>
      <!-- Repeat cards -->
    </div>
  </div>
</section>
```

---

## Template G — Summary / Closing

Best for: action items, conclusion, next steps. Use reduced padding.

Add to the `<style>` block: `section[data-index="N"] { padding: 44px 48px; }`

```html
<section data-index="N">
  <div class="container">
    <span class="eyebrow" data-in>Summary</span>
    <h2 data-in style="font-size:clamp(28px,3.4vw,50px);margin-bottom:10px">Summary Title</h2>
    <p class="lead" data-in style="font-size:clamp(14px,1.4vw,17px);margin-bottom:12px">Closing message.</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:14px">
      <div class="card card-blue" data-in style="padding:18px 22px">
        <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent);margin-bottom:8px">CATEGORY A</div>
        <div style="font-size:15px;font-weight:700;margin-bottom:8px">Item Title</div>
        <p style="font-size:13px;color:var(--text-muted);line-height:1.55">Detail.</p>
      </div>
      <div class="card card-purple" data-in style="padding:18px 22px">
        <div style="font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent-purple);margin-bottom:8px">CATEGORY B</div>
        <div style="font-size:15px;font-weight:700;margin-bottom:8px">Item Title</div>
        <p style="font-size:13px;color:var(--text-muted);line-height:1.55">Detail.</p>
      </div>
    </div>
    <div class="card" data-in style="padding:18px 28px">
      <div style="font-size:17px;font-weight:700;color:var(--text);margin-bottom:8px">Closing statement</div>
      <p style="font-size:14px;color:var(--text-muted);line-height:1.6">Details and next steps.</p>
    </div>
  </div>
</section>
```

---

## Selecting the Right Template

| Situation | Template |
|---|---|
| Opening / title slide | A (Hero) |
| Two competing ideas, problem vs solution | B (2-col) |
| 4 equal items, strategies, pillars | C (4-grid) |
| Showing data + insight narrative | D (Chart+cards) |
| Step-by-step process or funnel | E (Pipeline) |
| Key findings, recommendations | F (Insights) |
| Conclusions, action items | G (Summary) |
| Text-heavy with supporting image | B with image in left column |
| Dashboard with 3 KPIs + donut | Custom — base on D |
