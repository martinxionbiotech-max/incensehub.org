# DESIGN-SYSTEM.md — IncenseHub

Design tokens and foundations. Values are starting points to be refined in implementation.

## Color tokens (light theme, premium editorial)

| Token | Role | Value (candidate) |
|---|---|---|
| `--ink` | primary text | deep charcoal `#1c1a17` |
| `--ink-soft` | secondary text | `#55514a` |
| `--paper` | page background | warm off-white `#faf7f1` (rice paper) |
| `--paper-raise` | card surface | `#ffffff` |
| `--line` | borders/dividers | `#e7e0d4` |
| `--amber` | accent (灯 / glow) | `#b07a3f` (muted amber, not loud gold) |
| `--amber-soft` | accent tint | `#f1e4d2` |
| `--jade` | botanical secondary | `#5c7260` (muted sage) |
| `--wood` | warm neutral | `#8a6b4f` |
| `--danger` | safety/alerts | `#a33d2f` |

Dark theme tokens deferred (define at implementation; keep contrast ≥ AA).

## Typography

- **Display / headings:** editorial serif (e.g. Source Serif 4 / Fraunces) — for brand + editorial gravitas.
- **Body / UI:** clean humanist sans (e.g. Inter / Source Sans 3) — readability, scientific neutrality.
- **Chinese glyphs:** fall back to a CJK serif (Noto Serif SC) for inline Chinese terms; render as regular weight, not decorative.

Type scale: modular 1.25 ratio; body ~16–18px; generous line-height (1.6–1.75).

## Spacing & layout

- 8px grid; generous section spacing (editorial air).
- Max content width ~720px for long-form reading; wider grids for catalogs/tables.
- Whitespace is a design element — avoid clutter.

## Elevation & texture

- Flat, minimal shadows; prefer hairline borders over heavy elevation.
- Subtle paper/grain texture optional, never noisy.

## Motion

- Minimal; only where it aids comprehension. No gratuitous animation.

## Accessibility baseline

- Contrast ≥ WCAG AA (4.5:1 body, 3:1 large).
- Focus states visible; semantic HTML; RTL-ready where Arabic/localized content may appear later.
