#!/usr/bin/env python3
"""Append 12 new P3g entities to ingredients.json (main + public + data-landeng)."""
import json, collections

E = [
    dict(termCode="juniper", name="Juniper", chinese="杜松", pinyin="dùsōng",
         sci="Juniperus communis", aroma="woody, piney, resinous, fresh", cat="Woods",
         desc="杜松 (dùsōng) is a Chinese botanical incense ingredient — Juniperus communis — with an aroma profile of woody, piney, resinous, fresh.",
         sameAs=["https://www.gbif.org/species/2684709"]),
    dict(termCode="basil", name="Basil", chinese="罗勒", pinyin="luólè",
         sci="Ocimum basilicum", aroma="sweet, green, spicy, anise-like", cat="Herbs",
         desc="罗勒 (luólè) is a Chinese botanical incense ingredient — Ocimum basilicum — with an aroma profile of sweet, green, spicy, anise-like.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200019914",
                 "https://www.gbif.org/species/2927096",
                 "https://zh.wikisource.org/wiki/本草綱目/菜之一"]),
    dict(termCode="elsholtzia", name="Elsholtzia", chinese="香薷", pinyin="xiāngrú",
         sci="Elsholtzia ciliata", aroma="minty, herbal, spicy, slightly sweet", cat="Herbs",
         desc="香薷 (xiāngrú) is a Chinese botanical incense ingredient — Elsholtzia ciliata — with an aroma profile of minty, herbal, spicy, slightly sweet.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200019619",
                 "https://www.gbif.org/species/2927075",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三",
                 "https://zh.wikisource.org/wiki/香乘"]),
    dict(termCode="aglaia", name="Aglaia", chinese="米仔兰", pinyin="mǐzǎilán",
         sci="Aglaia odorata", aroma="sweet, floral, fruity, delicate", cat="Flowers",
         desc="米仔兰 (mǐzǎilán) is a Chinese botanical incense ingredient — Aglaia odorata — with an aroma profile of sweet, floral, fruity, delicate.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200012497",
                 "https://www.gbif.org/species/5597349"]),
    dict(termCode="peony", name="Peony", chinese="芍药", pinyin="sháoyào",
         sci="Paeonia lactiflora", aroma="floral, rosy, sweet, green", cat="Flowers",
         desc="芍药 (sháoyào) is a Chinese botanical incense ingredient — Paeonia lactiflora — with an aroma profile of floral, rosy, sweet, green.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200008034",
                 "https://www.gbif.org/species/3083486",
                 "https://zh.wikisource.org/wiki/本草綱目/草之三"]),
    dict(termCode="anise", name="Anise", chinese="茴芹", pinyin="huíqín",
         sci="Pimpinella anisum", aroma="sweet, licorice, warm, spicy", cat="Spices",
         desc="茴芹 (huíqín) is a Chinese botanical incense ingredient — Pimpinella anisum — with an aroma profile of sweet, licorice, warm, spicy.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200015767",
                 "https://www.gbif.org/species/8080300"]),
    dict(termCode="cumin", name="Cumin", chinese="孜然", pinyin="zīrán",
         sci="Cuminum cyminum", aroma="warm, spicy, earthy, slightly bitter", cat="Spices",
         desc="孜然 (zīrán) is a Chinese botanical incense ingredient — Cuminum cyminum — with an aroma profile of warm, spicy, earthy, slightly bitter.",
         sameAs=["https://www.gbif.org/species/3034775"]),
    dict(termCode="shellac", name="Shellac", chinese="紫草茸", pinyin="zǐcǎoróng",
         sci="Kerria lacca (lac insect; formerly Laccifer lacca) — lac resin", aroma="resinous, waxy, subtle, slightly sweet", cat="Resins",
         desc="紫草茸 (zǐcǎoróng) is a Chinese incense ingredient (insect-derived, not botanical) — lac resin, the secretion of the lac insect Kerria lacca (formerly Laccifer lacca) — with an aroma profile of resinous, waxy, subtle, slightly sweet.",
         sameAs=["https://www.gbif.org/species/5812747",
                 "https://zh.wikisource.org/wiki/本草綱目/蟲之一",
                 "https://zh.wikisource.org/wiki/香乘"]),
    dict(termCode="beeswax", name="Beeswax", chinese="蜂蜡", pinyin="fēnglà",
         sci="Apis cerana & A. mellifera (bee product) — beeswax", aroma="waxy, honeyed, warm, slightly sweet", cat="Animal-derived",
         desc="蜂蜡 (fēnglà) is a Chinese incense ingredient (bee product, not botanical) — beeswax, the wax of honey bees (Apis cerana & A. mellifera) — with an aroma profile of waxy, honeyed, warm, slightly sweet.",
         sameAs=["https://www.gbif.org/species/1341979",
                 "https://www.gbif.org/species/1341976",
                 "https://zh.wikisource.org/wiki/本草綱目/蟲之一"]),
    dict(termCode="torreya", name="Torreya", chinese="香榧", pinyin="xiāngfěi",
         sci="Torreya grandis", aroma="nutty, woody, resinous, roasted", cat="Seeds",
         desc="香榧 (xiāngfěi) is a Chinese botanical incense ingredient — Torreya grandis — with an aroma profile of nutty, woody, resinous, roasted.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=200005500",
                 "https://www.gbif.org/species/5284483",
                 "https://zh.wikisource.org/wiki/本草綱目/果之三"]),
    dict(termCode="kumquat", name="Kumquat", chinese="金橘", pinyin="jīnjú",
         sci="Citrus japonica (syn. Fortunella japonica)", aroma="citrus, sweet, floral, bright", cat="Fruits",
         desc="金橘 (jīnjú) is a Chinese botanical incense ingredient — Citrus japonica (syn. Fortunella japonica) — with an aroma profile of citrus, sweet, floral, bright.",
         sameAs=["http://www.efloras.org/florataxon.aspx?flora_id=2&taxon_id=242313265",
                 "https://www.gbif.org/species/3831801",
                 "https://zh.wikisource.org/wiki/本草綱目/果之二"]),
    dict(termCode="castoreum", name="Castoreum", chinese="海狸香", pinyin="hǎilíxiāng",
         sci="Castor fiber (Eurasian beaver) — animal secretion", aroma="animalic, leathery, smoky, sweet", cat="Animal",
         desc="海狸香 (hǎilíxiāng) is a Chinese incense ingredient (animal-derived, not botanical) — castoreum, a beaver (Castor fiber) secretion — with an aroma profile of animalic, leathery, smoky, sweet. Historical Western perfumery fixative; modern 'castoreum' is synthetic.",
         sameAs=["https://www.gbif.org/species/4409131"]),
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

paths = [
    "data/ingredients.json",
    "public/data/ingredients.json",
]
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
