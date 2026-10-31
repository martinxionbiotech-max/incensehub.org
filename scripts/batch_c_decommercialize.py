#!/usr/bin/env python3
"""Batch C — de-commercialize T2 ingredient pages.

Deterministic removal of the three commercial-framework sections that the
transformation plan (docs/incensehub-transformation-plan.md §1.1) mandates
deleting on every ingredient entity page:

  - ## What buyers should look for
  - ## Our Industry View
  - ## Modern commercial applications

Each section is removed header-through-content, up to (but not including) the
next `## ` heading. This is structural removal, not sentence substitution; the
neutral knowledge value (species identity, quality factors, product forms) is
already carried by the parallel neutral sections ("What determines X quality",
"Common forms", "Botanical identity", etc.).

Also neutralizes the "sourcing notes" framing that survives in mixed
conservation/quality sections, and drops the wholesale-guide CTA.

Usage: python3 scripts/batch_c_decommercialize.py <slug> [slug ...]
       (empty args = all slugs in /tmp/t2_60.txt)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "src" / "content" / "ingredients"

COMMERCIAL_SECTIONS = [
    "What buyers should look for",
    "Our Industry View",
    "Modern commercial applications",
]

# Neutralization map: (old, new) applied to surviving mixed sections only.
HEADER_RENAMES = [
    ("## Quality and sourcing notes", "## Quality notes"),
    ("## Conservation and sourcing notes", "## Conservation notes"),
    ("## Sustainability & sourcing", "## Sustainability"),
    ("## Sustainability and sourcing", "## Sustainability"),
]

FRAMING_FIXES = [
    ("Practical points for buyers:", "Practical points:"),
    ("For a sourcing buyer, the checks are:", "The practical checks are:"),
    ("For a sourcing buyer:", "For a discerning user:"),
    ("For an incense maker or sourcing buyer:", "For an incense maker or discerning user:"),
    ("For a food, fragrance, or sourcing buyer:", "For a food, fragrance, or incense user:"),
    ("For a buyer, the practical checks are", "The practical checks are"),
    ("for the general sourcing framework.", "for the general identification and quality framework."),
]

# Lines (full-line, after strip) that carry a pure buying CTA and are dropped.
CTA_LINE_PATTERNS = [
    re.compile(r"^See the \[wholesale guide\]\([^)]*\) for the general sourcing framework\.?$"),
]


def remove_commercial_sections(text: str) -> tuple[str, int]:
    """Remove the three commercial sections. Returns (new_text, sections_removed)."""
    removed = 0
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## ") and line[3:].strip() in COMMERCIAL_SECTIONS:
            removed += 1
            i += 1
            # Skip until the next `## ` heading (or EOF), keeping that heading.
            while i < len(lines) and not lines[i].startswith("## "):
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out), removed


def neutralize_framing(text: str) -> str:
    """Apply header renames and neutral framing fixes; drop pure CTA lines."""
    for old, new in HEADER_RENAMES:
        text = text.replace(old, new)
    for old, new in FRAMING_FIXES:
        text = text.replace(old, new)
    lines = text.split("\n")
    out = []
    for line in lines:
        if any(p.match(line.strip()) for p in CTA_LINE_PATTERNS):
            continue
        out.append(line)
    return "\n".join(out)


def process(slug: str) -> dict:
    path = ING / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    new, removed = remove_commercial_sections(text)
    new = neutralize_framing(new)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return {"slug": slug, "sections_removed": removed, "changed": new != text}


def main():
    slugs = sys.argv[1:]
    if not slugs:
        slugs = [l.strip() for l in (ROOT / "tmp_t2_60.txt").read_text().splitlines() if l.strip()]
        # fallback: /tmp file
        if not slugs:
            slugs = [l.strip() for l in Path("/tmp/t2_60.txt").read_text().splitlines() if l.strip()]
    results = [process(s) for s in slugs]
    total = sum(r["sections_removed"] for r in results)
    changed = sum(1 for r in results if r["changed"])
    print(f"processed={len(results)} changed={changed} commercial_sections_removed={total}")
    for r in results:
        if r["sections_removed"]:
            print(f"  {r['slug']}: -{r['sections_removed']}")


if __name__ == "__main__":
    main()
