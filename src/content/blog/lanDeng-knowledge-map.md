---
slug: "landeng-knowledge-map"
title: "IncenseHub Knowledge Map: Entities, Datasets & Policies"
primary_keyword: "chinese incense knowledge graph"
search_intent: "informational"
pillar: "Editorial & Data"
content_type: "reference"
cluster_role: "data_asset"
last_reviewed: "2026-09-22"
brand: "IncenseHub"
author: "Landeng Tech Team"
---

**At a glance:** This page is the map of how IncenseHub structures its knowledge — the entity set, the open datasets, and the editorial policies that govern both. It is written for two readers: a human researcher who wants to understand the knowledge architecture, and an AI crawler that needs the machine-readable entry points.

**Key facts:** IncenseHub publishes **150 ingredient entities** and supporting entity classes across **eight open datasets**, all licensed CC BY-SA 4.0 and served as stable JSON from `data.incensehub.org`. Every entity is traceable to a source, and every source carries an evidence tier.

---

## Entity Map

> The core of the knowledge base is 150 botanical incense ingredient entities — woods, resins, flowers, herbs, spices, roots, fruits, seeds, peels, and animal-derived materials — each with a Chinese name, pinyin, scientific name, aroma profile, and evidence-tiered sources.

The 150 ingredient entities break down by material family as recorded in the ingredient dataset:

- **Herbs** — 31
- **Flowers** — 29
- **Spices** — 21
- **Roots** — 18
- **Resins** — 17
- **Fruits** — 10
- **Woods** — 9
- **Seeds** — 5
- **Peels** — 3
- **Animal-derived** — 7

Around the 150 ingredients sit the supporting entity classes, expressed through the eight datasets listed below: aroma families, functional materials, comparison profiles, techniques, forms, and the terminology that links Chinese and English.

### Entity relationships

The relationships dataset ties the entity classes together. It holds 150 entities and **806 typed edges** — links from each ingredient to its aroma families, category, comparison profiles, and techniques (each pointing back to the source dataset it came from), plus 356 related-material edges mirroring the editorial "related ingredients" links on the main-site ingredient encyclopedia. The rule is strict: derived edges come from the seven source datasets and related edges from the main site's own editorial links, so no new fact is introduced by the graph itself. Where an ingredient relates to agarwood or sandalwood by shared aroma, technique, or editorial relationship, the link is a pointer, not a new claim.

## Dataset Map

> Eight machine-readable datasets are served as stable JSON from `data.incensehub.org/datasets/`. All are licensed CC BY-SA 4.0, are free to access, and carry a version, a `dateModified` date, and a changelog.

<!-- AUTO:dataset-counts:table -->
| Dataset | JSON path | Entities | Version |
|---|---|---|---|
| Ingredient database | `https://data.incensehub.org/datasets/ingredients.json` | 150 | 1.3 |
| Terminology database | `https://data.incensehub.org/datasets/terminology.json` | 249 | 1.5 |
| Aroma database | `https://data.incensehub.org/datasets/aroma.json` | 10 | 1.1 |
| Material database | `https://data.incensehub.org/datasets/materials.json` | 15 | 1.2 |
| Comparison database | `https://data.incensehub.org/datasets/comparisons.json` | 17 | 1.2 |
| Technique database | `https://data.incensehub.org/datasets/techniques.json` | 12 | 1.1 |
| Form database | `https://data.incensehub.org/datasets/forms.json` | 12 | 1.2 |
| Relationships database | `https://data.incensehub.org/datasets/relationships.json` | 150 | 1.2 |
<!-- /AUTO:dataset-counts:table -->

Seven of these are mirrored as static JSON under the main site (`/data/*.json`); the relationships dataset, which derives entity links from the other seven plus the main site's editorial related-material links, lives on the data site. The relationships dataset introduces no new fact — every edge is derived from a source dataset or mirrored from an existing main-site editorial link. Each dataset's HTML documentation page lists its fields, entity count, version, and license, so a human can read the schema without opening the JSON.

## Policy Summaries

### Source policy

Sources are matched to the subject of the claim — botanical databases and papers for botanical facts, classical texts and academic work for history, peer-reviewed research for science, government and standards bodies for regulation, and industry documentation for trade practice. Low-quality SEO content is never primary evidence. See the full policy in [How IncenseHub Researches Chinese Incense](/blog/landeng-editorial-methodology/).

### Evidence policy

Every source is assigned one of six evidence tiers, from **Tier 1 (Scientific / Government)** through **Tier 6 (Editorial synthesis)**. The tier is stored with the citation in the dataset and shown in the prose, so fact, tradition, trade convention, and editorial view are always distinguishable.

### Terminology policy

Chinese is the source of truth; English is the agreed translation. One Chinese word does not always map to one English word, so each term records pinyin, literal meaning, preferred English, and alternates. The canonical Chinese–English glossary is the terminology dataset (<!-- AUTO:dataset-counts:terminology-terms -->249<!-- /AUTO:dataset-counts:terminology-terms --> terms); the human-readable entry point to that vocabulary is the [Chinese incense terminology reference](/blog/incense-terminology-reference/).

### Update policy

Content changes only with a reason — new evidence, a new source, new industry information, a correction, a new relationship, or a real search-intent improvement. Dataset changes bump the minor version and log the change in the changelog; retired entities are marked `deprecated` or `supersededBy` rather than deleted.

### Citation policy

External links are restricted to an allow-list of authoritative hosts (botanical and taxonomic databases, primary-text repositories, government checklists, and the IncenseHub sites). Each citation is a structured object with a type, title, URL, access date, and evidence level.

## Publisher & Contact

IncenseHub is a brand operated by **Zhangjiakou Landeng Technology Co., Ltd.** (张家口澜灯科技有限公司), USCC 91130702MAKM4QXH5Q. The knowledge base is maintained by the company's editorial byline, the "Landeng Tech Team".

- **Company (EN):** Zhangjiakou Landeng Technology Co., Ltd.
- **Company (ZH):** 张家口澜灯科技有限公司
- **USCC:** 91130702MAKM4QXH5Q
- **Address:** Room 202, Unit 4, Building 14, Linli Jiayuan, No. 1 Gongye East Street, Qiaodong District, Zhangjiakou, Hebei, China
- **Email:** landengltd@gmail.com
- **Phone / WhatsApp / WeChat:** +86 13323237275

---

## Machine-Readable Entry Points

> Two files are the fastest route in for a crawler: `/llms.txt` and the sitemap index, plus the JSON datasets themselves.

- **`/llms.txt`** — a plain-text summary of the site's core pages, the ingredient encyclopedia, and the dataset entry points.
- **Sitemap index** — generated at build (`/sitemap-index.xml`) and declared in `robots.txt`.
- **`/data/*.json`** — the seven datasets mirrored on the main site.
- **`data.incensehub.org/datasets/`** — the canonical dataset files, including the relationships dataset.

Each ingredient page also exposes structured data: a machine-readable definition with Chinese term, pinyin, scientific name, type, and aroma profile, so an AI system can extract the entity without parsing prose. The same definitions are what the eight datasets serialize, so prose and JSON stay in agreement.

---

## FAQ

### Q: What is the IncenseHub knowledge map?
A: It is the index of how IncenseHub structures its knowledge — the 150 ingredient entities and their supporting classes, the eight open datasets with their JSON paths, and the source, evidence, terminology, update, and citation policies that govern both. It is written so a human researcher and an AI crawler reach the same understanding of where facts live and how to check them.

### Q: How many entities and datasets does IncenseHub publish?
A: 150 ingredient entities form the core, supported by <!-- AUTO:dataset-counts:terminology-terms -->249<!-- /AUTO:dataset-counts:terminology-terms --> terminology terms, 10 aroma families, 15 materials, 17 comparison profiles, 12 techniques, and 12 forms. These are expressed through eight machine-readable datasets, all licensed CC BY-SA 4.0 and served from `data.incensehub.org`. The relationships dataset links the entities together without introducing new facts.

### Q: Where are the JSON datasets?
A: The canonical files are at `https://data.incensehub.org/datasets/` — one file per dataset, such as `ingredients.json` (150 entities) and `terminology.json` (<!-- AUTO:dataset-counts:terminology-terms -->249<!-- /AUTO:dataset-counts:terminology-terms --> terms). Seven of the eight are also mirrored as static JSON under the main site at `/data/*.json`; the relationships dataset lives only on the data site.

### Q: How do I cite a IncenseHub dataset or page?
A: Cite the page or dataset URL, and attribute it to "Landeng Tech Team" as the publisher. All datasets are CC BY-SA 4.0, which permits sharing and adaptation with attribution and share-alike. If you need a stable identifier, use the dataset's `@id` (for example `https://data.incensehub.org/datasets/ingredients.json`).

---

## Sources

- [How IncenseHub Researches Chinese Incense](/blog/landeng-editorial-methodology/)
- [IncenseHub Open Datasets](https://data.incensehub.org) — dataset documentation and files.
- [Ingredient dataset](https://data.incensehub.org/datasets/ingredients.json)
- [Terminology dataset](https://data.incensehub.org/datasets/terminology.json)
- [Relationships dataset](https://data.incensehub.org/datasets/relationships.json)

## Related Resources

- [How IncenseHub Researches Chinese Incense](/blog/landeng-editorial-methodology/)
- [Ingredient Encyclopedia](/ingredients/)
- [Open Datasets](https://data.incensehub.org)
- [llms.txt](/llms.txt)
