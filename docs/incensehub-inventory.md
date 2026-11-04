# IncenseHub.org 内容清册（Batch A — Inventory & Disposition）

> 生成方式：对仓库只读分析（不修改任何内容）。范围：`src/content`（266 篇：ingredients 150 · concepts 1 · blog 115）＋ 非内容静态页（15：13 独立页 + 2 索引页）。总渲染页面 281（`dist`/sitemap 均 281，另 404）。


## 1. 结构总览

| 维度 | 值 |
|---|---|
| 内容集合 | `ingredients`（香材实体）、`concepts`（支柱概念，单篇 `/chinese-incense/`）、`blog`（知识文章/香方/工艺/文化） |
| 内容文件总数 | 266（ingredients 150 · concepts 1 · blog 115） |
| 非内容渲染页 | 15（13 独立静态页 + blog/ingredients 索引页；另 404） |
| 总渲染页面 | 281 |
| 站点配置域名 | `https://incensehub.org`（`astro.config.mjs` → 目标 `IncenseHub.org`） |
| 技术栈 | Astro 5 静态生成 + `@astrojs/sitemap`；`output: static` |
| 字数范围 | min 817 · max 4013 · 均值 2069 · 中位 2259 |
| 结构完整性 | 全部 266 篇均有 H2 分区；无空泛短页（<300 词：0 篇） |

## 2. 语言分布

**当前语言 = 英语（English-primary），中文术语为“源真值”内嵌注释。** 无纯中文页，无双语平行页——**无需翻译式语言转换策略**；需做的是术语规范化（中文名→英文统一 + 拼音标注一致性）。

| 语言 | 篇数 | 说明 |
|---|---|---|
| EN（纯英文正文） | 194 | 正文全英文，无中文字符 |
| MIX（英文正文 + 中文术语） | 72 | 正文英文，含少量中文名/引文（约 1–5% CJK），如 `沉香`、`檀香`、香乘引文 |
| ZH（纯中文） | 0 | 不存在 |

## 3. 与 incensehubdata 兄弟仓关系

`incensehubdata` 是**权威数据源**（唯一源），主仓通过 `scripts/sync-datasets.mjs` 幂等同步 8 个 `datasets/*.json` 到 `data/` 与 `public/data/`。数据站域名 `data.incensehub.org`（→ 目标 `data.incensehub.org`）。本批只分析不触碰数据层。


## 4. 处置分布汇总

| 处置 | 内容 .md 篇数 | 非内容页 | 合计 | 含义 |
|---|---|---|---|---|
| TRANSFORM · T1 | 19 | 1（首页 index） | 20 | 首批改造：最高搜索潜力 + 核心主题价值 |
| TRANSFORM · T2 | 140 | 1（about） | 141 | 第二批：次核心实体/工艺/香气/地域 |
| TRANSFORM · T3 | 72 | 0 | 72 | 第三批：长尾香材/香方/场景/文化 |
| KEEP | 21 | 7（两索引页 + 法律页×5） | 28 | 已达标：证据分层 + 无商业污染 |
| CUT | 14 | 6（商业转化页） | 20 | 降权重写/合并标注（不删页不换 URL） |
| **合计** | **266** | **15** | **281** | — |

## 5. 重复检测（页间相似度 top）

Jaccard（正文去图/去链接/去表格后词集相似度）。高相似主要来自**实体页共用模板骨架**（不属真正抄袭），真正需合并的是**对比簇**与**OEM 簇**：

| 相似度 | 页面 A | 页面 B | 判定 |
|---|---|---|---|
| 0.650 | champaca | gardenia | 模板骨架相似 → T2 差异化加深（非 CUT） |
| 0.618 | galangal | ginger | 同上 |
| 0.618 | citron | finger-citron | 同上 |
| 0.610 | agarwood-vs-frankincense | sandalwood-vs-frankincense | **对比簇重叠 → 合并/加区分度** |
| 0.496 | frankincense-vs-myrrh | sandalwood-vs-frankincense | 对比簇重叠 |
| 0.493 | agarwood-vs-frankincense | agarwood-vs-sandalwood | 对比簇重叠 |
| 0.483 | oem-private-label-guide | oem-vs-private-label | **OEM 簇重复 → 合并为单篇**（均 CUT） |

## 6. 商业/营销段落命中

| 类型 | 命中数 | 说明 |
|---|---|---|
| 硬转化 CTA（request a sample/quote、get a quote、MOQ、minimum order、lead time、buy now） | 20 篇（12 纯 B2B CUT + 8 知识页内嵌） | CUT 剥离后删页；知识页剥离 CTA 保留知识 |
| 商业框架小节（Our Industry View / What Buyers Should Look For / Modern Commercial Applications） | 157 篇（ingredients 150 = **实体页 100%**；blog 7） | 实体模板**系统性内嵌**商业框架——改造核心：转“买家/批发/OEM”框架为“鉴别/质量/应用”中性知识框架 |
| 纯商业转化静态页 | 6 页 | incense-manufacturer / oem / private-label / request-a-quote / wholesale / contact → CUT |

---

## 7. 全量清册（逐篇处置）

> Disposition 列：KEEP（已达标）/ TRANSFORM·T1/T2/T3（按优先级改造）/ CUT（降权重写或合并，不删页不换 URL）。


### ingredients（150 篇）

| # | 处置 | URL | 题名 | 字数 | 语言 | H2 | 主题/栏目 |
|---|---|---|---|---|---|---|---|
| 1 | KEEP | `/ingredients/agarwood/` | Agarwood (沉香) — Grades & Fakes | 4013 | EN | 25 | informational |
| 2 | KEEP | `/ingredients/ambergris/` | Ambergris (龙涎香) — Animal Fixative | 2580 | EN | 17 | informational |
| 3 | KEEP | `/ingredients/benzoin/` | Benzoin (安息香) — Sweet Resin | 2638 | EN | 23 | informational |
| 4 | KEEP | `/ingredients/borneol/` | Borneol (龙脑) — Dragon Brain Aromatic | 2555 | EN | 22 | informational |
| 5 | KEEP | `/ingredients/camphor/` | Camphor (樟木) — Aromatic Laurel Wood | 2543 | EN | 21 | informational |
| 6 | KEEP | `/ingredients/cedar/` | Cedar (雪松) — Woody Note | 3428 | EN | 24 | informational |
| 7 | KEEP | `/ingredients/dragons-blood/` | Dragon's Blood (血竭) — Red Resin | 2401 | EN | 19 | informational |
| 8 | KEEP | `/ingredients/frankincense/` | Frankincense (乳香) — Ritual Resin | 2702 | EN | 23 | informational |
| 9 | KEEP | `/ingredients/jiangzhenxiang/` | Jiangzhenxiang (降真香) — Resinous Wood | 2726 | MIX | 21 | informational |
| 10 | KEEP | `/ingredients/musk/` | Musk (麝香) — Historical Animal Fixative | 2850 | EN | 18 | informational |
| 11 | KEEP | `/ingredients/myrrh/` | Myrrh (没药) — Bitter Resin | 2601 | EN | 22 | informational |
| 12 | KEEP | `/ingredients/red-sandalwood/` | Red Sandalwood (紫檀) — Crimson Dye Wood | 2882 | EN | 21 | informational |
| 13 | KEEP | `/ingredients/sandalwood/` | Sandalwood (檀香) — Use vs Evidence | 2934 | EN | 22 | informational |
| 14 | TRANSFORM · T2 | `/ingredients/agastache-rugosa/` | Agastache (藿香) — Aromatic Herb | 2383 | MIX | 19 | informational |
| 15 | TRANSFORM · T2 | `/ingredients/amber/` | Amber (琥珀) — Fossil Resin | 2185 | EN | 18 | informational |
| 16 | TRANSFORM · T2 | `/ingredients/amomum-villosum/` | Amomum villosum (砂仁) | 2468 | MIX | 20 | informational |
| 17 | TRANSFORM · T2 | `/ingredients/angelica/` | Angelica (白芷) — Aromatic Root | 2413 | EN | 23 | informational |
| 18 | TRANSFORM · T2 | `/ingredients/angelica-sinensis/` | Dong Quai (当归) — Aromatic Root | 2577 | MIX | 22 | informational |
| 19 | TRANSFORM · T2 | `/ingredients/anise/` | Anise (茴芹) — Sweet Licorice Spice | 2688 | EN | 19 | informational |
| 20 | TRANSFORM · T2 | `/ingredients/apricot-kernel/` | Apricot Kernel (杏仁) — Fragrant Seed | 2558 | EN | 20 | informational |
| 21 | TRANSFORM · T2 | `/ingredients/artemisia-annua/` | Sweet Wormwood (青蒿) | 2497 | MIX | 22 | informational |
| 22 | TRANSFORM · T2 | `/ingredients/asarum/` | Asarum (细辛) — Pungent Root | 2641 | MIX | 20 | informational |
| 23 | TRANSFORM · T2 | `/ingredients/atractylodes/` | Atractylodes (苍术) — Herbal Root | 2716 | EN | 22 | informational |
| 24 | TRANSFORM · T2 | `/ingredients/bamboo-leaves/` | Bamboo Leaves (竹叶) — Fresh Green Leaf | 2111 | MIX | 18 | informational |
| 25 | TRANSFORM · T2 | `/ingredients/basil/` | Basil (罗勒) — Herb of Lan Xiang | 2589 | MIX | 20 | informational |
| 26 | TRANSFORM · T2 | `/ingredients/bay-leaf/` | Bay Leaf (月桂叶) — Camphoraceous Herb | 2293 | EN | 19 | informational |
| 27 | TRANSFORM · T2 | `/ingredients/beeswax/` | Beeswax (蜂蜡) — Wax Binder | 2186 | MIX | 18 | informational |
| 28 | TRANSFORM · T2 | `/ingredients/bergamot/` | Bergamot (佛手柑) — Citrus Essential Oil | 2467 | EN | 19 | informational |
| 29 | TRANSFORM · T2 | `/ingredients/bletilla/` | Bletilla (白及) — Incense Binder Root | 2331 | EN | 18 | informational |
| 30 | TRANSFORM · T2 | `/ingredients/borneol-oil/` | Borneol Oil (龙脑油) — Aromatic Extract | 2717 | MIX | 24 | informational |
| 31 | TRANSFORM · T2 | `/ingredients/calamus/` | Calamus (菖蒲) — Spicy Rhizome | 2799 | EN | 23 | informational |
| 32 | TRANSFORM · T2 | `/ingredients/cardamom/` | Cardamom (白豆蔻) — White Cardamom | 2480 | MIX | 23 | informational |
| 33 | TRANSFORM · T2 | `/ingredients/cassia-twig/` | Cassia Twig (桂枝) — Aromatic Branch | 2200 | MIX | 19 | informational |
| 34 | TRANSFORM · T2 | `/ingredients/castoreum/` | Castoreum (海狸香) | 2738 | EN | 20 | informational |
| 35 | TRANSFORM · T2 | `/ingredients/champaca/` | Champaca (白兰花) — White Champaca | 2536 | EN | 22 | informational |
| 36 | TRANSFORM · T2 | `/ingredients/chrysanthemum/` | Chrysanthemum (菊花) — Herbal Floral | 2908 | EN | 23 | informational |
| 37 | TRANSFORM · T2 | `/ingredients/cinnamon/` | Cinnamon (桂皮) — Cassia Distinction | 2740 | EN | 22 | informational |
| 38 | TRANSFORM · T2 | `/ingredients/citron/` | Citron (香橼) — Aromatic Citrus Fruit | 2395 | EN | 19 | informational |
| 39 | TRANSFORM · T2 | `/ingredients/citronella/` | Citronella (香茅) — Lemongrass | 2591 | EN | 22 | informational |
| 40 | TRANSFORM · T2 | `/ingredients/civet/` | Civet (灵猫香) | 3222 | EN | 21 | informational |
| 41 | TRANSFORM · T2 | `/ingredients/clove/` | Clove (丁香) — Warm Spice Note | 2708 | EN | 22 | informational |
| 42 | TRANSFORM · T2 | `/ingredients/copaiba/` | Copaiba (古巴香脂) — Amazon Resin | 2110 | EN | 17 | informational |
| 43 | TRANSFORM · T2 | `/ingredients/coriander-seed/` | Coriander Seed (芫荽籽) — Citrus Spice | 2376 | EN | 18 | informational |
| 44 | TRANSFORM · T2 | `/ingredients/cubeb/` | Cubeb (荜澄茄) — Peppery Spice | 2052 | EN | 22 | informational |
| 45 | TRANSFORM · T2 | `/ingredients/cumin/` | Cumin (孜然) — Western Regions Spice | 2603 | EN | 19 | informational |
| 46 | TRANSFORM · T2 | `/ingredients/cypress-seed/` | Cypress Seed (柏子) — Scholar's Incense | 2290 | MIX | 22 | informational |
| 47 | TRANSFORM · T2 | `/ingredients/dill/` | Dill (莳萝) — Aromatic Spice Herb | 2539 | MIX | 21 | informational |
| 48 | TRANSFORM · T2 | `/ingredients/elsholtzia/` | Elsholtzia (香薷) — Aromatic Herb | 2567 | MIX | 19 | informational |
| 49 | TRANSFORM · T2 | `/ingredients/eucalyptus/` | Eucalyptus (桉叶) — Camphoraceous Leaf | 2626 | EN | 21 | informational |
| 50 | TRANSFORM · T2 | `/ingredients/fennel/` | Fennel (小茴香) — Anise-Sweet Spice | 2554 | EN | 22 | informational |
| 51 | TRANSFORM · T2 | `/ingredients/finger-citron/` | Finger Citron (佛手) | 2485 | EN | 19 | informational |
| 52 | TRANSFORM · T2 | `/ingredients/galangal/` | Galangal (高良姜) — Ginger Root Spice | 2446 | EN | 22 | informational |
| 53 | TRANSFORM · T2 | `/ingredients/galbanum/` | Galbanum (白松香) — Green Balsamic Resin | 2472 | EN | 20 | informational |
| 54 | TRANSFORM · T2 | `/ingredients/gardenia/` | Gardenia (栀子花) — Creamy White Floral | 2524 | EN | 22 | informational |
| 55 | TRANSFORM · T2 | `/ingredients/ginger/` | Dried Ginger (干姜) — Warming Spice | 2436 | EN | 22 | informational |
| 56 | TRANSFORM · T2 | `/ingredients/ginkgo/` | Ginkgo Nut (银杏) — Living-Fossil Seed | 2445 | EN | 19 | informational |
| 57 | TRANSFORM · T2 | `/ingredients/grapefruit/` | Grapefruit (葡萄柚) | 2828 | EN | 21 | informational |
| 58 | TRANSFORM · T2 | `/ingredients/honey/` | Honey (蜂蜜) — Blending Binder | 2549 | MIX | 19 | informational |
| 59 | TRANSFORM · T2 | `/ingredients/honeysuckle/` | Honeysuckle (金银花) — Sweet Floral | 2339 | EN | 22 | informational |
| 60 | TRANSFORM · T2 | `/ingredients/jasmine/` | Jasmine (茉莉花) — Sweet Floral | 2969 | EN | 23 | informational |
| 61 | TRANSFORM · T2 | `/ingredients/jasmine-grandiflorum/` | Spanish Jasmine (素馨) | 2399 | MIX | 19 | informational |
| 62 | TRANSFORM · T2 | `/ingredients/juniper/` | Juniper (杜松) — Modern Aromatic Wood | 2450 | EN | 21 | informational |
| 63 | TRANSFORM · T2 | `/ingredients/katsumadai/` | Katsumadai (草豆蔻) — Alpinia Seed | 2167 | MIX | 19 | informational |
| 64 | TRANSFORM · T2 | `/ingredients/kumquat/` | Kumquat (金橘) — Fragrant Citrus Fruit | 2437 | MIX | 19 | informational |
| 65 | TRANSFORM · T2 | `/ingredients/labdanum/` | Labdanum (岩蔷薇) | 2769 | EN | 20 | informational |
| 66 | TRANSFORM · T2 | `/ingredients/lavender/` | Lavender (薰衣草) — Floral Herb | 2363 | EN | 20 | informational |
| 67 | TRANSFORM · T2 | `/ingredients/lemon/` | Lemon (柠檬) | 2633 | EN | 20 | informational |
| 68 | TRANSFORM · T2 | `/ingredients/licorice/` | Licorice (甘草) — Sweetening Root | 2714 | EN | 20 | informational |
| 69 | TRANSFORM · T2 | `/ingredients/ligusticum/` | Ligusticum (藁本) — Aromatic Root Herb | 2533 | EN | 23 | informational |
| 70 | TRANSFORM · T2 | `/ingredients/ligusticum-chuanxiong/` | Chuanxiong (川芎) — Aromatic Root | 2648 | MIX | 20 | informational |
| 71 | TRANSFORM · T2 | `/ingredients/lily-of-the-valley/` | Lily of the Valley (铃兰) | 2633 | EN | 19 | informational |
| 72 | TRANSFORM · T2 | `/ingredients/litchi-husk/` | Litchi Husk (荔枝壳) — Fruity Peel | 2798 | EN | 20 | informational |
| 73 | TRANSFORM · T2 | `/ingredients/long-pepper/` | Long Pepper (荜茇) — Warming Spice | 2206 | EN | 18 | informational |
| 74 | TRANSFORM · T2 | `/ingredients/lotus-flower/` | Lotus Flower (莲花) | 2683 | EN | 22 | informational |
| 75 | TRANSFORM · T2 | `/ingredients/magnolia-flower/` | Magnolia Flower (辛夷) — Spicy Floral | 2540 | EN | 19 | informational |
| 76 | TRANSFORM · T2 | `/ingredients/mastic/` | Mastic (玛蹄脂) — Fresh Piney Resin | 2731 | EN | 20 | informational |
| 77 | TRANSFORM · T2 | `/ingredients/mint/` | Mint (薄荷) — Cooling Herb | 2664 | EN | 23 | informational |
| 78 | TRANSFORM · T2 | `/ingredients/mugwort/` | Mugwort (艾草) — Chinese Tradition | 2555 | EN | 22 | informational |
| 79 | TRANSFORM · T2 | `/ingredients/mulberry-leaf/` | Mulberry Leaf (桑叶) | 2484 | EN | 20 | informational |
| 80 | TRANSFORM · T2 | `/ingredients/mustard/` | Mustard Seed (芥子) — Pungent Spice Seed | 2399 | EN | 18 | informational |
| 81 | TRANSFORM · T2 | `/ingredients/neroli/` | Neroli (橙花) — Orange Blossom | 2189 | EN | 16 | informational |
| 82 | TRANSFORM · T2 | `/ingredients/nutmeg/` | Nutmeg (肉豆蔻) — Warm Spice Seed | 2099 | EN | 22 | informational |
| 83 | TRANSFORM · T2 | `/ingredients/onycha/` | Onycha (甲香) | 2655 | EN | 19 | informational |
| 84 | TRANSFORM · T2 | `/ingredients/orange-peel/` | Orange Peel (陈皮) — Aged Peel | 2928 | EN | 24 | informational |
| 85 | TRANSFORM · T2 | `/ingredients/orchid/` | Orchid (兰花) — Cymbidium Flower | 2025 | MIX | 15 | informational |
| 86 | TRANSFORM · T2 | `/ingredients/orris-root/` | Orris Root (鸢尾根) — Perfume Fixative | 2478 | EN | 23 | informational |
| 87 | TRANSFORM · T2 | `/ingredients/osmanthus/` | Osmanthus (桂花) — Sweet Floral | 2692 | EN | 24 | informational |
| 88 | TRANSFORM · T2 | `/ingredients/oxyphylla/` | Sharp-Leaf Galangal (益智仁) | 2298 | MIX | 19 | informational |
| 89 | TRANSFORM · T2 | `/ingredients/patchouli/` | Patchouli (广藿香) — Earthy Leaf | 2629 | EN | 21 | informational |
| 90 | TRANSFORM · T2 | `/ingredients/peony/` | Peony (芍药) | 2143 | MIX | 16 | informational |
| 91 | TRANSFORM · T2 | `/ingredients/pepper/` | Pepper (胡椒) — Warm Spice | 2619 | EN | 21 | informational |
| 92 | TRANSFORM · T2 | `/ingredients/peppermint/` | Peppermint (胡椒薄荷) — Sharp Cooling Mint | 2143 | EN | 16 | informational |
| 93 | TRANSFORM · T2 | `/ingredients/perilla/` | Perilla (紫苏) — Aromatic Herb | 2587 | EN | 19 | informational |
| 94 | TRANSFORM · T2 | `/ingredients/peru-balsam/` | Peru Balsam (秘鲁香脂) — Sweet Resin | 2427 | EN | 18 | informational |
| 95 | TRANSFORM · T2 | `/ingredients/pine-needles/` | Pine Needles (松针) | 2507 | MIX | 20 | informational |
| 96 | TRANSFORM · T2 | `/ingredients/pine-resin/` | Pine Resin (松香) — Woody Resin | 2858 | EN | 23 | informational |
| 97 | TRANSFORM · T2 | `/ingredients/platycladus-leaves/` | Arborvitae Leaves (侧柏叶) | 2446 | MIX | 22 | informational |
| 98 | TRANSFORM · T2 | `/ingredients/plum-blossom/` | Plum Blossom (梅花) — Winter Flower | 2586 | MIX | 22 | informational |
| 99 | TRANSFORM · T2 | `/ingredients/pomelo-peel/` | Pomelo Peel (柚皮) — Citrus Peel | 2763 | EN | 20 | informational |
| 100 | TRANSFORM · T2 | `/ingredients/prickly-ash/` | Sichuan Pepper (蜀椒) — Prickly Ash | 2542 | MIX | 19 | informational |
| 101 | TRANSFORM · T2 | `/ingredients/quince/` | Quince (木瓜) — Fragrant Scholar's Fruit | 2467 | MIX | 19 | informational |
| 102 | TRANSFORM · T2 | `/ingredients/rose/` | Rose (玫瑰) — Sweet Floral | 2654 | EN | 22 | informational |
| 103 | TRANSFORM · T2 | `/ingredients/rosemary/` | Rosemary (迷迭香) — Camphoraceous Herb | 2357 | EN | 19 | informational |
| 104 | TRANSFORM · T2 | `/ingredients/sage/` | Sage (鼠尾草) — Savory Herb | 2104 | EN | 18 | informational |
| 105 | TRANSFORM · T2 | `/ingredients/sand-ginger/` | Sand Ginger (山柰) — Aromatic Rhizome | 2519 | EN | 20 | informational |
| 106 | TRANSFORM · T2 | `/ingredients/schizonepeta/` | Schizonepeta (荆芥) — Aromatic Herb | 1838 | MIX | 15 | informational |
| 107 | TRANSFORM · T2 | `/ingredients/shellac/` | Shellac (紫草茸) — Lac Resin | 2425 | MIX | 19 | informational |
| 108 | TRANSFORM · T2 | `/ingredients/spearmint/` | Spearmint (留兰香) — Sweet Cooling Mint | 2185 | EN | 16 | informational |
| 109 | TRANSFORM · T2 | `/ingredients/star-anise/` | Star Anise (八角) — Culinary Spice | 2673 | EN | 23 | informational |
| 110 | TRANSFORM · T2 | `/ingredients/styrax-resin/` | Storax (苏合香) — Imported Resin | 2514 | MIX | 20 | informational |
| 111 | TRANSFORM · T2 | `/ingredients/sweetgum/` | Sweetgum (枫香) — Sweet Resin | 2672 | MIX | 20 | informational |
| 112 | TRANSFORM · T2 | `/ingredients/thuja/` | Thuja (崖柏) — Fragrant Endemic Conifer | 3085 | EN | 22 | informational |
| 113 | TRANSFORM · T2 | `/ingredients/thyme/` | Thyme (百里香) — Culinary Herb | 2082 | EN | 18 | informational |
| 114 | TRANSFORM · T2 | `/ingredients/torreya/` | Torreya (香榧) — Fragrant Nut Seed | 2173 | MIX | 18 | informational |
| 115 | TRANSFORM · T2 | `/ingredients/tree-peony/` | Tree Peony (牡丹) — Floral King | 2246 | MIX | 19 | informational |
| 116 | TRANSFORM · T2 | `/ingredients/tsao-ko/` | Tsaoko (草果) — Smoky Aromatic Fruit | 2356 | MIX | 21 | informational |
| 117 | TRANSFORM · T2 | `/ingredients/tuberose/` | Tuberose (晚香玉) — Night-Fragrant Flower | 2071 | EN | 15 | informational |
| 118 | TRANSFORM · T2 | `/ingredients/valerian/` | Valerian (缬草) — Earthy Root | 2321 | EN | 19 | informational |
| 119 | TRANSFORM · T2 | `/ingredients/vetiver/` | Vetiver (岩兰草) — Earthy Root Note | 2344 | EN | 21 | informational |
| 120 | TRANSFORM · T2 | `/ingredients/violet/` | Violet (紫罗兰) — Powdery Flower | 2331 | EN | 19 | informational |
| 121 | TRANSFORM · T2 | `/ingredients/wintersweet/` | Wintersweet (蜡梅) — Winter Floral | 2452 | EN | 19 | informational |
| 122 | TRANSFORM · T2 | `/ingredients/ylang-ylang/` | Ylang-Ylang (依兰) — Tropical Flower | 2420 | EN | 20 | informational |
| 123 | TRANSFORM · T3 | `/ingredients/aglaia/` | Aglaia (米仔兰) | 1971 | MIX | 15 | informational |
| 124 | TRANSFORM · T3 | `/ingredients/aromatic-turmeric/` | Aromatic Turmeric (郁金) — Wild Turmeric | 2477 | MIX | 22 | informational |
| 125 | TRANSFORM · T3 | `/ingredients/asafoetida/` | Asafoetida (阿魏) | 2190 | EN | 17 | informational |
| 126 | TRANSFORM · T3 | `/ingredients/banksia-rose/` | Banksia Rose (木香花) | 2722 | MIX | 20 | informational |
| 127 | TRANSFORM · T3 | `/ingredients/blumea-balsamifera/` | Blumea Balsamifera (艾纳香) | 2130 | MIX | 15 | informational |
| 128 | TRANSFORM · T3 | `/ingredients/chamomile/` | Chamomile (洋甘菊) — Apple-Scented Flower | 2259 | MIX | 20 | informational |
| 129 | TRANSFORM · T3 | `/ingredients/costus/` | Costus (木香) — Earthy Root | 2503 | EN | 20 | informational |
| 130 | TRANSFORM · T3 | `/ingredients/cyperus/` | Cyperus (香附子) — Sedge Root | 2324 | MIX | 19 | informational |
| 131 | TRANSFORM · T3 | `/ingredients/daphne/` | Daphne (瑞香) — Winter Daphne | 1961 | MIX | 14 | informational |
| 132 | TRANSFORM · T3 | `/ingredients/eupatorium/` | Eupatorium (佩兰) — Fragrant Herb | 2527 | EN | 22 | informational |
| 133 | TRANSFORM · T3 | `/ingredients/eupatorium-japonicum/` | Zelan (泽兰) — Fragrant Eupatorium Herb | 2332 | MIX | 19 | informational |
| 134 | TRANSFORM · T3 | `/ingredients/fenugreek/` | Fenugreek (葫芦巴) — Sweet Spice Seed | 2402 | MIX | 19 | informational |
| 135 | TRANSFORM · T3 | `/ingredients/lemon-balm/` | Lemon Balm (香蜂草) — Lemony Mint Herb | 2589 | EN | 20 | informational |
| 136 | TRANSFORM · T3 | `/ingredients/linglingxiang/` | Linglingxiang (零陵香) — Sweet Herb | 2623 | MIX | 19 | informational |
| 137 | TRANSFORM · T3 | `/ingredients/litsea-cubeba/` | Mountain Pepper (山鸡椒) — Litsea Cubeba | 2632 | EN | 20 | informational |
| 138 | TRANSFORM · T3 | `/ingredients/michelia-figo/` | Banana Shrub (含笑花) — Michelia Figo | 2015 | MIX | 15 | informational |
| 139 | TRANSFORM · T3 | `/ingredients/paicao/` | Paicao (排草) — Aromatic Herb | 2445 | MIX | 19 | informational |
| 140 | TRANSFORM · T3 | `/ingredients/rue/` | Rue (芸香) — Bitter Aromatic Herb | 2775 | MIX | 20 | informational |
| 141 | TRANSFORM · T3 | `/ingredients/schisandra/` | Schisandra (五味子) — Five-Flavor Berry | 2708 | MIX | 21 | informational |
| 142 | TRANSFORM · T3 | `/ingredients/silk-tree/` | Silk Tree Flower (合欢花) | 2375 | MIX | 19 | informational |
| 143 | TRANSFORM · T3 | `/ingredients/sophora-flower/` | Sophora Flower (槐花) — Sweet Blossom | 2418 | MIX | 20 | informational |
| 144 | TRANSFORM · T3 | `/ingredients/spikenard-nardostachys/` | Spikenard (甘松) — Himalayan Root | 2536 | EN | 23 | informational |
| 145 | TRANSFORM · T3 | `/ingredients/tarragon/` | Tarragon (龙蒿) — Anise-Like Artemisia | 2413 | EN | 16 | informational |
| 146 | TRANSFORM · T3 | `/ingredients/tree-peony-bark/` | Tree Peony Bark (牡丹皮) — Root Bark | 2578 | MIX | 20 | informational |
| 147 | TRANSFORM · T3 | `/ingredients/turmeric/` | Turmeric (姜黄) — Earthy Rhizome | 2388 | EN | 19 | informational |
| 148 | TRANSFORM · T3 | `/ingredients/vanilla/` | Vanilla Bean (香草荚) — Fragrant Pod | 2648 | EN | 21 | informational |
| 149 | TRANSFORM · T3 | `/ingredients/yulan-magnolia/` | Yulan Magnolia (玉兰) | 2402 | EN | 19 | informational |
| 150 | TRANSFORM · T3 | `/ingredients/zedoary/` | Zedoary (莪术) — Medicinal Rhizome | 2559 | MIX | 22 | informational |


### concepts（1 篇）

| # | 处置 | URL | 题名 | 字数 | 语言 | H2 | 主题/栏目 |
|---|---|---|---|---|---|---|---|
| 1 | KEEP | `/chinese-incense/` | What Is Chinese Incense? History, Types & 香道 | 1262 | MIX | 11 | informational |


### blog（115 篇）

| # | 处置 | URL | 题名 | 字数 | 语言 | H2 | 主题/栏目 |
|---|---|---|---|---|---|---|---|
| 1 | KEEP | `/blog/chinese-vs-japanese-incense/` | Chinese vs Japanese Incense: 合香 and Kōdō Compared | 2251 | EN | 16 | P8 — Regional Incense Traditions |
| 2 | KEEP | `/blog/history-of-chinese-incense/` | History of Chinese Incense: Shang to Revival | 1603 | MIX | 13 | P1 — Chinese Incense 101 |
| 3 | KEEP | `/blog/japanese-incense-kodo/` | Japanese Incense & Kōdō (香道): The Art From China | 2196 | EN | 17 | P8 — Regional Incense Traditions |
| 4 | KEEP | `/blog/landeng-editorial-methodology/` | How IncenseHub Researches Chinese Incense | 1931 | EN | 9 | Editorial & Data |
| 5 | KEEP | `/blog/landeng-knowledge-map/` | IncenseHub Knowledge Map: Entities, Datasets & Policies | 1238 | EN | 8 | Editorial & Data |
| 6 | KEEP | `/blog/what-is-chinese-incense/` | What Is Chinese Incense? 香 (Xiāng) | 2770 | EN | 19 | P1 — Chinese Incense 101 |
| 7 | KEEP | `/blog/xiangpu-incense-manuals/` | 香谱 Incense Manuals: Complete, Rarely Translated | 973 | MIX | 10 | P1 — Chinese Incense 101 |
| 8 | TRANSFORM · T1 | `/blog/agarwood-grading-guide/` | Agarwood Grading: 沉香, 沉水 & 奇楠 | 2115 | MIX | 18 | P2 — Scent & Ingredient Guide |
| 9 | TRANSFORM · T1 | `/blog/agarwood-incense/` | Agarwood Incense (沉香): Grading & Spotting Fakes | 2559 | EN | 19 | P2 — Scent & Ingredient Guide |
| 10 | TRANSFORM · T1 | `/blog/agarwood-powder-vs-chips/` | Agarwood Powder vs Chips: Appreciation vs Incense Making | 2246 | EN | 15 | P2 — Scent & Ingredient Guide |
| 11 | TRANSFORM · T1 | `/blog/agarwood-vs-frankincense/` | Agarwood vs Frankincense: Wood and Resin Compared | 2162 | EN | 16 | P2 — Scent & Ingredient Guide |
| 12 | TRANSFORM · T1 | `/blog/agarwood-vs-sandalwood/` | Agarwood vs Sandalwood: The Two Reference Woods Compared | 2229 | EN | 18 | P2 — Scent & Ingredient Guide |
| 13 | TRANSFORM · T1 | `/blog/borneol-vs-camphor/` | Borneol vs Camphor: Two Cooling Crystals, Different Plants | 2141 | EN | 16 | P2 — Scent & Ingredient Guide |
| 14 | TRANSFORM · T1 | `/blog/chinese-vs-indian-incense/` | Chinese vs Indian Incense: 合香 and Agarbatti Compared | 2168 | EN | 16 | P8 — Regional Incense Traditions |
| 15 | TRANSFORM · T1 | `/blog/frankincense-incense/` | Frankincense Incense (乳香): A Focusing Resin | 1760 | EN | 13 | P2 — Scent & Ingredient Guide |
| 16 | TRANSFORM · T1 | `/blog/frankincense-vs-myrrh/` | Frankincense vs Myrrh: The Two Resins Compared | 2164 | EN | 17 | P2 — Scent & Ingredient Guide |
| 17 | TRANSFORM · T1 | `/blog/hexiang-blending-system/` | The 合香 Blending System: Composed Like a Formula | 1987 | MIX | 15 | P10 — Incense Craft & Materials |
| 18 | TRANSFORM · T1 | `/blog/incense-authentication-database/` | Incense Authentication: Fake Agarwood & Resin | 963 | EN | 10 | P10 — Incense Craft & Materials |
| 19 | TRANSFORM · T1 | `/blog/incense-material-comparison-matrix/` | Incense Material Comparison Matrix: 7 Classics | 936 | EN | 8 | P2 — Scent & Ingredient Guide |
| 20 | TRANSFORM · T1 | `/blog/incense-substitution-cross-reference/` | Incense Substitution Cross-Reference: Label Traps | 1964 | EN | 18 | P5 — Buying & Selection |
| 21 | TRANSFORM · T1 | `/blog/natural-vs-synthetic-incense/` | Natural vs Synthetic Incense: Telling Them Apart | 1347 | EN | 13 | P5 — Buying & Selection |
| 22 | TRANSFORM · T1 | `/blog/qinan-buying-authentication/` | Buying 奇楠 (Qinan): What to Check Before You Pay | 1138 | EN | 9 | P10 — Incense Craft & Materials |
| 23 | TRANSFORM · T1 | `/blog/qinan-kyara/` | 奇楠 (Qinan / Kyara): A Grade by Many Names | 1041 | MIX | 9 | P2 — Scent & Ingredient Guide |
| 24 | TRANSFORM · T1 | `/blog/sandalwood-incense/` | Sandalwood Incense (檀香): Reading the Claims | 2543 | EN | 18 | P2 — Scent & Ingredient Guide |
| 25 | TRANSFORM · T1 | `/blog/sandalwood-vs-frankincense/` | Sandalwood vs Frankincense: Creamy Wood and Citrus Resin Compared | 2215 | EN | 16 | P2 — Scent & Ingredient Guide |
| 26 | TRANSFORM · T1 | `/blog/sandalwood-vs-red-sandalwood/` | Sandalwood vs Red Sandalwood: 檀香 vs 紫檀 — The Shared-Character Trap | 885 | EN | 8 | P2 — Scent & Ingredient Guide |
| 27 | TRANSFORM · T2 | `/blog/aromatherapy-beads/` | Aromatherapy Beads & Bracelets: Worn, Not Burned | 1453 | EN | 12 | P4 — Product Formats & Tools |
| 28 | TRANSFORM · T2 | `/blog/backflow-cones/` | Backflow Incense Cones: The Waterfall Effect | 1230 | EN | 11 | P4 — Product Formats & Tools |
| 29 | TRANSFORM · T2 | `/blog/boshan-censer/` | 博山炉 (Boshan Censer): The Han Mountain Burner | 823 | MIX | 8 | P4 — Product Formats & Tools |
| 30 | TRANSFORM · T2 | `/blog/citrus-incense/` | Citrus Incense (柑橘): A Bright Top Note | 1416 | EN | 13 | P2 — Scent & Ingredient Guide |
| 31 | TRANSFORM · T2 | `/blog/floral-aroma-family/` | The Floral Aroma Family: Blossom, Honeyed, Heady | 1495 | EN | 10 | P2 — Scent & Ingredient Guide |
| 32 | TRANSFORM · T2 | `/blog/gehuo-fenxiang-setup/` | 隔火焚香 (Indirect-Fire Incense): Scent, No Smoke | 1011 | EN | 9 | P4 — Product Formats & Tools |
| 33 | TRANSFORM · T2 | `/blog/how-to-choose-incense/` | How to Choose Incense: A Honest Buying Guide | 1434 | EN | 15 | P5 — Buying & Selection |
| 34 | TRANSFORM · T2 | `/blog/incense-aroma-families/` | The 10 Incense Aroma Families: A Complete Map | 1518 | EN | 9 | P2 — Scent & Ingredient Guide |
| 35 | TRANSFORM · T2 | `/blog/incense-burn-time-format-matrix/` | Incense Burn Time Format Matrix: Stick to Powder | 1299 | EN | 9 | P4 — Product Formats & Tools |
| 36 | TRANSFORM · T2 | `/blog/incense-burners-tools/` | Chinese Incense Burners & Tools (香炉香具) | 841 | EN | 8 | P4 — Product Formats & Tools |
| 37 | TRANSFORM · T2 | `/blog/incense-coils/` | Incense Coils: The Hours-Long Burn, Explained | 1134 | EN | 11 | P4 — Product Formats & Tools |
| 38 | TRANSFORM · T2 | `/blog/incense-gift-guide/` | Incense Gift Guide: Choosing a Thoughtful Gift | 1193 | EN | 11 | P5 — Buying & Selection |
| 39 | TRANSFORM · T2 | `/blog/incense-holder-burner-guide/` | Incense Holder & Burner Guide: What You Need | 1062 | EN | 12 | P5 — Buying & Selection |
| 40 | TRANSFORM · T2 | `/blog/incense-powder-resin/` | Incense Powder & Resin: Smoke-Light Format | 1257 | EN | 12 | P4 — Product Formats & Tools |
| 41 | TRANSFORM · T2 | `/blog/incense-powder-vs-wood-chips/` | Incense Powder vs Wood Chips: The Form Decides the Use | 2353 | EN | 15 | P4 — Product Formats & Tools |
| 42 | TRANSFORM · T2 | `/blog/incense-seal-zhuanxiang/` | 香篆 (Seal Incense): Powder Pressed Into Patterns | 1026 | EN | 9 | P4 — Product Formats & Tools |
| 43 | TRANSFORM · T2 | `/blog/incense-stick-vs-cone/` | Incense Stick vs Cone: Burn Time, Smoke, and When Each Fits | 1975 | EN | 14 | P4 — Product Formats & Tools |
| 44 | TRANSFORM · T2 | `/blog/incense-sticks/` | Incense Sticks: The Everyday Format, Explained | 1332 | EN | 12 | P4 — Product Formats & Tools |
| 45 | TRANSFORM · T2 | `/blog/incense-tools-utensils/` | 香具 (The Incense Tool Set): Chopsticks & Spoons | 973 | MIX | 9 | P4 — Product Formats & Tools |
| 46 | TRANSFORM · T2 | `/blog/indian-incense-agarbatti/` | Indian Incense (Agarbatti): Two Different Grades | 1633 | EN | 14 | P8 — Regional Incense Traditions |
| 47 | TRANSFORM · T2 | `/blog/lavender-incense/` | Lavender Incense: A Western Scent | 1644 | EN | 11 | P2 — Scent & Ingredient Guide |
| 48 | TRANSFORM · T2 | `/blog/lotus-incense/` | Lotus Incense (莲花): Purity and Lift | 1465 | EN | 12 | P2 — Scent & Ingredient Guide |
| 49 | TRANSFORM · T2 | `/blog/middle-eastern-incense/` | Middle Eastern Incense (Bakhoor & Oud) | 1550 | EN | 14 | P8 — Regional Incense Traditions |
| 50 | TRANSFORM · T2 | `/blog/resinous-aroma-family/` | The Resinous Aroma Family: Deep, Sticky, Aromatic | 1508 | EN | 10 | P2 — Scent & Ingredient Guide |
| 51 | TRANSFORM · T2 | `/blog/scent-guide/` | Incense Scent Guide: Choosing by Atmosphere | 2201 | EN | 19 | P2 — Scent & Ingredient Guide |
| 52 | TRANSFORM · T2 | `/blog/scent-wheel/` | The Incense Scent Wheel: Atmosphere to Scenario | 1712 | EN | 10 | P2 — Scent & Ingredient Guide |
| 53 | TRANSFORM · T2 | `/blog/tibetan-incense/` | Tibetan Incense (藏香): Herbal, Not a Single Note | 1604 | EN | 14 | P8 — Regional Incense Traditions |
| 54 | TRANSFORM · T2 | `/blog/which-incense-format/` | Which Incense Format Is Right for You? | 1569 | EN | 13 | P4 — Product Formats & Tools |
| 55 | TRANSFORM · T2 | `/blog/woody-aroma-family/` | The Woody Aroma Family: Incense's Wood Backbone | 1479 | EN | 9 | P2 — Scent & Ingredient Guide |
| 56 | TRANSFORM · T2 | `/blog/world-incense-traditions/` | World Incense Traditions: China to Middle East | 1188 | EN | 11 | P8 — Regional Incense Traditions |
| 57 | TRANSFORM · T2 | `/blog/xuande-censer/` | 宣德炉 (Xuande Censer): The Ming Collector's Censer | 919 | EN | 8 | P4 — Product Formats & Tools |
| 58 | TRANSFORM · T3 | `/blog/aroma-molecules-and-mood/` | Aroma Molecules and Mood: What Chemistry Says | 1316 | EN | 10 | P11 — Aromatherapy & Botany |
| 59 | TRANSFORM · T3 | `/blog/baizi-incense-recipe/` | 柏子香 (Cypress-Seed Incense): The Scholar's Incense | 1042 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 60 | TRANSFORM · T3 | `/blog/best-incense-for-small-room/` | Best Incense for a Small Room: Smoke & Burn Time | 1397 | EN | 12 | P7 — Incense vs Alternatives |
| 61 | TRANSFORM · T3 | `/blog/calming-evening-ritual/` | Calming Evening Ritual (No Sleep-Aid Hype) | 1336 | EN | 10 | P12 — Culture & Mindfulness |
| 62 | TRANSFORM · T3 | `/blog/chinese-incense-recipes/` | Chinese Incense Recipes (香方): Classical Manuals | 1196 | MIX | 11 | P9 — Chinese Incense Recipes (香方) |
| 63 | TRANSFORM · T3 | `/blog/chinese-incense-vs-essential-oils-candles/` | Chinese Incense vs Essential Oils vs Candles | 1054 | EN | 10 | P1 — Chinese Incense 101 |
| 64 | TRANSFORM · T3 | `/blog/ersu-jiuju-recipe/` | 二苏旧局 (The Two Sus' Gathering): A Revival Recipe | 969 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 65 | TRANSFORM · T3 | `/blog/essential-oils-in-incense/` | Essential Oils in Incense: How They Differ | 1501 | EN | 11 | P11 — Aromatherapy & Botany |
| 66 | TRANSFORM · T3 | `/blog/evening-unwinding/` | Incense for Evening Unwinding: Not a Sleep Aid | 1164 | EN | 11 | P3 — Use Scenarios |
| 67 | TRANSFORM · T3 | `/blog/four-leisure-arts/` | 四般闲事 (The Four Leisure Arts) | 817 | MIX | 9 | P12 — Culture & Mindfulness |
| 68 | TRANSFORM · T3 | `/blog/hand-rolled-vs-machine-made/` | Hand-Rolled vs Machine-Made Incense | 1193 | EN | 11 | P10 — Incense Craft & Materials |
| 69 | TRANSFORM · T3 | `/blog/home-ambiance/` | Incense for Home Ambiance: Scent & Hospitality | 1369 | EN | 12 | P3 — Use Scenarios |
| 70 | TRANSFORM · T3 | `/blog/how-aromatherapy-works/` | How Aromatherapy Works: Smell, Memory & Science | 1381 | EN | 10 | P11 — Aromatherapy & Botany |
| 71 | TRANSFORM · T3 | `/blog/how-incense-is-dried-and-cured/` | How Incense Is Dried and Cured: The Waiting That Shapes Scent | 1947 | EN | 11 | P10 — Incense Craft & Materials |
| 72 | TRANSFORM · T3 | `/blog/how-incense-is-made/` | How Incense Is Made: From Raw Material to Finished Product | 2681 | EN | 16 | P10 — Incense Craft & Materials |
| 73 | TRANSFORM · T3 | `/blog/how-incense-powder-is-made/` | How Incense Powder Is Made: Grinding, Sieving, and Blending | 1958 | EN | 12 | P10 — Incense Craft & Materials |
| 74 | TRANSFORM · T3 | `/blog/how-to-burn-incense-safely/` | How to Burn Incense Safely: Holders & Placement | 1081 | EN | 10 | P6 — Care & Safety |
| 75 | TRANSFORM · T3 | `/blog/huarui-furen-yamen-recipe/` | 花蕊夫人衙香 (Huarui Furen's Court Incense): Recipe | 951 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 76 | TRANSFORM · T3 | `/blog/incense-and-breathwork/` | Incense and Breathwork: Scent as a Focus | 1305 | EN | 10 | P12 — Culture & Mindfulness |
| 77 | TRANSFORM · T3 | `/blog/incense-for-meditation/` | Incense for Meditation: Formats & Burn Times | 1727 | EN | 12 | P12 — Culture & Mindfulness |
| 78 | TRANSFORM · T3 | `/blog/incense-in-daily-ritual/` | Incense in Daily Ritual: Scent as a Time Marker | 1359 | EN | 12 | P12 — Culture & Mindfulness |
| 79 | TRANSFORM · T3 | `/blog/incense-ingredients-glossary/` | Incense Ingredients Glossary: Wood to Spice | 2147 | EN | 18 | P10 — Incense Craft & Materials |
| 80 | TRANSFORM · T3 | `/blog/incense-manufacturing-quality-control/` | Incense Manufacturing Quality Control: What Buyers Should Check | 2053 | EN | 13 | P10 — Incense Craft & Materials |
| 81 | TRANSFORM · T3 | `/blog/incense-materials-techniques-forms/` | Incense Materials, Techniques & Forms: The Craft Taxonomy | 1322 | EN | 12 | P10 — Incense Craft & Materials |
| 82 | TRANSFORM · T3 | `/blog/incense-pets-sensitivities/` | Incense, Pets & Sensitivities: What to Watch | 1014 | EN | 10 | P6 — Care & Safety |
| 83 | TRANSFORM · T3 | `/blog/incense-safety-guide/` | Incense Safety Guide: Smoke & Ventilation | 1185 | EN | 11 | P6 — Care & Safety |
| 84 | TRANSFORM · T3 | `/blog/incense-smoke-air-quality-evidence/` | Incense Smoke & Air Quality: The Evidence | 1359 | EN | 9 | P6 — Care & Safety |
| 85 | TRANSFORM · T3 | `/blog/incense-sticks-vs-candles/` | Incense Sticks vs Candles: Flame & Smoke | 1298 | EN | 11 | P7 — Incense vs Alternatives |
| 86 | TRANSFORM · T3 | `/blog/incense-storage-longevity/` | Incense Storage & Longevity: Keeping Scent | 1098 | EN | 10 | P6 — Care & Safety |
| 87 | TRANSFORM · T3 | `/blog/incense-terminology-reference/` | Chinese Incense Terminology: The 249-Term Reference | 1485 | MIX | 11 | P1 — Chinese Incense 101 |
| 88 | TRANSFORM · T3 | `/blog/incense-ventilation-indoor-air/` | Incense, Ventilation & Indoor Air | 1078 | EN | 10 | P6 — Care & Safety |
| 89 | TRANSFORM · T3 | `/blog/incense-vs-candles-vs-diffusers/` | Incense vs Candles vs Diffusers: Which Is Right? | 1649 | EN | 10 | P7 — Incense vs Alternatives |
| 90 | TRANSFORM · T3 | `/blog/incense-vs-essential-oil-diffuser/` | Incense vs Essential Oil Diffuser: Smoke & Scent | 2316 | EN | 17 | P7 — Incense vs Alternatives |
| 91 | TRANSFORM · T3 | `/blog/incense-vs-reed-diffuser-wax-melts/` | Incense vs Reed Diffuser vs Wax Melts | 1037 | EN | 10 | P7 — Incense vs Alternatives |
| 92 | TRANSFORM · T3 | `/blog/jiangnan-lizhu-bedchamber-recipe/` | 江南李主帐中香 (Jiangnan Lord's Bedchamber Incense) | 1045 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 93 | TRANSFORM · T3 | `/blog/lotus-incense-recipe/` | 荷香 (Lotus Incense): The Symbol Over the Flower | 1120 | MIX | 8 | P9 — Chinese Incense Recipes (香方) |
| 94 | TRANSFORM · T3 | `/blog/makko-natural-binders/` | Makko & Natural Binders: The Binding Wood Powder | 1385 | EN | 11 | P10 — Incense Craft & Materials |
| 95 | TRANSFORM · T3 | `/blog/plant-sources-of-incense-scents/` | Plant Sources of Incense Scents: A Botanical Map | 1063 | EN | 10 | P11 — Aromatherapy & Botany |
| 96 | TRANSFORM · T3 | `/blog/scent-by-intention/` | Incense by Intention: Scent for Your Purpose | 1380 | EN | 11 | P3 — Use Scenarios |
| 97 | TRANSFORM · T3 | `/blog/shouyang-princess-plum-recipe/` | 寿阳公主梅花香 (Shouyang Princess's Plum Incense) | 925 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 98 | TRANSFORM · T3 | `/blog/study-deep-work/` | Incense for Study & Deep Work: Not a Focus Drug | 1312 | EN | 12 | P3 — Use Scenarios |
| 99 | TRANSFORM · T3 | `/blog/what-makes-incense-natural/` | What Makes Incense \"Natural\"? The Label Problem | 1592 | EN | 12 | P10 — Incense Craft & Materials |
| 100 | TRANSFORM · T3 | `/blog/xuezhong-chunxin-recipe/` | 雪中春信 (Snow in Spring): The Cool 'Snow' Note | 983 | MIX | 9 | P9 — Chinese Incense Recipes (香方) |
| 101 | TRANSFORM · T3 | `/blog/yoga-breathwork/` | Incense for Yoga & Breathwork: A Grounding Scent | 1417 | EN | 12 | P3 — Use Scenarios |
| 102 | CUT | `/blog/bulk-incense-ingredient-sourcing/` | Bulk Incense Ingredient Sourcing: Buying Raw Materials | 2215 | EN | 13 | Commercial — B2B Buying & Supply |
| 103 | CUT | `/blog/custom-fragrance-development/` | Custom Fragrance Development: Brief to Sample | 1305 | EN | 11 | Commercial — B2B Buying & Supply |
| 104 | CUT | `/blog/factory-vetting-guide/` | Factory Vetting Guide: Auditing a Manufacturer | 1219 | EN | 10 | Commercial — B2B Buying & Supply |
| 105 | CUT | `/blog/how-to-buy-agarwood-for-incense-manufacturing/` | Buying Agarwood for Incense Manufacturing: A Sourcing Checklist | 2928 | EN | 16 | Commercial — B2B Buying & Supply |
| 106 | CUT | `/blog/incense-export-considerations/` | Incense Export Considerations: Compliance, CITES & Documentation | 1940 | EN | 13 | Commercial — B2B Buying & Supply |
| 107 | CUT | `/blog/incense-for-business/` | Incense for Business: Buying Wholesale & OEM | 1358 | EN | 10 | Commercial — B2B Buying & Supply |
| 108 | CUT | `/blog/incense-spec-sheet-coa/` | Incense Spec Sheets & COAs: What a Buyer Should Actually Check | 923 | EN | 7 | P8 — Sourcing & Manufacturing |
| 109 | CUT | `/blog/incense-terminology-glossary/` | Incense Terminology Glossary: Stick to Powder | 1108 | MIX | 9 | P1 — Chinese Incense 101 |
| 110 | CUT | `/blog/moq-pricing-guide/` | MOQ & Pricing Guide: Quotes Over Price Lists | 1249 | EN | 10 | Commercial — B2B Buying & Supply |
| 111 | CUT | `/blog/oem-private-label-guide/` | OEM & Private Label Incense: Custom Manufacturing | 1313 | EN | 10 | Commercial — B2B Buying & Supply |
| 112 | CUT | `/blog/oem-vs-private-label/` | OEM vs Private Label Incense: Which Route Fits Your Brand? | 2321 | EN | 14 | Commercial — B2B Buying & Supply |
| 113 | CUT | `/blog/packaging-shipping-guide/` | Packaging & Export Guide: Packing & Shipping | 1370 | EN | 10 | Commercial — B2B Buying & Supply |
| 114 | CUT | `/blog/samples-program/` | Incense Samples Program: What Samples Verify | 1174 | EN | 10 | Commercial — B2B Buying & Supply |
| 115 | CUT | `/blog/wholesale-guide/` | Wholesale Incense Buying Guide: Vet a Supplier | 2084 | EN | 13 | Commercial — B2B Buying & Supply |

### 非内容渲染页（15）

| 页面 | URL | 处置 | 说明 |
|---|---|---|---|
| incense-manufacturer | `/incense-manufacturer/` | CUT | 纯商业转化 → CUT（降权重/去询盘） |
| oem | `/oem/` | CUT | 纯商业转化 → CUT |
| private-label | `/private-label/` | CUT | 纯商业转化 → CUT |
| request-a-quote | `/request-a-quote/` | CUT | 纯询盘表单 → CUT |
| wholesale | `/wholesale/` | CUT | 纯商业转化 → CUT |
| contact | `/contact/` | CUT | 询盘/样品表单 → CUT |
| index | `/index/` | T1 | 首页 → T1 重定位为知识平台首页 |
| about | `/about/` | T2 | 关于页 → T2 品牌去商业化改写 |
| blog/index | `/blog/index/` | KEEP | 索引页 KEEP（重排栏目） |
| ingredients/index | `/ingredients/index/` | KEEP | 索引页 KEEP（重排栏目） |
| cookies | `/cookies/` | KEEP | 法律页 KEEP |
| disclaimer | `/disclaimer/` | KEEP | 法律页 KEEP |
| privacy-policy | `/privacy-policy/` | KEEP | 法律页 KEEP |
| safety | `/safety/` | KEEP | 安全页 KEEP |
| terms-of-service | `/terms-of-service/` | KEEP | 法律页 KEEP |
