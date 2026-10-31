# WIREFRAMES.md — IncenseHub

Text wireframes for the core page types. Wireframes precede implementation (see IMPLEMENTATION-PLAN.md). Layout is editorial, restrained, typography-led (see ART-DIRECTION.md / DESIGN-SYSTEM.md).

## 1. Homepage

```
Header (brand 澜灯 IncenseHub · nav)
Hero — restrained: brand line + one-sentence "what is Chinese botanical incense"
  → not a product catalog; lead with knowledge
Section: What is Chinese botanical incense (direct answer + link to /chinese-incense/)
Section: Explore by entity — Ingredients · Materials (card grid)
Section: Knowledge hub teaser — /learn/ + /research/
Section: Featured products (product cards)
Section: Wholesale / OEM (commercial bridge)
Section: Original knowledge / trust (authority signals)
Footer — inquiry CTA + company + legal + sitemap
```

## 2. Knowledge Hub index (/learn/)

```
Header
Breadcrumb
H1: Learn — Chinese Incense Knowledge
Section links: History · Culture · Materials · Ingredients · Making · Burning · Safety · Glossary
Featured entities (ingredient/material cards)
Latest journal
Footer
```

## 3. Ingredient / entity page (/ingredients/agarwood/)

```
Breadcrumb (Home > Ingredients > Agarwood)
IngredientHeader — name · 沉香 · chénxiāng · Aquilaria · type badge
DirectAnswer — 1–2 sentence AIO answer
FactBox — key facts (botanical, aroma, origin, grade)
AromaProfile — aroma notes
Body (editorial long-form):
  - Botanical source / origin
  - Materials + processing
  - Traditional + historical context
  - Incense use + burning characteristics
  - Quality factors + adulteration (buyer intelligence)
  - Safety + EvidenceLevel
ComparisonTable — vs related entity (e.g. sandalwood)
FAQ (schema-backed)
Related entities / research / products
QuoteCta (contextual, non-aggressive)
Footer
```

## 4. Article / guide page (/learn/...)

```
Breadcrumb
ArticleHeader — title, entity, meta, author (when real)
DirectAnswer (AIO)
ArticleBody — structured prose, tables, fact/evidence boxes
SourceBox — provenance
Related entities / articles
Footer
```

## 5. Product page (/products/...)

```
Breadcrumb
Product summary (name, format, aroma, key specs)
Aroma profile + ingredients + materials
Manufacturing + burn characteristics
Traditional context + suggested use
SafetyBox (combustion disclosure)
Related knowledge / ingredients / products
Wholesale / OEM bridge
Request Sample / Quote CTA
Footer
```

## 6. Wholesale + OEM + Request Quote (/wholesale/ · /oem/ · /request-a-quote/)

```
Header
H1 + intro (product range, materials, packaging, MOQ, sampling, lead time, customization, QC, documentation, shipping)
Capability sections (only verified facts; UNKNOWN items → MATERIAL-REQUESTS)
InquiryForm — sample / quote / wholesale / OEM / private label
Trust signals (company, quality)
Footer
```

## Notes

- Every page: canonical, schema JSON-LD (WebPage/Article/Product/DefinedTerm/BreadcrumbList), AIO direct-answer block.
- No fake reviews/ratings/prices/authors. No thin pages.
- Commerce is a **contextual bridge**, never aggressive interruption.
