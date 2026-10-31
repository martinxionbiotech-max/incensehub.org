# Content Gap Analysis — Real Gaps Only (No Auto-Production)

> Audit-only. Per §36 fields. **No articles are created here** (§53 content gate).
> Priority: P0 = critical existing-page repair · P1 = high-value missing knowledge · P2 = useful supporting · P3 = optional long-tail.

## Structural / technical gaps (P0)

| # | Topic | Intent | Primary entity | Related entities | Existing URL | Gap | Reason | Priority | Commercial | AIO | Required sources |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G01 | Data-site mirror parity | data | — | 150 entities | `data/` + `public/data/` (7 files) | `relationships.json` (450 edges) absent from main-site mirror; data site has 8 files | Cross-site consistency (§31); main site cannot serve the relationship graph | **P0** | Low | High | `data-landeng/datasets/relationships.json` |
| G02 | Homepage duplicate schema | technical | organization | — | `/` | Organization + WebSite JSON-LD emitted twice (index + BaseLayout) | Duplicate @id in one document | **P0** | Low | High | `src/pages/index.astro`, `BaseLayout.astro` |
| G03 | Custom 404 page | technical | — | — | none | No `src/pages/404.astro` | Broken-link UX + crawl waste | **P0** | Low | Low | Astro 404 convention |
| G04 | Vestigial `status: draft` | governance | 150 ingredients | — | `src/content/ingredients/*` | All 150 files `status: draft` yet built/served | Status field unwired; misleads future gating | **P0** | Low | Low | content.config.ts + templates |
| G05 | Classical-fixative orphan repair | identification | amber, onycha, castoreum, shellac | civet, ambergris, musk | `/ingredients/amber/` etc. | 0 inbound links on classical fixatives | Graph under-links high-value classical entities | **P0** | Medium | Medium | existing entity pages |
| G06 | llms.txt dataset coverage | AIO | — | — | `/llms.txt` | Lists 2 of 8 datasets | Incomplete machine-readable index | **P0** | Low | High | 8 dataset JSONs |

## High-value missing knowledge (P1)

| # | Topic | Intent | Primary entity | Related entities | Existing URL | Gap | Reason | Priority | Commercial | AIO | Required sources |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G07 | Dedicated comparison pages for Tier-1 pairs | comparison | agarwood | sandalwood, frankincense, borneol | `/blog/incense-material-comparison-matrix` (data_asset), `/blog/agarwood-incense` | No standalone entity-vs-entity comparison page type; comparisons live in P7 (format-level) only | §16 comparison priority; Tier-1 has strong comparison potential | **P1** | Medium | High | entity pages + comparisons.json (17) |
| G08 | Materials / Techniques / Forms hub pages on main site | definition | materials, techniques, forms | — | `/blog/how-incense-is-made` (covers craft) | No navigable main-site hub surfacing materials.json(15)/techniques.json(12)/forms.json(12) | §11 architecture; data-site taxonomy not surfaced to humans on main site | **P1** | Medium | High | data-site datasets |
| G09 | Aroma family pages | definition | aroma (10 families) | 150 entities | `/blog/scent-wheel`, `/blog/scent-guide` | 10 aroma families (aroma.json) not surfaced as per-family entity pages | §11 "Aroma" cluster | **P1** | Low | Medium | aroma.json |
| G10 | Terminology glossary as entity set | terminology | terminology (249) | — | `/blog/incense-terminology-glossary` | 249-term dataset has no first-class main-site reference page | §32 terminology asset | **P1** | Low | High | terminology.json |
| G11 | Tier-1 commercial context depth | buying guide | agarwood, sandalwood | benzoin, frankincense | entity pages ("What buyers should look for") | Tier-1 entities lack uniform commercial-context section | §18 funnel; §8 depth standard (item 17) | **P1** | High | Medium | existing entity + wholesale/oem pages |
| G12 | Safety cross-linking to entity pages | safety | calamus, asarum, artemisia | — | `/safety/`, `/blog/incense-safety-guide` | Safety caveats live on entity pages but not centrally linked | §23 safety conservatism | **P1** | Low | Medium | entity safety sections |

## Useful supporting (P2)

| # | Topic | Intent | Existing URL | Gap | Reason | Priority |
|---|---|---|---|---|---|---|
| G13 | Meta-description dedup audit | technical | — | No programmatic duplicate-description check exists | §4 SEO block | P2 |
| G14 | `related[]` ↔ `relationships.json` sync | data | entity pages + dataset | Frontmatter `related[]` (flat) under-represents the 450-edge typed layer | §14 relationship types | P2 |
| G15 | Performance/CLS field audit | performance | — | No field (CrUX) or lab metric baseline recorded | §44 | P2 |
| G16 | `sameAs` allow-list review | schema | entity pages | Only 3 hosts allowed (efloras/gbif/cites); no wikisource | §27 sameAs verification | P2 |

## Optional long-tail (P3)

| # | Topic | Intent | Existing URL | Gap | Reason | Priority |
|---|---|---|---|---|---|---|
| G17 | Tier-3 entity deepening | definition | 65 Tier-3 pages | Do **not** force-expand long-tail entities | §7 "Do not artificially force every entity" | P3 |
| G18 | External authority / backlink strategy | authority | — | No off-site authority layer | §60 roadmap P3 | P3 |

## Cannibalization watch (carried for §38 review)

- **Agarwood intent overlap:** `agarwood-grading-guide` (grading), `agarwood-incense` (scent guide), `agarwood-powder-vs-chips` (format) + entity `agarwood` (definition) — 4 URLs around one entity. Decision deferred: KEEP SEPARATE (distinct intent: grading / appreciation / format / definition), but cross-link order should be normalized.
- **"vs" cluster:** P7 has 5 "incense vs X" posts sharing comparison intent — intents are distinct enough (candles / diffuser / reed / small-room) to keep separate; no merge signaled.
- **Cinnamon/cassia naming:** `cinnamon` (桂皮) entity + `cassia-twig` (桂枝) entity + blog "cassia distinction" — naming-trap overlap flagged for disambiguation cross-links, not merge.

**Bottom line:** the site's real gaps are **structural/data-layer** (G01–G06) and **graph-surfacing** (G07–G12), not missing article volume. No new articles are proposed in this batch.
