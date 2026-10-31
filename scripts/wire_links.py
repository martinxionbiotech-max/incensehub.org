#!/usr/bin/env python3
"""Additive pillar<->cluster bidirectional interlinking.

Body-safe: appends markdown only (no edits to existing content), idempotent,
and inserts additions before a trailing "## FAQ" section when one exists.

- Hub page: appends a "## Cluster directory" section listing ALL cluster
  members (when any member is not already linked).
- Cluster page: appends a natural "See [hub] ..." backlink (when the hub is
  not already linked).

Usage:
  python3 wire_links.py report              # show what would change
  python3 wire_links.py apply [--cluster P4]  # apply (optionally one cluster)
"""
import re
import sys
import glob
import os
import json

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


def canon(raw: str) -> str:
    for p, c in CANON:
        if raw.startswith(p):
            return c
    return raw


def split_frontmatter(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1)
    body = text[m.end():]

    def get(field):
        mm = re.search(rf"^{re.escape(field)}:\s*\"?(.*?)\"?\s*$", fm, re.M)
        return mm.group(1) if mm else None
    return fm, body, get


def linked_slugs(body: str):
    return set(re.findall(r"\]\(/blog/([a-z0-9-]+)/", body))


def insert_before_faq_or_append(body: str, addition: str) -> str:
    """Insert addition before a trailing '## FAQ' section, else append at end."""
    m = re.search(r"\n## FAQ\b", body)
    if m:
        idx = m.start()
        # preserve the blank line structure: put addition + two newlines before FAQ
        return body[:idx] + addition + "\n" + body[idx:]
    # append at end (ensure exactly one trailing newline)
    return body.rstrip("\n") + "\n" + addition + "\n"


def main():
    args = sys.argv[1:]
    mode = "report" if not args else args[0]
    only = None
    if "--cluster" in args:
        only = args[args.index("--cluster") + 1]

    from collections import defaultdict

    pages = {}
    for f in sorted(glob.glob(os.path.join(BLOG, "*.md"))):
        text = open(f, encoding="utf-8").read()
        fm, body, get = split_frontmatter(text)
        slug = get("slug")
        pages[slug] = dict(file=f, body=body, title=get("title"),
                           pillar=canon(get("pillar")), role=get("cluster_role"))

    clusters = defaultdict(list)
    for slug, p in pages.items():
        clusters[p["pillar"]].append(slug)

    plan = []  # (file, kind, detail)

    for cname in sorted(clusters, key=lambda c: c.split(" ")[0]):
        if only and not cname.startswith(only):
            continue
        members = clusters[cname]
        hubs = [s for s in members if pages[s]["role"] == "hub"]
        assert len(hubs) == 1, (cname, hubs)
        hub = hubs[0]
        others = sorted(s for s in members if s != hub)
        hub_linked = linked_slugs(pages[hub]["body"])
        missing = [s for s in others if s not in hub_linked]
        if missing:
            lines = "\n\n".join(f"- [{pages[s]['title']}](/blog/{s}/)" for s in others)
            plan.append((pages[hub]["file"], "hub-directory", f"{hub}: add directory for {len(others)} members (was missing {len(missing)})"))

        for s in others:
            linked = linked_slugs(pages[s]["body"])
            if hub not in linked:
                plan.append((pages[s]["file"], "backlink", f"{s}: add backlink to hub {hub}"))

    if mode == "report":
        print(f"== plan: {len(plan)} changes ==")
        for f, kind, detail in plan:
            print(f"{kind:14s} {detail}")
        return

    # apply
    changed = 0
    for cname in sorted(clusters, key=lambda c: c.split(" ")[0]):
        if only and not cname.startswith(only):
            continue
        members = clusters[cname]
        hubs = [s for s in members if pages[s]["role"] == "hub"][0]
        others = sorted(s for s in members if s != hubs)

        # 1. hub directory
        hub_linked = linked_slugs(pages[hubs]["body"])
        missing = [s for s in others if s not in hub_linked]
        if missing:
            lines = "\n".join(f"- [{pages[s]['title']}](/blog/{s}/)" for s in others)
            addition = "## Cluster directory\n\n" + lines
            fpath = pages[hubs]["file"]
            body = pages[hubs]["body"]
            new_body = insert_before_faq_or_append(body, addition)
            if new_body != body:
                write_body(fpath, new_body)
                changed += 1

        # 2. member backlinks
        for s in others:
            linked = linked_slugs(pages[s]["body"])
            if hubs not in linked:
                addition = f"See [{pages[hubs]['title']}](/blog/{hubs}/) for the full guide."
                fpath = pages[s]["file"]
                body = pages[s]["body"]
                new_body = insert_before_faq_or_append(body, addition)
                if new_body != body:
                    write_body(fpath, new_body)
                    changed += 1

    print(f"== APPLIED: {changed} files changed")


def write_body(fpath, new_body):
    text = open(fpath, encoding="utf-8").read()
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    new_text = text[:m.end()] + new_body
    # safety: frontmatter must be unchanged
    assert text[:m.end()] == new_text[:m.end()]
    open(fpath, "w", encoding="utf-8").write(new_text)


if __name__ == "__main__":
    main()
