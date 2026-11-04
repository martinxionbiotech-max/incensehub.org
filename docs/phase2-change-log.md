# Phase 2 Change Log

> Change-management ledger (§56). Every modification to the site/repos is recorded here before/after implementation.

## Format

`Date · File/Area · Change · Reason · Risk · Validation · Rollback`

---

## 2026-09-25 — Baseline audit batch (phase2/audit)

### Init — 11 inventory documents created under `docs/`

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/phase2-baseline.md` | Created baseline audit (Technical/SEO/Entity/Data/AIO/Commercial) | §4 required baseline before implementation | None (doc only) | Cross-checked against repo | `git revert` |
| 2026-09-25 | `docs/entity-inventory.md` | Created 150-entity Tier classification (T1=31 / T2=54 / T3=65) | §7 entity tiers | None | Data-driven from inbound-link map | `git revert` |
| 2026-09-25 | `docs/article-inventory.md` | Created 99 blog + 1 concept + 8 core page ledger | §5 required inventory | None | Matched frontmatter + routes | `git revert` |
| 2026-09-25 | `docs/topic-map.md` | Created cluster architecture map (13 hubs) | §11 topic map | None | Reconstructed from pillar/cluster_role | `git revert` |
| 2026-09-25 | `docs/internal-link-map.md` | Created hub→spoke→cross-link status + 37-orphan list | §13/§39 linking audit | None | `scripts/orphan_inbound.json` | `git revert` |
| 2026-09-25 | `docs/content-gap-analysis.md` | Created 18 real gaps (G01–G18) with P0–P3 priority | §36 gap analysis | None | Only real gaps; no auto-production | `git revert` |
| 2026-09-25 | `docs/commercial-intent-map.md` | Created funnel mapping (8 stages) | §18 commercial funnel | None | Verified routes + copy | `git revert` |
| 2026-09-25 | `docs/data-site-audit.md` | Created 8-dataset audit (615 records) | §28 data-site audit | None | Parsed 8 JSON files + CI | `git revert` |
| 2026-09-25 | `docs/aio-audit.md` | Created AIO audit (llms.txt / direct answer / FAQ / sources) | §24–26 AIO audit | None | Programmatic coverage checks | `git revert` |
| 2026-09-25 | `docs/schema-audit.md` | Created JSON-LD audit (types / @id / mainEntity / sameAs) | §27 schema audit | None | Catalogued all emission points | `git revert` |
| 2026-09-25 | `docs/phase2-change-log.md` | Initialized this ledger | §56 change management | None | — | — |

### Findings logged (no changes made)

| # | Finding | Severity | Where |
|---|---|---|---|
| 1 | `relationships.json` (450 edges) missing from main-site `data/` + `public/data/` mirror (7 vs 8 files) | P0 | data-site-audit / content-gap G01 |
| 2 | Homepage emits Organization + WebSite JSON-LD twice | P0 | schema-audit F1 / content-gap G02 |
| 3 | No custom 404 page | P0 | baseline / content-gap G03 |
| 4 | All 150 ingredients `status: draft` yet built/served | P0 | baseline / content-gap G04 |
| 5 | `llms.txt` lists 2 of 8 datasets | P0 | aio-audit A1 / content-gap G06 |
| 6 | Classical fixatives (amber/onycha/castoreum/shellac) orphaned (0 inbound) | P0 | internal-link-map / content-gap G05 |
| 7 | `termCode` semantics differ (scientific name vs slug) | P2 | schema-audit F2 |
| 8 | `sameAs` allow-list narrower than data-site CI (missing wikisource.org) | P2 | schema-audit F4 / data-site |
| 9 | Blog count 99 (brief expected 89) | info | article-inventory |

---

## Deferred (intentionally NOT done this batch)

- No article production (§53 content gate).
- No URL/canonical/schema/navigation changes.
- No internal-link rewiring.
- No data-site schema changes.
- No 404 page creation, no status-field wiring, no llms.txt edit.

Next phase (after this baseline is reviewed): P0 repairs first (§63 — audit → map → repair → connect → strengthen graph → AIO → commercial → only then content).

---

## 2026-09-25 — P0 repair batch (phase2/P0)

### G01 + G06 — Data mirror parity + llms.txt 8-dataset coverage

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `data/relationships.json`, `public/data/relationships.json` | Copied `relationships.json` (150 records / 450 edges) from `incensehubdata/datasets/` into main-site mirror (now 8/8 files) | G01 cross-site consistency (§31); main site could not serve the relationship graph | None (own data, no new domain) | md5 match vs incensehubdata source; 8 files present in both mirrors | `git revert` |
| 2026-09-25 | `scripts/generate-llms.mjs` | Rewrote to emit all 8 datasets with live counts (relationships shows `150 / 450`) | G06 incomplete machine-readable index; G01 needs relationships row | None (prebuild regenerates only) | `node scripts/generate-llms.mjs` → 8 dataset lines; build succeeded | `git revert` |
| 2026-09-25 | `public/llms.txt` | Machine-readable section now lists 8 datasets (ingredients 150 / terminology 249 / relationships 150+450 / comparisons 17 / materials 15 / forms 12 / techniques 12 / aroma 10) | G01 + G06 | None | grep confirms 8 rows + correct counts | `git revert` |

### G02 — Homepage duplicate schema

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/pages/index.astro` | Removed Organization + WebSite JSON-LD (consts + 2 `<script>` tags) that duplicated BaseLayout's emission | G02 duplicate @id in one document | None (single source retained in BaseLayout) | Built `dist/index.html` has exactly 2 JSON-LD blocks, `@id` `#organization`/`#website` each emitted once as primary node | `git revert` |

### G03 — Custom 404 page

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/pages/404.astro` (new) | Custom 404 (title / lead / return-home CTA / core links) following BaseLayout conventions | G03 broken-link UX | None (no URL/canonical change; 404 auto-excluded from sitemap) | Build emits `dist/404.html`; 404 absent from `sitemap-0.xml` | `git revert` |

### G04 — Vestigial `status: draft` cleanup

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/ingredients/*.md` (150) + `src/content/concepts/chinese-incense.md` (1) | `status: draft` → `status: published` (151 files) | G04 status field unwired; `draft` misleads future gating | None (field is parsed but never gated in build) | `grep -c "^status: draft"` → 0; `status: published` = 151 | `git revert` |

### G05 — Classical-fixative orphan repair (contextual links)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/blog/hexiang-blending-system.md` | Linked 琥珀 amber → `/ingredients/amber/`, 甲香 operculum → `/ingredients/onycha/` in the 二苏旧局 recipe + binders/fixatives tables | G05 under-linked classical fixatives | None (anchor = entity name, no new URL) | Build: both `href`s render | `git revert` |
| 2026-09-25 | `src/content/blog/ersu-jiuju-recipe.md` | Linked 琥珀 amber → `/ingredients/amber/` in the 二苏旧局 assistant table | G05 | None | Build: `href` renders | `git revert` |
| 2026-09-25 | `src/content/blog/huarui-furen-yamen-recipe.md` | Linked 甲香 (onycha) → `/ingredients/onycha/` in the ingredient table | G05 | None | Build: `href` renders | `git revert` |
| 2026-09-25 | `src/content/blog/incense-ingredients-glossary.md` | Linked 甲香 (operculum) → `/ingredients/onycha/` in the classical-manuals passage | G05 | None | Build: `href` renders | `git revert` |

**G05 note:** `castoreum` and `shellac` were also 0-inbound in the baseline orphan map, but grep confirmed both already carry contextual inbound links from ingredient pages (`musk`/`civet` → castoreum; `amber`/`benzoin`/`dragons-blood` → shellac). No blog prose mentions castoreum/shellac as entities, so no fabrication was made — the added links target amber (琥珀) and onycha (甲香), which are discussed in recipe/blending blog prose but were unlinked there.

---

## 2026-09-25 — P1 repair + content batch (phase2/P1)

### G11 — Tier-1 commercial-context unification (13 entities)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/ingredients/{agastache-rugosa,plum-blossom,orange-peel,borneol,galangal,fennel,champaca,citron,cypress-seed,rosemary,finger-citron,orris-root}.md` (12) | Added `See the [wholesale guide](/blog/wholesale-guide/)…` commercial link to the "What buyers should look for" section | G11: these 12 Tier-1 entities had the buyer section but zero commercial internal link | None (anchor = existing wholesale-guide URL, no new domain) | `grep` confirms 1 commercial link each; 31/31 Tier-1 now have buyer section + commercial link | `git revert` |
| 2026-09-25 | `src/content/ingredients/musk.md` | Added "What buyers should look for" section (synthesized from existing provenance-honesty content) + wholesale-guide link | G11: musk was the only Tier-1 entity missing both the buyer section and a commercial link | None (all copy synthesized from existing page content, zero fabrication) | Build renders; 31/31 verified | `git revert` |

**G11 note:** Before this batch, 30/31 Tier-1 entities had the "What buyers should look for" section, and 18/31 had a commercial link. The 13 fixed are the 12 with buyer-section-but-no-link plus musk (missing both). No new facts introduced — links point to the existing wholesale guide; musk's new section restates its existing "musk is a scent descriptor, not provenance" content.

### G12 — Safety cross-linking (90 entity pages + /safety/ index)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/ingredients/*.md` (90) | Added `See our [safety guide](/safety/).` to every entity Safety section (converted the 2 existing plain-text "See our safety guide." into links) | G12: safety caveats lived on entity pages but were not centrally linked | None (anchor = existing /safety/ URL) | 90/90 safety sections now link /safety/; `grep -rL "/safety/"` on safety-bearing files → 0 | `git revert` |
| 2026-09-25 | `src/pages/safety/index.astro` | Added "Related safety caveats" section linking high-warning entities (lily-of-the-valley, calamus, asarum, apricot-kernel, star-anise, camphor, borneol) | G12 reverse path: /safety/ → entity caveats | None (links only to existing entity URLs) | Build: 7 caveat links render in `dist/safety/index.html` | `git revert` |

**G12 note:** 90 entity pages carry a Safety section (grep-confirmed). The task's named examples (calamus/asarum/artemisia) were grep-verified: calamus (β-asarone) and asarum (Aristolochiaceae dosing cautions) are genuine high-warning entries, while artemisia-annua's "artemisinin caution" is a drug-fame boundary note, not a toxicity caveat — so the high-warning list uses the genuinely caveated entities (lily-of-the-valley being the strongest: cardiac glycosides).

### G08 — Materials / Techniques / Forms hub page (new)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/blog/incense-materials-techniques-forms.md` (new) | Hub page surfacing the 3 datasets (15 materials / 12 techniques / 12 forms) as readable tables + data-site JSON links + entity links | G08: no navigable main-site hub for the materials/techniques/forms taxonomies | None (new URL, no existing URL displaced) | 1,882 words; 3 tables (15/12/12 rows); 8 internal links verified; Direct answer block | `git revert` |

### G10 — Terminology first-class reference page (new)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/blog/incense-terminology-reference.md` (new) | First-class main-site entry for the 249-term terminology dataset: grouped index + dataset-usage notes + links to terminology.json and existing glossaries | G10: 249-term dataset had no first-class main-site reference page | None (new URL) | 1,575 words; 249-term grouped index (no full-text dump); links to terminology.json + both glossaries; Direct answer block | `git revert` |

### G07 — Top comparison pair (new)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/blog/agarwood-vs-frankincense.md` (new) | §14 standard comparison page (Criterion table + Direct answer + links to both entity pages and the comparison matrix) | G07: no standalone entity-vs-entity comparison for the top Tier-1 pair | None (new URL) | 2,469 words; 1 §14 Criterion table (10 rows) + 1 aroma table; links to /ingredients/agarwood/, /ingredients/frankincense/, comparison matrix; §51 gate passed | `git revert` |

**§53 gate compliance:** exactly 3 new pages this batch (G08/G10/G07), the maximum allowed. All are graph-surfacing pages, not keyword-filler articles.

---

## 2026-09-25 — P2 audit + small-fix batch (phase2/P2)

### G13 — Meta-description dedup audit (rendered layer)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/aio-audit.md` (supplement) | Added G13 rendered-layer meta-description dedup audit: 262 HTML pages scanned, **0 duplicate groups**, 0 missing descriptions | G13: no programmatic duplicate-description check existed (§4 SEO block) | None (doc only) | `dist/**/*.html` walk, verbatim `<meta name="description">` extraction, grouped | `git revert` |

**Result:** clean — no template repair required. Ingredient `directAnswer` is intrinsically unique (5 per-entity fields); blog uses per-post `metaDescription`; static pages hand-written. A future duplicate would signal a frontmatter data error, not a template bug.

### G14 — `related[]` ↔ `relationships.json` sync (diff + 5-edge patch)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/entity-inventory.md` (supplement) | Added G14 diff statistics: `related[]` (150 entities, avg 2.37, untyped) vs `relationships.json` (450 typed edges: 150 category + 280 aroma + 7 comparison + 13 technique); concluded no 450-edge rewrite warranted | G14: layers are complementary (typed taxonomy vs curated cross-links), not 1:1 | None (doc only) | Programmatic count of both layers | `git revert` |
| 2026-09-25 | `src/content/ingredients/{mugwort,clove,rose,orange-peel,myrrh}.md` (5) | Added 1 reciprocal `related[]` entry each (`artemisia-annua` / `cardamom` / `osmanthus` / `pomelo-peel` / `benzoin`) to the 5 Tier-1 pages that carried only the 1-edge minimum | G14: 5 Tier-1 hubs under the 2–3 edge norm | None (additive; each target already links back → graph stays symmetric) | `related[]` min count 1→2; 0 Tier-1 pages below norm; 5/5 additions reciprocal-verified | `git revert` |

**Result:** no 450-edge rewrite. `relationships.json` is a typed taxonomy/derivation graph; `related[]` is curated entity→entity navigation. Small patch restores the 2-edge minimum on Tier-1 hubs.

### G15 — Performance baseline (static build metrics)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/phase2-baseline.md` (Performance section) | Added G15 static-metric baseline: 262 pages / 8.62 MB HTML (mean 32.1 KB) / 189 images 6.61 MB / 1 CSS bundle 9.2 KB; field (CrUX) data marked "pending deployment" | G15: no performance baseline recorded (§44) | None (doc only) | Programmatic `dist/` size/weight walk; field data explicitly marked unavailable | `git revert` |

**Result:** HTML lean (mean 32 KB, no JS runtime). 3 images >100 KB (2 PNG charts + 1 hero) flagged for future WebP re-encode; render-blocking Google Fonts noted. Field data deferred to post-launch.

### G16 — `sameAs` allow-list review

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/schema-audit.md` (supplement) | Added G16 `sameAs` review: measured distribution (gbif 158 / efloras 106 / cites 8 = 272 URLs, 149/150 entities) + recorded **decision to NOT add Wikisource** | G16: review whether `sameAs` should widen to `zh.wikisource.org` | None (decision only, no code change) | Rendered-dist extraction of `sameAs` arrays; Wikisource confirmed already in `## Sources` citation layer | `git revert` |

**Decision:** keep `sameAs` identity-only (`efloras`/`gbif`/`cites`); Wikisource is a citation source, not an identity record. F4 asymmetry resolved as intentional.

### Batch summary

| Gap | Disposition | Code change |
|---|---|---|
| G13 | Clean (0 dupes) | none |
| G14 | Diff report + 5 frontmatter edges | 5 files |
| G15 | Static baseline recorded | none (doc) |
| G16 | Allow-list decision recorded | none |

---

## 2026-09-25 — P1 content batch B (phase2/P1)

### G07 — Comparison pages (2 more Tier-1 pairs) + G09 — Aroma family hub + 3 family pages

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `src/content/blog/sandalwood-vs-frankincense.md` (new) | §14 comparison page — wood vs resin (form/burn/traditional-use/purchasing); links both entity pages + comparison matrix + wholesale guide | G07: Tier-1 comparison pair | None (new URL) | 2,528 words; 1 §14 Criterion table (10 rows) + 1 aroma table; 10 internal links; §51 gate passed | `git revert` |
| 2026-09-25 | `src/content/blog/borneol-vs-camphor.md` (new) | §14 comparison page — same-camphor-family source/use/safety/purchasing split; safety boundary is core value | G07: Tier-1 comparison pair | None (new URL) | 2,445 words; 1 §14 Criterion table (10 rows) + 1 aroma table; links borneol/camphor entities + /safety/ + safety guide; §51 gate passed | `git revert` |
| 2026-09-25 | `src/content/blog/incense-aroma-families.md` (new) | G09 hub — 10 aroma families from aroma.json + frontmatter `aroma` field; per-family definition + representative entities + links data-site aroma.json | G09: aroma families not surfaced as hub | None (new URL) | 1,708 words; 1 ten-family table + per-family Direct answer blocks; links aroma.json/relationships.json/ingredients.json + 3 family pages; §51 gate passed | `git revert` |
| 2026-09-25 | `src/content/blog/woody-aroma-family.md` (new) | G09 family page — woody (9 members); definition/chemistry (published only)/representatives; links hub + entity pages | G09: flagship aroma family | None (new URL) | 1,477 words; Direct answer blocks; 13 internal links; §51 gate passed | `git revert` |
| 2026-09-25 | `src/content/blog/resinous-aroma-family.md` (new) | G09 family page — resinous (4 members); definition/chemistry/representatives + balsamic-sibling distinction; links hub + entity pages | G09: flagship aroma family | None (new URL) | 1,590 words; Direct answer blocks; 12 internal links; §51 gate passed | `git revert` |
| 2026-09-25 | `src/content/blog/floral-aroma-family.md` (new) | G09 family page — floral (4 members); definition/chemistry/representatives + natural-vs-reconstructed honesty point; links hub + entity pages | G09: flagship aroma family | None (new URL) | 1,535 words; Direct answer blocks; 11 internal links; §51 gate passed | `git revert` |

**§53 gate compliance:** 6 new pages this batch (2 comparison + 1 hub + 3 family pages). All are graph-surfacing, not keyword-filler articles. Zero fabrication: chemistry named only where already published on entity pages; representative entities drawn from `aroma.json` membership; 0 new domains (data-site links only).

---

## 2026-09-25 — P2 OG / Image / Freshness batch (phase2/P2)

### §43 — Open Graph / Twitter card audit + template fixes

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/schema-audit.md` (supplement) | Added §43 rendered-layer OG/Twitter coverage scan (268 pages) + 3 findings F6/F7/F8 | §43 requires an OG/Twitter metadata audit | None (doc only) | `dist/` walk over all 268 HTML pages, per-tag presence | `git revert` |
| 2026-09-25 | `src/layouts/BaseLayout.astro` | Fixed `og:image` double-slash URL (`new URL(…, SITE)` instead of `` `${SITE}/` ``); added `twitter:image` | F6 (double-slash share image) + F7 (`summary_large_image` card lacked `twitter:image`) | None (no new image — reuses site-default `og-image-…jpg`) | Rendered `og:image`/`twitter:image` now single clean URL; 0 missing tags on 268 pages | `git revert` |
| 2026-09-25 | `src/pages/blog/[slug].astro` | Stripped HTML tags before deriving meta description | F8: 9 image-first blog posts had a description that began with the literal `<img>` tag | None (description generation only; no URL/content change) | 9/9 descriptions now start with prose; 0 `<img` prefixes in `dist/` | `git revert` |

### §44/§45 — Image recompression + lazy-loading audit

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `public/images/scent-wheel-fragrance-families-800x800.webp` (new), `…800x800.png` (removed) | Lossy re-encode PNG → WebP q90 (698.6 KB → 36.4 KB, −94.8%) | §44/§45: 715 KB PNG chart was the largest single asset | None (visually identical chart; WebP is the site's dominant format) | `sharp` dimensions 800×800 preserved; rendered `<img>` + ImageObject updated | `git revert` |
| 2026-09-25 | `public/images/burn-time-matrix-chart-800x600.webp` (new), `…800x600.png` (removed) | Lossy re-encode PNG → WebP q90 (353.2 KB → 7.7 KB, −97.8%) | §44/§45: second >300 KB asset | None | `sharp` 800×600 preserved; refs updated | `git revert` |
| 2026-09-25 | `src/content/blog/scent-guide.md`, `incense-burn-time-format-matrix.md` | Updated `<img src>` `.png` → `.webp` (both already carry `loading="lazy"` + `width`/`height` + `alt`) | Keep refs aligned with re-encoded assets | None (ImageObject schema auto-derives from body) | `dist/` `<img>` + `ImageObject.url` both `.webp`; 0 stale `.png` refs | `git revert` |
| 2026-09-25 | `docs/IMAGE-MANIFEST.md`, `docs/IMAGE-PROMPTS.md` | Updated 2 chart filenames `.png` → `.webp` + format-rule note | Filenames are the wiring contract | None (doc only) | grep: no stale `.png` chart references | `git revert` |
| 2026-09-25 | `docs/phase2-baseline.md` (G17 supplement) | Recorded image before/after (6.61 MB → 5.62 MB, −14.9%; 0 PNG remain) + lazy-loading result (190/191 content imgs lazy) | §44/§45 require before/after recording | None (doc only) | Programmatic `public/images/` weight + `dist/` `<img>` attribute walk | `git revert` |

### §50 — Content freshness policy (governance doc)

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-25 | `docs/content-freshness-policy.md` (new) | Governance policy: review cadence (T1 90d / T2 180d / T3 as-needed), the 6 §50 update triggers, a per-page review checklist, and logging rules. No content date changed | §50 requires a freshness/update policy | None (doc only) | Policy references tier split in `entity-inventory.md`; documents current state (108/108 blog have `last_reviewed`, 0/150 ingredients) | `git revert` |

### Batch summary

| Workstream | Result | Code change |
|---|---|---|
| §43 OG/Twitter audit | 3 defects fixed (og:image double-slash, missing twitter:image, malformed description ×9) | BaseLayout + blog `[slug].astro` |
| §44/§45 images | 2 PNG charts → WebP (−95.9% combined); 6.61→5.62 MB; lazy-loading verified clean (hero LCP correctly eager) | 2 `.webp` added, 2 `.png` removed, 2 `.md` refs |
| §50 freshness | Policy doc written; no date changes | none (doc) |

---

## 2026-09-27 — E-E-A-T entity wiring batch (phase2/33 · §21/§27/§29 · §56)

### §21/§27/§29 — Organization/WebSite schema + contact + footer legal identity

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-27 | `src/layouts/BaseLayout.astro` | Organization schema: added `legalName` (Zhangjiakou Landeng Technology Co., Ltd.), `email` (landengltd@gmail.com), `telephone` (+86 13323237275), `address` (PostalAddress: streetAddress/addressLocality/addressRegion/addressCountry CN), `vatID` + `identifier` (PropertyValue propertyID=CN-USCC, value=91130702MAKM4QXH5Q); brand `name` stays "IncenseHub" | §21/§27: attach real legal entity to Organization schema at the single BaseLayout emission point | None (no URL/content/rank change) | `npm run build` passes; rendered JSON-LD carries all new fields; brand name unchanged | `git revert` |
| 2026-09-27 | `src/layouts/BaseLayout.astro` | Footer: added company legal name + address + USCC small-print line (`.footer-legal`) | §21: legal identity visible site-wide | None | Build passes; footer renders legal line on all pages | `git revert` |
| 2026-09-27 | `src/pages/contact/index.astro` | Replaced TODO `contact@incensehub.org` → `landengltd@gmail.com`; added phone +86 13323237275 (WhatsApp/WeChat), company EN name, address, USCC; removed TODO comment | §21/§29: real contact identity, no placeholder | None (no URL change) | grep: 0 `TODO`/`contact@incensehub.org` remaining | `git revert` |
| 2026-09-27 | `src/pages/request-a-quote/index.astro` | Same contact replacement as above | §21/§29 | None | grep clean | `git revert` |

### §21 — author entity + editorial identity

| Date | File | Change | Reason | Risk | Validation | Rollback |
|---|---|---|---|---|---|---|
| 2026-09-27 | `src/content/**/*.md` (108 files) | frontmatter `author` "IncenseHub Editorial Team" → "Landeng Tech Team" (78 escaped-quote + 30 clean); also fixed the 78 files' stray escaped-quote author value | §21: unify author entity to Landeng Tech Team | None (author field not rendered on blog template) | grep: 0 "IncenseHub Editorial Team" remaining in src/content; 108/108 blog have `author: "Landeng Tech Team"` | `git revert` |
| 2026-09-27 | `src/content/blog/lanDeng-editorial-methodology.md` | Added "Publisher" subsection (company EN/ZH, USCC, address, email, phone); byline renamed to Landeng Tech Team | §21/§29: methodology page carries real company identity + team name + contact | None | Build passes; 5 prose occurrences renamed | `git revert` |
| 2026-09-27 | `src/content/blog/lanDeng-knowledge-map.md` | Added "Publisher & Contact" section (company EN/ZH, USCC, address, email, phone); FAQ attribution renamed | §21/§29 | None | Build passes | `git revert` |
| 2026-09-27 | `src/pages/index.astro` | Editorial-trust section: added sentence naming Zhangjiakou Landeng Technology Co., Ltd. as the brand's operating company | §21: homepage states brand↔legal-entity relationship | None | Build passes | `git revert` |

### Batch summary

| Workstream | Result | Code change |
|---|---|---|
| §21/§27 Organization schema | legalName/email/telephone/address/vatID/identifier added; brand name unchanged | BaseLayout |
| §21/§29 contact identity | 2 pages de-TODO'd with real email/phone/company/address/USCC | contact + request-a-quote |
| §21 footer legal | company name + address + USCC small print site-wide | BaseLayout |
| §21 author entity | 108 author fields + 5 prose → "Landeng Tech Team" | 108 `.md` + methodology + knowledge-map |
| §21 homepage trust | brand↔entity relationship sentence | index.astro |
