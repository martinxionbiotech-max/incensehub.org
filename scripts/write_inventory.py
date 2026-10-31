#!/usr/bin/env python3
"""Generate CONTENT-INVENTORY.md from /tmp/inventory.tsv."""
import collections

rows = []
for line in open("/tmp/inventory.tsv", encoding="utf-8").read().strip().split("\n")[1:]:
    slug, pillar, role, status, wc = line.split("\t")
    rows.append((slug, pillar, role, status, int(wc)))

# Cluster summary (hub slug + page count + words), in ledger order.
clusters = collections.OrderedDict()
hub_of = {}
for slug, pillar, role, status, wc in rows:
    clusters.setdefault(pillar, []).append((slug, role, wc))
    if role == "hub":
        hub_of[pillar] = slug

summary_lines = []
for pillar, members in clusters.items():
    n = len(members)
    w = sum(m[2] for m in members)
    hub = hub_of.get(pillar, "—")
    summary_lines.append(f"| {pillar} | {n} | {hub} | {w} |")

total_words = sum(wc for _, _, _, _, wc in rows)

ledger_lines = []
for slug, pillar, role, status, wc in rows:
    ledger_lines.append(f"| `{slug}` | {pillar} | `{role}` | {status} | {wc} |")

md = f"""# CONTENT-INVENTORY.md — LanDeng

Live ledger of every content asset in the Astro content collections
(`src/content/{{blog,ingredients,concepts}}`). One row per page, generated from
actual frontmatter (2026-09-20). Status `live` = built and served.

## Columns

| Field | Meaning |
|---|---|
| slug | content ID / URL segment |
| pillar | canonical pillar-cluster (blog: P1–P11 + Commercial) |
| cluster_role | role within the cluster — `hub` = the single pillar hub; others: `article · recipe · guide · glossary · authority_reference · data_asset · history · how_to · buyer_intelligence · reference` |
| status | `live` (all pages are built and served) |
| words | body word count (frontmatter excluded) |

## Cluster summary

| Pillar | Pages | Hub | Words |
|---|---|---|---|
{chr(10).join(summary_lines)}

**Totals:** {len(rows)} pages · {total_words:,} words.

## Full ledger

| slug | pillar | cluster_role | status | words |
|---|---|---|---|---|
{chr(10).join(ledger_lines)}

## Notes

- **12 canonical clusters** = P1–P11 + Commercial (B2B Buying & Supply). Exactly one `hub` per cluster.
- **Ingredient entity pages** (150) and the **Chinese-incense concept page** (1) live in separate
  collections and are not part of the P1–P11 blog taxonomy; they carry `entity` / `pillar` roles.
- Ingredient/concept frontmatter still uses `status: draft`; they are nonetheless built and served
  (no draft filter in the collection routes), so this ledger records them as `live`.
- Word counts are body-only (frontmatter stripped) and include markdown link/anchor text.
"""

open("docs/CONTENT-INVENTORY.md", "w", encoding="utf-8").write(md)
print(f"Wrote docs/CONTENT-INVENTORY.md ({len(rows)} rows, {total_words} words)")
