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


**Direct answer:** This page is the entry point to IncenseHub's **Chinese–English incense terminology** — a canonical glossary of **249 terms** spanning materials, grades, forms, techniques, tools, and cultural vocabulary. It is not a 249-entry dictionary printed here; it is a **structured index** that sorts the vocabulary by direction, samples the important terms, and points to the two places the full set lives: the machine-readable `terminology.json` dataset and the human-readable [terminology glossary](/blog/incense-terminology-glossary/).

## Key facts

- The dataset holds **249 terms**, each recorded as a structured record with a Chinese source term (the source of truth), a pinyin reading, a literal meaning, and a preferred English translation.
- The data is licensed **CC BY-SA 4.0**, carries a version (currently 1.4), and is served from `data.incensehub.org`.
- One Chinese word does not always map to one English word — the dataset records context rather than forcing a single gloss.
- The 249 terms group into roughly a dozen directions: materials, grades, aroma, forms, techniques, tools, texts, manufacturing, geography, culture, and adulteration.

## The Shape of a Single Record

**Direct answer:** Every one of the 249 terms is stored with the same four fields — a Chinese name, a pinyin reading, a literal meaning, and a preferred English translation — so the whole set can be read by a machine or a person alike.

Take 沉香 (chénxiāng), the agarwood term, as the worked example:

| Field | Value | The job it does |
|---|---|---|
| Chinese (name) | 沉香 | Anchors the term to its origin |
| Pinyin | chénxiāng | Makes it pronounceable and searchable across scripts |
| Literal meaning | sinking fragrance | Preserves the image the characters encode |
| Preferred English | agarwood | The agreed translation, not a literal gloss |

The four fields each carry a distinct job. The Chinese name pins the term to its source; the pinyin makes it speakable and searchable; the literal meaning keeps the imagery alive (沉香 literally reads "sinking fragrance," after the density test that separates resin-heavy wood); the preferred English is the working translation. Splitting them this way lets a reader move in either direction — from a Chinese label to its English sense, or from an English word back to the Chinese it came from.

## One Word, Several Senses

**Direct answer:** The dataset's central editorial rule is stated in its own description — *"One Chinese word does not always map to one English word"* — and the classic demonstration is 藿香 (huòxiāng), which can name two entirely different plants depending on context.

This is the most important idea on the page because it breaks the lazy assumption that a glossary is a two-column lookup table. The word 藿香 can mean agastache (*Agastache rugosa*) or patchouli (*Pogostemon cablin*). Which sense is meant depends on the recipe, the era, or the source text. Pin a single gloss onto the word and you quietly corrupt every reading that uses the other sense.

The dataset's remedy is to record context alongside the translation → the reader sees each plant name in its setting → the correct sense resolves instead of being guessed → downstream readers stop mistranslating classical recipes. Chinese is kept as the source of truth and English as the agreed translation, which is a deliberate stance: the Chinese term owns the identity, and the English rendering is a decision made about it, not a definition that replaces it. The [incense ingredients glossary](/blog/incense-ingredients-glossary/) applies the same principle on the ingredient side.

## A Map of the Directions

**Direct answer:** The 249 terms fall into a small set of natural directions — materials and grades, aroma and burn behaviour, forms, techniques, tools, texts, manufacturing, geography and trade, culture, and adulteration — and this overview samples each so you can find a path into the full dataset.

The table below is an editorial navigation aid rather than a dataset field. The counts are approximate groupings of the 249 records, offered to show where the vocabulary runs dense and where it runs thin.

| Direction | Approx. count | Representative terms |
|---|---|---|
| Materials and grades | ~90 | 沉香 (agarwood), 檀香 (sandalwood), 奇楠 (qínán), 沉水 (sinking grade) |
| Aroma and burn behaviour | ~28 | 甜 (sweet), 前调 (top note), 发烟量 (smoke output), 留香 (longevity) |
| Forms and formats | ~25 | 线香 (stick), 盘香 (coil), 塔香 (cone), 倒流香 (backflow cone) |
| Tools and vessels | ~27 | 香炉 (censer), 博山炉 (Boshan censer), 香匙 (spoon), 银叶 (silver leaf) |
| Techniques and practice | ~23 | 隔火焚香 (indirect-fire), 合香 (blending), 篆香 (seal incense) |
| Texts | ~7 | 香乘 (the Incense Compendium), 陈氏香谱 (a manual) |
| Manufacturing | ~8 | 打粉 (grinding), 筛粉 (sieving), 含水率 (moisture content) |
| Geography and trade | ~8 | 海南香 (Hainan agarwood), 安南香 (Vietnamese agarwood) |
| Culture and ritual | ~9 | 香市 (incense market), 香会 (incense gathering), 手炉 (hand warmer) |
| Adulteration and fakes | ~3 | 假货 (counterfeit), 高压灌油 (high-pressure oil injection) |

The shape of the table tells its own story. Materials and grades dominate because agarwood alone carries a deep grading vocabulary — sinking grade, the five colour grades of qínán, live-formed versus mature-formed, insect-bored. That density reflects a market where precise grading moves real money, so the language had to grow precise enough to keep up.

## Materials and Grades

**Direct answer:** The largest direction is ingredient names and the grading vocabulary built around agarwood, where a single material carries a dozen graded states and each state has its own term.

The ingredient names form the base layer: 沉香 (agarwood), 檀香 (sandalwood), 乳香 (frankincense), 没药 (myrrh), 麝香 (musk), 龙脑 (borneol), and 安息香 (benzoin). Around agarwood the grading terms stack upward: 沉水 (sinking grade), 奇楠 (qínán), the five colour grades 白奇楠 / 绿奇楠 / 黄奇楠 / 黑奇楠 / 紫奇楠, 半沉半浮 (semi-sinking), 生结 (live-formed), 熟结 (mature-formed), and 虫漏 (insect-bored). Each grade names a different resin-loading or formation path, and resolving one correctly is exactly where the "one word, several senses" principle pays off — 奇楠 is not interchangeable with ordinary agarwood, and 沉水 is a density claim rather than a flavour note. The [agarwood entity page](/ingredients/agarwood/) carries the full treatment.

## Aroma, Forms, and Techniques

**Direct answer:** The aroma vocabulary names how a burn feels, the form vocabulary names what shape the material takes, and the technique vocabulary names what the practitioner does — three layers a reader needs to keep apart.

The aroma and burn-behaviour terms describe the experience: 甜 (sweet), 辛 (pungent), 清 (clear), 凉 (cooling), 醇 (mellow), and 雅 (refined), plus the note structure 前调 / 中调 / 后调 (top / middle / base note) and the physical behaviour terms 发烟量 (smoke output), 燃烧速率 (burn rate), 留香 (longevity), and 定香剂 (fixative).

The form terms name the physical shapes: 线香 (stick), 盘香 (coil), 塔香 (cone), 倒流香 (backflow cone), 香粉 (powder), 香丸 (pill), 香饼 (cake), 香牌 (plaque), 香珠 (bead), 竹签香 (bamboo-core stick), 微烟香 (low-smoke), and 无烟香 (smokeless). These overlap the [forms dataset](/blog/incense-materials-techniques-forms/).

The technique terms name what the practitioner does: 隔火焚香 (indirect-fire), 篆香 (seal incense), 合香 (blending), 品香 (appreciation), 香道 (the way of incense), 空熏 (no-flame heating), 单方 (single-material), 复方 (compound formula), and 四般闲事 (the Four Leisure Arts). A reader who can hold these three layers apart — what it smells like, what shape it takes, what I do with it — already commands most of the working vocabulary.

## Tools, Vessels, Texts, and the Rest

**Direct answer:** Beyond materials and practice sit the supporting directions — tools and vessels, classical texts, manufacturing, geography and trade, culture, and the small but important adulteration list.

Tools and vessels name the apparatus of the incense table: 香炉 (censer), 博山炉 (Boshan censer), 宣德炉 (Xuande censer), 香匙 (spoon), 香箸 (chopsticks), 香盒 (box), 香灰 (ash), 香几 (stand), 香铲 (spatula), 银叶 (silver leaf), and 云母 (mica).

The remaining directions are smaller but not minor. **Texts** include 香乘 (the Incense Compendium), 本草 (materia medica), and the manuals 陈氏香谱 and 洪芻香谱. **Manufacturing** covers 打粉 (grinding), 筛粉 (sieving), 粒径 (particle size), 含水率 (moisture content), 粘粉 (binder powder), and 成型 (forming). **Geography and trade** names the source regions — 海南香 (Hainan agarwood), 安南香 (Vietnamese agarwood), 真腊 (Chenla), 占城 (Champa), 渤泥 (Borneo), and 番香 (foreign incense). **Culture and ritual** holds 香市 (incense market), 香会 (incense gathering), 香户 (incense household), 香婆 (incense woman), 香界 (incense realm), 熏笼 (fumigation cage), and 手炉 (hand warmer). The **adulteration** list — 假货 (counterfeit), 高压灌油 (high-pressure oil injection), and 泡药水 (chemical/dye soaking) — is tiny but valuable precisely because it names the fakes a buyer should watch for.

## Where the Full Set Lives

**Direct answer:** The complete 249-term vocabulary lives in two places — the machine-readable `terminology.json` dataset (the canonical source of truth) and the human-readable glossaries for forms and ingredients — and this page is the index that sits between them.

- **Machine-readable:** [Terminology dataset](https://data.incensehub.org/datasets/terminology.json) — 249 records, CC BY-SA 4.0, version 1.4.
- **Human-readable (forms):** [Incense Terminology Glossary](/blog/incense-terminology-glossary/) — the form and practice vocabulary in table form.
- **Human-readable (ingredients):** [Incense Ingredients Glossary](/blog/incense-ingredients-glossary/) — the ingredient vocabulary.

The dataset carries a version, a `dateModified`, and a changelog, so its history is auditable rather than a silent edit — a reader can see when a term changed and trace back to the change. The full eight-dataset inventory is on the [knowledge map](/blog/landeng-knowledge-map/).

## How to Put the Terminology to Work

**Direct answer:** Three practical uses — pin down a Chinese name's English translation before choosing, read a classical recipe or manual, or build a Chinese–English reference against the machine-readable dataset — and the direction index above is the fastest human entry point.

- **For choosing** — a label or recipe name such as 白奇楠 should resolve to "white qínán (agarwood grade)," not a guess; the glossary is the resolution table.
- **For reading** — classical manuals and 合香 recipes use 香道, 合香, 隔火焚香, and 君臣佐使; the glossary is the translation layer between the source and the reader.
- **For building** — the JSON is licensed CC BY-SA 4.0 and carries `termCode`, `alternateName`, and `description`, so it can be consumed as a reference dataset with attribution.

## Common Mistakes

1. **Treating one Chinese word as one English word.** Context decides the sense — 藿香 is the classic trap.
2. **Expecting all 249 terms on one page.** This is the index; the dictionary is the dataset and the two glossaries.
3. **Guessing a translation from a single character.** 香 compounds — 香炉, 香灰, 香几, 香盒 — share one character but name different objects.

## The Author's Take

**Position:** Terminology is the entry fee to the whole topic — most reader confusion about Chinese incense is a translation problem, not a knowledge problem.

**Reasoning:**

- A reader who can resolve 沉香 → agarwood and 奇楠 → qínán has already cleared most of the confusion; the rest is detail.
- The direction index serves a human better than an alphabetical dump would, because the vocabulary clusters around the things a reader actually does — choose, read, build.
- The "one word, several senses" principle is not a pedantic caveat; it is the difference between a glossary that helps and one that quietly misleads.

*This is the author's editorial view — not a verified fact.*

## Verification Notes

- The 249-record count and the per-term fields are drawn directly from `terminology.json` (version 1.4).
- Direction groupings and their approximate counts are an editorial navigation aid, not dataset fields.
- The "one Chinese word ≠ one English word" principle is the dataset's own stated description.

## Summary

- The terminology layer is a strategic asset: Chinese terms are the source of truth, and English is the agreed translation.
- 249 terms group into roughly a dozen directions, with materials and grades the densest.
- Every term carries four fields — Chinese name, pinyin, literal meaning, and preferred English.
- The full set lives in `terminology.json` and the two human-readable glossaries; this page is the index between them.
- One Chinese word does not always map to one English word, and the dataset records context rather than forcing a gloss.

## FAQ

### Q: How many terms are in the IncenseHub terminology dataset?
249. Each term is stored as a structured record with a Chinese name (the source of truth), a pinyin reading, a literal meaning, and a preferred English translation. The dataset is versioned (1.4), licensed CC BY-SA 4.0, and served from `data.incensehub.org/datasets/terminology.json`. See the [knowledge map](/blog/landeng-knowledge-map/) for the full dataset inventory.

### Q: Why does one Chinese word sometimes have multiple English meanings?
Because context determines the translation. The word 藿香 can mean agastache (*Agastache rugosa*) or patchouli (*Pogostemon cablin*), and the dataset records context alongside the translation rather than forcing a single gloss. This is why the glossary keeps Chinese as the source of truth and English as the agreed translation rather than a one-to-one mapping.

### Q: Where do I find the full terminology list?
In two places: the machine-readable [terminology.json](https://data.incensehub.org/datasets/terminology.json) dataset (the canonical 249-term source), and the human-readable glossaries — the [incense terminology glossary](/blog/incense-terminology-glossary/) for form vocabulary and the [incense ingredients glossary](/blog/incense-ingredients-glossary/) for ingredient vocabulary. This page is the index between them.

### Q: What does 沉香 (chénxiāng) mean?
沉香 means "sinking fragrance" — agarwood. The name records the classical density test: the most resin-saturated pieces sink in water. The preferred English translation is "agarwood." See the [agarwood entity page](/ingredients/agarwood/) for the full treatment.

### Q: What is indirect-fire incense (隔火焚香)?
隔火焚香 (gé huǒ fén xiāng) means "incense across fire" — the indirect-fire method of warming material over buried charcoal so it releases aroma without combusting. It is the direct ancestor of Japanese kōdō. See the [gehuo fenxiang setup](/blog/gehuo-fenxiang-setup/) and the [terminology glossary](/blog/incense-terminology-glossary/).

### Q: What is the difference between 单方 and 复方?
单方 (dān fāng) is single-material appreciation — one wood or resin on its own. 复方 (fù fāng) is compound formula — blended incense (合香) proper, with multiple materials composed on the 君臣佐使 (chief–minister–assistant–guide) principle. Traditional Chinese incense is usually 复方. See the [hexiang blending system](/blog/hexiang-blending-system/).

### Q: Can I reuse the terminology dataset in my own project?
Yes, under its license. The dataset is CC BY-SA 4.0, which permits reuse and adaptation as long as you attribute the source and share any derivative work under the same terms. Because each record carries structured fields — a `termCode`, `alternateName`, and `description` — it can be consumed as a reference dataset rather than scraped from prose. That reusability is the reason the terminology is stored as structured data instead of a flat list.

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
