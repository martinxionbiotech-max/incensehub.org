# Entity Inventory — 150 Ingredient Entities (Tier Classification)

> Audit-only. Populated from actual frontmatter + the internal-link map (`scripts/orphan_inbound.json`).

## Method

Tier assignment is **data-driven** from the current knowledge graph, using one measurable signal: **inbound internal-link count** (how many other pages link into each entity page — a proxy for editorial importance and current graph connectivity). No external search-volume data was used (none is available in-repo).

| Tier | Criterion | Count |
|---|---|---|
| **Tier 1** | ≥ 5 inbound internal links (current graph hubs) | **31** |
| **Tier 2** | 2–4 inbound internal links (moderate connectivity) | **54** |
| **Tier 3** | 0–1 inbound internal links (long-tail / weak connectivity) | **65** |

Inbound distribution across 150 entities: `12×3, 11×2, 10×3, 9×2, 8×2, 7×6, 6×6, 5×7, 4×8, 3×15, 2×32, 1×29, 0×36`.

Every entity carries the full frontmatter set (chinese / pinyin / scientificName / aroma / related) and a `## Sources` section (150/150 verified).

## Tier 1 — 31 highest-value entities (≥5 inbound links)

| Entity | 中文 | Scientific | Inbound |
|---|---|---|---|
| sandalwood | 檀香 | Santalum album | 12 |
| jasmine | 茉莉 | Jasminum sambac | 12 |
| osmanthus | 桂花 | Osmanthus fragrans | 12 |
| cinnamon | 桂皮 | Cinnamomum cassia | 11 |
| mugwort | 艾草 | Artemisia spp. | 11 |
| frankincense | 乳香 | Boswellia spp. | 10 |
| agastache-rugosa | 藿香 | Agastache rugosa | 10 |
| clove | 丁香 | Syzygium aromaticum | 10 |
| cedar | 雪松 | Cedrus spp. | 9 |
| rose | 玫瑰 | Rosa rugosa | 9 |
| benzoin | 安息香 | Styrax tonkinensis | 8 |
| plum-blossom | 梅花 | Prunus mume | 8 |
| agarwood | 沉香 | Aquilaria spp. | 7 |
| orange-peel | 陈皮 | Citrus reticulata | 7 |
| borneol | 龙脑 | Dryobalanops aromatica | 7 |
| pine-resin | 松香 | Pinus spp. | 7 |
| galangal | 高良姜 | Alpinia officinarum | 7 |
| fennel | 小茴香 | Foeniculum vulgare | 7 |
| myrrh | 没药 | Commiphora myrrha | 6 |
| champaca | 白兰花 | Michelia alba | 6 |
| cardamom | 白豆蔻 | Amomum kravanh | 6 |
| angelica | 白芷 | Angelica dahurica | 6 |
| mint | 薄荷 | Mentha haplocalyx | 6 |
| citron | 香橼 | Citrus medica | 6 |
| patchouli | 广藿香 | Pogostemon cablin | 5 |
| cypress-seed | 柏子 | Platycladus orientalis | 5 |
| rosemary | 迷迭香 | Salvia rosmarinus | 5 |
| musk | 麝香 | Moschus spp. | 5 |
| finger-citron | 佛手 | Citrus medica var. sarcodactylis | 5 |
| orris-root | 鸢尾根 | Iris germanica / I. pallida | 5 |
| vetiver | 岩兰草 | Chrysopogon zizanioides | 5 |

### Tier-1 flag: classical core under-linked in the current graph

Several classical Chinese-incense materials rank **below** their deserved tier purely due to weak internal linking (orphan status), not editorial value:

- **amber (琥珀)** — 0 inbound links. A major 合香 fixative/resin; fully written page, but no page links into it.
- **ambergris (龙涎香)** — 4 inbound. The canonical animal fixative (Tier-2 by raw count, Tier-1 by value).
- **onycha (甲香)** — 0 inbound. Classical marine fixative.
- **civet (灵猫香) / castoreum (海狸香) / shellac (紫草茸)** — 0–1 inbound. The animal/mineral fixative family is systematically under-linked.

These are carried as Tier-3/2 by the data-driven rule, but flagged for Tier-1 elevation + internal-link repair in the linking phase.

## Tier 2 — 54 moderate-connectivity entities (2–4 inbound)

`ambergris, peony, perilla, camphor, ginger, bergamot, spikenard-nardostachys, sand-ginger, red-sandalwood, michelia-figo, styrax-resin, calamus, star-anise, platycladus-leaves, thuja, long-pepper, coriander-seed, pomelo-peel, chrysanthemum, amomum-villosum, cubeb, artemisia-annua, bay-leaf, tsao-ko, atractylodes, angelica-sinensis, licorice, turmeric, costus, ligusticum, mulberry-leaf, neroli, borneol-oil, katsumadai, juniper, yulan-magnolia, gardenia, lemon, peru-balsam, labdanum, wintersweet, cumin, pine-needles, anise, kumquat, jasmine-grandiflorum, basil, citronella, spearmint, peppermint, pepper, litchi-husk, honeysuckle, magnolia-flower`

## Tier 3 — 65 long-tail entities (0–1 inbound)

`zedoary, schizonepeta, honey, blumea-balsamifera, civet, lavender, chamomile, cassia-twig, lemon-balm, litsea-cubeba, eupatorium, eupatorium-japonicum, asafoetida, torreya, ligusticum-chuanxiong, tarragon, bamboo-leaves, sophora-flower, linglingxiang, vanilla, jiangzhenxiang, thyme, dragons-blood, lotus-flower, sweetgum, sage, tree-peony, tuberose, aromatic-turmeric, aglaia, amber, apricot-kernel, asarum, banksia-rose, beeswax, bletilla, castoreum, copaiba, cyperus, daphne, dill, elsholtzia, eucalyptus, fenugreek, galbanum, ginkgo, grapefruit, lily-of-the-valley, mastic, mustard, nutmeg, onycha, orchid, oxyphylla, paicao, prickly-ash, quince, rue, schisandra, shellac, silk-tree, tree-peony-bark, valerian, violet, ylang-ylang`

## Notes

- **Entity depth vs tier:** the 31 Tier-1 entities are the current graph hubs and the natural subjects of deep editorial treatment (§8 depth standard). Tier-3 entities are long-tail and should not be force-expanded.
- **Data-site linkage:** all 150 entities have a matching record in `ingredients.json` (termCode = slug) and a `relationships.json` record (450 edges total). The dataset relationship layer is **more complete** than the frontmatter `related[]` layer — a graph-surfacing opportunity, not a data gap.
- **Link-map artifact:** the internal-link map contains 151 ingredient entries vs 150 files — one empty-slug entry (a trailing-slash link bug) should be fixed in the linking phase.

## G14 supplement — `related[]` ↔ `relationships.json` coverage (phase2/P2)

> Diff statistics only (§14). The 450-edge typed layer was **not** rewritten; the frontmatter layer received a minimal 5-line patch for clearly under-linked Tier-1 pages.

**Two layers, different roles (both legitimate):**

| Layer | Shape | Edge types | Scale |
|---|---|---|---|
| Frontmatter `related[]` | flat slug list (entity→entity) | untyped (implicit "related to") | 150 entities, avg 2.37 edges (min 2 / max 3 after P2) |
| `relationships.json` | typed graph | `category` (150) · `aroma` (280) · `comparison` (7) · `technique` (13) | 450 typed edges |

**Key finding — the layers are not 1:1 and should not be forced to match.** `relationships.json` edges are mostly **entity→taxonomy** (150 category + 280 aroma = 430 of 450 edges point at category/aroma entities, not other ingredients). Only **7 of 450** edges are entity→entity (the `comparison` edges), and those are self-referential by design (each `comparison` edge points at the entity's own comparison record). The frontmatter `related[]` layer is the only **entity→entity navigational** layer, and it is intentionally a curated short list (2–3 links), not a full graph dump.

**Coverage conclusion:** no 450-edge rewrite is warranted. The dataset is a typed taxonomy/derivation graph; frontmatter `related[]` is a curated cross-linking layer. They are complementary.

**Action taken (small):** 5 Tier-1 pages carried a single `related[]` entry (the minimum) — below the 2–3 norm for Tier-1 hubs. Each gained one reciprocal, data-grounded co-aroma/category peer (targets verified to already link back, so the graph stays symmetric):

| Entity | Added `related[]` entry | Basis |
|---|---|---|
| mugwort | `artemisia-annua` | same genus (Artemisia), shared herbal/camphoraceous aroma |
| clove | `cardamom` | shared spicy/warm aroma cluster |
| rose | `osmanthus` | shared sweet/floral aroma cluster |
| orange-peel | `pomelo-peel` | citrus peel family, shared citrus/bittersweet/woody aroma |
| myrrh | `benzoin` | balsamic resin family |

**Result:** `related[]` min count rises 1→2; no Tier-1 page below the 2-edge norm; all 5 additions are reciprocal (verified the target's own `related[]` already names the source).
