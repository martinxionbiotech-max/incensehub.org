# ENTITY-MODEL.md — IncenseHub

Canonical entity definitions. Every entity has a stable ID, a set of names/aliases, and typed relationships. This file is the seed; the full graph lives in KNOWLEDGE-GRAPH.md and the structured data layer.

## Entity types

| Type | Example |
|---|---|
| Ingredient | Agarwood 沉香 |
| Botanical source | *Aquilaria* trees |
| Material | Agarwood chips / powder |
| Processing | drying, grinding, blending |
| Aroma | woody, resinous, sweet |
| Formula | a combined incense recipe (合香) |
| Incense format | stick / cone / sachet |
| Tradition | 香道 (incense ceremony) |
| Use case | meditation, evening ritual |
| Product | a commercial SKU |
| Commercial | wholesale, OEM, private label |

## Seed entities (P0)

### Chinese Botanical Incense (core entity)
- **Chinese:** 香 / 熏香 / 合香
- **Type:** Domain / concept
- **Not:** a medical treatment, a sleep aid, an anxiety remedy.

### Agarwood (沉香)
- **Scientific:** *Aquilaria* spp. (resin-bearing)
- **Aroma:** woody, resinous, sweet, complex
- **Chinese terms:** 沉香 (chénxiāng), 奇楠 (qínán, top grade)
- **Relations:** botanical → resin material → incense → tradition → product → wholesale

### Sandalwood (檀香)
- **Scientific:** *Santalum album* (and other spp.)
- **Aroma:** creamy, sweet, woody
- **Chinese:** 檀香 (tánxiāng)

### Mugwort (艾草)
- **Scientific:** *Artemisia* spp.
- **Aroma:** herbal, bitter-green
- **Chinese:** 艾草 (àicǎo), 艾 (ài)

### Frankincense (乳香) / Myrrh (没药)
- **Scientific:** *Boswellia* / *Commiphora*
- **Type:** gum-resins (imported into Chinese incense tradition)

### Floral / citrus / spice botanicals
Osmanthus 桂花 · Jasmine 茉莉 · Rose 玫瑰 · Chrysanthemum 菊花 · Orange peel 陈皮 · Clove 丁香 · Cinnamon 桂皮 · Benzoin 安息香 · Cedar 雪松 · Vetiver 岩兰草 · Patchouli 广藿香.

## Entity fields (per entity, when a page is built)

- ID · Name · Slug · Aliases · Chinese term · Pinyin · Scientific name · Botanical family
- Origin · Geographic distribution · Aroma profile · Aroma notes
- Traditional context · Historical context · Incense use · Processing · Burning characteristics
- Sourcing · Quality factors · Adulteration notes · Storage · Safety · Evidence level
- Related materials · Related ingredients · Related articles · Related research · Related products

> **Do not mass-create ingredient pages.** Each requires verified content + a passing Content Quality Gate. Entities above are candidates, not commitments.
