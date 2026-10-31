# DEMAND-INVENTORY.md — IncenseHub

Demand ledger. Populated from real demand research (SERP + community + Chinese-source), not guessed keyword lists. The **Covering page(s)** column maps each demand to the live page(s) that satisfy it (see [CONTENT-INVENTORY.md](CONTENT-INVENTORY.md) for the full ledger). `—` = no live page yet (still proposed/backlog).

| Demand ID | Query | Intent | Entity | Question | Missing asset | Priority | Status | Covering page(s) |
|---|---|---|---|---|---|---|---|---|
| D-001 | what is chinese incense | informational | Chinese incense | what it is / types / history | authoritative encyclopedia (SERP = thin retail blogs) | P0 | validated | `what-is-chinese-incense` (hub) · `chinese-incense` (concept) |
| D-002 | what is agarwood / chen xiang | informational | Agarwood | what it is, how it forms, grading | entity page + Chinese grading depth (奇楠/沉水) | P0 | validated | `agarwood` (entity) · `agarwood-grading-guide` |
| D-003 | agarwood vs sandalwood | comparison | Agarwood/Sandalwood | premium wood comparison | comparison page | P1 | proposed | partial — `agarwood` · `sandalwood` (entity pages) |
| D-004 | is agarwood real / how to spot fake | informational+commercial | Agarwood | authenticity/adulteration | buyer-authentication guide | P0 | validated | `qinan-buying-authentication` · `incense-authentication-database` · `agarwood` |
| D-005 | sandalwood incense benefits | informational | Sandalwood | benefits (flooded with overclaims) | evidence-governed guide (honest, no medical overclaim) | P0 | validated | `sandalwood-incense` · `sandalwood` (entity) |
| D-006 | how to burn incense sticks | informational | Incense sticks | method | guide | P1 | proposed | `how-to-burn-incense-safely` · `incense-sticks` |
| D-007 | chinese vs japanese incense | comparison | Chinese incense | comparison | comparison page | P1 | proposed | `japanese-incense-kodo` · `what-is-chinese-incense` |
| D-008 | incense cones vs sticks | comparison | Formats | comparison | comparison page | P2 | proposed | `incense-sticks-vs-candles` · `which-incense-format` (hub) |
| D-009 | is incense smoke safe | informational | Safety | safety | safety guide (combustion disclosure) | P0 | proposed | `incense-safety-guide` (hub) · `incense-smoke-air-quality-evidence` |
| D-010 | incense wholesale / bulk | commercial | Wholesale | sourcing | commercial page | P1 | proposed | `wholesale-guide` · `incense-for-business` (hub) |
| D-011 | private label incense | commercial | OEM | manufacturing | commercial page | P1 | proposed | `oem-private-label-guide` |

## Key SERP insights (2026-09-08)

1. **"chinese incense"** — SERP dominated by DTC retail blogs (thin "guide" content). No authoritative, entity-deep encyclopedia. **Gap: authoritative knowledge platform.**
2. **"what is agarwood"** — best content combines botanical + grading + sourcing + adulteration. **Gap: Chinese grading/terminology (奇楠, 沉水, 油包木 vs 木包油) is barely present in English.**
3. **"sandalwood incense"** — SERP is almost entirely "benefits" content repeating unproven claims (cures insomnia, relieves anxiety). **Gap: honest, evidence-governed content (traditional use vs modern evidence) is the differentiator.**

> Demand rows are validated only after SERP + community + Chinese-source review. Rows marked "proposed" still need validation. Coverage was reconciled against the live content ledger on 2026-09-19.
