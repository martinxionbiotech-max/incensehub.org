#!/usr/bin/env python3
"""Analyze current pillar<->cluster linking state (read-only)."""
import re, glob, os, sys
from collections import defaultdict

BLOG = "src/content/blog"

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
HUBS = {
    "what-is-chinese-incense", "scent-guide", "scent-by-intention",
    "which-incense-format", "how-to-choose-incense", "incense-safety-guide",
    "incense-vs-candles-vs-diffusers", "world-incense-traditions",
    "how-incense-is-made", "how-aromatherapy-works", "incense-in-daily-ritual",
    "incense-for-business",
}

def canon(raw):
    for p, c in CANON:
        if raw.startswith(p):
            return c
    return raw

def frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1); body = text[m.end():]
    def get(f):
        mm = re.search(rf"^{re.escape(f)}:\s*\"?(.*?)\"?\s*$", fm, re.M)
        return mm.group(1) if mm else None
    return fm, body, get

pages = {}
for f in sorted(glob.glob(os.path.join(BLOG, "*.md"))):
    text = open(f, encoding="utf-8").read()
    fm, body, get = frontmatter(text)
    slug = get("slug"); pillar = get("pillar")
    pages[slug] = dict(file=f, body=body, pillar=canon(pillar), raw=pillar, role=get("cluster_role"))

clusters = defaultdict(list)
for slug, p in pages.items():
    clusters[p["pillar"]].append(slug)

def linked_slugs(body):
    return set(re.findall(r"\]\(/blog/([a-z0-9-]+)/", body))

print("== hub -> cluster link coverage ==")
total_missing_hub_links = 0
for canon_name in sorted(clusters, key=lambda c: c.split(" ")[0]):
    members = clusters[canon_name]
    hub = [s for s in members if pages[s]["role"] == "hub"]
    assert len(hub) == 1, (canon_name, hub)
    hub = hub[0]
    others = [s for s in members if s != hub]
    linked = linked_slugs(pages[hub]["body"])
    missing = [s for s in others if s not in linked]
    total_missing_hub_links += len(missing)
    print(f"{canon_name}: hub={hub}, members={len(others)}, already-linked={len(others)-len(missing)}, missing={len(missing)} {missing if missing else ''}")

print()
print("== cluster -> hub backlink coverage ==")
total_missing_backlinks = 0
for canon_name in sorted(clusters, key=lambda c: c.split(" ")[0]):
    members = clusters[canon_name]
    hub = [s for s in members if pages[s]["role"] == "hub"][0]
    missing = []
    for s in members:
        if s == hub: continue
        linked = linked_slugs(pages[s]["body"])
        if hub not in linked:
            missing.append(s)
    total_missing_backlinks += len(missing)
    print(f"{canon_name}: hub={hub}, members-missing-backlink={len(missing)} {missing if missing else ''}")

print()
print(f"TOTAL hub->cluster missing links: {total_missing_hub_links}")
print(f"TOTAL cluster->hub missing backlinks: {total_missing_backlinks}")
