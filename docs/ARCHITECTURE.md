# ARCHITECTURE.md — IncenseHub

## 1. System identity

IncenseHub is not a "website". It is a composite system:

**Knowledge platform + entity graph + research system + demand-intelligence system + original data asset + AI-discovery asset + organic-acquisition engine + commercial lead engine.**

## 2. Information architecture (logical)

```
/
  /chinese-incense/          — pillar: what Chinese incense is
  /herbal-incense/           — herbal subset
  /botanical-incense/        — botanical subset
  /natural-incense/          — natural subset

  /incense-sticks/           — format: sticks (线香)
  /incense-cones/            — format: cones (塔香)
  /incense-sachets/          — format: sachets (香囊)

  /ingredients/              — ingredient encyclopedia (entity pages)
  /materials/                — material reference (entity pages)

  /learn/                    — knowledge hub (encyclopedia + field guide + editorial)
  /research/                 — research hub (methodology + findings)

  /products/                 — product catalog (knowledge-rich, no thin pages)
  /wholesale/                — wholesale
  /oem/                      — OEM / private label

  /journal/                  — editorial journal

  /about/                    — brand / company
  /manufacturing/            — manufacturing
  /quality/                  — quality
  /safety/                   — safety (transparent combustion disclosure)

  /contact/
  /request-a-quote/
```

URL taxonomy is validated against search demand + entity architecture + commercial intent before any page is built. **Pages are never created merely to fill the sitemap.**

## 3. Content architecture

```
PILLAR  →  CLUSTER  →  ENTITY  →  SUPPORTING  →  PRODUCT  →  COMMERCIAL
```

Content types: Encyclopedia · Guide · Research · Comparison · Glossary · Timeline · FAQ · Journal · Product · Wholesale · OEM.

## 4. Entity architecture

Every strategic entity (e.g. **Agarwood 沉香**) is a cluster, not one page:

Definition · History · Botanical source · Geography · Chinese terminology · Aroma · Materials · Processing · Traditional use · Incense use · Burning · Quality · Safety · Comparisons · Research · FAQ · Products · Wholesale · OEM.

Entity relationship graph: see [KNOWLEDGE-GRAPH.md](KNOWLEDGE-GRAPH.md).

## 5. Knowledge graph

```
Ingredient → Botanical Source → Material → Processing → Aroma → Formula
→ Incense → Tradition → Use Case → Product → Wholesale → OEM
```

Plus cross-links: Ingredient ↔ Material ↔ Article ↔ Research ↔ Culture ↔ Terminology ↔ Product.

## 6. Technical architecture

- **Frontend:** Astro, static generation (aggressively cacheable). Content collections + structured entity data.
- **Commerce:** WooCommerce (REST API) as product/SKU/attribute source of truth. Astro is the presentation layer.
- **Phase 1:** No cart/checkout/accounts/payment. Inquiry + quote only.
- **Server Islands:** only where genuinely dynamic content is required.

```
Astro (static)
  ├── Knowledge / SEO / AIO / Products
  └── Inquiry / Quote
WooCommerce API (separate)
  └── Products · SKUs · Inventory · Attributes · future pricing/orders
```

## 7. Subdomain strategy

Phase 1: **one primary domain only.** No SEO subdomains, no doorway networks. Future subdomains (learn. / research. / data.) only when genuinely independent systems justify them.

## 8. Key cross-cutting rules

- **No information gain = no page.**
- **Chinese knowledge → analysis → synthesis → original English content** (never translation).
- **Never invent** MOQ, certifications, capacity, test results, factory facts.
- **Medical claims governed** — see [CONTENT-GOVERNANCE.md](CONTENT-GOVERNANCE.md).
- **First-party data loop** feeds demand → content → research → product → commercial.
