# IMAGE-PROMPTS.md — IncenseHub

Generation prompts for the 30 images in IMAGE-MANIFEST.md, aligned with DESIGN-SYSTEM.md (color tokens) and ART-DIRECTION.md (editorial photography, "lantern on the waves" motif, restrained palette).

## Universal style block (prepend or append to every prompt)

```
Editorial photography for a premium Chinese incense brand (澜灯 IncenseHub).
Palette: warm off-white rice paper (#faf7f1), muted amber (#b07a3f), muted sage (#5c7260),
deep charcoal (#1c1a17), warm wood (#8a6b4f). Restrained magazine-editorial composition,
generous negative space, subtle "lantern glow over still water" mood. Realistic textures
(wood, bronze, ceramic, botanical). Soft natural window light. Medium-format look, shallow
depth of field, 8k detail.
Negative: no text, no watermark, no logo, no people, no neon, no oversaturated colors,
no cluttered background.
```

Aspect-ratio settings per image: 16:9 → `--ar 16:9` · 1200×630 → `--ar 1.91:1` · 800×800 → `--ar 1:1` · 800×600 → `--ar 4:3` · 800×533 → `--ar 3:2`.

## P0 — 15 prompts

1. `home-hero-incense-smoke-1600x900.webp` (16:9)
   A thin spiral of incense smoke rising from a small dark ceramic censer on a dark wood table; warm amber glow from one side, deep charcoal background, fine smoke detail, minimalist composition with generous empty space on the left for headline text.

2. `og-image-incense-still-life-1200x630.jpg` (1.91:1)
   Overhead still life of Chinese incense tools on rice paper: a small bronze censer, several incense sticks, a tiny porcelain dish of wood powder; muted amber and sage tones, soft diffuse daylight, clean editorial composition.

3. `chinese-incense-sticks-bundle-1200x675.webp` (16:9)
   A bundle of hand-made Chinese incense sticks tied with natural cotton twine, lying diagonally on warm rice-paper background; macro texture of the stick surface, soft window light, shallow depth of field.

4. `boshan-censer-bronze-han-1200x675.webp` (16:9)
   Ancient Chinese Boshan bronze mountain censer (博山炉), Han-dynasty style, wisps of smoke rising from the mountain-shaped lid; dark charcoal background, warm amber rim light, museum-grade editorial product photography.

5. `scent-wheel-fragrance-families-800x800.webp` (1:1, flat diagram)
   Circular fragrance-wheel diagram in muted editorial palette — segments in cream, muted amber, sage and soft brown; clean flat vector style, no labels, subtle rice-paper texture background, perfectly centered.

6. `agarwood-grades-sinking-floating-1200x675.webp` (16:9)
   Several small pieces of agarwood arranged on neutral sage cloth in two clearly separated groups — dense dark sinking-grade pieces and lighter floating-grade pieces; macro detail of resin veins, soft diffused light, documentation-editorial style.

7. `qinan-agarwood-closeup-1200x675.webp` (16:9)
   Extreme close-up of qinan agarwood surface showing rich resin veins and oily texture; warm amber side lighting on deep charcoal, luxury macro product photography, razor-sharp focus.

8. `incense-formats-lineup-sticks-coils-cones-1600x675.webp` (16:9)
   A neat editorial lineup of incense formats on warm rice paper — sticks, a spiral coil, a backflow cone, a small mound of powder — evenly spaced left to right; soft daylight, muted palette, minimalist museum-display style.

9. `burn-time-matrix-chart-800x600.webp` (4:3, flat diagram)
   Minimalist horizontal bar infographic comparing incense burn times by format; cream background, muted amber and sage bars, clean flat style, no labels, subtle paper texture.

10. `incense-seal-stamp-tools-1200x675.webp` (16:9)
    Chinese incense seal (香篆): a brass seal template and a small wooden tamper resting beside a freshly pressed incense-powder pattern on rice paper; warm soft light, editorial still life, muted amber and charcoal.

11. `censer-porcelain-song-style-1200x675.webp` (16:9)
    A Song-dynasty-style celadon porcelain censer with subtle crackle glaze and a faint smoke trail; warm off-white background with soft sage accents, gentle window light, refined museum photography.

12. `evening-ritual-incense-tea-desk-1200x675.webp` (16:9)
    A quiet evening scene: a tea cup, a small censer with a thin line of smoke, an open book on a dark wood desk lit by one warm lamp; deep shadows, amber glow, cozy editorial lifestyle photography.

13. `japanese-kodo-ceremony-1200x675.webp` (16:9)
    Japanese kodo ceremony utensils — a small koro burner, mica plate and kodo tools arranged precisely on tatami against a neutral paper backdrop; restrained minimal composition, soft diffused light, documentary-editorial style.

14. `recipe-ingredients-still-life-1600x675.webp` (16:9)
    Wide still life of Chinese incense ingredients on rice paper: sandalwood chips, agarwood pieces, dried botanicals, a small brass scale, ceramic dishes arranged in a gentle arc; muted amber/sage/charcoal palette, soft daylight.

15. `hexiang-blending-ingredients-1200x675.webp` (16:9)
    Flat lay of incense blending: a brass balance scale weighing aromatic wood powder, small dishes of resins and botanicals, paper and calligraphy brush in the background; warm editorial tones, hands not visible.

## P1 — 10 prompts

16. `sandalwood-powder-wood-1200x675.webp` — Sandalwood powder in a shallow ceramic dish beside a raw sandalwood block; macro grain detail, warm wood tones, soft side light.
17. `meditation-incense-minimal-1200x675.webp` — One incense stick in a tiny ceramic holder on an empty warm-white surface, single thin smoke line; extreme minimalism, zen negative space, soft morning light.
18. `incense-quality-indicators-closeup-1200x675.webp` — Macro of a premium incense stick: even coating, fine powder texture, clean burn line, pale ash; documentation style, neutral background.
19. `hand-rolled-vs-machine-made-comparison-1200x675.webp` — Two incense sticks side by side on rice paper: one irregular hand-rolled, one perfectly uniform machine-made; macro comparison, soft light, editorial product photography.
20. `recipe-baizi-cypress-seeds-800x533.webp` — A small pile of cypress seeds in a ceramic dish with a few seeds scattered; warm muted tones, rustic editorial still life.
21. `recipe-xuezhong-chunxin-plum-800x533.webp` — Plum blossoms on a winter branch beside a small censer with smoke; cold cream background with a single warm amber accent, poetic Song-dynasty mood.
22. `recipe-shouyang-plum-blossom-800x533.webp` — Plum blossom petals with small dishes of pale aromatic powders; soft feminine palette of cream and faint pink, delicate editorial styling.
23. `recipe-jiangnan-pear-bedchamber-800x533.webp` — A pear and subtle bedchamber incense props (small censer, silk cloth) in soft window light; intimate warm still life.
24. `recipe-lotus-summer-800x533.webp` — Lotus pod and summer aromatics in a ceramic dish, fresh sage-green accents on warm paper; light summery editorial still life.
25. `regional-incense-map-asia-1200x675.webp` — Minimalist flat map illustration of Asia with soft amber and sage region markers; cream background, subtle dotted travel lines, no labels.

## P2 — 5 prompts

26. `incense-history-timeline-artifacts-1600x675.webp` — A wide editorial banner of incense-related artifacts across eras (bronze censer, porcelain burner, carved wooden tools) on a dark neutral shelf, soft museum lighting, chronological left-to-right arrangement.
27. `four-leisure-arts-ensemble-1200x675.webp` — The four leisure arts ensemble: incense, tea, a hanging scroll and an ikebana-style flower arrangement on a scholar's desk; warm amber and sage palette, Song-dynasty aesthetic.
28. `recipe-ersu-jiuju-tea-incense-800x533.webp` — Tea incense theme: tea leaves and a small mound of incense powder in matching ceramic dishes; warm kitchen-scholar mood, soft daylight.
29. `recipe-huarui-yamen-800x533.webp` — Court incense theme: refined agarwood pieces and small gold-accented dish on dark silk; subtle luxury, deep charcoal with muted amber highlights.
30. `wholesale-packaging-boxes-1200x675.webp` — Neutral kraft export packaging boxes with plain paper wrap on a warehouse table, one box open showing foam packing; honest documentary style, no branding (real photos only).

## Tool settings
- Midjourney: append `--ar` values above + `--style raw --v 6` (or 6.1) for the photographic ones; diagrams use `--style raw --no text`.
- DALL-E 3 / GPT-4o image: set the aspect in the tool UI; paste the style block + image prompt + "no text" instruction.
- Flux/Stable Diffusion: use the negative prompt line verbatim; photorealistic models recommended.
