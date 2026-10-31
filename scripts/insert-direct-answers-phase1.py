#!/usr/bin/env python3
"""Phase 1 Task 1, Phase B: insert Direct answer blockquotes.

For each ingredient page missing the "> **Direct answer:**" blockquote,
convert its existing opening bold lead (the page's own "what is it" answer)
into the standardized blockquote format. Content is a 40-80 word, conclusion-first
synthesis of the page's own existing lead text only — no new facts/sources/links.

Zero fabrication: the block text in da-blocks-*.json is derived strictly from
each page's existing opening lead paragraph.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ING = os.path.join(ROOT, "src", "content", "ingredients")
REPORT_DIR = "/root/.openclaw/workspace/phase2/optimization-reports"

def load_blocks():
    blocks = {}
    for f in ["da-blocks-1.json", "da-blocks-2.json"]:
        with open(os.path.join(REPORT_DIR, f), encoding="utf-8") as fh:
            blocks.update(json.load(fh))
    return blocks

def main():
    blocks = load_blocks()
    changed = []
    skipped = []
    for name, block in blocks.items():
        path = os.path.join(ING, name + ".md")
        if not os.path.exists(path):
            skipped.append((name, "file missing"))
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()

        # find the opening bold lead line: **Label:** rest
        pattern = re.compile(r'^(\*\*(?:Technical answer|Direct answer|Key takeaway|Data summary|Definition|At a glance|Quick answer):\*\*) (.*)$', re.M)
        m = pattern.search(text)
        if not m:
            skipped.append((name, "no lead line"))
            continue

        lead_text = m.group(2).strip()
        new_line = f"> **Direct answer:** {block}"
        new_text = pattern.sub(lambda mm: new_line, text, count=1)

        if new_text == text:
            skipped.append((name, "no change"))
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        changed.append(name)

    print(f"changed: {len(changed)}")
    print(f"skipped: {len(skipped)}")
    if skipped:
        for s in skipped:
            print("  SKIP:", s)

    # quick validation: all changed pages now have blockquote
    for name in changed:
        t = open(os.path.join(ING, name + ".md"), encoding="utf-8").read()
        if not re.search(r'^>\s*\*\*Direct answer:', t, re.M):
            print(f"  VALIDATION FAIL: {name}")

if __name__ == "__main__":
    main()
