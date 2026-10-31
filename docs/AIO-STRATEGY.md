# AIO-STRATEGY.md — IncenseHub

AI optimization for **AI search (AIO)** and **agent discovery**, layered on top of — never at the expense of — SEO, performance and security.

## Principles

1. **Usefulness > completeness.** We implement only what the architecture justifies.
2. **A scanner is a validation source, not an authority.** A FAIL is not automatically a problem; NOT_REQUIRED is a valid decision.
3. **Never fabricate** fake reviews, ratings, prices, authors, agents, MCP servers, or agent cards.
4. **SEO must never be sacrificed** for AI scores.

## AI content structure (for important pages)

Every important page supports the AI answer pattern:

```
Direct answer → Definition → Key facts → Detailed explanation → Comparison
→ Evidence / sources → Original analysis → Examples → Related entities
→ Related products → Further reading
```

Optimize for: clear answers, entity clarity, factual precision, structured information, source transparency, original insights, tables, visuals.

## Machine-readable layers (build-time, static)

| Layer | Status | Notes |
|---|---|---|
| Semantic HTML | planned | Astro static output |
| Schema.org JSON-LD | planned | Organization / WebSite / WebPage / Article / Product / DefinedTerm / BreadcrumbList |
| `llms.txt` | planned | Site map for AI crawlers |
| Datasets (JSON) | planned | Ingredient / material / terminology databases — see ORIGINAL-DATA-ASSETS.md |
| `_headers` (Content-Signal, Link describedby) | planned | Cloudflare Pages, build-time |
| hreflang | only if genuinely justified | English-primary; skip until multilingual is real |
| API Catalog / OpenAPI | NOT_REQUIRED (Phase 1) | No public API |
| WebMCP / MCP Server | NOT_REQUIRED (Phase 1) | No interactive tools / backend logic |
| OAuth / OIDC | NOT_REQUIRED (Phase 1) | No protected resources |
| A2A / Agent Card | NOT_REQUIRED | Not an agent; never fake one |
| Markdown negotiation | DEFER | Cloudflare "Markdown for Agents" needs Pro/Business; `llms.txt` is the Free fallback |

## Entity clarity

Every entity page exposes a machine-readable definition: name, aliases, Chinese term + pinyin, scientific name (botanicals), type, relationships. See ENTITY-MODEL.md and CHINESE-ENGLISH-GLOSSARY.md.

## Source transparency

Research pages carry provenance (source, type, date, language, claim, evidence level) so AI systems can trace claims. Conflicts are shown, never hidden.

## Measurement

Track AI visibility: AI Overview / AI-mode presence, AI-referenced pages and entities, AI referral traffic where measurable. See ORGANIC-ACQUISITION.md.
