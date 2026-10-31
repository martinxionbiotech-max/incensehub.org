# DEPLOYMENT.md — IncenseHub

Deployment plan. Target: **Cloudflare Pages** (static), consistent with the Astro static architecture.

## Stack

- **Hosting:** Cloudflare Pages (static)
- **Source:** GitHub (`martinxionbiotech-max/IncenseHub`), push-to-deploy
- **Commerce:** WooCommerce (separate service, later)
- **Domain:** TBD (see MATERIAL-REQUESTS.md)

## Pipeline

1. `git push` to `main` → Cloudflare Pages auto-build
2. Build command: `npm run build` (Astro static)
3. Output: `dist/`

## Edge configuration (planned, build-time static)

- `_headers`: `Content-Signal`, `Link: describedby` for datasets
- `_redirects`: canonical redirects (apex/legacy) as needed
- `robots.txt` + `sitemap.xml` + `llms.txt` generated at build

## DNS / domains

- Apex primary; `www` → apex 301 (edge redirect).
- No SEO subdomains in Phase 1.

## Environment variables

- WooCommerce secrets (later) as build/server env vars, **never** public-prefixed or committed.

## Rollout

1. Phase 0: docs only (this repo)
2. Phase 3: scaffold Astro + wireframes-approved templates
3. Launch gate passes → first deploy
4. Post-launch: Search Console verification, sitemap submission, monitoring

## Rollback

- Git revert + redeploy (static, trivially reversible).
