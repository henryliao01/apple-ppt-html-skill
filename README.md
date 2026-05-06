# apple-ppt-html — Claude Code Skill

A Claude Code skill that generates **Apple-style interactive HTML slide decks** — frosted glass cards, radial gradient backgrounds, SVG charts with animations, smooth slide transitions, and a built-in text edit mode.

## Preview

Each generated deck is a **single self-contained `.html` file** with all CSS, JS, SVG, and images inlined. No internet connection required to view.

Design language: squircle cards, backdrop-filter blur, SF Pro Display font, blue-purple radial gradient, animated `data-in` entrance effects.

## Installation

**Option A — npm (Node.js 16+ required):**

```bash
npm install -g github:henryliao01/apple-ppt-html-skill
```

**Option B — git clone (recommended, no npm needed):**

```bash
# Mac / Linux
git clone https://github.com/henryliao01/apple-ppt-html-skill ~/.claude/skills/apple-ppt-html

# Windows PowerShell
git clone https://github.com/henryliao01/apple-ppt-html-skill "$env:USERPROFILE\.claude\skills\apple-ppt-html"
```

Restart Claude Code after installation.

**Update (git clone方式):**

```bash
cd ~/.claude/skills/apple-ppt-html && git pull
```

### Uninstall

```bash
rm -rf ~/.claude/skills/apple-ppt-html
```

## Usage

Just describe your presentation in plain language. The skill triggers automatically when you mention slide decks, PPT, presentations, or HTML reports.

**Examples:**

```
帮我做一个季度复盘PPT，主题是Q2增长分析，数据是…
```

```
Generate an Apple-style HTML deck for our product launch.
5 slides: hero, features, pricing, roadmap, CTA.
```

```
做一个带折线图和环形图的数据分析汇报，毛玻璃风格
```

The output is a single `.html` file you can open in any browser and edit inline.

## What's included

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill instructions |
| `references/design-system.md` | Full CSS design tokens, glass cards, typography |
| `references/slide-templates.md` | 7 layout templates (hero, 2-col, 4-card, chart, pipeline…) |
| `references/chart-templates.md` | SVG chart types + animation keyframes |
| `references/js-system.md` | Navigation JS, edit mode, localStorage |
| `scripts/validate_output.py` | 13-point output validator |

## Features

- **7 slide layouts** — hero, 2-column, 4-card grid, chart+insight, pipeline steps, tag cards, compact summary
- **4 chart types** — line (animated stroke), bar (before/after), donut/ring, flow diagram
- **Edit mode** — sidebar with text/color pickers, persisted to localStorage, one-click HTML download
- **Keyboard navigation** — arrow keys, mouse wheel, touch swipe
- **Zero dependencies** — no CDN, no external fonts, works offline

## License

MIT
