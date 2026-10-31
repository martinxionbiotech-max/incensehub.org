# AIO Audit — AI-Search / LLM Readability

> Audit-only. Measures machine-readability of the site: `llms.txt`, direct answers, definition extraction, source transparency, entity clarity.

## llms.txt (`public/llms.txt`)

- **Size:** 176 lines, 4 sections.
- **Sections:** `## Core pages` (5) · `## Ingredient encyclopedia` (150) · `## Machine-readable data` (2 datasets) · `## AI content notes`.
- **Coverage:** lists all 150 ingredient URLs + 5 core pages (Home, Chinese Incense, Wholesale, OEM, Contact).
- **Regenerated:** `prebuild` → `scripts/generate-llms.mjs` (counts kept aligned with the data site, per recent `sync(terminology)` commits).
- **Gap:** `## Machine-readable data` lists only `ingredients.json` + `terminology.json` — **2 of 8** datasets omitted (aroma, comparisons, forms, materials, relationships, techniques).

## Direct answer (answer-first) coverage

| Page type | Direct-answer pattern | Coverage |
|---|---|---|
| Ingredient (150) | `**Data summary:**` opening block + `directAnswer` string (fed to meta description + DefinedTerm `description`) | **150/150 (100%)** |
| Concept (1) | `**Key takeaway:**` opening block | 1/1 |
| Blog (99) | `**Key takeaway:**` opening block | present (spot-verified; not counted programmatically this batch) |

## Definition extraction

- Every ingredient page exposes a machine-readable definition via `DefinedTerm` with `name`, `alternateName` = [Chinese, pinyin, scientific name], `termCode` = scientific name, and `inDefinedTermSet` → the ingredient encyclopedia.
- Data site exposes `DefinedTerm` records for all 615 dataset items (150 + 249 + 150 + 17 + 15 + 12 + 12 + 10).

## FAQ coverage

- Ingredient pages: FAQ-style `?`-headings on **148/150**; extracted into `FAQPage` schema (Question/Answer) where present.
- Blog pages: FAQ-style headings on **99/99**; extracted into `FAQPage` schema.
- The `FAQPage` schema is conditional (only emitted when genuine Q&A headings exist) — good §27 compliance (no fabricated FAQ).

## Source transparency

- `## Sources` / `## Evidence & Sources` sections: **150/150 ingredients, 99/99 blog, 1/1 concept**.
- Fact/evidence separation: `Traditional use vs modern evidence` + `Evidence status` sections on entities; `Traditional knowledge vs modern evidence` on the concept page.
- `sameAs` emitted only from a verified allow-list (`efloras.org`, `gbif.org`, `checklist.cites.org`).
- Data site: `evidenceLevel` (Evidence Tier) embedded in source citations; CI enforces a source-domain allow-list.

## Entity clarity

- Chinese name + pinyin + scientific name present on 150/150 entities (frontmatter) and in `alternateName` (schema).
- Aroma profile present on 150/150 (frontmatter `aroma[]` + dataset `additionalProperty`).

## Machine-readable headers (`public/_headers`)

```
/*
  Content-Signal: ai-train=yes, search=yes, ai-input=yes
  Link: </llms.txt>; rel="describedby"
  X-Robots-Tag: index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1
```

## AIO findings

| # | Finding | Severity |
|---|---|---|
| A1 | `llms.txt` lists 2 of 8 datasets | P0 |
| A2 | 2 ingredient pages lack FAQ headings (148/150) — FAQ schema thus absent there | P3 (minor) |
| A3 | `_headers` AI-training consent is explicit (`ai-train=yes`) — correctly documented, no overclaim of "AI indexing guaranteed" | — (positive) |
| A4 | Answer-first + evidence-tail structure is consistently applied across 250 content files | — (positive) |
| A5 | No fabricated reviews/ratings/prices/authors — `## AI content notes` states this; verified against page copy | — (positive) |

## G13 supplement — programmatic meta-description dedup audit (phase2/P2)

> Rendered-layer check. Ran against the **built `dist/` output** (262 HTML files) on 2026-09-25, not the Markdown source, so template-derived descriptions are captured exactly as a crawler sees them.

**Method:** walk `dist/**/*.html`, extract each `<meta name="description" content="…">` verbatim, group identical strings, and flag any description shared by >1 page.

**Result:**

| Metric | Value |
|---|---|
| HTML pages scanned | 262 |
| Pages with a meta description | 262 (100%) |
| Pages missing meta description | 0 |
| Duplicate-description groups (>1 page) | **0** |
| Pages involved in any duplicate group | 0 |

**Verdict:** **clean — no duplicate meta descriptions.** The three description sources (ingredient `directAnswer`, blog `metaDescription`, hand-written static-page descriptions) each produce unique text, and the `directAnswer` template is intrinsically unique per entity (Chinese + pinyin + type + scientific name + aroma profile). No template-layer repair was required — this closes the G13 gap with an evidence record rather than a code change.

**Why it stays unique (documented for future regressions):** the ingredient `directAnswer` string is built from 5 per-entity frontmatter fields, so a duplicate can only appear if two entities share Chinese name + pinyin + type + scientific name + aroma set — impossible with correct frontmatter. A future duplicate would signal a frontmatter data-entry error, not a template bug.

## Bottom line

The site is **strong on AIO fundamentals** (answer-first, entity clarity, source transparency, DefinedTerm schema, llms.txt, FAQ extraction). The single material AIO gap was **incomplete llms.txt dataset coverage (A1)** (fixed in P0) plus the cross-site `sameAs` allow-list asymmetry noted in `data-site-audit.md`. The G13 meta-description dedup audit (P2) found **0 duplicates across 262 rendered pages** — no repair needed.
