#!/usr/bin/env python3
"""Batch D — residual framing cleanup for ingredient pages.

After batch C's decompose + neutralize passes, a few commercial/buyer framing
stragglers remain: (buyer intelligence) section headers, "Sourcing and
modern-status notes", sourcing-labelled Evidence subheaders, "Key buying
risk/note" table cells, and wholesale-guide CTA sentences. This pass converts
them to the neutral informational voice. Deterministic string edits only.

Usage: python3 scripts/batch_d_neutralize_ingredients.py <slug> [slug ...]
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = ROOT / "src" / "content" / "ingredients"

# Section header renames: buyer-intelligence framing -> neutral topic.
HEADER_RENAMES = [
    ("## The two kinds (buyer intelligence)", "## The two kinds"),
    ("## The storax / sweetgum distinction (buyer intelligence)", "## The storax / sweetgum distinction"),
    ("## The aging story (buyer intelligence)", "## The aging story"),
    ("## The naming problem (buyer intelligence)", "## The naming problem"),
    ("## Quality & authenticity (buyer intelligence)", "## Quality & authenticity"),
    ("## The source problem (buyer intelligence)", "## The source problem"),
    ('## The "oily grade" buyer-intelligence note', '## The "oily grade" note'),
    ("## Sourcing and modern-status notes", "## Modern-status notes"),
    ("### Modern status / sourcing", "### Modern status"),
    ("### Conservation / sourcing", "### Conservation"),
    ("### Sourcing / provenance", "### Provenance"),
    ("### Authenticity / sourcing", "### Authenticity"),
]

# Body phrase neutralization: buyer-intelligence -> identification.
BODY_FIXES = [
    ("This is the most useful buyer-intelligence point about", "This is the most useful identification point about"),
    ("This is the core buyer-intelligence point for", "This is the core identification point for"),
    ("are the page's buyer-intelligence points", "are the page's identification points"),
    ("This is buyer-intelligence that has not aged in a millennium.", "This is identification guidance that has not aged in a millennium."),
    ("remains the most useful buyer-intelligence.", "remains the most useful identification guidance."),
    ("and it reads like modern buyer intelligence:", "and it reads like modern identification guidance:"),
]

# Buying framing -> identification / sourcing / acquisition.
BUYING_FIXES = [
    ("| Key buying risk |", "| Key identification risk |"),
    ("| Key buying note |", "| Key identification note |"),
    ("The two buying risks are naming", "The two identification risks are naming"),
    ("The main buying risk is naming", "The main identification risk is naming"),
    ("The main buying risk is substitution", "The main identification risk is substitution"),
    ("it is the buying decision.", "it is the identification decision."),
    ("when buying orris.", "when sourcing orris."),
    ("should be confirmed when buying.", "should be confirmed when sourcing."),
    ("a key point to check when buying.", "a key point to check when sourcing."),
    ("Confirm species and legal origin when buying.", "Confirm species and legal origin when sourcing."),
    ("Rarity and sourcing pressure are worth checking when buying.", "Rarity and sourcing pressure are worth checking when sourcing."),
    ("the actual source is worth checking before buying.", "the actual source is worth checking before sourcing."),
    ("worth checking which one you are buying.", "worth checking which one you have."),
    ("does not tell you which you are buying.", "does not tell you which you are getting."),
    ("The formulator is therefore buying *freshness of the volatile fraction*, not just \"pepper.\"", "The formulator is therefore after *freshness of the volatile fraction*, not just \"pepper.\""),
    ("Practical points for anyone researching or buying:", "Practical points for anyone researching:"),
    ("rather than as a material to buy.", "rather than as a material to acquire."),
]

# Wholesale-guide CTA clause removal (trailing reference sentences).
CTA_CLAUSES = [
    " See the [wholesale guide](/blog/wholesale-guide/) for the sourcing framework.",
    " See the [wholesale guide](/blog/wholesale-guide/).",
    " For the commercial side of sourcing, see the [wholesale guide](/blog/wholesale-guide/).",
]


def process(slug: str) -> dict:
    path = ING / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    changes = []
    for old, new in HEADER_RENAMES:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"header: {old[:60]}")
    for old, new in BODY_FIXES:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"body: {old[:50]}")
    for old, new in BUYING_FIXES:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"buying: {old[:50]}")
    for clause in CTA_CLAUSES:
        if clause in text:
            text = text.replace(clause, ".")
            changes.append(f"cta: {clause[:40]}")
    if changes:
        path.write_text(text, encoding="utf-8")
    return {"slug": slug, "changes": changes}


def main():
    slugs = sys.argv[1:]
    results = [process(s) for s in slugs]
    changed = [r for r in results if r["changes"]]
    print(f"processed={len(results)} changed={len(changed)}")
    for r in changed:
        for c in r["changes"]:
            print(f"  {r['slug']}: {c}")


if __name__ == "__main__":
    main()
