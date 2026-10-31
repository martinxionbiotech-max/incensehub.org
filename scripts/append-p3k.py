#!/usr/bin/env python3
"""Append 8 new P3k entities to ingredients.json across main repo + data repo."""
import json, collections

E = [
    dict(termCode="lemon", name="Lemon", chinese="柠檬", pinyin="níngméng",
         sci="Citrus × limon", aroma="citrus, bright, zesty, sweet, slightly sour", cat="Fruits",
         desc="柠檬 (níngméng) is a Chinese botanical incense ingredient — Citrus × limon — with an aroma profile of citrus, bright, zesty, sweet, slightly sour.",
         sameAs=["https://www.gbif.org/species/7647136"]),
    dict(termCode="grapefruit", name="Grapefruit", chinese="葡萄柚", pinyin="pútáoyòu",
         sci="Citrus × paradisi", aroma="citrus, fresh, bittersweet, green, slightly woody", cat="Fruits",
         desc="葡萄柚 (pútáoyòu) is a Chinese botanical incense ingredient — Citrus × paradisi — with an aroma profile of citrus, fresh, bittersweet, green, slightly woody.",
         sameAs=["https://www.gbif.org/species/7469645"]),
    dict(termCode="tarragon", name="Tarragon", chinese="龙蒿", pinyin="lónghāo",
         sci="Artemisia dracunculus", aroma="herbal, anise-like, green, slightly sweet", cat="Herbs",
         desc="龙蒿 (lónghāo) is a Chinese botanical incense ingredient — Artemisia dracunculus — with an aroma profile of herbal, anise-like, green, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200023201",
                 "https://www.gbif.org/species/3121581"]),
    dict(termCode="spearmint", name="Spearmint", chinese="留兰香", pinyin="liúlánxiāng",
         sci="Mentha spicata", aroma="cooling, minty, sweet, fresh, green", cat="Herbs",
         desc="留兰香 (liúlánxiāng) is a Chinese botanical incense ingredient — Mentha spicata — with an aroma profile of cooling, minty, sweet, fresh, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200019821",
                 "https://www.gbif.org/species/2927175"]),
    dict(termCode="peppermint", name="Peppermint", chinese="胡椒薄荷", pinyin="hújiāo bòhé",
         sci="Mentha × piperita", aroma="cooling, minty, sharp, camphoraceous, sweet", cat="Herbs",
         desc="胡椒薄荷 (hújiāo bòhé) is a Chinese botanical incense ingredient — Mentha × piperita — with an aroma profile of cooling, minty, sharp, camphoraceous, sweet.",
         sameAs=["https://www.gbif.org/species/8707933"]),
    dict(termCode="eucalyptus", name="Eucalyptus", chinese="桉叶", pinyin="ānyè",
         sci="Eucalyptus globulus", aroma="camphoraceous, fresh, sharp, slightly medicinal, clean", cat="Herbs",
         desc="桉叶 (ānyè) is a Chinese botanical incense ingredient — Eucalyptus globulus — with an aroma profile of camphoraceous, fresh, sharp, slightly medicinal, clean.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200014782",
                 "https://www.gbif.org/species/3176787"]),
    dict(termCode="lemon-balm", name="Lemon Balm", chinese="香蜂草", pinyin="xiāngfēngcǎo",
         sci="Melissa officinalis", aroma="lemony, herbal, fresh, slightly sweet, green", cat="Herbs",
         desc="香蜂草 (xiāngfēngcǎo) is a Chinese botanical incense ingredient — Melissa officinalis — with an aroma profile of lemony, herbal, fresh, slightly sweet, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200019809",
                 "https://www.gbif.org/species/5341501"]),
    dict(termCode="lily-of-the-valley", name="Lily of the Valley", chinese="铃兰", pinyin="línglán",
         sci="Convallaria majalis", aroma="floral, green, sweet, fresh, delicate", cat="Flowers",
         desc="铃兰 (línglán) is a Chinese botanical incense ingredient — Convallaria majalis — with an aroma profile of floral, green, sweet, fresh, delicate.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200027600",
                 "https://www.gbif.org/species/7459480"]),
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
