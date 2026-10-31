# IMAGE-MANIFEST.md — IncenseHub

Image requirements for the IncenseHub site. Each entry: **exact filename** (must match for wiring), **dimensions**, page/placement, and what the image should show.

## Naming & format rules
- Filenames are the contract — images are wired by exact filename.
- Format: photography → `.jpg` (or `.webp` if available); charts/diagrams → `.png` (re-encoded to `.webp` for the >300 KB lossy-compression pass — see §45/G17).
- Deliver files into `public/images/` (ask the operator to provide the matching files).
- Aspect ratios: 16:9 (content/hero) · 3:2 (recipes) · 4:3 (charts) · 1:1 (wheel) · og 1.91:1.

## P0 — Must-have (15)

| # | Filename | Dimensions | Page | Shows |
|---|---|---|---|---|
| 1 | `home-hero-incense-smoke-1600x900.webp` | 1600×900 | Home hero | Incense smoke / 香道 scene, dark background |
| 2 | `og-image-incense-still-life-1200x630.jpg` | 1200×630 | Site-wide OG/share | Incense tools + sticks still life |
| 3 | `chinese-incense-sticks-bundle-1200x675.webp` | 1200×675 | what-is-chinese-incense | Bundle of Chinese incense sticks |
| 4 | `boshan-censer-bronze-han-1200x675.webp` | 1200×675 | boshan-censer | Boshan mountain censer (Han style bronze) |
| 5 | `scent-wheel-fragrance-families-800x800.webp` | 800×800 | scent-guide | Fragrance wheel diagram (woody/floral/citrus/resinous…) |
| 6 | `agarwood-grades-sinking-floating-1200x675.webp` | 1200×675 | agarwood-grading-guide | Agarwood pieces, sinking vs floating grades |
| 7 | `qinan-agarwood-closeup-1200x675.webp` | 1200×675 | qinan-buying-authentication | Qinan agarwood close-up, texture |
| 8 | `incense-formats-lineup-sticks-coils-cones-1600x675.webp` | 1600×675 | which-incense-format (hub) | Lineup: sticks, coils, cones, powder |
| 9 | `burn-time-matrix-chart-800x600.webp` | 800×600 | incense-burn-time-format-matrix | Burn-time comparison chart |
| 10 | `incense-seal-stamp-tools-1200x675.webp` | 1200×675 | incense-burners-tools | 香篆 seal + stamping tools |
| 11 | `censer-porcelain-song-style-1200x675.webp` | 1200×675 | incense-burners-tools | Song-style porcelain censer |
| 12 | `evening-ritual-incense-tea-desk-1200x675.webp` | 1200×675 | calming-evening-ritual | Evening desk: incense + tea + warm light |
| 13 | `japanese-kodo-ceremony-1200x675.webp` | 1200×675 | japanese-incense-kodo | Kodo ceremony utensils |
| 14 | `recipe-ingredients-still-life-1600x675.webp` | 1600×675 | chinese-incense-recipes (hub) | Botanical ingredients still life (woods, resins, spices) |
| 15 | `hexiang-blending-ingredients-1200x675.webp` | 1200×675 | hexiang-blending-system | 合香 blending ingredients + scale |

## P1 — Enhancement (10)

| # | Filename | Dimensions | Page | Shows |
|---|---|---|---|---|
| 16 | `sandalwood-powder-wood-1200x675.webp` | 1200×675 | sandalwood-incense | Sandalwood powder + wood |
| 17 | `meditation-incense-minimal-1200x675.webp` | 1200×675 | incense-for-meditation | Minimal incense setting |
| 18 | `incense-quality-indicators-closeup-1200x675.webp` | 1200×675 | how-to-choose-incense | Stick close-up: ash, color, material quality |
| 19 | `hand-rolled-vs-machine-made-comparison-1200x675.webp` | 1200×675 | hand-rolled-vs-machine-made | Two stick types side by side |
| 20 | `recipe-baizi-cypress-seeds-800x533.webp` | 800×533 | baizi-incense-recipe | Cypress seeds / 柏子 |
| 21 | `recipe-xuezhong-chunxin-plum-800x533.webp` | 800×533 | xuezhong-chunxin-recipe | Plum blossom winter theme |
| 22 | `recipe-shouyang-plum-blossom-800x533.webp` | 800×533 | shouyang-princess-plum-recipe | Plum blossom + aromatics |
| 23 | `recipe-jiangnan-pear-bedchamber-800x533.webp` | 800×533 | jiangnan-lizhu-bedchamber-recipe | Pear / bedchamber incense theme |
| 24 | `recipe-lotus-summer-800x533.webp` | 800×533 | lotus-incense-recipe | Lotus / summer theme |
| 25 | `regional-incense-map-asia-1200x675.webp` | 1200×675 | world-incense-traditions | Map or regional collage |

## P2 — Optional (5)

| # | Filename | Dimensions | Page | Shows |
|---|---|---|---|---|
| 26 | `incense-history-timeline-artifacts-1600x675.webp` | 1600×675 | history-of-chinese-incense | Timeline banner with artifacts |
| 27 | `four-leisure-arts-ensemble-1200x675.webp` | 1200×675 | four-leisure-arts | 焚香点茶挂画插花 ensemble |
| 28 | `recipe-ersu-jiuju-tea-incense-800x533.webp` | 800×533 | ersu-jiuju-recipe | Tea incense theme |
| 29 | `recipe-huarui-yamen-800x533.webp` | 800×533 | huarui-furen-yamen-recipe | Court incense theme |
| 30 | `wholesale-packaging-boxes-1200x675.webp` | 1200×675 | packaging-shipping-guide | Export packaging boxes (real photos only) |

## Wiring notes
- Charts (#5 scent wheel, #9 burn-time matrix) may also be rendered as inline HTML/SVG — images complement, not replace.
- Commercial pages: use **real product/packaging photos only**; no stock "factory" imagery implying false claims.
- Alt text will be generated from the table's "Shows" column at wiring time.
