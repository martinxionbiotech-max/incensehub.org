#!/usr/bin/env python3
"""Generate content inventory data: slug | pillar | cluster_role | status | words."""
import re, glob, os

BLOG = "src/content/blog"
ING = "src/content/ingredients"
CON = "src/content/concepts"


def split(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1)
    body = text[m.end():]

    def get(f):
        mm = re.search(rf"^{re.escape(f)}:\s*\"?(.*?)\"?\s*$", fm, re.M)
        return mm.group(1) if mm else None
    return fm, body, get


def words(body):
    # strip markdown-ish tokens for a reasonable word count
    b = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)  # images
    b = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", b)  # links -> text
    b = re.sub(r"`[^`]*`", " ", b)
    b = re.sub(r"[#>*|~\-]+", " ", b)
    return len(b.split())


rows = []

for f in sorted(glob.glob(os.path.join(BLOG, "*.md"))):
    text = open(f, encoding="utf-8").read()
    fm, body, get = split(text)
    slug = get("slug")
    rows.append((slug, get("pillar"), get("cluster_role"), "live", words(body)))

for f in sorted(glob.glob(os.path.join(ING, "*.md"))):
    text = open(f, encoding="utf-8").read()
    fm, body, get = split(text)
    slug = os.path.basename(f)[:-3]
    rows.append((slug, "Ingredient Encyclopedia", "entity", "live", words(body)))

for f in sorted(glob.glob(os.path.join(CON, "*.md"))):
    text = open(f, encoding="utf-8").read()
    fm, body, get = split(text)
    slug = os.path.basename(f)[:-3]
    rows.append((slug, "Chinese Incense (concept)", "pillar", "live", words(body)))

# Sort: commercial first, then P1..P11, then ingredients, then concepts
def key(r):
    slug, pillar, role, status, wc = r
    if pillar.startswith("Commercial"):
        return (0, slug)
    if pillar.startswith("P"):
        try:
            n = int(pillar.split(" ")[0][1:])
            return (1, n, slug)
        except ValueError:
            return (2, slug)
    if pillar == "Ingredient Encyclopedia":
        return (3, slug)
    return (4, slug)


rows.sort(key=key)

import collections
by_cluster = collections.OrderedDict()
total_words = 0
for slug, pillar, role, status, wc in rows:
    by_cluster.setdefault(pillar, []).append((slug, role, wc))
    total_words += wc

print(f"TOTAL pages: {len(rows)}")
print(f"TOTAL words: {total_words}")
print()
for pillar, members in by_cluster.items():
    print(f"{pillar}: {len(members)} pages, {sum(m[2] for m in members)} words")

# Emit TSV for the ledger
import sys
out = sys.argv[1] if len(sys.argv) > 1 else None
lines = ["slug\tpillar\tcluster_role\tstatus\twords"]
for slug, pillar, role, status, wc in rows:
    lines.append(f"{slug}\t{pillar}\t{role}\t{status}\t{wc}")
tsv = "\n".join(lines) + "\n"
if out:
    open(out, "w", encoding="utf-8").write(tsv)
    print(f"\nWrote TSV to {out}")
else:
    print("\n" + tsv)
