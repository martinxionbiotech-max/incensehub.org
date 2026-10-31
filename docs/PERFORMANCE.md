# PERFORMANCE.md — IncenseHub

Performance is an architectural constraint. Prefer build-time over runtime, static over dynamic, edge over origin.

## Targets

- Lighthouse: Performance ≥ 95 · Accessibility ≥ 95 · Best Practices ≥ 95 · SEO 100
- Core Web Vitals: LCP < 2.5s · INP < 200ms · CLS < 0.1

## Strategies

- Static generation (Astro), aggressively cacheable
- Optimized images (responsive, lazy-loaded, modern formats)
- Minimal JavaScript (no client framework for content pages)
- Efficient fonts (subset, `font-display: swap`, preload critical)
- CDN + caching (Cloudflare)
- Small bundles
- Server Islands only where genuinely dynamic

## Guardrails

- Do not add SSR / a database / a Worker / heavy middleware just for a small feature.
- Do not let AIO/agent layers degrade performance (e.g. no runtime HTML→Markdown conversion in Phase 1).

## Validation (before launch)

- [ ] Lighthouse 4-category audit on key templates
- [ ] CWV field/lab check on mobile
- [ ] Image audit (no oversized images)
- [ ] Bundle size check
