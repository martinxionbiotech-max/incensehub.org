# KNOWLEDGE-GRAPH.md — IncenseHub

Semantic relationship graph. One record per meaningful relationship. This file is the human-readable seed; the structured-data layer (Schema.org) expresses the same graph for machines.

## Core chain

```
Ingredient → Botanical Source → Material → Processing → Aroma
  → Formula → Incense → Tradition → Use Case → Product → Wholesale → OEM
```

## Cross-links

```
Ingredient ↔ Material ↔ Article ↔ Research ↔ Culture ↔ Terminology ↔ Product
```

## Relationship types

| Relation | Meaning | Example |
|---|---|---|
| `has_botanical_source` | ingredient ← botanical | Agarwood ← *Aquilaria* |
| `yields` | botanical → material | *Aquilaria* → agarwood chips |
| `processed_by` | material → processing | chips → powder (grinding) |
| `has_aroma` | material → aroma | agarwood → woody/resinous/sweet |
| `composed_of` | formula → ingredients | 合香 → agarwood + sandalwood + ... |
| `produced_as` | formula → format | formula → stick / cone |
| `used_in_tradition` | ingredient → tradition | agarwood → 香道 |
| `serves_use_case` | incense → use case | evening incense → evening ritual |
| `offered_as` | formula → product | formula → SKU |
| `sold_via` | product → commercial | SKU → wholesale / OEM |
| `related_to` | loose association | sandalwood ↔ agarwood |

## Seed relationships (P0)

- Agarwood `has_botanical_source` *Aquilaria* spp.
- *Aquilaria* `yields` agarwood resin wood
- Agarwood `has_aroma` woody / resinous / sweet
- Agarwood `used_in_tradition` 香道
- Agarwood `related_to` Sandalwood (both premium wood/resin materials)
- Sandalwood `has_botanical_source` *Santalum album*
- Mugwort `has_botanical_source` *Artemisia* spp.
- Mugwort `related_to` Herbal incense (herbal subset)
- 合香 (formula) `composed_of` multiple ingredients
- Incense stick `produced_as` 线香
- Product `sold_via` Wholesale / OEM

## Maintenance rules

- Every entity page must declare its relationships (parent / siblings / children / related).
- A relationship is added only when it is factually defensible (traceable source).
- The graph is a living model — updated as research and materials arrive.
