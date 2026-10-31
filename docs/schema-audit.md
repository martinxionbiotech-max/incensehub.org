# Schema Audit — JSON-LD / Structured Data

> Audit-only. Catalogues every `application/ld+json` emission point and type, and checks `@id` consistency, `mainEntity`, and `sameAs`.

## Emission points (6 files, 9 `<script type="application/ld+json">` templates)

| File | Emitted types | Applies to |
|---|---|---|
| `src/layouts/BaseLayout.astro` | Organization, WebSite | **every page** (site-wide) |
| `src/pages/index.astro` | Organization, WebSite | homepage (duplicate — see F1) |
| `src/pages/ingredients/[slug].astro` | WebPage, BreadcrumbList, DefinedTerm (+ FAQPage conditional, ImageObject, PropertyValue) | 150 entity pages |
| `src/pages/ingredients/index.astro` | CollectionPage (→ ItemList → ListItem), BreadcrumbList | ingredient index |
| `src/pages/blog/[slug].astro` | Article, BreadcrumbList (+ FAQPage conditional) | 99 blog pages |
| `src/pages/chinese-incense/index.astro` | WebPage, BreadcrumbList, Article | concept page |

> Note: the Phase-2 brief referenced "764 JSON-LD blocks". The **actual** rendered block count is far lower — the site uses ~9 schema templates (not per-entity inline blocks). Organization + WebSite render on all 258 URLs; WebPage/BreadcrumbList/DefinedTerm on 150 entity pages; Article/BreadcrumbList on 99 blog pages. Per-page blocks are constructed programmatically, not stored as 764 literal blocks.

## Type distribution (Schema.org)

`Organization · WebSite · WebPage · BreadcrumbList · ListItem · DefinedTerm · DefinedTermSet · CollectionPage · ItemList · Article · FAQPage · Question · Answer · ImageObject · PropertyValue` — plus, on the data site: `Dataset · DefinedTerm · DataDownload`.

**Schema usage is conservative** — no `Product`, no `Review`, no `AggregateRating`, no fabricated ratings/reviews (matches §27 policy).

## `@id` consistency

| @id | Defined in | Notes |
|---|---|---|
| `{SITE}#organization` | BaseLayout + index.astro | ⚠️ duplicated on homepage (F1) |
| `{SITE}#website` | BaseLayout + index.astro | ⚠️ duplicated on homepage (F1) |
| `{pageUrl}#webpage` | ingredients/[slug] | unique per entity |
| `{pageUrl}#breadcrumb` | ingredients/[slug], blog/[slug], chinese-incense | unique per page |
| `{pageUrl}#definedterm` | ingredients/[slug] | unique per entity |
| `{pageUrl}#article` | blog/[slug], chinese-incense | unique per page |

`isPartOf` / `publisher` / `breadcrumb` references resolve to `#website` / `#organization` / `#breadcrumb` consistently.

## `mainEntity` relationships

- **Entity page:** `WebPage.mainEntity → DefinedTerm` (correct).
- **Ingredient index:** `CollectionPage.mainEntity → ItemList` (correct).
- **Concept page:** `WebPage.mainEntity → Article` (correct).
- **Blog page:** `Article` is the top-level node (correct — no WebPage wrapper, minor structural inconsistency vs entity pages).

## `sameAs` handling

- Emitted only on entity pages, from the `## Sources` section, filtered through `SAMEAS_HOSTS = ['efloras.org', 'gbif.org', 'checklist.cites.org']`.
- `termCode` = scientific name (not slug) — a deliberate choice but a potential identity-mismatch: the data-site `ingredients.json` uses `termCode = slug`. **Cross-system `termCode` semantics differ** (scientific name on main site vs slug on data site).

## `DefinedTermSet` / dataset linkage

- Entity pages emit `inDefinedTermSet` → "IncenseHub Chinese Botanical Incense Ingredient Encyclopedia" (URL = `/ingredients/`).
- The data site is the authoritative `Dataset` layer (8 files).

## Findings

| # | Finding | Severity |
|---|---|---|
| F1 | Homepage emits Organization + WebSite **twice** (index.astro + BaseLayout) → duplicate `@id` in one document | **P0** |
| F2 | `termCode` semantics differ between main site (scientific name) and data site (slug) | P2 |
| F3 | Blog pages have no `WebPage` wrapper (Article is top-level) — minor structural inconsistency vs entity/concept pages | P3 |
| F4 | `sameAs` allow-list narrower than data-site CI allow-list (missing `wikisource.org`) | P2 |
| F5 | No `sameAs` emitted unless sources contain allow-listed URLs — some Tier-1 entities may lack `sameAs` entirely | P3 |

## G16 supplement — `sameAs` allow-list review (phase2/P2)

> Review of the entity-page `sameAs` emission against the rendered build, to decide whether the `SAMEAS_HOSTS` allow-list should be widened.

### Measured `sameAs` distribution (dist render, 150 entity pages)

| Host | sameAs URLs emitted |
|---|---|
| `www.gbif.org` | 158 |
| `www.efloras.org` | 106 |
| `checklist.cites.org` | 8 |
| **Total** | **272** |

- Entity pages emitting `sameAs`: **149/150**. The single exception is `amber` (琥珀) — its `## Sources` section cites `本草纲目` / `香乘` on Wikisource, which are outside the current allow-list, so no `sameAs` is emitted there (F5, documented, not a defect per §27).
- The current allow-list (`SAMEAS_HOSTS = ['efloras.org', 'gbif.org', 'checklist.cites.org']`) yields **only species-authority identity URLs** — exactly the references that unambiguously identify a botanical entity.

### Question: add `zh.wikisource.org` (Wikisource) to the allow-list?

Wikisource is already **extensively cited in `## Sources` sections** — 74 content files link `zh.wikisource.org` (香乘, 香譜, 本草綱目, 遵生八箋, 夢粱錄), and the data-site CI allow-list includes `wikisource.org` for **citation** URLs.

**Decision: do NOT add Wikisource to `sameAs`. Keep the allow-list identity-only.**

Rationale:
1. **Semantic distinction.** `sameAs` should point to references that *identify the entity* (taxonomic authority records). Wikisource pages are **historical texts / citations**, not identity records — a `本草綱目` chapter describes many materials and does not canonically identify a single ingredient. Mixing citations into `sameAs` would dilute the identity graph.
2. **Wikisource already has a home.** Classical texts are correctly emitted in `## Sources` (citation layer), which is where they belong. Nothing is lost by excluding them from `sameAs`.
3. **The F4 "asymmetry" is resolved as intentional, not a defect.** The data-site CI allow-list governs *citation/source* URLs (broad, includes Wikisource); the main-site `SAMEAS_HOSTS` governs *identity* URLs (narrow, species authorities). Two different allow-lists serve two different purposes — consistent, not divergent.

**Resolution recorded:** no code change. `sameAs` remains restricted to `efloras.org` / `gbif.org` / `checklist.cites.org`. `amber`'s missing `sameAs` is accepted (its authority citations are textual, not taxonomic).

## Bottom line

Structured data is **correctly conservative and largely consistent** (single @id graph, mainEntity wiring, no fabricated ratings/reviews). The concrete defects are the homepage duplicate (F1, fixed in P0) and the `termCode` semantics asymmetry (F2, deferred). The F4 `sameAs` asymmetry is **resolved as intentional** in the G16 review (P2): `sameAs` stays identity-only; Wikisource remains a citation-layer domain.

---

## §43 supplement — Open Graph / Twitter card audit (phase2/P2)

> Rendered-layer scan of the social-share metadata emitted by `BaseLayout.astro` across the full `dist/` build. Covers `og:title` / `og:description` / `og:image` / `og:url` / `twitter:card` (plus `og:type`, `og:site_name`, `twitter:title`, `twitter:description`, `twitter:image`).

### Coverage (268 rendered HTML pages)

| Tag | Missing before | Missing after |
|---|---|---|
| `og:title` | 0 | 0 |
| `og:description` | 0 | 0 |
| `og:image` | 0 | 0 |
| `og:url` | 0 | 0 |
| `twitter:card` | 0 | 0 |
| `og:type` | 0 | 0 |
| `og:site_name` | 0 | 0 |
| `twitter:title` | 0 | 0 |
| `twitter:description` | 0 | 0 |
| `twitter:image` | **268** | 0 |

All five required tags were already present on every page via the single `BaseLayout.astro` emission point (no per-page override, no partial templates). The audit nevertheless surfaced **three template-layer defects**, all fixed.

### Defect 1 — `og:image` double-slash URL (fixed)

`BaseLayout.astro` built the share image URL with `new URL('images/…', \`${SITE}/\`)`, and `SITE` (= `Astro.site.toString()`) already carries a trailing slash — producing `https://incensehub.org//images/og-image-…jpg` (double slash after the host).

**Fix:** `new URL('images/…', SITE)` (drop the extra `/`). Rendered output is now a clean single-slash URL. The image itself (`public/images/og-image-incense-still-life-1200x630.jpg`, the existing site-default share image) is reused — no new image was created.

### Defect 2 — `twitter:image` absent (fixed)

The card is declared `summary_large_image` but `twitter:image` was never emitted (268/268 missing). X/Twitter falls back to `og:image`, so the card still rendered, but the explicit tag is required for a reliable large-image card and for platforms that do not read `og:*`.

**Fix:** added `<meta name="twitter:image" content={ogImage} />` pointing at the same site-default share image (no new image).

### Defect 3 — malformed `description` on 9 image-first blog posts (fixed)

`blog/[slug].astro` derives the meta description (and therefore `og:description` + `twitter:description`) from `post.body` by stripping markdown punctuation only. Nine blog posts open their body with an `<img>` tag before any prose, so their description **began with the literal `<img src=…>` tag** (hyphens collapsed to spaces by the punctuation-strip regex). This corrupted the SERP meta description and the social-share description for those 9 pages.

**Fix:** strip HTML tags (`<[^>]+>`) before punctuation-stripping in the description derivation. Verified: all 9 descriptions now start with real prose (e.g. `Quick answer: Aromatherapy works through the sense of smell…`); 0 remaining `<img` prefixes in `dist/`.

### Findings table (additions)

| # | Finding | Severity | Disposition |
|---|---|---|---|
| F6 | `og:image` URL had a double slash after the host | P2 | Fixed (BaseLayout) |
| F7 | `twitter:image` missing on all 268 pages (card = `summary_large_image`) | P2 | Fixed (BaseLayout) |
| F8 | Meta/OG/Twitter description began with an `<img>` tag on 9 image-first blog posts | P2 | Fixed (blog `[slug].astro`) |
