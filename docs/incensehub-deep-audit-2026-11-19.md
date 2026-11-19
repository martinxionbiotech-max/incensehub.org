# IncenseHub.org — Deep Audit: Content, Structure, SEO, AIO

**Date:** 2026-11-19  
**Mode:** READ_ONLY — no content page changed  
**Site:** https://incensehub.org/  
**Repo:** `/root/.openclaw/workspace/repos/incensehub.org`  
**HEAD:** `cc4bd1e`  
**Build:** 285 HTML files / 278 sitemap URLs / 1 Markdown sidecar

---

## 1. Executive summary

IncenseHub is a substantial, long-form content site with a clean technical base and low internal duplication. It is not a thin-content or template-spam site in its current form.

The main problems are **metadata scale, AIO consistency and internal linking**, not body-copy quality:

- 68 rendered titles exceed 60 characters.
- 23 rendered descriptions exceed 160 characters.
- 2 commercial pages are orphaned: `/private-label/` and `/incense-manufacturer/`.
- `/privacy/` returns 404, while `/privacy-policy/` is the live legal page.
- `llms.txt` has 277 normalized links versus 278 sitemap URLs; 6 llms links are not in the sitemap and 7 sitemap URLs are absent from llms.
- `llms.txt` contains `.md` links that return 404.
- Only 1 Markdown sidecar is generated; Markdown negotiation works, but the sidecar/link layer is incomplete.
- 254/285 pages emit FAQPage schema; this needs a quality check, not automatic removal.

**Current evidence score: 79.1 / 100 — good, with P1 metadata/AIO cleanup remaining.**

No evidence of current internal body duplication: no 4-gram pair reached 0.30.

The old 2026-10-31 audit alleged near-total duplication against `/root/.openclaw/workspace/repos/IncenseHub`. That source path is now absent. Against the available `/root/.openclaw/workspace/repos/LanDeng` archive, 264 matching files show **mean 4-gram Jaccard 0.018, max 0.081** — no support for the old “266/266 highly similar” conclusion. Treat that comparison as archive-dependent, not proof about an unavailable source.

---

## 2. Inventory

### Content

| Collection | Files | Word range | Mean |
|---|---:|---:|---:|
| ingredients | 150 | 3,881–11,402 | 6,123 |
| blog | 117 | 1,282–9,213 | 3,892 |
| concepts | 2 | 4,182–4,983 | 4,582 |
| **Total** | **269** | | |

Rendered word distribution:

```text
1,500+ words: 273 pages
800–1,500: 5 pages
300–800: 2 pages
under 300: 4 pages
```

The four under-300 pages are utility/index-type pages, not thin articles.

### URL structure

| Section | Sitemap URLs |
|---|---:|
| ingredients | 151 |
| blog | 118 |
| home | 1 |
| about | 1 |
| chinese-incense | 1 |
| agarwood-sandalwood | 1 |
| cookies | 1 |
| disclaimer | 1 |
| privacy-policy | 1 |
| safety | 1 |
| terms-of-service | 1 |
| **Total** | **278** |

Build contains 285 HTML files: 278 sitemap pages + 6 noindex commercial pages + 404.

### Metadata and provenance

| Item | Coverage |
|---|---:|
| Content files with Sources/References | 269 / 269 |
| `last_reviewed` | 269 / 269 |
| Blog author | 117 / 117 |
| Ingredient author | 0 / 150 |
| Concept author | 0 / 2 |
| Sources with external links | 269 / 269 |

The source layer is complete in the sense that every content page has a Sources section. Author attribution is uneven: blog has an author field; ingredients and concepts do not.

---

## 3. Content quality

### Internal duplication — PASS

No 4-gram pair within any collection reached 0.30.

Unique-sentence share:

| Collection | Mean | Min |
|---|---:|---:|
| blog | 0.90 | 0.75 |
| concepts | 0.86 | 0.80 |
| ingredients | 0.91 | 0.84 |

The lowest pages are `agarwood-grading-guide` (0.75), `agarwood-formation-and-species` (0.80), and `zedoary`/`cedar`/`sandalwood` (0.84–0.85). These are manual-review candidates, not rewrite candidates.

### Repetition against the available source archive

Comparison target: `/root/.openclaw/workspace/repos/LanDeng/src/content`  
Matched files: 264 / 269 (5 current files have no source counterpart).

| Metric | Result |
|---|---:|
| Mean 4-gram Jaccard | **0.018** |
| Median | 0.015 |
| Max | 0.081 |
| Pairs ≥0.80 | 0 |

This is evidence that the current corpus is substantially rewritten relative to the available archive. It does **not** prove originality against the missing `/repos/IncenseHub` source.

### AI-style language — PARTIAL / P2

Mechanical phrase scan:

```text
208 hits across 269 content files
```

The site has a long-form, specific voice, but the phrase count is high enough for a targeted edit pass. Do not remove technical vocabulary mechanically.

### Empty marketing language — PASS

Only 3 empty-phrase hits were found across the corpus.

### Thin content — PASS

No editorial page is under 300 words. The four short pages are utility/index pages.

### Content depth — strong

- Ingredients: 3,881–11,402 words, mean 6,123.
- Blog: 1,282–9,213 words, mean 3,892.
- Concepts: 4,182–4,983 words.
- 273 pages are 1,500+ words.

This is a deep corpus, not a “more pages” problem.

---

## 4. Structure and internal linking

### Verified

- 285 HTML files.
- 278 sitemap URLs.
- 6 noindex commercial pages, correctly excluded from sitemap.
- 0 broken internal links.
- 2 orphan HTML pages in the local link graph.
- Canonical self-reference: 0 mismatches.
- Single H1: 0 violations.
- 0 duplicate titles.
- hreflang: none; correct for a single-language site.

### Orphans

The local link graph identifies these as having no inbound internal link:

```text
/private-label/
/incense-manufacturer/
```

`/404.html` is also unlinked but is not an editorial page.

Both orphans are commercial pages and should receive contextual links from:

- `/contact/`
- `/request-a-quote/`
- `/wholesale/`
- relevant `oem` / custom-development pages
- at least one blog page about manufacturing or private label

### Legacy legal URL

`/privacy/` returns **404**, while the correct page is:

```text
/privacy-policy/
```

If `/privacy/` has ever been linked or indexed, add a 301 to `/privacy-policy/`. Do not create a duplicate legal page.

---

## 5. SEO

### Verified

| Check | Result |
|---|---:|
| Missing title / description / canonical | 0 |
| Duplicate titles | 0 |
| H1 ≠ 1 | 0 |
| Broken internal links | 0 |
| JSON-LD parse errors | 0 |
| Sitemap URLs | 278 |
| Sitemap includes noindex | 0 |
| Canonical mismatch | 0 |

### Issues

**P1 — rendered titles over 60 characters**

```text
68 / 285 pages
```

Examples:

```text
/                                     66
/ingredients/                         63
/ingredients/aromatic-turmeric/       63
/ingredients/litsea-cubeba/           62
/ingredients/ligusticum/              61
```

**P1 — rendered descriptions over 160 characters**

```text
23 / 285 pages
```

**P2 — privacy route**

`/privacy/` 404; `/privacy-policy/` 200. Add a redirect only if the old route has inbound links or historical indexing.

### Social / structured data

- Organization: 284 pages.
- WebSite: 284 pages.
- BreadcrumbList: 270 pages.
- FAQPage: 254 pages.
- WebPage: 152 pages.
- DefinedTerm: 150 pages.
- Article: 119 pages.
- CollectionPage: 1 page.
- JSON-LD parse errors: 0.

FAQPage on 254 pages is very broad. It is not automatically invalid, but every page should have actual visible FAQ content and a unique Q&A set. Do not remove schema before checking the visible FAQ blocks.

---

## 6. AIO configuration

### Working

- `llms.txt`: 200, 18,976 bytes, 277 normalized links.
- Markdown negotiation:

```text
Accept: text/markdown
→ 200
→ content-type: text/markdown; charset=utf-8
→ vary: Accept
```

- `Accept: text/markdown;q=0` returns HTML.
- `robots.txt` explicitly allows major AI crawlers (GPTBot, ClaudeBot, PerplexityBot, CCBot and others).
- Markdown response includes frontmatter.
- HTML and Markdown negotiation work on sampled home, blog and ingredient pages.

### Gaps

**P1 — llms/sitemap mismatch**

```text
sitemap: 278
llms normalized links: 277
llms links not in sitemap: 6
sitemap URLs absent from llms: 7
```

Examples of llms-only links:

```text
/blog/agarwood-grading-guide.md
/chinese-incense.md
/ingredients/agarwood.md
/contact/
```

Examples of sitemap URLs missing from llms:

```text
/agarwood-sandalwood/
/cookies/
/disclaimer/
/ingredients/
/privacy-policy/
/safety/
/terms-of-service/
```

**P1 — `.md` links return 404**

`llms.txt` points at URLs such as:

```text
/blog/agarwood-grading-guide.md
/ingredients/agarwood.md
```

These return **404**, not Markdown.

**P1 — sidecar coverage**

Only 1 Markdown sidecar exists in the build. Markdown negotiation works dynamically, but direct `.md` sidecars are not a complete parallel representation.

### Fix direction

- Either generate all `.md` sidecars and make llms links point to them,
- or remove `.md` links from llms and use HTML URLs.
- Add the missing 7 sitemap pages to llms where they are genuinely useful.
- Do not include noindex commercial pages in llms unless they are intentionally public.

---

## 7. Technical and security

- Live homepage: 200.
- `robots.txt`: 200, 440 bytes, explicit AI crawler policy.
- `sitemap-index.xml`: 200, `application/xml`.
- `llms.txt`: 200, `text/plain`.
- `http://` and `www` resolve to the apex HTTPS site.
- Unknown path returns a real 404.
- 285 HTML / 278 sitemap / 6 noindex is internally consistent.
- No internal broken links were found by the local scan.
- 2 orphans are a structure issue, not a broken-link issue.

Not measured:

- Lighthouse / Core Web Vitals.
- GSC traffic, coverage or manual actions.
- Deep `data.IncenseHub` content consistency.

---

## 8. Seven-dimension score

| Dimension | Weight | Score | Evidence |
|---|---:|---:|---|
| Completeness | 15% | 90 | 285 HTML / 278 sitemap; 2 orphans; 1 md sidecar |
| SEO | 20% | 70 | 68 long titles, 23 long descriptions; canonical/H1 clean |
| AIO | 15% | 60 | negotiation works; llms mismatch and broken `.md` links |
| Data consistency | 10% | 80 | all content sources/last_reviewed; author gaps; 6 noindex consistent |
| Originality | 25% | 90 | no internal duplicates; available archive mean 0.018; external original unverified |
| Subjective insight | 10% | 75 | long-form opinion present; ingredient/concept author attribution thin |
| Content depth | 5% | 92 | 273 pages 1,500+ words; no thin editorial pages |
| **Weighted total** | | **79.1** | **Good / needs P1 cleanup** |

This is an evidence score, not a Google ranking prediction.

---

## 9. Priority fix list

### P0

None found in the current build.

### P1

1. **Fix llms/sitemap coherence**
   - Align 277/278 counts.
   - Remove or generate the 6 `.md` links that currently 404.
   - Add the 7 sitemap pages that are absent from llms where relevant.
2. **Fix 68 long rendered titles**
   - Fix at template/metadata layer, not by rewriting bodies.
3. **Fix 23 long rendered descriptions**
   - Prioritize high-intent ingredient and blog pages.
4. **Add inbound links to the two orphans**
   - `/private-label/`
   - `/incense-manufacturer/`
5. **Decide the `/privacy/` legacy route**
   - 301 to `/privacy-policy/` if it has inbound or historical links; otherwise leave 404.

### P2

6. Add author/byline for ingredients and concepts, or explicitly state “editorial team” ownership.
7. Audit the 254 FAQPage instances against visible FAQ blocks; remove empty or duplicated FAQ schema only after verification.
8. Run a targeted AI-phrase cleanup (208 hits) without flattening technical language.
9. Review the 4 under-300 utility pages for missing context.
10. Audit `data.IncenseHub` entity/source consistency separately.

---

## 10. Old audit correction

The 2026-10-31 report claimed:

- 266/266 files at ≥0.80 similarity to `/repos/IncenseHub`.
- Mean 0.9409.
- 51 identical files.

That source path is no longer available in the workspace. The available `LanDeng` archive comparison gives:

```text
matched files: 264 / 269
mean Jaccard: 0.018
max: 0.081
≥0.80: 0
```

The old result cannot be independently reproduced and should not be carried forward as a current finding. The current corpus should be judged on the available archive and on a future source-corpus audit if the original archive is restored.

---

## 11. Verdict

IncenseHub is **content-rich, internally unique, and technically routable**. It is not a thin-content site.

The current release risks are:

1. **AIO link integrity** — llms points at missing `.md` URLs and disagrees with the sitemap.
2. **Metadata scale** — 68 long titles and 23 long descriptions.
3. **Two orphan commercial pages**.
4. **A missing legacy `/privacy/` route**.
5. **FAQPage schema breadth** requiring visible-content verification.

Do not add more articles until these P1 structural/AIO issues are fixed.
