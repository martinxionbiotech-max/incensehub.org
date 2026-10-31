#!/usr/bin/env python3
"""Append 12 new P3j entities to ingredients.json across main repo + data repo."""
import json, collections

E = [
    dict(termCode="valerian", name="Valerian", chinese="缬草", pinyin="xiécǎo",
         sci="Valeriana officinalis", aroma="earthy, musky, woody, rooty", cat="Roots",
         desc="缬草 (xiécǎo) is a Chinese botanical incense ingredient — Valeriana officinalis — with an aroma profile of earthy, musky, woody, rooty.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200022560",
                 "https://www.gbif.org/species/2888763"]),
    dict(termCode="schisandra", name="Schisandra", chinese="五味子", pinyin="wǔwèizǐ",
         sci="Schisandra chinensis", aroma="fruity, berry, sour, slightly woody", cat="Fruits",
         desc="五味子 (wǔwèizǐ) is a Chinese botanical incense ingredient — Schisandra chinensis — with an aroma profile of fruity, berry, sour, slightly woody.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200008486",
                 "https://www.gbif.org/species/7696841",
                 "https://zh.wikisource.org/wiki/本草綱目/草之七"]),
    dict(termCode="asarum", name="Asarum", chinese="细辛", pinyin="xìxīn",
         sci="Asarum sieboldii", aroma="pungent, spicy, rooty, camphoraceous", cat="Roots",
         desc="细辛 (xìxīn) is a Chinese botanical incense ingredient — Asarum sieboldii — with an aroma profile of pungent, spicy, rooty, camphoraceous.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200006671",
                 "https://www.gbif.org/species/7313629",
                 "https://zh.wikisource.org/wiki/本草綱目/草之二"]),
    dict(termCode="eupatorium-japonicum", name="Zelan", chinese="泽兰", pinyin="zélán",
         sci="Eupatorium japonicum", aroma="herbal, aromatic, fresh, slightly sweet", cat="Herbs",
         desc="泽兰 (zélán) is a Chinese botanical incense ingredient — Eupatorium japonicum — with an aroma profile of herbal, aromatic, fresh, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200023936",
                 "https://www.gbif.org/species/5403118",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="tree-peony-bark", name="Tree Peony Bark", chinese="牡丹皮", pinyin="mǔdān pí",
         sci="Paeonia suffruticosa (root bark)", aroma="rooty, earthy, woody, faintly floral", cat="Roots",
         desc="牡丹皮 (mǔdān pí) is a Chinese botanical incense ingredient — Paeonia suffruticosa (root bark) — with an aroma profile of rooty, earthy, woody, faintly floral.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200008041",
                 "https://www.gbif.org/species/7155259",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="lavender", name="Lavender", chinese="薰衣草", pinyin="xūnyīcǎo",
         sci="Lavandula angustifolia", aroma="floral, herbal, fresh, camphoraceous", cat="Flowers",
         desc="薰衣草 (xūnyīcǎo) is a Chinese botanical incense ingredient — Lavandula angustifolia — with an aroma profile of floral, herbal, fresh, camphoraceous.",
         sameAs=["https://www.gbif.org/species/2927305"]),
    dict(termCode="sage", name="Sage", chinese="鼠尾草", pinyin="shǔwěicǎo",
         sci="Salvia officinalis", aroma="herbal, camphoraceous, green, slightly peppery", cat="Herbs",
         desc="鼠尾草 (shǔwěicǎo) is a Chinese botanical incense ingredient — Salvia officinalis — with an aroma profile of herbal, camphoraceous, green, slightly peppery.",
         sameAs=["https://www.gbif.org/species/2927004"]),
    dict(termCode="thyme", name="Thyme", chinese="百里香", pinyin="bǎilǐxiāng",
         sci="Thymus vulgaris", aroma="herbal, green, spicy, slightly medicinal", cat="Herbs",
         desc="百里香 (bǎilǐxiāng) is a Chinese botanical incense ingredient — Thymus vulgaris — with an aroma profile of herbal, green, spicy, slightly medicinal.",
         sameAs=["https://www.gbif.org/species/5341442"]),
    dict(termCode="chamomile", name="Chamomile", chinese="洋甘菊", pinyin="yánggānjú",
         sci="Matricaria chamomilla", aroma="sweet, apple-like, floral, hay-like", cat="Flowers",
         desc="洋甘菊 (yánggānjú) is a Chinese botanical incense ingredient — Matricaria chamomilla — with an aroma profile of sweet, apple-like, floral, hay-like.",
         sameAs=["https://www.gbif.org/species/8370958"]),
    dict(termCode="ylang-ylang", name="Ylang-Ylang", chinese="依兰", pinyin="yīlán",
         sci="Cananga odorata", aroma="floral, sweet, creamy, slightly fruity", cat="Flowers",
         desc="依兰 (yīlán) is a Chinese botanical incense ingredient — Cananga odorata — with an aroma profile of floral, sweet, creamy, slightly fruity.",
         sameAs=["https://www.gbif.org/species/5407583"]),
    dict(termCode="copaiba", name="Copaiba", chinese="古巴香脂", pinyin="gǔbā xiāngzhī",
         sci="Copaifera spp. (resin)", aroma="woody, balsamic, resinous, slightly sweet", cat="Resins",
         desc="古巴香脂 (gǔbā xiāngzhī) is a Chinese botanical incense ingredient — Copaifera spp. (resin) — with an aroma profile of woody, balsamic, resinous, slightly sweet.",
         sameAs=["https://www.gbif.org/species/2978115"]),
    dict(termCode="violet", name="Violet", chinese="紫罗兰", pinyin="zǐluólán",
         sci="Viola odorata", aroma="floral, sweet, powdery, green", cat="Flowers",
         desc="紫罗兰 (zǐluólán) is a Chinese botanical incense ingredient — Viola odorata — with an aroma profile of floral, sweet, powdery, green.",
         sameAs=["https://www.gbif.org/species/5331181"]),
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
