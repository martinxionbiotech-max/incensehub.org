# Markdown negotiation — same URL, two representations

IncenseHub serves every eligible page as HTML by default and as Markdown when a client
explicitly asks for it. The URL never changes and there is no separate `/md/` route.

## Files

| File | Role |
|---|---|
| `functions/_middleware.js` | Pages Functions middleware: reads `Accept`, looks up the page in the manifest, returns the Markdown asset with `Content-Type: text/markdown` |
| `scripts/generate-markdown.mjs` | Post-build step: converts each eligible `dist/**/index.html` into `dist/**/index.md`, writes `dist/_md/manifest.json` |
| `public/_headers` | `/*.md` → `Content-Type: text/markdown; charset=utf-8` for direct `.md` requests |
| `dist/_md/manifest.json` | Map of page URL → Markdown file (275 entries at last build) |

## Selection policy

Markdown is returned only when the request names `text/markdown` explicitly with `q > 0`
**and** its q-value is at least the q-value of `text/html`. Ties go to Markdown (an explicit
ask signals intent). Wildcards and `q=0` never trigger Markdown.

`GET` and `HEAD` only. Any error (missing manifest, missing file, non-200) falls back to the
HTML response.

## What is excluded

- `404.html`
- Pages with `noindex` (the 6 retired commercial landing pages)
- Pages without a `<main>` block or with too little content

At the last build: **275 generated, 7 skipped, 0 missing**.

## Verified test matrix

Run against `npx wrangler pages dev dist` (Pages Functions + `_headers` applied):

| Request | Result |
|---|---|
| `GET /about/` (no Accept) | `text/html` |
| `GET /about/` · `Accept: text/markdown` | `text/markdown`, body starts `# About IncenseHub` |
| `GET /about/` · `Accept: text/markdown;q=0` | `text/html` |
| `GET /about/` · `Accept: text/html,text/markdown;q=0.5` | `text/html` |
| `GET /about/` · `Accept: text/html,text/markdown` (tie) | `text/markdown` |
| `GET /about/index.md` | `text/markdown` (static asset + `/*.md` header) |
| `GET /blog/incense-sticks/` · `Accept: text/markdown` | `text/markdown` |
| `GET /ingredients/agarwood/` · `Accept: text/markdown` | `text/markdown` |
| `GET /` · `Accept: text/markdown` | `text/markdown` |
| `GET /request-a-quote/` · `Accept: text/markdown` | `text/html` (noindex → excluded) |

## Deploy requirements

- The middleware is a **Pages Function**: it only runs on Cloudflare Pages when `functions/`
  is part of the deployed project. Git integration builds it automatically; a CLI deploy must
  run `wrangler pages deploy dist` from the repository root.
- Uploading only `dist/` assets without the Functions build will serve HTML for every request.
- `_headers` is copied from `public/` into `dist/` by Astro.

## Manual checks after deploy

```bash
curl -sI https://incensehub.org/about/ | grep -i content-type
# text/html; charset=utf-8

curl -sI -H 'Accept: text/markdown' https://incensehub.org/about/ | grep -i content-type
# text/markdown; charset=utf-8

curl -s -H 'Accept: text/markdown' https://incensehub.org/about/ | head -1
# # About IncenseHub

curl -sI https://incensehub.org/about/index.md | grep -i content-type
# text/markdown; charset=utf-8

curl -s https://incensehub.org/_md/manifest.json | head -c 120
# { "/about/": "/about/index.md", ... }
```
