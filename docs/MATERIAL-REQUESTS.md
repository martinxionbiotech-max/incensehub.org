# MATERIAL-REQUESTS.md — IncenseHub

Missing first-party information. **Never invent these — request them.** Each item is labeled `UNKNOWN · REQUIRED · OPTIONAL · VERIFIED · PENDING`.

## Brand / entity (blocking)

| Item | Status | Notes |
|---|---|---|
| Legal entity name | UNKNOWN / REQUIRED | for Organization schema + legal pages |
| Domain name | UNKNOWN / REQUIRED | for URL taxonomy, canonical, schema |
| Contact email | UNKNOWN / REQUIRED | for contact + inquiry + schema contactPoint |
| Business address / region | UNKNOWN / REQUIRED | for About + schema |
| Brand story / origin | PENDING | founder voice, history |
| Logo + brand assets | PENDING | ART-DIRECTION input |

## Commerce / manufacturing (required before product/wholesale/OEM pages)

| Item | Status |
|---|---|
| Product catalog (names, formats, ingredients) | PENDING |
| Ingredient/material sourcing (origin, suppliers) | PENDING |
| Manufacturing process | PENDING |
| MOQ (per product / wholesale) | UNKNOWN |
| Certifications (ISO, HACCP, etc.) | UNKNOWN |
| Capacity / lead time | UNKNOWN |
| Test reports | UNKNOWN |
| Packaging options | PENDING |
| OEM / private-label capabilities | PENDING |
| Product photography | PENDING |

## Knowledge / research (optional, improves originality)

| Item | Status |
|---|---|
| Chinese source documents (articles, PDFs, historical material) | PENDING |
| Ingredient specification sheets | PENDING |
| Company/manufacturing info | PENDING |
| Sample products | PENDING |

## Rules

- Label every unknown clearly. Do not publish a page that depends on a missing fact.
- As materials arrive, run the material-processing pipeline (see MASTER-BUILD-PROMPT §51): extract facts → entities → terminology → claims → evidence → gaps → update graph/inventories → propose assets.
