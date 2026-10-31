---
slug: "incense-terminology-reference"
title: "Chinese Incense Terminology: The 249-Term Reference"
primary_keyword: "chinese incense terminology"
search_intent: "informational"
pillar: "P1 — Chinese Incense 101"
content_type: "reference"
cluster_role: "reference"
last_reviewed: "2026-09-25"
brand: "IncenseHub"
author: "Landeng Tech Team"
---


**Direct answer:** This is the main-site entry point to IncenseHub's **Chinese–English incense terminology** — a 249-term canonical glossary covering materials, grades, forms, techniques, tools, and cultural terms. It is not a 249-entry dictionary on this page; instead it is a **structured index** that groups the vocabulary by direction, shows representative terms, and points to the two places the full set lives: the machine-readable `terminology.json` dataset and the human-readable [terminology glossary](/blog/incense-terminology-glossary/).

**Key facts:** The terminology dataset holds **249 terms**, each with a Chinese source term (source of truth), a pinyin reading, a literal meaning, and a preferred English translation. It is licensed CC BY-SA 4.0, versioned (currently 1.4), and served from `data.incensehub.org`. One Chinese word does not always map to one English word.

---

## Key Takeaways

- The terminology layer is a **strategic asset** — Chinese terms are the source of truth; English is the agreed translation.
- The **249 terms group into roughly a dozen directions**: materials, grades, aroma, forms, techniques, tools, texts, manufacturing, geography, culture, and adulteration.
- The full set lives in **`terminology.json`** (machine-readable) and the **[terminology glossary](/blog/incense-terminology-glossary/)** (human-readable form terms).
- This page is the **index**, not the dictionary — it shows how to navigate the vocabulary.

---

## How the Terminology Is Structured

> **Direct answer:** Every one of the 249 terms is a DefinedTerm with a Chinese name (source of truth), a pinyin reading, a literal meaning, and a preferred English translation. The dataset explicitly guards against a common error — assuming one Chinese word equals one English word.

A single record looks like this (using 沉香 as the example):

| Field | Value |
|---|---|
| Chinese (name) | 沉香 |
| Pinyin | chénxiāng |
| Literal meaning | sinking fragrance |
| Preferred English | agarwood |

The key editorial principle is stated in the dataset's own description: **"One Chinese word does not always map to one English word."** A term like 藿香 can mean agastache (*Agastache rugosa*) or patchouli (*Pogostemon cablin*) depending on context, which is why the glossary records context alongside the translation rather than forcing a single gloss. See the [incense ingredients glossary](/blog/incense-ingredients-glossary/) for the ingredient-side treatment.

## The Directions (Grouped Index)

> **Direct answer:** The 249 terms fall into a small number of natural directions — materials and grades, aroma and burn behavior, forms, techniques, tools, texts, manufacturing, geography and trade, culture, and adulteration — and this section samples each so you can find your way into the full dataset.

The grouping below is an editorial index for navigation, not a field in the dataset. Counts are approximate groupings of the 249 records.

### Materials and grades (~90 terms)

The largest direction: ingredient names (沉香 agarwood, 檀香 sandalwood, 乳香 frankincense, 没药 myrrh, 麝香 musk, 龙脑 borneol, 安息香 benzoin) and the agarwood grading vocabulary (沉水 sinking grade, 奇楠 qínán, 白奇楠/绿奇楠/黄奇楠/黑奇楠/紫奇楠 the five color grades, 半沉半浮 semi-sinking, 生结 live-formed, 熟结 mature-formed, 虫漏 insect-bored).

### Aroma and burn behavior (~28 terms)

The descriptors and behavior terms: 甜 sweet, 辛 pungent, 清 clear, 凉 cooling, 醇 mellow, 雅 refined, plus the note structure 前调/中调/top/middle/base note (后调), 发烟量 smoke output, 燃烧速率 burn rate, 留香 longevity, 定香剂 fixative.

### Forms and formats (~25 terms)

线香 stick, 盘香 coil, 塔香 cone, 倒流香 backflow cone, 香粉 powder, 香丸 pill, 香饼 cake, 香牌 plaque, 香珠 bead, 竹签香 bamboo-core stick, 微烟香 low-smoke, 无烟香 smokeless. This overlaps the [forms dataset](/blog/incense-materials-techniques-forms/).

### Techniques and practice (~23 terms)

隔火焚香 indirect-fire, 篆香 seal incense, 合香 blending, 品香 appreciation, 香道 the way of incense, 空熏 no-flame heating, 单方 single-material, 复方 compound formula, 四般闲事 the Four Leisure Arts.

### Tools and vessels (~27 terms)

香炉 censer, 博山炉 Boshan censer, 宣德炉 Xuande censer, 香匙 incense spoon, 香箸 incense chopsticks, 香盒 incense box, 香灰 incense ash, 香几 incense stand, 香铲 spatula, 银叶 silver leaf, 云母 mica.

### Texts, manufacturing, geography, and the rest

- **Texts** (~7): 香乘 the Incense Compendium, 本草 materia medica, 陈氏香谱 and 洪芻香谱 manuals, 梦粱录 the Meng Liang Lu.
- **Manufacturing** (~8): 打粉 grinding, 筛粉 sieving, 粒径 particle size, 含水率 moisture content, 粘粉 binder powder, 成型 forming.
- **Geography and trade** (~8): 海南香 Hainan agarwood, 安南香 Vietnamese agarwood, 真腊 Chenla, 占城 Champa, 渤泥 Borneo, 番香 foreign incense.
- **Culture and ritual** (~9): 香市 incense market, 香会 incense gathering, 香户 incense household, 香婆 incense woman, 香界 incense realm, 熏笼 fumigation cage, 手炉 hand warmer.
- **Adulteration and fakes** (~3): 假货 counterfeit, 高压灌油 high-pressure oil injection, 泡药水 chemical/dye soaking.

## Where the Full Set Lives

> **Direct answer:** The complete 249-term vocabulary lives in two places — the machine-readable `terminology.json` dataset (the canonical source of truth) and the human-readable terminology glossary for form vocabulary. This page is the index between them.

- **Machine-readable:** [Terminology dataset](https://data.incensehub.org/datasets/terminology.json) — 249 DefinedTerm records, CC BY-SA 4.0, version 1.4.
- **Human-readable (forms):** [Incense Terminology Glossary](/blog/incense-terminology-glossary/) — the form and practice vocabulary in table form.
- **Human-readable (ingredients):** [Incense Ingredients Glossary](/blog/incense-ingredients-glossary/) — the ingredient vocabulary.

The dataset carries a version, a `dateModified`, and a changelog, so its history is auditable rather than a silent edit. The full eight-dataset inventory is on the [knowledge map](/blog/landeng-knowledge-map/).

## How to Use the Terminology

> **Direct answer:** Three practical uses — pin down a Chinese name's English translation before buying, read a recipe or manual, or build a Chinese–English reference against the machine-readable dataset. The direction index above is the fastest entry for a human.

- **For buying** — a label or recipe name like 白奇楠 should resolve to "white qínán (agarwood grade)", not a guess; the glossary is the resolution table.
- **For reading** — classical manuals and 合香 recipes use 香道, 合香, 隔火焚香, 君臣佐使; the glossary is the translation layer.
- **For building** — the JSON is licensed CC BY-SA 4.0 and carries `termCode` + `alternateName` + `description`, so it can be consumed as a reference dataset with attribution.

## Common Mistakes

1. **Treating one Chinese word as one English word.** Context matters — 藿香 is the classic trap.
2. **Expecting all 249 terms on one page.** This is the index; the dictionary is the dataset and the glossaries.
3. **Guessing a translation from a single character.** 香 compounds (香炉, 香灰, 香几, 香盒) share a character but name different objects.

## The Author's Take

**Position:** Terminology is the entry fee to the whole topic — most reader confusion about Chinese incense is really a translation problem, not a knowledge problem.

**Reasoning:**
- A buyer who can resolve 沉香 → agarwood and 奇楠 → qínán is already past most of the confusion.
- The direction index is more useful than an alphabetical dump for a human reader.

*This is the author's editorial view — not a verified fact.*

## Verification Notes

- The 249-record count and per-term fields are drawn directly from `terminology.json` (version 1.4).
- Direction groupings and approximate counts are an editorial navigation aid, not dataset fields.
- The "one Chinese word ≠ one English word" principle is the dataset's own stated description.

---

## FAQ

### Q: How many terms are in the IncenseHub terminology dataset?
249. Each term is a DefinedTerm with a Chinese name (source of truth), a pinyin reading, a literal meaning, and a preferred English translation. The dataset is versioned (1.4), licensed CC BY-SA 4.0, and served from `data.incensehub.org/datasets/terminology.json`. See the [knowledge map](/blog/landeng-knowledge-map/) for the full dataset inventory.

### Q: Why does one Chinese word sometimes have multiple English meanings?
Because context determines the translation. 藿香 can mean agastache (*Agastache rugosa*) or patchouli (*Pogostemon cablin*), and the dataset records context alongside the translation rather than forcing a single gloss. This is why the glossary records Chinese as the source of truth and English as the agreed translation, not a one-to-one mapping.

### Q: Where do I find the full terminology list?
In two places: the machine-readable [terminology.json](https://data.incensehub.org/datasets/terminology.json) dataset (the canonical 249-term source), and the human-readable glossaries — [incense terminology glossary](/blog/incense-terminology-glossary/) for form vocabulary and [incense ingredients glossary](/blog/incense-ingredients-glossary/) for ingredient vocabulary. This page is the index between them.

### Q: What does 沉香 (chénxiāng) mean?
沉香 means "sinking fragrance" — agarwood. The name records the classical density test: the most resin-saturated pieces sink in water. The preferred English translation is "agarwood." See the [agarwood entity page](/ingredients/agarwood/) for the full treatment.

### Q: What is indirect-fire incense (隔火焚香)?
隔火焚香 (gé huǒ fén xiāng) means "incense across fire" — the indirect-fire method of warming material over buried charcoal so it releases aroma without combusting. It is the direct ancestor of Japanese kōdō. See the [gehuo fenxiang setup](/blog/gehuo-fenxiang-setup/) and the [terminology glossary](/blog/incense-terminology-glossary/).

### Q: What is the difference between 单方 and 复方?
单方 (dān fāng) is single-material appreciation — one wood or resin on its own. 复方 (fù fāng) is compound formula — blended incense (合香) proper, multiple materials composed on the 君臣佐使 (chief–minister–assistant–guide) principle. Traditional Chinese incense is usually 复方. See the [hexiang blending system](/blog/hexiang-blending-system/).

---

## Sources

- [IncenseHub Terminology dataset](https://data.incensehub.org/datasets/terminology.json) — the canonical 249-term source.
- The [terminology glossary](/blog/incense-terminology-glossary/) and [ingredients glossary](/blog/incense-ingredients-glossary/) — human-readable companions.
- [Xiang Cheng (香乘) full text on Wikisource](https://zh.wikisource.org/wiki/香乘) — classical terminology source.

## Related Resources

- [Incense Terminology Glossary](/blog/incense-terminology-glossary/)
- [Incense Ingredients Glossary](/blog/incense-ingredients-glossary/)
- [Incense Materials, Techniques & Forms](/blog/incense-materials-techniques-forms/)
- [IncenseHub Knowledge Map](/blog/landeng-knowledge-map/)

**Natural next step:** resolve form vocabulary in the [terminology glossary](/blog/incense-terminology-glossary/), or see how the whole taxonomy fits together in [materials, techniques & forms](/blog/incense-materials-techniques-forms/).
