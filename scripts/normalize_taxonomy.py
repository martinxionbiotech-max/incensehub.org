#!/usr/bin/env python3
"""LanDeng pillar-cluster taxonomy normalization.

Deterministic, body-safe: performs TARGETED LINE EDITS on the full file text,
never reconstructing or touching the markdown body.

  pillar       -> canonical cluster name (12 clusters: P1-P11 + Commercial)
  cluster_role -> role within cluster (exactly one 'hub' per cluster)

Usage:
  python3 normalize_taxonomy.py report   # dry-run: print mapping + validation
  python3 normalize_taxonomy.py apply    # write pillar + cluster_role lines only
"""
import re
import sys
import glob
import os

BLOG = "src/content/blog"

# Canonical cluster names, keyed by the raw pillar prefix (before the em dash).
CANON = [
    ("P1 \u2014", "P1 \u2014 Chinese Incense 101"),
    ("P2 \u2014", "P2 \u2014 Scent & Ingredient Guide"),
    ("P3 \u2014", "P3 \u2014 Use Scenarios"),
    ("P4 \u2014", "P4 \u2014 Product Formats & Tools"),
    ("P5 \u2014", "P5 \u2014 Buying & Selection"),
    ("P6 \u2014", "P6 \u2014 Care & Safety"),
    ("P7 \u2014", "P7 \u2014 Incense vs Alternatives"),
    ("P8 \u2014", "P8 \u2014 Regional Incense Traditions"),
    ("P9 \u2014", "P9 \u2014 Incense Craft & Recipes"),
    ("P10 \u2014", "P10 \u2014 Aromatherapy & Botany"),
    ("P11 \u2014", "P11 \u2014 Culture & Mindfulness"),
    ("Commercial \u2014", "Commercial \u2014 B2B Buying & Supply"),
]

# The single pillar hub per cluster.
HUBS = {
    "what-is-chinese-incense": "P1 \u2014 Chinese Incense 101",
    "scent-guide": "P2 \u2014 Scent & Ingredient Guide",
    "scent-by-intention": "P3 \u2014 Use Scenarios",
    "which-incense-format": "P4 \u2014 Product Formats & Tools",
    "how-to-choose-incense": "P5 \u2014 Buying & Selection",
    "incense-safety-guide": "P6 \u2014 Care & Safety",
    "incense-vs-candles-vs-diffusers": "P7 \u2014 Incense vs Alternatives",
    "world-incense-traditions": "P8 \u2014 Regional Incense Traditions",
    "how-incense-is-made": "P9 \u2014 Incense Craft & Recipes",
    "how-aromatherapy-works": "P10 \u2014 Aromatherapy & Botany",
    "incense-in-daily-ritual": "P11 \u2014 Culture & Mindfulness",
    "incense-for-business": "Commercial \u2014 B2B Buying & Supply",
}

# Demoted "hub" pages get a descriptive role instead.
ROLE_OVERRIDES = {
    "chinese-incense-recipes": "recipe",
    "incense-burners-tools": "reference",
}


def canonical_pillar(raw: str) -> str:
    for prefix, canon in CANON:
        if raw.startswith(prefix):
            return canon
    raise ValueError(f"unmapped pillar: {raw!r}")


def compute_role(slug: str, raw_pillar: str, content_type: str) -> str:
    if slug in HUBS:
        return "hub"
    if slug in ROLE_OVERRIDES:
        return ROLE_OVERRIDES[slug]
    p = raw_pillar
    if "(history)" in p:
        return "history"
    if "(how-to)" in p:
        return "how_to"
    if "(buyer intelligence)" in p:
        return "buyer_intelligence"
    if "(authority reference)" in p:
        return "authority_reference"
    if "data asset)" in p:  # "(data asset)" and "(comparison data asset)"
        return "data_asset"
    if "(reference)" in p:
        return "reference"
    if "(evidence pillar)" in p:
        return "authority_reference"
    ct = content_type
    if ct == "recipe":
        return "recipe"
    if ct == "guide":
        return "guide"
    if ct == "glossary":
        return "glossary"
    if ct == "authority_reference":
        return "authority_reference"
    if ct == "data_asset":
        return "data_asset"
    if ct == "reference_database":
        return "buyer_intelligence"
    if ct == "reference":
        return "reference"
    if ct == "how_to":
        return "how_to"
    return "article"


def read_fields(text: str):
    """Return (slug, raw_pillar, content_type) from frontmatter; raise on missing."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    fm = m.group(1)

    def get(field):
        mm = re.search(rf"^{re.escape(field)}:\s*\"?(.*?)\"?\s*$", fm, re.M)
        return mm.group(1) if mm else None

    slug = get("slug")
    raw_pillar = get("pillar")
    content_type = get("content_type")
    if slug is None or raw_pillar is None or content_type is None:
        raise ValueError("missing slug/pillar/content_type")
    return slug, raw_pillar, content_type


def edit_frontmatter(text: str, canon: str, role: str) -> str:
    """Targeted line edits: pillar + cluster_role. Body untouched."""
    out = re.sub(r'(?m)^pillar:\s*"[^"]*"\s*$', f'pillar: "{canon}"', text, count=1)
    if re.search(r"(?m)^cluster_role:\s*", out):
        out = re.sub(r'(?m)^cluster_role:\s*"[^"]*"\s*$', f'cluster_role: "{role}"', out, count=1)
    else:
        out = re.sub(
            r'(?m)^content_type:\s*"[^"]*"\s*$',
            lambda m: m.group(0) + f'\ncluster_role: "{role}"',
            out,
            count=1,
        )
    return out


def body_of(text: str) -> str:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    return text[m.end():]


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "report"
    files = sorted(glob.glob(os.path.join(BLOG, "*.md")))

    from collections import defaultdict, Counter

    rows = []
    for f in files:
        text = open(f, encoding="utf-8").read()
        slug, raw_pillar, content_type = read_fields(text)
        canon = canonical_pillar(raw_pillar)
        role = compute_role(slug, raw_pillar, content_type)
        rows.append((f, slug, raw_pillar, content_type, canon, role, text))

    clusters = defaultdict(list)
    for f, slug, raw, ct, canon, role, text in rows:
        clusters[canon].append((slug, role))

    print(f"== total pages: {len(rows)}")
    print(f"== distinct pillar variants BEFORE: {len(set(r[2] for r in rows))}")
    print(f"== distinct pillar values AFTER: {len(set(r[4] for r in rows))}")
    print()
    print("== per-cluster summary ==")
    ok = True
    for canon in sorted(clusters, key=lambda c: c.split(" ")[0]):
        members = clusters[canon]
        hubs = [s for s, r in members if r == "hub"]
        flag = "OK" if len(hubs) == 1 else "!!"
        if len(hubs) != 1:
            ok = False
        print(f"{flag} {canon}: {len(members)} pages, hub={hubs}")
    print()
    rc = Counter(r for members in clusters.values() for _, r in members)
    print("== role distribution ==")
    for k in sorted(rc):
        print(f"  {k}: {rc[k]}")
    print()
    if not ok:
        print("VALIDATION FAILED: clusters without exactly one hub.")
        sys.exit(2)

    if mode == "report":
        print("== full mapping (slug | role | raw pillar -> canon) ==")
        for f, slug, raw, ct, canon, role, text in rows:
            print(f"{slug:45s} {role:22s} {raw!r} -> {canon!r}")
        return

    changed = 0
    for f, slug, raw, ct, canon, role, text in rows:
        new_text = edit_frontmatter(text, canon, role)
        if new_text != text:
            # Safety assertion: markdown body must be byte-identical.
            assert body_of(new_text) == body_of(text), f"body changed for {slug}"
            open(f, "w", encoding="utf-8").write(new_text)
            changed += 1
    print(f"== APPLIED: {changed} files changed")


if __name__ == "__main__":
    main()
