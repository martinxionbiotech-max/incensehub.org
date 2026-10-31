# COMPONENT-SYSTEM.md — IncenseHub

Reusable Astro components. One component per responsibility. Keep client-side JS minimal (mostly static).

## Layout / chrome

- `Header` — brand, primary nav, language (if ever needed)
- `Footer` — company, trust, legal, sitemap links
- `Breadcrumb` — schema-backed breadcrumb
- `Hero` — editorial hero (restrained)

## Content

- `ArticleHeader` — title, meta, entity, lead
- `ArticleBody` — long-form prose
- `Section` — generic section wrapper
- `FactBox` — key facts callout
- `DirectAnswer` — AIO direct-answer block (top of page)

## Entity (ingredient / material)

- `IngredientHeader` — name, Chinese term + pinyin, scientific name, type
- `IngredientFacts` — key/​value fact table
- `AromaProfile` — aroma notes visualization
- `MaterialCard` — material summary card
- `GlossaryDefinition` — term definition block

## Research

- `SourceMatrix` — source table (S1–S5)
- `EvidenceLevel` — evidence badge/label
- `Timeline` — historical timeline
- `ClaimComparison` — claim vs source comparison table
- `ChineseEnglishTable` — terminology side-by-side
- `TraditionalVsScientific` — distinction block
- `RegionalComparison` — regional comparison table
- `MaterialClassification` — classification display
- `ResearchSummary` — findings summary
- `UncertaintyBox` — open questions / conflicts callout

## Comparison / data

- `ComparisonTable` — entity/format comparison

## Commerce

- `ProductCard` — product summary card
- `QuoteCta` — contextual commercial bridge (non-aggressive)
- `InquiryForm` — sample/quote/wholesale/OEM form

## Safety

- `SafetyBox` — combustion/safety disclosure
- `EvidenceBox` — evidence callout

## Rules

- Components are **static-first** (Astro server/build render); add interactivity only when necessary.
- No duplicate tool/handler registration on hydration (WebMCP etc. is NOT_REQUIRED in Phase 1).
- Every component maps to a Schema.org signal where applicable.
