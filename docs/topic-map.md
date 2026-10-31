# Topic Map — Cluster Architecture (Based on Actual Content)

> Audit-only. Reconstructed from actual `pillar` / `cluster_role` frontmatter + page routes.

## Top-level conceptual map

The site's actual content maps cleanly onto the §11 target architecture:

```
Chinese Botanical Incense  (concept: /chinese-incense/)
│
├── Ingredients          → /ingredients/ + 150 entity pages (type: ingredient)
│
├── Materials            → P10 hub "How Incense Is Made" + materials.json (15) — partial
│
├── Terminology          → /blog/incense-terminology-glossary + terminology.json (249)
│
├── Aroma                → P2 "Scent Guide" + scent-wheel + aroma.json (10 families)
│
├── Incense Forms        → P4 "Which Incense Format" + forms.json (12)
│
├── Manufacturing        → P10 "How Incense Is Made" + techniques.json (12)
│
├── Techniques           → P10 (gehuo-fenxiang-setup, incense-seal-zhuanxiang) + techniques.json
│
├── Quality              → P5/P6/P10 QC + authentication content
│
├── Authentication       → P10 incense-authentication-database + qinan-buying-authentication
│
├── History & Culture    → P1 history + P8 regional + P12 culture
│
├── Comparisons          → P7 "Incense vs Alternatives" + P2 comparison-matrix + comparisons.json (17)
│
├── Safety               → /safety/ + P6 "Incense Safety Guide"
│
├── Buying Guides        → P5 "How to Choose Incense" + Commercial cluster
│
├── Wholesale            → /wholesale/ + wholesale-guide
│
└── OEM                  → /oem/ + oem-private-label-guide + custom-fragrance-development
```

## Pillar → hub → spokes (actual, from `cluster_role`)

| Pillar (cluster) | Hub (pillar page) | Spokes |
|---|---|---|
| P1 Chinese Incense 101 | what-is-chinese-incense | 4 articles/glossary/reference |
| P2 Scent & Ingredient Guide | scent-guide | 11 (incl. 2 data_asset) |
| P3 Use Scenarios | scent-by-intention | 4 |
| P4 Product Formats & Tools | which-incense-format | 14 |
| P5 Buying & Selection | how-to-choose-incense | 4 |
| P6 Care & Safety | incense-safety-guide | 5 |
| P7 Incense vs Alternatives | incense-vs-candles-vs-diffusers | 4 |
| P8 Regional Incense Traditions | world-incense-traditions | 4 |
| P9 Chinese Incense Recipes (香方) | chinese-incense-recipes | 7 |
| P10 Incense Craft & Materials | how-incense-is-made | 10 |
| P11 Aromatherapy & Botany | how-aromatherapy-works | 3 |
| P12 Culture & Mindfulness | incense-in-daily-ritual | 4 |
| Commercial B2B Buying & Supply | incense-for-business | 10 |
| Editorial & Data | — | 2 |

**13 hubs** (one per pillar cluster + concept). Every cluster has exactly one `hub` except Editorial & Data.

## Coverage vs §11 target architecture — gaps

| §11 target | Actual status |
|---|---|
| Ingredients | ✅ fully covered (150 entities) |
| Materials | ⚠️ partial — P10 covers craft materials; dedicated material taxonomy page absent (materials.json has 15 records, no matching content collection) |
| Terminology | ✅ glossary + 249-term dataset (no dedicated content collection) |
| Aroma | ✅ scent-guide + scent-wheel + 10 aroma families |
| Incense Forms | ✅ P4 + forms.json (12) |
| Manufacturing | ✅ P10 hub |
| Techniques | ⚠️ partial — techniques.json (12) exists; content is embedded in P10/P4 how_tos |
| Quality | ✅ P5/P6/P10 QC |
| Authentication | ✅ P10 |
| History & Culture | ✅ P1/P8/P12 |
| Comparisons | ✅ P7 + comparison-matrix + comparisons.json |
| Safety | ✅ /safety/ + P6 |
| Buying Guides | ✅ P5 + Commercial |
| Wholesale | ✅ |
| OEM | ✅ |

## Missing structural bridge (not a content gap, a navigation gap)

The **Materials / Techniques / Forms / Aroma** data-site taxonomies are not surfaced as navigable hub pages on the main site — they exist only inside blog articles and the data-site JSON. This is the single largest structural disconnect between the "knowledge graph" layer (data site) and the "content" layer (main site).
