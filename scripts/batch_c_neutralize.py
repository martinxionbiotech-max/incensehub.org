#!/usr/bin/env python3
"""Batch C — neutralize residual buyer/commercial framing in T2 ingredient pages.

After the three commercial sections are removed, knowledge sentences still carry
"buyer"/"sourcing buyer"/"commercial" framing. This pass converts that framing
to the neutral informational-platform voice (reader / identification / trade),
drops remaining wholesale-guide CTAs, and fixes dangling "Our Industry View"
references. It does NOT touch factual trade terms ("commercial product/form/
material", "commercial jasmine absolute", "commercial borneol").

Usage: python3 scripts/batch_c_neutralize.py <slug> [slug ...]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "src" / "content" / "ingredients"

# Ordered phrase rewrites (applied before the global word swap). Longest first.
PHRASES = [
    # commercial-adjective framing -> neutral
    ("the practical questions are commercial", "the practical questions are ones of identification"),
    ("The practical sourcing questions are commercial", "The practical sourcing questions are ones of identification"),
    ("The sourcing questions are commercial", "The sourcing questions are ones of identification"),
    ("the practical sourcing questions are commercial", "the practical sourcing questions are ones of identification"),
    ("defining commercial risk", "defining identification risk"),
    ("defining commercial fact", "defining identifying fact"),
    ("central commercial hazard", "central identification hazard"),
    ("decisive commercial question", "decisive identification question"),
    ("The commercial question", "The identification question"),
    ("the commercial question", "the identification question"),
    ("commercial lesson is", "lesson is"),
    ("key commercial nuance", "key distinguishing nuance"),
    ("Its commercial identity", "Its identity"),
    ("its commercial identity", "its identity"),
    ("commercial value is", "value is"),
    ("Its commercial value", "Its value"),
    ("its commercial value", "its value"),
    ("key commercial points", "key identifying points"),
    ("key commercial point", "key identifying point"),
    ("Commercial grading", "Trade grading"),
    ("Commercially", "In trade"),
    ("commercially", "in trade"),
    # buyer -> reader special cases (awkward if done globally)
    ("For powder buyers, ", "For powder, "),
    ("For a fragrance buyer, ", "For fragrance, "),
    ("For a contemporary buyer, ", "For the contemporary reader, "),
    ("For a contemporary buyer", "For the contemporary reader"),
    ("For a buyer, ", "For the reader, "),
    ("For a buyer: ", "For the reader: "),
    ("For a buyer,", "For the reader,"),
    ("for a buyer", "for the reader"),
    ("a buyer's first job", "the reader's first task"),
    ("a buyer's main job", "the reader's main task"),
    ("the buyer's first job", "the reader's first task"),
    ("the buyer's first question", "the reader's first question"),
    ("the buyer's real question", "the reader's real question"),
    ("the buyer's real specification", "the reader's real specification"),
    ("the buyer's job", "the reader's task"),
    ("buyer intelligence", "identification note"),
    ("(a buyer's note)", "(an identification note)"),
    ("a buyer's note", "an identification note"),
    ("key buyer points", "key identification points"),
    ("buyer points", "identification points"),
    ("the buyer notes below", "the identification notes below"),
    ("buyer note", "identification note"),
    ("How should a buyer judge", "How is"),
    ("For a sourcing buyer, the quality checks are:", "The practical quality checks are:"),
    ("For a sourcing buyer, the checks are:", "The practical checks are:"),
    ("For a sourcing buyer,", "For sourcing,"),
    ("For an incense maker or sourcing buyer:", "For an incense maker or formulator:"),
    # dangling references to the removed section
    ("(see Our Industry View below)", ""),
    (" (see Our Industry View below)", ""),
    ("see Our Industry View below", "see below"),
    # wholesale-guide CTA sentence (drop)
    ("See the [wholesale guide](/blog/wholesale-guide/) for the general identification and quality framework.", ""),
    ("See the [wholesale guide](/blog/wholesale-guide/) for the general sourcing framework.", ""),
]

# Global word swap (applied last), after special cases.
WORD_SWAP = [
    ("buyers'", "readers'"),
    ("buyers", "readers"),
    ("buyer's", "reader's"),
    ("buyer", "reader"),
]

# Whole-line CTA drops (after strip).
CTA_LINE = [
    re.compile(r"^See the \[wholesale guide\]\([^)]*\) for the general (identification and quality|sourcing) framework\.?$"),
]


def neutralize(text: str) -> str:
    for old, new in PHRASES:
        text = text.replace(old, new)
    for old, new in WORD_SWAP:
        text = text.replace(old, new)
    lines = text.split("\n")
    out = []
    for line in lines:
        if any(p.match(line.strip()) for p in CTA_LINE):
            continue
        # drop now-empty "See the wholesale guide ..." fragments
        s = line.strip()
        if s.startswith("See the [wholesale guide]") and s.endswith("framework."):
            continue
        out.append(line)
    return "\n".join(out)


def process(slug: str) -> dict:
    path = ING / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    new = neutralize(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return {"slug": slug, "changed": new != text}


def main():
    slugs = sys.argv[1:]
    if not slugs:
        slugs = [l.strip() for l in Path("/tmp/t2_60.txt").read_text().splitlines() if l.strip()]
    results = [process(s) for s in slugs]
    changed = sum(1 for r in results if r["changed"])
    print(f"processed={len(results)} changed={changed}")


if __name__ == "__main__":
    main()
