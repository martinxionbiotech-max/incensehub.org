# Site audit — 2026-11-02

Scope: 281 rendered pages (282 HTML incl. 404), 266 content files, 206 images, 275 Markdown variants.
Method: `scripts/site-audit.py` over `dist/`, 4-gram similarity verifier vs the IncenseHub source archive, dataset validation, link crawl, `llms.txt`/sitemap/robots checks.

## Scorecard (weighted)

| Dimension | Score | Weight |
|---|---|---|
| Completeness | 90 | 15% |
| SEO (technical) | 85 | 20% |
| AIO / machine readability | 76 | 15% |
| Data consistency | 78 | 10% |
| Originality | 55 | 25% |
| Subjective insight | 86 | 10% |
| Content depth | 90 | 5% |
| **Overall** | **77 / 100** | 100% |

## Evidence

### Completeness — 90
- 281 indexable pages, sitemap 281 URLs, 150 ingredient pages = 150 dataset entities, 115 blog pages.
- 206 images, 193 rendered images with descriptive ALT (0 missing), 195 watermarked.
- 275 Markdown variants (7 intentionally skipped: 404 + 6 noindex).
- Gaps: 5 broken internal link targets (7 occurrences); 6 noindex pages still listed in sitemap.

### SEO — 85
- 100% unique titles and descriptions; canonical 100% self-referencing; one H1 per page (100%); lang=en 100%; viewport 100%.
- JSON-LD on 100% of pages, 0 parse errors: Organization/WebSite 281, FAQPage 254, DefinedTerm 150, Article 116, WebPage 151, BreadcrumbList 267.
- OG complete 100%, Twitter card 100%.
- Gaps: title length in 30–65 chars 90.4%; description length in 120–165 only 68.7% (69 too short, 19 too long); 5 broken links.

### AIO — 76
- `llms.txt` present (155 links, 0 broken); Markdown negotiation verified (275/282); robots.txt allows GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, CCBot and others; `Content-Signal` + `Link: describedby` headers.
- Gaps: `llms.txt` still advertises Wholesale / OEM / Private Label / "samples, quotes" — contradicts the knowledge-platform positioning; no Dataset schema in page JSON-LD (data lives on the separate data site).

### Data consistency — 78
- ingredients 150 unique = 150 pages; terminology 249 unique; comparisons 17; relationships 150; no duplicate termCodes.
- Gaps: 150 `relatedEntity` category refs point to `inDataset: ingredients.json` but use category names (`Woods`, `Resins`, …) that are not termCodes in that dataset (categories are stored as `additionalProperty`); data files `dateModified: 2026-09-28` are stale relative to 2026-11-02 content changes.

### Originality — 55
- 120/266 content files < 0.40 similarity vs IncenseHub; mean 0.663.
- 142/266 (53%) remain ≥ 0.80 similarity — essentially near-verbatim source copies.
- 265/266 have at least one original asset; 245/266 free of mechanical phrases.

### Subjective insight — 86
- 238/266 (89.5%) have ≥ 2 viewpoint markers; editorial boundaries ("does not mean", "unless", "misconception") present.
- Gaps: 28 pages below 2; two meta pages (knowledge map, editorial methodology) are structural, not content.

### Content depth — 90
- Mean 3,303 words, median 2,449, p10 1,959; 94.7% pages contain tables (1,088 total); FAQ 95.7%; Sources 95.7%; Direct answer 95%.
- Gaps: 19 `[need-source]` markers; 6 thin pages (<600 words) are all noindex commercial pages.

## Priority fixes

1. **P0 — Originality debt:** 142 pages ≥0.80 similarity. Rewrite in descending similarity order; this is the single largest score driver.
2. **P0 — Broken links:** map the five retired slugs to their current equivalents.
3. **P1 — Sitemap hygiene:** exclude the 6 noindex URLs from `sitemap-0.xml`.
4. **P1 — `llms.txt`:** remove Wholesale/OEM/Private Label/"samples, quotes" entries; align with the current positioning.
5. **P1 — Meta descriptions:** bring 88 outliers into 120–165 characters.
6. **P2 — Dataset:** fix category refs (add a categories dataset or point to the correct dataset); refresh `dateModified` after content changes.
7. **P2 — Insight/mechanics:** raise the 28 low-viewpoint pages; clear mechanical phrases on the 21 pages that still contain them.
