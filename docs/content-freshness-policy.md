# Content Freshness Policy — IncenseHerbs (IncenseHub)

> Governance document (§50). Defines **when** content is re-reviewed and **what** triggers an update.
> This is a policy only — it does **not** change any content date, and it does not retroactively add or alter `last_reviewed` values. Dates stay truthful.

## 1. Purpose

Content freshness here means **substantive correctness**, not a manufactured "recently updated" stamp. The site is an evergreen knowledge base (botanical identity, traditional use, sourcing guidance) where most facts are stable, but a subset — evidence status, dataset counts, relationships, commercial guidance — can drift. This policy makes that review explicit and cadence-driven, without inventing update signals.

## 2. Review cadence by tier

The review frequency is driven by the entity-tier classification in `docs/entity-inventory.md` (T1 = 31 / T2 = 54 / T3 = 65, by inbound-link depth).

| Tier | Cadence | Rationale |
|---|---|---|
| **T1** (hub entities, ≥5 inbound) | **every 90 days** | Highest authority surface; any staleness here propagates to every linking page |
| **T2** (mid, 2–4 inbound) | **every 180 days** | Regular but lower-visibility entities |
| **T3** (long-tail, ≤1 inbound) | **as-needed** (on trigger) | Rarely inspected; review only when a trigger fires, not on a fixed clock |

**Blog / guide / concept pages** are not tiered — they follow a flat **180-day** cadence (same as T2), unless they carry buyer-intelligence or commercial guidance, which follows the **90-day** cadence.

> **Current state (2026-09-25):** `last_reviewed` is present on **108/108 blog** files, but **0/150 ingredient** files and **0/1 concept** file. Ingredient pages carry no date field at all and emit no `dateModified` in their schema. This policy records the cadence; the act of back-filling `last_reviewed` onto ingredient files is a separate, date-truthful migration (not done here).

## 3. Update trigger conditions (§50 — six conditions)

Update a page **only** when at least one of the following is true:

1. **Evidence changed** — a source the page relies on has been corrected, retracted, or materially revised.
2. **Information is outdated** — a fact is no longer current (e.g. taxonomy reclassification, regulatory change).
3. **New useful source exists** — a higher-quality or more authoritative reference becomes available.
4. **Entity relationship changed** — the entity's `related[]` / `relationships.json` edges or taxonomy membership shift.
5. **Dataset changed** — a data-site dataset (`ingredients.json`, `terminology.json`, `relationships.json`, etc.) is updated and the page mirrors it.
6. **Significant factual correction required** — the page contains a genuine error, not just a phrasing preference.

**Do NOT update merely to create a new date.** A date bump without a substantive change is prohibited (matches §50 and §56 change-management).

## 4. Review checklist (per page, when a trigger fires or a cadence tick elapses)

- [ ] **Correctness** — re-verify the entity's scientific name, Chinese, pinyin, and primary facts against the current source.
- [ ] **Evidence status** — check the "Traditional use vs modern evidence" / "Evidence status" sections still reflect the source's position.
- [ ] **Dataset consistency** — confirm any mirrored counts/records match the data-site dataset (termCode, record counts).
- [ ] **Relationship integrity** — confirm `related[]` edges still point at live slugs; confirm reciprocity.
- [ ] **Source links** — verify `## Sources` / `## Evidence & Sources` URLs still resolve and are still on the appropriate allow-list (`efloras.org` / `gbif.org` / `checklist.cites.org` for identity `sameAs`; Wikisource stays in the citation layer).
- [ ] **Commercial accuracy** — for buyer/wholesale/OEM copy, confirm no fabricated MOQ/capacity/pricing/geographic claims were introduced.
- [ ] **Date truthfulness** — if updated, set `last_reviewed` to the actual review date; if nothing changed, leave the date untouched.

## 5. Logging

Every update (or a documented "no-change" review) is recorded in `docs/phase2-change-log.md` with the §56 ledger format (Date · File · Change · Reason · Risk · Validation · Rollback). A no-change review is logged as such — it is never disguised as a content update.

## 6. Non-goals

- No automatic date-bumping scripts.
- No bulk "refreshed on" rewrites.
- No retroactive `last_reviewed` back-fill without a real review.
