# Commercial Intent Map — Funnel Mapping (Current State)

> Audit-only. Maps the §18 funnel (Knowledge → Entity → Guide → Quality/Comparison → Buying → Wholesale → OEM → Contact) against actual routes/content.

## Funnel stages → actual assets

| Funnel stage | Main-site assets | Data-site assets | Status |
|---|---|---|---|
| **Knowledge** | `/chinese-incense/` (concept), P1–P12 informational (72 informational posts) | — | ✅ strong |
| **Entity** | `/ingredients/` + 150 DefinedTerm entity pages | `ingredients.json` (150) | ✅ strong |
| **Guide** | blog `guide`/`hub` (12 hub + 10 guide) + `landeng-editorial-methodology` | — | ✅ strong |
| **Quality / Comparison** | P5 `how-to-choose-incense`, P2 `incense-material-comparison-matrix`, P7 "vs" cluster, P10 QC | `comparisons.json` (17) | ✅ present |
| **Buying Guide** | P5 hub + `incense-gift-guide`, Commercial cluster | — | ✅ present |
| **Wholesale** | `/wholesale/` + `wholesale-guide`, `moq-pricing-guide`, `factory-vetting-guide`, `bulk-incense-ingredient-sourcing`, `how-to-buy-agarwood-for-incense-manufacturing` | — | ✅ present |
| **OEM / Private Label** | `/oem/` + `oem-private-label-guide`, `custom-fragrance-development` | — | ✅ present |
| **Contact** | `/contact/`, `/request-a-quote/` | — | ✅ present |

## Commercial blog cluster (11 posts, `Commercial — B2B Buying & Supply`)

- **Hub:** `incense-for-business`
- **Guides (8):** wholesale-guide · moq-pricing-guide · factory-vetting-guide · oem-private-label-guide · custom-fragrance-development · packaging-shipping-guide · samples-program
- **Buyer intelligence (3):** bulk-incense-ingredient-sourcing · how-to-buy-agarwood-for-incense-manufacturing · incense-export-considerations

## Dedicated commercial routes (4)

| Route | Function |
|---|---|
| `/wholesale/` | Wholesale inquiries |
| `/oem/` | OEM & private-label development |
| `/contact/` | Samples, quotes, wholesale & OEM inquiries |
| `/request-a-quote/` | RFQ form |

## Knowledge → commercial paths (verified pattern)

Entity pages carry commercial context sections (`What buyers should look for`, `Modern commercial applications`) and link outward to wholesale/OEM. Example verified: `agarwood.md` → "What buyers should look for" + "Modern commercial applications" sections.

The commercial layer is correctly **subordinate** to knowledge: header nav = Home/Ingredients/Wholesale/OEM/Contact (knowledge-first, commercial present but not dominant).

## Funnel integrity findings

1. **OEM/wholesale unverified-claims guardrail holds:** no fabricated MOQ/certification/capacity/pricing/factory/customer claims found in `/wholesale/` or `/oem/` copy (neutral/inquiry-first language).
2. **Commercial content is well-developed;** the gap is on the **knowledge→commercial bridge from entity pages**, not on missing commercial pages:
   - Only a subset of Tier-1 entities carry a full "What buyers should look for" section (§8 depth item 17).
   - No entity page links to `incense-export-considerations` (it is a 0-inbound orphan) — a lost B2B path.
3. **No commercial landing pages for specific product lines** (e.g., no "agarwood wholesale" page) — consistent with the knowledge-first stance; flagged as a future decision, not a defect.
4. **`samples-program` / `factory-vetting-guide`** are present and inquiry-oriented (good B2B funnel hygiene).

## Funnel stage gaps to note (for later phase, not this batch)

- **Quality/Comparison → Buying** transition is the weakest link: comparison content (P7) does not currently route readers into the Commercial cluster or `/request-a-quote/`.
- **Entity → Wholesale/OEM** is one-directional (entity → wholesale exists); there is no reverse path from wholesale/OEM back to the relevant entity knowledge pages for trust-building.
