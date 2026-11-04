# IncenseHub — Chinese Incense Knowledge

**An independent, English-language knowledge platform for Chinese botanical incense.**

IncenseHub documents Chinese incense — its materials, botanicals, history, terminology, craft and culture — as original, machine-readable, search- and AI-discoverable English content. It is a knowledge platform, not a store: there is no catalog, no quote process, and nothing to buy here.

## Positioning

- **What it is:** an independent reference for Chinese incense — what each material is, how it forms or is made, how it is graded, and how to judge quality against adulteration.
- **What it is not:** a sleep-medicine site, an insomnia-treatment site, an anxiety-treatment site, a generic aromatherapy store, or a manufacturer's sitefront.
- **"Evening ritual" is a use-case cluster, not a medical claim.**
- **Knowledge first:** every claim is traced to its source; traditional knowledge is labeled separately from modern evidence; no health or medical claims are made.

## Content model

Seven knowledge domains organize the site: materials & entities, authentication & quality, formation & principles, craft & technique, aroma & atmosphere, culture & history, and the 合香 blending system. See [docs/incensehub-transformation-plan.md](docs/incensehub-transformation-plan.md) and [docs/incensehub-inventory.md](docs/incensehub-inventory.md) for the content disposition.

## Technical stack

- **Astro** (static generation) — knowledge / SEO / AIO content
- **Schema.org JSON-LD** — Article, DefinedTerm, BreadcrumbList, FAQPage, Organization
- **Open datasets** — eight machine-readable JSON datasets (ingredients, terminology, aroma, materials, comparisons, techniques, forms, relationships), served from `data.incensehub.org` under CC BY-SA 4.0
- **`llms.txt`** + Markdown content negotiation for AI crawlers

## Documentation-first workflow

This repository follows a documentation-first gate. The `docs/` directory is the single source of truth for strategy, models, inventories and governance.

## Documentation index

| Doc | Purpose |
|---|---|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Information + technical architecture |
| [SITEMAP.md](docs/SITEMAP.md) | URL taxonomy |
| [SEO-MASTER-MAP.md](docs/SEO-MASTER-MAP.md) | Keyword → intent → entity → page map |
| [AIO-STRATEGY.md](docs/AIO-STRATEGY.md) | AI search / agent discovery strategy |
| [ENTITY-MODEL.md](docs/ENTITY-MODEL.md) | Entity definitions |
| [KNOWLEDGE-GRAPH.md](docs/KNOWLEDGE-GRAPH.md) | Entity relationship graph |
| [CONTENT-MODEL.md](docs/CONTENT-MODEL.md) | Content types + templates |
| [CONTENT-GOVERNANCE.md](docs/CONTENT-GOVERNANCE.md) | Editorial rules + quality gate |
| [CHINESE-SOURCE-INTELLIGENCE.md](docs/CHINESE-SOURCE-INTELLIGENCE.md) | Chinese-language research system |
| [CHINESE-ENGLISH-GLOSSARY.md](docs/CHINESE-ENGLISH-GLOSSARY.md) | Terminology ledger |
| [RESEARCH-MODEL.md](docs/RESEARCH-MODEL.md) + [RESEARCH-INVENTORY.md](docs/RESEARCH-INVENTORY.md) | Research tracking |
| [ORIGINAL-DATA-ASSETS.md](docs/ORIGINAL-DATA-ASSETS.md) | First-party datasets |
| [ART-DIRECTION.md](docs/ART-DIRECTION.md) + [DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) + [COMPONENT-SYSTEM.md](docs/COMPONENT-SYSTEM.md) | Visual + component system |
| [MATERIAL-REQUESTS.md](docs/MATERIAL-REQUESTS.md) | Missing first-party info |
| [SECURITY.md](docs/SECURITY.md) + [PERFORMANCE.md](docs/PERFORMANCE.md) + [QA.md](docs/QA.md) + [DEPLOYMENT.md](docs/DEPLOYMENT.md) | Technical gates |

## Brand facts

| Field | Value |
|---|---|
| Brand name | IncenseHub (IncenseHub) |
| Legal entity | IncenseHub (张家口IncenseHub科技有限公司) |
| Domain | incensehub.org (placeholder) |
| Data domain | data.incensehub.org |
| Datasets license | CC BY-SA 4.0 |
