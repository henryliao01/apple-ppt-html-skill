---
name: apple-ppt-html
description: >
  Generate Apple-style interactive HTML presentation decks (PPT-format) with
  frosted glass cards, smooth slide transitions, SVG charts, and a built-in
  text edit mode. Use this skill whenever the user wants to create a slide deck,
  presentation, report, strategy doc, or "PPT" as an HTML file — especially when
  they provide text content, data tables, images, or a mix. Also trigger when
  the user asks for "Apple风格 PPT", "动态汇报", "毛玻璃风格", "炫酷PPT",
  "HTML幻灯片", or any presentation/deck in HTML form. Always invoke BEFORE
  generating any HTML slide deck.
---

# Apple-Style Interactive HTML Presentation Skill

You are generating a **self-contained single-file HTML presentation deck** in
the style established by the reference design (SMS营销策略优化方案 6.2/6.3).
The output is one `.html` file with all CSS, JS, SVG, and images (base64) inlined.
No external CDN or font links allowed.

---

## How to Use This Skill

This skill is organized into reference files. Load the ones you need:

| File | When to load |
|---|---|
| `references/design-system.md` | Always — CSS tokens, typography, glass cards, background |
| `references/slide-templates.md` | Always — 7 layout templates with full HTML code |
| `references/chart-templates.md` | When deck needs data charts (bar, line, donut, flow) |
| `references/js-system.md` | Always — navigation JS + edit mode JS |

**Read all 4 reference files before generating output.** They contain the exact
CSS and JS code to copy — don't rewrite them from memory.

---

## Generation Workflow

### Step 1 — Understand the input

Identify what the user has provided:

- **Text / outline** → parse into slides (see Input Processing below)
- **Data / numbers / CSV** → plan chart slides (see chart-templates.md)
- **Images** → embed as base64, place in glass card frames
- **Mixed** → interleave content and chart slides; hero opens, summary closes

Ask clarifying questions ONLY if the topic and structure are completely unclear.
For most inputs you can proceed directly.

### Step 2 — Plan the slide structure

Before writing code, sketch the slide plan:

```
Slide 0 (Hero):    Title, subtitle, 3–4 stat pills
Slide 1:           [Topic A] — layout template?
Slide 2:           [Topic B] — layout template?
...
Slide N (Summary): Key takeaways / next steps
```

Aim for 6–12 slides. More than 12 = too dense; fewer than 5 = too thin.

### Step 3 — Build the HTML

1. Start with the full document skeleton from `references/js-system.md`
2. Apply CSS design tokens from `references/design-system.md`
3. Build each `<section data-index="N">` from templates in `references/slide-templates.md`
4. Add SVG charts from `references/chart-templates.md` where needed
5. Populate SLIDE_FIELDS in the edit mode JS to cover every slide's text

### Step 4 — Verify before delivering

Run through the checklist mentally (or use `scripts/validate_output.py` on the file):

- [ ] Every `<section>` has a unique `data-index`
- [ ] Key display elements have `data-in` for stagger animation
- [ ] Navigation JS auto-generates dots for all slides
- [ ] Edit mode sidebar: SLIDE_FIELDS covers every slide
- [ ] No `<link>`, `<script src>`, or `<img src="http...">` tags
- [ ] Charts animate only when their slide is `.active`
- [ ] All text is in HTML (not SVG text only) — makes it editable
- [ ] Layout constraints verified per slide (see below)

---

## Input Processing Guide

### Plain text / bullet points
- Map top-level headings → slide titles + eyebrow tags
- Group 3–5 bullet points → `.card` list items or grid cells
- Extract standalone numbers / percentages → stat banner or large number callout
- Identify contrast pairs (before/after, pro/con) → Template B 2-column

### Data tables / CSV / numbers
- Single metric trend → line chart
- Before/after or ranking → bar chart
- Category breakdown / share → donut chart
- Put raw values in SVG data points; compute delta for badge labels (+X%)

### Images
- Encode to base64: `data:image/[type];base64,[data]`
- Wrap in: `<img src="..." style="width:100%;border-radius:24px;object-fit:cover">`
- Place inside `.card` or as left column in a 6:4 layout
- Add a frosted caption overlay with `position:absolute; bottom:0`

### Mixed (text + data + images)
- Images → their own slide or left-column hero
- Data → dedicated chart slide (Template D)
- Text → surrounding context slides
- Narrative flow: Problem → Evidence → Solution → Result → Action

---

## Layout Constraints (enforce on every slide)

| Constraint | Rule |
|---|---|
| Equal height | `align-items:stretch` on grid parent; never let one column be shorter |
| Screen coverage | Core content occupies 75–85% of viewport height |
| Visual balance | Left–right weight difference ≤ 15%; heavier side gets narrower column |
| Responsive | Grids collapse to 1 column below 960px via `@media` block |

After generating each slide, add a one-line layout note in your thinking:
> "Layout: 6:4 · ~80% screen height · whitespace top 8% bottom 12%"

---

## Slide Container CSS (always include in `<style>`)

```css
html, body { height:100%; overflow:hidden; }
.deck { height:100vh; overflow:hidden; position:relative; z-index:1; }
section {
  position:absolute; inset:0;
  display:flex; align-items:center; justify-content:center;
  padding:72px 48px;
  opacity:0; pointer-events:none;
  transform:translateY(48px) scale(.97);
  transition: opacity .65s cubic-bezier(.25,.46,.45,.94),
              transform .65s cubic-bezier(.25,.46,.45,.94);
  will-change:opacity,transform;
}
section.active { opacity:1; pointer-events:auto; transform:translateY(0) scale(1); }
section.prev   { opacity:0; transform:translateY(-48px) scale(.97); }
[data-in] { opacity:0; transform:translateY(18px);
  transition: opacity .55s cubic-bezier(.25,.46,.45,.94),
              transform .55s cubic-bezier(.25,.46,.45,.94); }
[data-in].visible { opacity:1; transform:translateY(0); }
section:not(.active) svg * { animation-play-state:paused !important; }
.container { width:100%; max-width:1220px; margin:0 auto; }
```

---

## Naming & Delivery

- Save to the path the user specifies, or to the same directory as their input file
- Default filename: `[topic]-presentation.html`
- After saving, report: file path, total slides, and any layout notes per slide
- If asked to modify slide N: find the `section[data-index="N"]`, edit in place,
  re-verify layout constraints, re-run validate script if available
