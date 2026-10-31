# QA.md — IncenseHub

Quality assurance checklist. Run before launch and on every significant change.

## Content QA

- [ ] Search intent defined; entity defined; user problem defined
- [ ] Information gain + original contribution present
- [ ] Sources verified; claims classified; conflicts shown
- [ ] Medical/safety claims reviewed (no unsupported health claims; combustion disclosed)
- [ ] Editorial pass (typos, tone, accuracy)

## SEO QA

- [ ] Canonicals correct; no duplicate content; no soft 404
- [ ] Sitemap valid; robots.txt correct; hreflang only where justified
- [ ] Metadata + Open Graph present
- [ ] Internal linking sane (no orphans, no keyword-stuffed anchors)
- [ ] No redirect loops / chains

## Schema QA

- [ ] Structured data valid (Rich Results test)
- [ ] No fabricated reviews/ratings/prices/authors
- [ ] JSON-LD matches visible content

## Technical QA

- [ ] Build clean; no broken internal links; assets resolve
- [ ] 404/410 handling correct
- [ ] Mobile UX validated

## Performance QA

- [ ] Lighthouse + CWV targets met (see PERFORMANCE.md)

## Accessibility QA

- [ ] Semantic HTML; contrast ≥ AA; focus states; alt text

## Security QA

- [ ] No secrets exposed; forms protected (see SECURITY.md)

## Commercial QA

- [ ] Inquiry forms tested end-to-end
- [ ] Product data verified (no invented MOQ/certs/capacity)

## Launch gate

Do not launch until all critical items pass. Re-run the relevant subset after each change.
