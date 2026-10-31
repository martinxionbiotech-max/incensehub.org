# ORIGINAL-DATA-ASSETS.md — IncenseHub

IncenseHub becomes a first-party knowledge database over time. Each dataset is a machine-readable, link-worthy asset. **All data must be accurate, traceable, structured, maintainable, reviewable.**

## Planned datasets

### 1. Ingredient database
`Ingredient · Botanical source · Scientific name · Origin · Aroma · Traditional context · Processing · Burning characteristics · Safety · Evidence`

### 2. Material database
`Material · Type · Source · Processing · Physical characteristics · Aroma · Burning behavior · Applications`

### 3. Aroma database
`Woody · Resinous · Sweet · Herbal · Spicy · Floral · Citrus · Earthy · Smoky · Balsamic`

### 4. Terminology database
`Chinese · Pinyin · English · Literal meaning · Preferred translation · Context`

### 5. Comparison database
`Material · Aroma · Smoke · Burn characteristics · Traditional context · Common uses · Quality factors`

## Format

- JSON (Schema.org `Dataset` + `DefinedTerm` / `Product`), served at stable URLs (e.g. `/data/ingredients.json`).
- Build-time static generation; no runtime database in Phase 1.
- Advertised via `llms.txt` + `_headers` (`Content-Signal`, `Link: describedby`).

## Governance

- **Never expose** sensitive or proprietary data.
- **Never fabricate** data to fill a dataset — thin/small data stays thin/small.
- Each dataset row keeps provenance where possible.
- Update date + versioning are tracked.

> Build order: terminology → ingredient → material → aroma → comparison, each gated by verified source data.
