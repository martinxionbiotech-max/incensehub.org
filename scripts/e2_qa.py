#!/usr/bin/env python3
"""E2 post-processing QA:
1. repair glued horizontal rules before headings (`---##` -> `---\n\n##`).
2. verify frontmatter is byte-identical to git HEAD for every target.
3. verify internal links resolve to an existing content slug or page route.
4. report remaining mechanical phrases.
Writes /tmp/e2_qa.json and prints a summary.
"""
import json, os, re, subprocess, sys

ROOT = "/root/.openclaw/workspace/repos/incensehub.org"
os.chdir(ROOT)
targets = [l.strip() for l in open("scripts/e2_targets.txt") if l.strip()]
FRONT = re.compile(r'\A---\s*\n.*?\n---\s*\n', re.S)

# 1. repair glued separators
fixed = []
for rel in targets:
    p = os.path.join("src/content", rel)
    s = open(p, encoding="utf-8").read()
    n = re.sub(r'---(#{2,4} )', r'---\n\n\1', s)
    n = re.sub(r'(?m)^(#{2,4} .*)\n(?!\n)(?=[^\s#|-])', r'\1\n\n', n)
    if n != s:
        open(p, "w", encoding="utf-8").write(n)
        fixed.append(rel)

# 2. frontmatter drift
drift = []
for rel in targets:
    p = os.path.join("src/content", rel)
    cur = open(p, encoding="utf-8").read()
    mc = FRONT.match(cur)
    try:
        old = subprocess.run(["git", "show", f"HEAD:src/content/{rel}"], capture_output=True, text=True).stdout
    except Exception:
        old = ""
    mo = FRONT.match(old)
    if mc and mo and mc.group(0) != mo.group(0):
        drift.append(rel)
    if not mc:
        drift.append(rel + " (no frontmatter)")

# 3. internal links
slugs = set()
for d in ("blog", "ingredients", "concepts"):
    for f in os.listdir(os.path.join("src/content", d)):
        if f.endswith(".md"):
            slugs.add(os.path.splitext(f)[0])
static = {"safety", "about", "contact", "privacy", "terms", "cookies", "disclaimer",
          "editorial-policy", "how-we-research", "knowledge-map"}
broken = {}
for rel in targets:
    p = os.path.join("src/content", rel)
    s = open(p, encoding="utf-8").read()
    body = FRONT.sub("", s, count=1)
    for m in re.finditer(r'\]\((/[^)\s]+)\)', body):
        href = m.group(1).split("#")[0].split("?")[0]
        parts = [x for x in href.split("/") if x]
        if not parts:
            continue
        if parts[0] in ("blog", "ingredients", "concepts"):
            if len(parts) < 2 or parts[1] not in slugs:
                broken.setdefault(rel, []).append(href)
        elif parts[0] in static or href.startswith("/safety"):
            continue

# 4. mechanical phrases
MECH = [r'\bhowever\b', r'\bmoreover\b', r'\bfurthermore\b', r'\badditionally\b',
        r'\bin addition\b', r'\bit is important to\b', r'\bit is worth noting\b',
        r'\bit should be noted\b', r'\bnotably\b', r'\bin conclusion\b',
        r'\bnevertheless\b', r'\bnonetheless\b', r'\bas mentioned\b',
        r'\bneedless to say\b', r'\bit is crucial to\b']
mech = {}
for rel in targets:
    body = FRONT.sub("", open(os.path.join("src/content", rel), encoding="utf-8").read(), count=1)
    hits = {m: len(re.findall(m, body, re.I)) for m in MECH}
    hits = {k: v for k, v in hits.items() if v}
    if hits:
        mech[rel] = hits

out = {"separator_fixed": fixed, "frontmatter_drift": drift, "broken_links": broken, "mechanical": mech}
json.dump(out, open("/tmp/e2_qa.json", "w"), indent=1)
print(f"separator repaired: {len(fixed)}")
print(f"frontmatter drift: {len(drift)} {drift[:5]}")
print(f"files with broken internal links: {len(broken)}")
for k, v in list(broken.items())[:20]:
    print("  ", k, v[:4])
print(f"files with mechanical phrases: {len(mech)}")
for k, v in list(mech.items())[:20]:
    print("  ", k, v)
