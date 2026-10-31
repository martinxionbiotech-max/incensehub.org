# SEO-MASTER-MAP.md — IncenseHub

Single ledger mapping **demand → intent → entity → page**. One row per validated opportunity. Rows are added only after passing the demand-intelligence + information-gain gate (see CONTENT-GOVERNANCE.md).

## Schema

| Field | Meaning |
|---|---|
| Keyword / query | Search query (or query cluster) |
| Language | en (primary) |
| Search intent | informational / commercial / transactional / navigational |
| Topic | Topic cluster |
| Entity | Primary entity |
| Page type | Encyclopedia / Guide / Comparison / Product / etc. |
| Primary URL | Target path |
| Parent topic | Parent in the pillar-cluster hierarchy |
| Supporting topics | Children / supporting pages |
| Related entities | Entities to link |
| Commercial relevance | low / medium / high |
| AIO potential | low / medium / high |
| Original info opportunity | What we can add that others don't have |
| Chinese-source opportunity | Gap the Chinese ecosystem can fill |
| Competition | low / medium / high |
| Priority | P0 / P1 / P2 / P3 |
| Status | proposed / researched / building / live |

## Seed rows (P0 entities — to validate before build)

| Keyword | Intent | Entity | Page type | URL | Status |
|---|---|---|---|---|---|
| what is chinese incense | informational | Chinese incense | Pillar | /chinese-incense/ | proposed |
| what is agarwood / chenxiang | informational | Agarwood | Encyclopedia | /ingredients/agarwood/ | proposed |
| sandalwood incense | informational+commercial | Sandalwood | Encyclopedia | /ingredients/sandalwood/ | proposed |
| how to burn incense sticks | informational | Incense sticks | Guide | /incense-sticks/ | proposed |
| chinese incense vs japanese incense | comparison | Chinese incense | Comparison | /learn/comparisons/ | proposed |
| incense cones vs sticks | comparison | Formats | Comparison | /learn/comparisons/ | proposed |
| is incense smoke safe | informational | Safety | Guide | /learn/safety/ | proposed |
| herbal incense ingredients | informational | Ingredients | Encyclopedia index | /ingredients/ | proposed |
| incense wholesale | commercial | Wholesale | Commercial | /wholesale/ | proposed |
| private label incense manufacturer | commercial | OEM | Commercial | /oem/ | proposed |

## Research-informed refinements (2026-09-08)

- **Agarwood** is the highest-value P0 entity: strong demand + the clearest Chinese/English gap (奇楠 vs 沉香, 沉水 grading, 油包木 vs 木包油, adulteration). Original angle: an English resource that explains Chinese grading/terminology authoritatively + honest buyer-authentication guidance.
- **Sandalwood** opportunity is **evidence governance**, not "more benefits content": the SERP is flooded with unproven health claims — we differentiate by honest traditional-use-vs-evidence framing.
- **"chinese incense" pillar**: the SERP is thin retail blogs; a genuinely authoritative encyclopedia with entity depth + first-party data is the gap.

> **Do not mass-expand this list.** Each row is validated individually (demand + information gap + originality + commercial relevance) before any page is created.
