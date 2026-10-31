#!/usr/bin/env python3
"""Append 12 new P3i entities to ingredients.json across main repo + data repo."""
import json, collections

E = [
    dict(termCode="pine-needles", name="Pine Needles", chinese="松针", pinyin="sōngzhēn",
         sci="Pinus spp. (the needles)", aroma="piney, conifer, fresh, green", cat="Herbs",
         desc="松针 (sōngzhēn) is a Chinese botanical incense ingredient — Pinus spp. (the needles) — with an aroma profile of piney, conifer, fresh, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200005343",
                 "https://www.gbif.org/species/5285215",
                 "https://zh.wikisource.org/wiki/本草綱目/木之一"]),
    dict(termCode="bamboo-leaves", name="Bamboo Leaves", chinese="竹叶", pinyin="zhúyè",
         sci="Phyllostachys spp. (the leaves)", aroma="green, fresh, grassy, slightly sweet", cat="Herbs",
         desc="竹叶 (zhúyè) is a Chinese botanical incense ingredient — Phyllostachys spp. (the leaves) — with an aroma profile of green, fresh, grassy, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200025925",
                 "https://www.gbif.org/species/5290171",
                 "https://zh.wikisource.org/wiki/本草綱目/木之五"]),
    dict(termCode="fenugreek", name="Fenugreek", chinese="葫芦巴", pinyin="húlúbā",
         sci="Trigonella foenum-graecum", aroma="sweet, maple-like, nutty, slightly bitter", cat="Spices",
         desc="葫芦巴 (húlúbā) is a Chinese botanical incense ingredient — Trigonella foenum-graecum — with an aroma profile of sweet, maple-like, nutty, slightly bitter.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200012345",
                 "https://www.gbif.org/species/5360475",
                 "https://zh.wikisource.org/wiki/本草綱目/草之四"]),
    dict(termCode="ligusticum-chuanxiong", name="Chuanxiong", chinese="川芎", pinyin="chuānxiōng",
         sci="Ligusticum chuanxiong (syn. Conioselinum anthriscoides)", aroma="herbal, aromatic, spicy, slightly bitter", cat="Roots",
         desc="川芎 (chuānxiōng) is a Chinese botanical incense ingredient — Ligusticum chuanxiong (syn. Conioselinum anthriscoides) — with an aroma profile of herbal, aromatic, spicy, slightly bitter.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=118546",
                 "https://www.gbif.org/species/3639592",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="sophora-flower", name="Sophora Flower", chinese="槐花", pinyin="huáihuā",
         sci="Styphnolobium japonicum (syn. Sophora japonica)", aroma="sweet, floral, delicate, honey-like", cat="Flowers",
         desc="槐花 (huáihuā) is a Chinese botanical incense ingredient — Styphnolobium japonicum (syn. Sophora japonica) — with an aroma profile of sweet, floral, delicate, honey-like.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200012322",
                 "https://www.gbif.org/species/2963569",
                 "https://zh.wikisource.org/wiki/本草綱目/木之二"]),
    dict(termCode="tree-peony", name="Tree Peony", chinese="牡丹", pinyin="mǔdān",
         sci="Paeonia suffruticosa", aroma="floral, rosy, sweet, green", cat="Flowers",
         desc="牡丹 (mǔdān) is a Chinese botanical incense ingredient — Paeonia suffruticosa — with an aroma profile of floral, rosy, sweet, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200008041",
                 "https://www.gbif.org/species/7155259",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="mulberry-leaf", name="Mulberry Leaf", chinese="桑叶", pinyin="sāngyè",
         sci="Morus alba (the leaves)", aroma="green, fresh, tea-like, slightly sweet", cat="Herbs",
         desc="桑叶 (sāngyè) is a Chinese botanical incense ingredient — Morus alba (the leaves) — with an aroma profile of green, fresh, tea-like, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200006379",
                 "https://www.gbif.org/species/5361889",
                 "https://zh.wikisource.org/wiki/本草綱目/木之三"]),
    dict(termCode="artemisia-annua", name="Sweet Wormwood", chinese="青蒿", pinyin="qīnghāo",
         sci="Artemisia annua", aroma="herbal, camphoraceous, fresh, slightly sweet", cat="Herbs",
         desc="青蒿 (qīnghāo) is a Chinese botanical incense ingredient — Artemisia annua — with an aroma profile of herbal, camphoraceous, fresh, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200023164",
                 "https://www.gbif.org/species/8373355",
                 "https://zh.wikisource.org/wiki/本草綱目/草之四"]),
    dict(termCode="schizonepeta", name="Schizonepeta", chinese="荆芥", pinyin="jīngjiè",
         sci="Schizonepeta tenuifolia (syn. Nepeta tenuifolia)", aroma="herbal, minty, spicy, fresh", cat="Herbs",
         desc="荆芥 (jīngjiè) is a Chinese botanical incense ingredient — Schizonepeta tenuifolia (syn. Nepeta tenuifolia) — with an aroma profile of herbal, minty, spicy, fresh.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=210001326",
                 "https://www.gbif.org/species/5609573",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="cassia-twig", name="Cassia Twig", chinese="桂枝", pinyin="guìzhī",
         sci="Cinnamomum cassia (the young twig); syn. C. aromaticum", aroma="warm, spicy, sweet, woody", cat="Woods",
         desc="桂枝 (guìzhī) is a Chinese botanical incense ingredient — Cinnamomum cassia (the young twig); syn. C. aromaticum — with an aroma profile of warm, spicy, sweet, woody.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200008698",
                 "https://www.gbif.org/species/3033982",
                 "https://zh.wikisource.org/wiki/本草綱目/木之一"]),
    dict(termCode="bergamot", name="Bergamot", chinese="佛手柑", pinyin="fóshǒugān",
         sci="Citrus × bergamia", aroma="citrus, floral, fresh, slightly bitter", cat="Fruits",
         desc="佛手柑 (fóshǒugān) is a Chinese botanical incense ingredient — Citrus × bergamia — with an aroma profile of citrus, floral, fresh, slightly bitter.",
         sameAs=["https://www.gbif.org/species/6433772"]),
    dict(termCode="neroli", name="Neroli", chinese="橙花", pinyin="chénghuā",
         sci="Citrus aurantium (the flower)", aroma="floral, citrus, sweet, green", cat="Flowers",
         desc="橙花 (chénghuā) is a Chinese botanical incense ingredient — Citrus aurantium (the flower) — with an aroma profile of floral, citrus, sweet, green.",
         sameAs=["https://www.gbif.org/species/8077391"]),
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
