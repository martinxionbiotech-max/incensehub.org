#!/usr/bin/env python3
"""Reproduce the orphan-page detection for the P2 internal-linking audit.

An "orphan" is a page that exists in the build output but receives ZERO
markdown internal links `[x](/...)` from any source file
(src/content/**/*.md and src/pages/**/*.astro).

Astro-template-generated lists (blog index, ingredients index, home card
grid, ingredients `related` block) are NOT markdown links and therefore do
NOT count as inbound links per the audit definition.

Nav-direct pages are excluded by default.
"""
import re
import glob
import os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

# Nav-direct pages that are exempt from the orphan test.
EXEMPT = {
    "/",
    "/blog/",
    "/ingredients/",
    "/wholesale/",
    "/oem/",
    "/safety/",
    "/contact/",
    "/chinese-incense/",
    "/recipes/",
    "/request-a-quote/",
}

# Regex for markdown links whose target starts with "/".
LINK_RE = re.compile(r"\]\((/(?:[^)\s]|[\s])*?)\)")


def normalize(path: str) -> str:
    """Normalize a link target to the canonical page URL form (trailing slash)."""
    # strip anchors and query
    path = path.split("#")[0].split("?")[0].strip()
    if not path.startswith("/"):
        return None
    # only keep site-internal paths
    if path.startswith("//"):
        return None
    if not path.endswith("/"):
        path += "/"
    return path


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def main():
    # ---- enumerate all pages (targets) ----
    pages = {}  # canonical url -> source description

    # blog
    for f in sorted(glob.glob(os.path.join(SRC, "content", "blog", "*.md"))):
        text = read(f)
        m = re.search(r'^slug:\s*"?([a-z0-9-]+)"?\s*$', text, re.M)
        if m:
            pages[f"/blog/{m.group(1)}/"] = f"blog:{m.group(1)}"

    # ingredients
    for f in sorted(glob.glob(os.path.join(SRC, "content", "ingredients", "*.md"))):
        slug = os.path.splitext(os.path.basename(f))[0]
        pages[f"/ingredients/{slug}/"] = f"ingredient:{slug}"

    # concepts (currently just chinese-incense, which is exempt)
    for f in sorted(glob.glob(os.path.join(SRC, "content", "concepts", "*.md"))):
        slug = os.path.splitext(os.path.basename(f))[0]
        pages[f"/{slug}/"] = f"concept:{slug}"

    # static pages (nav + others in src/pages)
    static = {
        "": "/",
        "blog/index": "/blog/",
        "ingredients/index": "/ingredients/",
        "chinese-incense/index": "/chinese-incense/",
        "wholesale/index": "/wholesale/",
        "oem/index": "/oem/",
        "safety/index": "/safety/",
        "contact/index": "/contact/",
        "request-a-quote/index": "/request-a-quote/",
    }
    for rel, url in static.items():
        if os.path.exists(os.path.join(SRC, "pages", rel + ".astro")):
            pages[url] = "static:" + (url or "/")

    # ---- scan all sources for markdown links ----
    sources = []
    sources += glob.glob(os.path.join(SRC, "content", "**", "*.md"), recursive=True)
    sources += glob.glob(os.path.join(SRC, "pages", "**", "*.astro"), recursive=True)

    inbound = defaultdict(set)  # target url -> set of source files
    for f in sorted(sources):
        text = read(f)
        for m in LINK_RE.finditer(text):
            target = normalize(m.group(1))
            if target and target in pages:
                inbound[target].add(os.path.relpath(f, ROOT))

    # ---- report ----
    orphans = []
    for url in sorted(pages):
        if url in EXEMPT:
            continue
        if len(inbound[url]) == 0:
            orphans.append((url, pages[url]))

    print(f"Total pages (excl. exempt): {sum(1 for u in pages if u not in EXEMPT)}")
    print(f"Total orphan pages: {len(orphans)}")
    print()
    for url, desc in orphans:
        print(f"{url}\t{desc}")

    # also dump per-page inbound counts for debugging (to a file)
    with open(os.path.join(ROOT, "scripts", "orphan_inbound.json"), "w") as out:
        import json
        json.dump({u: sorted(v) for u, v in inbound.items()}, out, indent=2)


if __name__ == "__main__":
    main()
