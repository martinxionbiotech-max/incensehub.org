#!/usr/bin/env python3
"""Batch D — neutralize buyer/buying framing in T2/T3 blog pages.

Converts the buyer/sourcing framing that survived batch C to the neutral
informational voice (reader / identification / choosing). Deterministic
phrase edits only; no structural changes.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "src" / "content" / "blog"

# Ordered phrase rewrites. Longest / most specific first.
PHRASES = [
    # buyer-intelligence -> identification
    ("buyer-intelligence discipline", "identification discipline"),
    ("buyer-intelligence editorial", "identification editorial"),
    ("buyer-intelligence logic", "identification logic"),
    ("buyer-intelligence", "identification"),
    # buyer -> reader (specific phrases first)
    ("buyer-facing honesty point", "reader-facing honesty point"),
    ("buyer-facing fact", "reader-facing fact"),
    ("buyer-facing decision", "reader-facing decision"),
    ("a buyer-facing", "a reader-facing"),
    ("buyer heuristics", "trade heuristics"),
    ("for an Indian-incense buyer", "for an Indian-incense reader"),
    ("for a modern buyer", "for a modern reader"),
    ("the buyer's checklist", "the identification checklist"),
    ("The buyer's side", "The reader's side"),
    ("the buyer should not pay absolute prices for an accord", "the reader should not pay absolute prices for an accord"),
    ("a buyer should already know", "a reader should already know"),
    ("A buyer who understands", "A reader who understands"),
    ("A buyer who has learned", "A reader who has learned"),
    ("A buyer who demands", "A reader who demands"),
    ("A buyer who can resolve", "A reader who can resolve"),
    ("A buyer can inspect chips by eye", "A reader can inspect chips by eye"),
    ("A buyer can verify", "A reader can verify"),
    ("A buyer should confirm", "A reader should confirm"),
    ("A buyer should ask", "A reader should ask"),
    ("a buyer should know which they are getting", "a reader should know which they are getting"),
    ("a buyer's impatience", "a reader's impatience"),
    ("a buyer's job", "a reader's task"),
    ("for a buyer", "for a reader"),
    ("to a buyer", "to a reader"),
    ("a buyer", "a reader"),
    ("the buyer", "the reader"),
    ("buyers", "readers"),
    # buying -> getting / choosing
    ("what you are actually buying", "what you are actually getting"),
    ("what you are buying", "what you are getting"),
    ("what you're actually buying", "what you're actually getting"),
    ("which you are buying", "which you are getting"),
    ("what kind of incense you are buying", "what kind of incense you are getting"),
    ("you are usually buying a floral accord", "you are usually getting a floral accord"),
    ("smelling and buying", "smelling and getting"),
    ("knowing which you are buying", "knowing which you are getting"),
    ("how to tell which you are buying", "how to tell which you are getting"),
    ("how to tell when buying", "how to tell when choosing"),
    ("before buying", "before choosing"),
    ("For buying", "For choosing"),
    ("the buying checks", "the identification checks"),
    ("The buying decision", "The decision"),
    ("buying guide", "selection guide"),
    ("Buying Guide", "Selection Guide"),
    ("buying a 宣德炉", "acquiring a 宣德炉"),
    ("the agarwood-specific buying guide", "the agarwood-specific guide"),
    ("The buying guidance", "The identification guidance"),
    # stale link text
    ("[Buying Qinan (奇楠): What to Check Before You Pay](/blog/qinan-buying-authentication/)", "[Authenticating 奇楠 (Qinan)](/blog/qinan-buying-authentication/)"),
    # wholesale-guide CTA (blog page)
    ("See the [wholesale guide](/blog/wholesale-guide/) for the sourcing framework.", ""),
]


def neutralize(text: str) -> tuple[str, int]:
    n = 0
    for old, new in PHRASES:
        if old in text:
            text = text.replace(old, new)
            n += 1
    return text, n


def process(slug: str) -> dict:
    path = BLOG / f"{slug}.md"
    if not path.exists():
        return {"slug": slug, "changed": 0, "n": 0}
    text = path.read_text(encoding="utf-8")
    new, n = neutralize(text)
    if new != text:
        path.write_text(new, encoding="utf-8")
    return {"slug": slug, "changed": new != text, "n": n}


def main():
    slugs = sys.argv[1:]
    results = [process(s) for s in slugs]
    changed = [r for r in results if r["changed"]]
    print(f"processed={len(results)} changed={len(changed)} total_edits={sum(r['n'] for r in results)}")
    for r in changed:
        print(f"  {r['slug']}: {r['n']} edits")


if __name__ == "__main__":
    main()
