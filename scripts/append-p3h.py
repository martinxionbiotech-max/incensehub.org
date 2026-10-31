#!/usr/bin/env python3
"""Append 12 new P3h entities to ingredients.json across main repo + data repo."""
import json, collections

E = [
    dict(termCode="blumea-balsamifera", name="Blumea Balsamifera", chinese="艾纳香", pinyin="àinàxiāng",
         sci="Blumea balsamifera", aroma="camphoraceous, herbal, cooling, slightly sweet", cat="Herbs",
         desc="艾纳香 (àinàxiāng) is a Chinese botanical incense ingredient — Blumea balsamifera — with an aroma profile of camphoraceous, herbal, cooling, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200023545",
                 "https://www.gbif.org/species/5395786",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="tuberose", name="Tuberose", chinese="晚香玉", pinyin="wǎnxiāngyù",
         sci="Agave amica (syn. Polianthes tuberosa)", aroma="sweet, floral, creamy, heady", cat="Flowers",
         desc="晚香玉 (wǎnxiāngyù) is a Chinese botanical incense ingredient — Agave amica (syn. Polianthes tuberosa) — with an aroma profile of sweet, floral, creamy, heady.",
         sameAs=["https://www.gbif.org/species/10868891",
                 "https://www.gbif.org/species/2775487"]),
    dict(termCode="dill", name="Dill", chinese="莳萝", pinyin="shíluó",
         sci="Anethum graveolens", aroma="herbal, fresh, anise-like, slightly sweet", cat="Spices",
         desc="莳萝 (shíluó) is a Chinese botanical incense ingredient — Anethum graveolens — with an aroma profile of herbal, fresh, anise-like, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200015349",
                 "https://www.gbif.org/species/3034646",
                 "https://zh.wikisource.org/wiki/本草綱目/菜之一"]),
    dict(termCode="mustard", name="Mustard Seed", chinese="芥子", pinyin="jièzǐ",
         sci="Sinapis alba (white mustard); Brassica juncea (brown/leaf mustard)", aroma="pungent, sharp, spicy, green", cat="Spices",
         desc="芥子 (jièzǐ) is a Chinese botanical incense ingredient — Sinapis alba (white mustard); Brassica juncea (brown/leaf mustard) — with an aroma profile of pungent, sharp, spicy, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200009253",
                 "https://www.gbif.org/species/3047621",
                 "https://www.gbif.org/species/3042751",
                 "https://zh.wikisource.org/wiki/本草綱目/菜之一"]),
    dict(termCode="apricot-kernel", name="Apricot Kernel", chinese="杏仁", pinyin="xìngrén",
         sci="Prunus armeniaca (apricot kernel)", aroma="sweet, nutty, almondy, bitter", cat="Seeds",
         desc="杏仁 (xìngrén) is a Chinese botanical incense ingredient — Prunus armeniaca (apricot kernel) — with an aroma profile of sweet, nutty, almondy, bitter.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200010636",
                 "https://www.gbif.org/species/7818643",
                 "https://zh.wikisource.org/wiki/本草綱目/果之一"]),
    dict(termCode="ginkgo", name="Ginkgo Nut", chinese="银杏", pinyin="yínxìng",
         sci="Ginkgo biloba", aroma="nutty, sweet, mild, slightly bitter", cat="Seeds",
         desc="银杏 (yínxìng) is a Chinese botanical incense ingredient — Ginkgo biloba — with an aroma profile of nutty, sweet, mild, slightly bitter.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200005235",
                 "https://www.gbif.org/species/2687885",
                 "https://zh.wikisource.org/wiki/本草綱目/果之二"]),
    dict(termCode="angelica-sinensis", name="Dong Quai", chinese="当归", pinyin="dāngguī",
         sci="Angelica sinensis", aroma="herbal, sweet, warm, slightly spicy", cat="Roots",
         desc="当归 (dāngguī) is a Chinese botanical incense ingredient — Angelica sinensis — with an aroma profile of herbal, sweet, warm, slightly spicy.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200015389",
                 "https://www.gbif.org/species/6027415",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="peru-balsam", name="Peru Balsam", chinese="秘鲁香脂", pinyin="bìlǔ xiāngzhī",
         sci="Myroxylon balsamum", aroma="sweet, vanilla, balsamic, warm", cat="Resins",
         desc="秘鲁香脂 (bìlǔ xiāngzhī) is a Chinese botanical incense ingredient — Myroxylon balsamum — with an aroma profile of sweet, vanilla, balsamic, warm.",
         sameAs=["https://www.gbif.org/species/5357190"]),
    dict(termCode="quince", name="Quince", chinese="木瓜", pinyin="mùguā",
         sci="Pseudocydonia sinensis (syn. Chaenomeles sinensis)", aroma="fruity, sweet, floral, tart", cat="Fruits",
         desc="木瓜 (mùguā) is a Chinese botanical incense ingredient — Pseudocydonia sinensis (syn. Chaenomeles sinensis) — with an aroma profile of fruity, sweet, floral, tart.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200010697",
                 "https://www.gbif.org/species/3000699",
                 "https://zh.wikisource.org/wiki/本草綱目/果之二"]),
    dict(termCode="platycladus-leaves", name="Arborvitae Leaves", chinese="侧柏叶", pinyin="cèbǎi yè",
         sci="Platycladus orientalis (the leafy branchlets)", aroma="woody, fresh, green, slightly resinous", cat="Herbs",
         desc="侧柏叶 (cèbǎi yè) is a Chinese botanical incense ingredient — Platycladus orientalis (the leafy branchlets) — with an aroma profile of woody, fresh, green, slightly resinous.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200005428",
                 "https://www.gbif.org/species/2684855",
                 "https://zh.wikisource.org/wiki/本草綱目/木之一"]),
    dict(termCode="vanilla", name="Vanilla Bean", chinese="香草荚", pinyin="xiāngcǎo jiá",
         sci="Vanilla planifolia", aroma="sweet, creamy, warm, gourmand", cat="Fruits",
         desc="香草荚 (xiāngcǎo jiá) is a Chinese botanical incense ingredient — Vanilla planifolia — with an aroma profile of sweet, creamy, warm, gourmand.",
         sameAs=["https://www.gbif.org/species/2803398"]),
    dict(termCode="silk-tree", name="Silk Tree Flower", chinese="合欢花", pinyin="héhuān huā",
         sci="Albizia julibrissin", aroma="sweet, floral, delicate, slightly powdery", cat="Flowers",
         desc="合欢花 (héhuān huā) is a Chinese botanical incense ingredient — Albizia julibrissin — with an aroma profile of sweet, floral, delicate, slightly powdery.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200011875",
                 "https://www.gbif.org/species/2972983",
                 "https://zh.wikisource.org/wiki/本草綱目/木之二"]),
]

def make_entity(e):
    return {
        "@type": "DefinedTerm",
        "termCode": e["termCode"],
        "name": e["name"],
        "alternateName": [e["chinese"], e["pinyin"], e["sci"]],
        "description": e["desc"],
        "additionalProperty": [
            {"@type": "PropertyValue", "name": "Chinese", "value": e["chinese"]},
            {"@type": "PropertyValue", "name": "Pinyin", "value": e["pinyin"]},
            {"@type": "PropertyValue", "name": "Scientific name", "value": e["sci"]},
            {"@type": "PropertyValue", "name": "Type", "value": "ingredient"},
            {"@type": "PropertyValue", "name": "Aroma", "value": e["aroma"]},
            {"@type": "PropertyValue", "name": "Category", "value": e["cat"]},
        ],
        "sameAs": e["sameAs"],
    }

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=collections.OrderedDict)

def dump(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

if __name__ == "__main__":
    import sys
    paths = sys.argv[1:] if len(sys.argv) > 1 else ["data/ingredients.json"]
    for p in paths:
        d = load(p)
        existing = {x["termCode"] for x in d["mainEntity"]}
        added = 0
        for e in E:
            if e["termCode"] in existing:
                print(f"  SKIP duplicate {e['termCode']} in {p}")
                continue
            d["mainEntity"].append(make_entity(e))
            added += 1
        dump(p, d)
        print(f"{p}: appended {added} entities -> {len(d['mainEntity'])} total")
