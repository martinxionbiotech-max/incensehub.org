# WOOCOMMERCE.md — IncenseHub

WooCommerce as the commercial backend (product source of truth). Astro is the frontend/presentation layer.

## Architecture

```
Astro (static frontend)
  ├── Knowledge / SEO / AIO / Product content
  └── Inquiry / Quote
WooCommerce REST API (separate service)
  └── Products · SKUs · Inventory · Attributes · future pricing/orders
```

## Phase 1 — commerce scope

**No:** cart, checkout, customer accounts, online payment.

**Yes:** product catalog, product knowledge, specifications, Request Sample, Request Quote, Wholesale, OEM, Private Label, Contact.

## Integration

- WooCommerce handles: products, SKUs, inventory, attributes, future pricing, future orders, future payment.
- Astro reads product data via WooCommerce REST API at **build time** (static generation) where practical.
- Use Store API for future customer-side commerce functionality.
- Use webhooks for event-driven sync where appropriate.

## Security

- **Never expose** WooCommerce secrets, consumer key/secret, or API credentials in client-side JS, public env vars, static HTML, or the git repo.
- Use server/build environment variables only.
- See SECURITY.md.

## Status

`NOT_BUILT` — WooCommerce is not provisioned in Phase 0. This document is the integration contract. Provisioning happens in Phase 3, after the documentation gate + product data are confirmed.
