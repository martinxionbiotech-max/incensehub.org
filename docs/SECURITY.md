# SECURITY.md — IncenseHub

Security requirements. Agent/machine accessibility must never become public access to internal infrastructure.

## Never expose

- API keys, WooCommerce secrets, webhook secrets
- Database credentials, admin credentials
- Internal service URLs, admin/debug endpoints
- Private datasets, authentication internals

## Where secrets must NOT live

- frontend JavaScript
- public environment variables (e.g. `VITE_` / `PUBLIC_` prefixed)
- static HTML
- the git repository

Secrets live in server/build environment variables only.

## Public surface (Phase 1)

Static HTML + robots.txt + llms.txt + sitemap + JSON datasets + inquiry forms. Read-only; no admin, no auth, no database.

## Checks (before launch)

- [ ] No secrets in repo / client bundle / public env
- [ ] Inquiry forms: CSRF + honeypot
- [ ] No admin/debug endpoints exposed
- [ ] CORS sane (no wildcard where not needed)
- [ ] Rate limiting / abuse consideration on forms
- [ ] Dependency audit (`npm audit`) clean or triaged

## Principle

**Security > agent access.** We do not add an agent/API/MCP layer if it creates exposure — and we never fabricate one for a readiness score.
