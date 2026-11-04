# Phase 2 Execution Report — IncenseHub (IncenseHub)

> §58/§59 structure. Summarises the actual Phase 2 work done on the main site (`repos/IncenseHub`) across three batches: **audit** → **P0 repair** → **P1 repair + content** → **P2 audit + small-fix**.
> Date: 2026-09-25. Data site (`repos/data-landeng`) remained read-only reference throughout.

---

## Executive Summary

Phase 2 moved the site from an **unverified scaffold** to a **verified, graph-surfaced knowledge platform** — without adding keyword-filler article volume. The work fell into four waves:

1. **Audit** — 11 inventory documents created, 18 real gaps identified (G01–G18) with P0–P3 priority. Bottom line: the site's real gaps are structural/data-layer and graph-surfacing, not missing articles.
2. **P0 repair** — 6 critical defects fixed: data-site mirror parity (G01), duplicate homepage schema (G02), custom 404 (G03), vestigial `status: draft` (G04), classical-fixative orphan repair (G05), llms.txt 8-dataset coverage (G06).
3. **P1 repair + content** — Tier-1 commercial-context unification (G11, 13 entities), safety cross-linking (G12, 90 pages), and exactly 3 new graph-surfacing pages (G08 hub, G10 terminology reference, G07 comparison) — the §53 maximum.
4. **P2 audit + small-fix** — meta-description dedup audit (G13, clean), `related[]`↔`relationships.json` diff + 5-edge patch (G14), static performance baseline (G15), `sameAs` allow-list review (G16, decision only).

**Net new URLs:** 4 (404 + 3 P1 pages). **Net content changes:** 5 frontmatter edges (G14) + the P1 edits. **No URL/canonical/schema/navigation changes beyond the specific fixes.**

---

## Technical SEO

| Area | Before | After |
|---|---|---|
| Duplicate homepage schema | Organization + WebSite emitted twice (index + BaseLayout) | Single emission in BaseLayout (G02) |
| 404 page | Host default | Custom `src/pages/404.astro` (G03) |
| Meta-description dedup | Never audited | **0 duplicates across 262 rendered pages** (G13) |
| Sitemap | `sitemap-index.xml` + robots reference | Unchanged (correct) |
| Canonical | Per-page, single, computed from `Astro.url.pathname` | Unchanged (correct) |
| Indexability | `index, follow` site-wide | Unchanged (correct) |
| `status` field | 150 ingredients `draft` but served | `published` (151 files, G04) |

**Title hygiene:** 250 unique titles, 0 duplicates (verified in audit, unchanged). **Meta descriptions:** unique per page — ingredients use the auto-derived `directAnswer`, blog uses per-post `metaDescription`, static pages hand-written.

## Entity Architecture

- **150 entities** (one Markdown each) + 1 concept, full frontmatter (Chinese / pinyin / scientific / aroma / related) on 150/150.
- **Tier split:** T1 = 31 (≥5 inbound), T2 = 54, T3 = 65 — data-driven from inbound-link count.
- **Classical-fixative orphans** (amber / onycha / castoreum / shellac) identified and partially repaired via contextual links in G05 (amber + onycha linked in recipe/blending prose; castoreum/shellac confirmed already linked from ingredient pages).
- **`related[]` layer** (G14): curated entity→entity navigation, avg 2.37 edges, min raised 1→2 on Tier-1 hubs.
- **`termCode` asymmetry** (F2, P2): main site uses scientific name, data site uses slug — deferred (identity decision, not a build defect).

## Internal Linking

- **Orphan map:** 37 URLs with 0 inbound (36 ingredients + 1 blog) identified in audit.
- **G05:** amber + onycha gained contextual inbound links (recipe/blending prose) — no fabrication; links use existing entity names.
- **G12:** 90 entity Safety sections now link `/safety/`; `/safety/` links back to 7 high-warning entities.
- **G14:** 5 Tier-1 hubs raised to the 2-edge `related[]` minimum with reciprocal additions (graph stays symmetric).
- **G11:** 31/31 Tier-1 entities now carry the "What buyers should look for" section + a commercial link (wholesale guide).
- 176 URLs have ≥2 inbound links (measured). No "Related Posts" keyword-stuffing pattern.

## Content Architecture

- **No article volume added** beyond the §53 maximum (3 pages in P1).
- The 3 new P1 pages are **graph-surfacing**: materials/techniques/forms hub (G08), terminology reference (G10), top comparison pair agarwood-vs-frankincense (G07).
- **Pillar-cluster structure** preserved: 13 hubs, `pillar` + `cluster_role` frontmatter taxonomy intact.
- **Cannibalization watch** carried: agarwood 4-URL cluster kept separate (distinct intent); "vs" cluster kept; cinnamon/cassia naming trap flagged for disambiguation cross-links (deferred).

## AIO (AI-Search Readability)

- **llms.txt** now lists all 8 datasets with live counts (was 2 of 8) — G06.
- **Direct answers:** 150/150 ingredients open with `**Data summary:**`; `directAnswer` feeds meta description + DefinedTerm `description`.
- **FAQ:** 148/150 ingredients + 99/99 blog → `FAQPage` schema (conditional, no fabricated FAQ).
- **Entity clarity:** Chinese + pinyin + scientific name on 150/150, in `alternateName` and `DefinedTerm`.
- **Source transparency:** `## Sources` / `## Evidence & Sources` on 150/150 + 99/99 + 1/1.
- **`_headers`:** `Content-Signal: ai-train=yes`, `Link: </llms.txt>; rel="describedby"`, `X-Robots-Tag: index, follow, max-snippet:-1`.

## Structured Data

- **Emission points:** 6 files, ~9 `<script type="application/ld+json">` templates (Organization / WebSite / WebPage / Article / DefinedTerm / BreadcrumbList / CollectionPage / FAQPage + conditional ImageObject / PropertyValue).
- **G02 fixed:** homepage duplicate `@id` removed.
- **`mainEntity` wiring:** WebPage→DefinedTerm (entity), CollectionPage→ItemList (index), WebPage→Article (concept) — correct.
- **`sameAs` (G16):** 272 URLs emitted (gbif 158 / efloras 106 / cites 8), 149/150 entities. Decision recorded: keep identity-only allow-list; Wikisource stays in the citation layer.
- **No fabricated ratings/reviews/prices/authors** — `Product`/`Review`/`AggregateRating` absent by policy.

## Data Site

- **8 datasets** (615 records): ingredients(150) / terminology(249) / relationships(150+450) / comparisons(17) / materials(15) / forms(12) / techniques(12) / aroma(10).
- **G01 fixed:** `relationships.json` now mirrored in main-site `data/` + `public/data/` (8/8 files, md5-matched).
- **`termCode` semantics** differ between sites (scientific name vs slug) — flagged F2, deferred.
- **Wikisource citation domains** present in both sites' source layers (74 content files on main site).

## Commercial Funnel

- **4 commercial routes** (`/wholesale/`, `/oem/`, `/contact/`, `/request-a-quote/`) + 11-post Commercial blog cluster.
- **G11:** Tier-1 buyer-intelligence uniformity — 31/31 entities carry buyer section + commercial link.
- **Knowledge→commercial paths:** entity pages link outward to wholesale/OEM; no fabricated MOQ/capacity/pricing/geographic claims (verified against neutral copy).

## Existing Content Preserved

- **0 URLs changed or removed.** All fixes are additive or internal-wiring.
- **No redirects added, no canonical changes, no schema re-typing.**
- 250 content files retain their frontmatter, URLs, and body copy — G11/G12/G14 edits were additive links/sections, not rewrites.
- `data/` and `public/data/` mirrors gained `relationships.json` only (additive).

## Content Gaps

- **18 gaps** (G01–G18) recorded in `docs/content-gap-analysis.md`.
- **Resolved:** G01–G06 (P0), G07–G08, G10–G12 (P1), G13–G16 (P2, audit+decision).
- **Still open (P2/P3, deferred):** G09 (aroma family pages), G17 (Tier-3 deepening — deliberately NOT forced), G18 (external authority/backlinks).
- **Cannibalization watch** items remain open (agarwood 4-URL cluster, cinnamon/cassia naming) — decision deferred to §38 review.

## Deferred Work

| Item | Reason | Next |
|---|---|---|
| G09 aroma-family pages | P1, not yet scheduled | Phase 3 |
| G17 Tier-3 deepening | §7 "do not force every entity" | Never / long-tail only |
| G18 backlink strategy | §60 roadmap P3 | Phase 3+ |
| `termCode` semantics (F2) | identity decision, not a build defect | Schema phase |
| F3 blog WebPage wrapper | minor structural inconsistency | Schema phase |
| Image >100 KB WebP re-encode (G15) | 3 assets (2 PNG charts + hero) | Asset pass |
| Field (CrUX) performance data | not deployed | Post-launch |
| Stale "replace domain before launch" TODOs | deployment-blocking, not SEO | Pre-launch |

## Risks

- **Field data absent** — all performance claims are static/lab-only until deployed.
- **`amber` lacks `sameAs`** — its authority citations are textual (Wikisource), not taxonomic; accepted, but means one Tier-3 entity has no machine identity link.
- **Cannibalization watch** — agarwood 4-URL cluster and cinnamon/cassia naming need disambiguation cross-links before they cause SERP self-competition.
- **Deployment TODOs** (`astro.config.mjs`, `robots.txt`) still carry stale domain placeholders — must be resolved before launch, not a code risk.

## Next Phase

1. **G09 aroma-family pages** (10 families) — the last surfacing gap.
2. **Schema phase** — resolve F2 (termCode) and F3 (blog WebPage wrapper).
3. **Asset pass** — re-encode 3 >100 KB PNG → WebP; consider `srcset`.
4. **Post-launch** — CrUX/RUM field baseline; extend `phase2-baseline.md` Performance section.
5. **Cannibalization review (§38)** — normalize cross-link order in the agarwood cluster; disambiguate cinnamon/cassia.
6. **G18 authority/backlink strategy** (P3, §60 roadmap).

---

## Batch ledger (for cross-reference)

| Batch | Tag | Scope |
|---|---|---|
| audit | `phase2/audit` | 11 inventory docs + gap analysis |
| P0 | `phase2/P0` | G01–G06 repairs |
| P1 | `phase2/P1` | G11/G12 + G08/G10/G07 content |
| P2 | `phase2/P2` | G13/G14/G15/G16 audit + small-fix |

Full before/after detail in `docs/phase2-change-log.md`.
