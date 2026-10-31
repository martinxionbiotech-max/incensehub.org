# INQUIRY-SYSTEM.md — IncenseHub

Phase 1 conversion system (no payment). Inquiries are the primary conversion — and the first-party data source for the demand loop.

## Inquiry types

- Request a Sample
- Request a Quote
- Wholesale Inquiry
- OEM Inquiry
- Private Label Inquiry
- Contact

## Required fields (per type)

| Field | Sample | Quote | Wholesale | OEM | Contact |
|---|---|---|---|---|---|
| Name | ✅ | ✅ | ✅ | ✅ | ✅ |
| Email | ✅ | ✅ | ✅ | ✅ | ✅ |
| Company | — | ✅ | ✅ | ✅ | — |
| Country / region | ✅ | ✅ | ✅ | ✅ | — |
| Product interest | ✅ | ✅ | ✅ | ✅ | — |
| Quantity / MOQ | — | ✅ | ✅ | ✅ | — |
| Message / spec | ✅ | ✅ | ✅ | ✅ | ✅ |

## Routing & storage

- Forms route to a first-party inbox (email) — **no public DB** in Phase 1.
- Storage/backends are provisioned in Phase 3. Do not hardcode email recipients in client-side code.

## First-party data loop

Every inquiry captures: query · landing page · topic · product/ingredient/material interest · wholesale/OEM intent · customer question · unmet information need.

Feed back into: demand intelligence → content → research → product → commercial. See DEMAND-MODEL.md.

## Security & spam

- CSRF + basic anti-spam (honeypot) at minimum.
- No secrets exposed client-side.
- Confirm double-opt-in where email marketing is ever added (not in Phase 1).
