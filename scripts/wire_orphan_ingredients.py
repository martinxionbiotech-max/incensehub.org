#!/usr/bin/env python3
"""Add reciprocal contextual "See also" inbound links for orphan ingredients.

For each orphan ingredient, add a markdown link to it in the "See also" line
of 2 sibling pages (its `related:` neighbours), so the orphan gains 2 inbound
markdown links. Each source page receives at most 2 new links (density guard).

Usage:
  python3 wire_orphan_ingredients.py report   # show what would change
  python3 wire_orphan_ingredients.py apply    # apply edits
"""
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ING = os.path.join(ROOT, "src", "content", "ingredients")

# orphan -> list of (source_slug, anchor)
ASSIGN = {
    "aglaia": [("michelia-figo", "aglaia"), ("champaca", "aglaia")],
    "amber": [("pine-resin", "amber"), ("styrax-resin", "amber")],
    "apricot-kernel": [("plum-blossom", "apricot kernel"), ("peony", "apricot kernel")],
    "asarum": [("ligusticum", "asarum"), ("angelica", "asarum")],
    "banksia-rose": [("costus", "banksia rose"), ("rose", "banksia rose")],
    "beeswax": [("honey", "beeswax")],  # 2nd link -> makko blog (handled separately)
    "bletilla": [("sandalwood", "bletilla"), ("agarwood", "bletilla")],
    "castoreum": [("civet", "castoreum"), ("musk", "castoreum")],
    "copaiba": [("peru-balsam", "copaiba"), ("benzoin", "copaiba")],
    "cyperus": [("vetiver", "cyperus"), ("calamus", "cyperus")],
    "daphne": [("wintersweet", "daphne"), ("plum-blossom", "daphne")],
    "dill": [("fennel", "dill"), ("cumin", "dill")],
    "elsholtzia": [("agastache-rugosa", "elsholtzia"), ("perilla", "elsholtzia")],
    "eucalyptus": [("camphor", "eucalyptus"), ("rosemary", "eucalyptus")],
    "fenugreek": [("cumin", "fenugreek"), ("fennel", "fenugreek")],
    "galbanum": [("asafoetida", "galbanum"), ("frankincense", "galbanum")],
    "ginkgo": [("torreya", "ginkgo nut"), ("cypress-seed", "ginkgo nut")],
    "grapefruit": [("pomelo-peel", "grapefruit"), ("citron", "grapefruit")],
    "lily-of-the-valley": [("jasmine", "lily of the valley"), ("orris-root", "lily of the valley")],
    "mastic": [("frankincense", "mastic"), ("myrrh", "mastic")],
    "mustard": [("pepper", "mustard seed"), ("cinnamon", "mustard seed")],
    "nutmeg": [("clove", "nutmeg"), ("cardamom", "nutmeg")],
    "onycha": [("ambergris", "onycha"), ("musk", "onycha")],
    "orchid": [("osmanthus", "orchid"), ("chrysanthemum", "orchid")],
    "oxyphylla": [("galangal", "sharp-leaf galangal"), ("katsumadai", "sharp-leaf galangal")],
    "paicao": [("linglingxiang", "paicao"), ("agastache-rugosa", "paicao")],
    "prickly-ash": [("pepper", "sichuan pepper"), ("long-pepper", "sichuan pepper")],
    "quince": [("kumquat", "quince"), ("citron", "quince")],
    "rue": [("mugwort", "rue"), ("citronella", "rue")],
    "schisandra": [("amomum-villosum", "schisandra"), ("licorice", "schisandra")],
    "shellac": [("dragons-blood", "shellac"), ("benzoin", "shellac")],
    "silk-tree": [("honeysuckle", "silk tree flower"), ("osmanthus", "silk tree flower")],
    "tree-peony-bark": [("tree-peony", "tree peony bark"), ("peony", "tree peony bark")],
    "valerian": [("spikenard-nardostachys", "valerian"), ("vetiver", "valerian")],
    "violet": [("orris-root", "violet"), ("rose", "violet")],
    "ylang-ylang": [("neroli", "ylang-ylang"), ("tuberose", "ylang-ylang")],
}


def insert_links(line: str, links: list) -> str:
    """Insert one or more links before the 'and/plus the full [scent guide]' tail,
    producing clean comma-separated grammar (no double commas)."""
    m = re.search(r"\s+(?:and|plus)\s+the full \[scent guide\]\(/blog/scent-guide/\)\.\s*$", line)
    if m:
        prefix = line[:m.start()]
        tail = line[m.start():]
    else:
        prefix = line.rstrip()
        tail = ""
        if prefix.endswith("."):
            prefix = prefix[:-1]
            tail = "."
    prefix = prefix.rstrip()
    if prefix.endswith(","):
        prefix = prefix[:-1].rstrip()
    addition = ", ".join(links)
    return f"{prefix}, {addition}{tail}"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "report"

    # group inserts by source file, in deterministic order
    per_file = defaultdict(list)  # path -> [link strings]
    for orphan in sorted(ASSIGN):
        for src_slug, anchor in ASSIGN[orphan]:
            path = os.path.join(ING, f"{src_slug}.md")
            if not os.path.exists(path):
                print(f"MISSING source ingredient: {src_slug} (for {orphan})")
                continue
            per_file[path].append(f"[{anchor}](/ingredients/{orphan}/)")

    total = 0
    for path in sorted(per_file):
        text = open(path, encoding="utf-8").read()
        lines = text.split("\n")
        idx = next((i for i, ln in enumerate(lines) if ln.startswith("See also:")), None)
        if idx is None:
            print(f"NO See also line: {path}")
            continue
        links = [l for l in per_file[path] if l not in lines[idx]]
        if not links:
            continue
        lines[idx] = insert_links(lines[idx], links)
        total += len(links)
        if mode == "apply":
            open(path, "w", encoding="utf-8").write("\n".join(lines))

    print(f"Total link insertions: {total}")
    print(f"Distinct source files: {len(per_file)}")
    if mode == "report":
        for path in sorted(per_file):
            print(f"  {os.path.basename(path)}: {len(per_file[path])} link(s)")


if __name__ == "__main__":
    main()
