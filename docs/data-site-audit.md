# Data Site Audit — data.incensehub.org (8 Datasets)

> Audit-only. Populated from `data-landeng/datasets/*.json`, `mkdocs.yml`, `.github/workflows/validate.yml`, `hooks.py`.

## Overview

| Dataset | `@type` | Records | `@type` (items) | Version | dateModified | License |
|---|---|---|---|---|---|---|
| `ingredients.json` | Dataset | 150 | DefinedTerm | 1.1 | 2026-09-22 | CC BY-SA 4.0 |
| `terminology.json` | Dataset | 249 | DefinedTerm | 1.4 | 2026-09-24 | CC BY-SA 4.0 |
| `relationships.json` | Dataset | 150 (450 edges) | DefinedTerm | 1.0 | 2026-09-22 | CC BY-SA 4.0 |
| `comparisons.json` | Dataset | 17 | DefinedTerm | 1.1 | 2026-09-22 | CC BY-SA 4.0 |
| `materials.json` | Dataset | 15 | DefinedTerm | 1.1 | 2026-09-22 | CC BY-SA 4.0 |
| `forms.json` | Dataset | 12 | DefinedTerm | 1.1 | 2026-09-22 | CC BY-SA 4.0 |
| `techniques.json` | Dataset | 12 | DefinedTerm | 1.1 | 2026-09-22 | CC BY-SA 4.0 |
| `aroma.json` | Dataset | 10 | DefinedTerm | 1.0 | 2026-09-22 | CC BY-SA 4.0 |

**Total records: 615** (150 + 249 + 150 + 17 + 15 + 12 + 12 + 10).

## Schema structure (uniform)

Every dataset file is a Schema.org `Dataset` with:

- `@context` (schema.org), `@type: Dataset`, `@id` (= canonical URL)
- `name`, `description`, `url`
- `publisher: { @id }`
- `dateModified`, `license`, `version`, `changelog`
- `inLanguage` (["en", "zh"] where applicable), `isAccessibleForFree: true`
- `distribution: { @type, encodingFormat, contentUrl }`
- `mainEntity: DefinedTerm[]`

### DefinedTerm record shape

- `ingredients.json` item: `@type, termCode (=slug), name, alternateName ([中文, pinyin, scientific]), description, additionalProperty ([Chinese, Pinyin, Scientific name, …]), sameAs, sources` (sources carry `evidenceLevel`).
- `terminology.json` item: `@type, termCode, name (中文), description, additionalProperty ([Pinyin, Literal meaning, Preferred English, …])`.
- `relationships.json` item: `@type, termCode, name, relatedEntity: [{ type: category|aroma|…, termCode, name, inDataset }]` — **450 edges total**; degree distribution `{1:7, 2:39, 3:67, 4:27, 5:8, 7:1, 9:1}`.

## Documentation (docs/ in data repo)

`index.md`, `datasets.md` (overview), `format.md` (governance), plus per-dataset pages: `ingredients.md`, `terminology.md`, `aroma.md`, `materials.md`, `comparisons.md`, `techniques.md`, `forms.md`, `relationships.md`.

## CI (`.github/workflows/validate.yml`)

Runs on push/PR to `main`, checks:
1. JSON parses for all 8 files (fails if count ≠ 8)
2. `termCode` uniqueness within each file
3. every citation/source URL domain is on the allow-list (`efloras.org`, `gbif.org`, `wikisource.org`, `checklist.cites.org`, `data.incensehub.org`, `incensehub.org`, `schema.org`)
4. MkDocs site builds cleanly

## Build / single-source-of-truth

- Canonical JSON lives in `datasets/`; `hooks.py` (`on_post_build`) copies `datasets/*.json` into the built `site/datasets/`.
- `mkdocs.yml` `site_url: https://data.incensehub.org`, `readthedocs` theme, cross-link nav to `incensehub.org`.

## Consistency with main site

| Check | Result |
|---|---|
| Entity name / Chinese / pinyin / scientific ↔ ingredient pages | ✅ match (termCode = slug = entity) |
| Terminology count synced | ✅ 249 across both sites + llms.txt |
| **`relationships.json` present in main-site `data/` + `public/data/`** | ❌ **missing** (main site holds 7 files, data site holds 8) |
| Main-site `_redirects` points `/data/*.json` → data site | ✅ correct 301 routing |

## Dataset governance (positive findings)

- Per-file `version` + `changelog` + truthful `dateModified`.
- `evidenceLevel` (Evidence Tier) embedded in source citations.
- License is explicit (CC BY-SA 4.0) — not fabricated.
- Deprecation/supersededBy governance documented in `format.md`.

## Findings / gaps

1. **P0 — main-site mirror missing `relationships.json`** (7 vs 8 files). Main site cannot serve the relationship graph locally.
2. **P2 — `sameAs` allow-list asymmetry:** data-site CI permits `wikisource.org`, but the main-site entity-page `SAMEAS_HOSTS` allow-list is narrower (`efloras.org`, `gbif.org`, `checklist.cites.org`) — sameAs may differ between the two layers.
3. **P2 — no human-readable dataset landing on the main site:** the 8 datasets are reachable only via data site + footer links; main site has no `/data/` overview page (redirected away).
4. **No machine-readable endpoint on the main-site origin** — all dataset URLs 301 to the data subdomain (correct for single-source-of-truth, worth documenting as intentional).
