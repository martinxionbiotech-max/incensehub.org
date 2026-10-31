# DEMAND-MODEL.md — IncenseHub

Schema for demand intelligence. Demand ≠ keyword. A keyword is a string; demand is a problem, question, or commercial intent behind it.

## Fields

| Field | Meaning |
|---|---|
| Demand ID | stable ID (D-###) |
| Query | query or query cluster |
| Language | en (primary) |
| Source | where demand was observed |
| Search intent | informational / commercial / transactional / navigational |
| Entity | primary entity |
| Question | the underlying question |
| Pain point | problem to solve |
| Commercial intent | low / medium / high |
| Topic | topic cluster |
| Existing page | if any |
| Missing asset | what we lack |
| Information gap | knowledge gap |
| Content opportunity | asset to create |
| Research opportunity | research to run |
| Commercial opportunity | commercial bridge |
| Priority | P0–P3 |
| Status | proposed / validated / built / live |
| Last reviewed | date |

## Demand sources

- **Google:** Search Console (later), autocomplete, People Also Ask, related searches, trends
- **Communities:** Reddit, Quora, forums, reviews, YouTube comments
- **Commercial:** product reviews, customer questions, marketplace/wholesale/OEM terminology
- **Chinese ecosystem:** Baidu/Sogou/360, forums, industry sites, academic/historical sources
- **First-party:** inquiries, quote/sample requests, sales questions (later)

## Rules

- **Do not equate keyword = demand.**
- Consolidate trivial query variations into authoritative resources (do not create a page per query).
- Every demand record must identify: question, problem, intent, entity, and a concrete next asset.
