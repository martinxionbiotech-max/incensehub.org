# IncenseHub.org 内容改造 · 批 C 执行报告（T2 优先篇 + 主题内链 + SEO/AIO）

日期：2026-10-31 · 批次：Batch C · 品牌：IncenseHub · 技术栈：Astro 5（静态生成，282 渲染页）

> 承接 `docs/incensehub-inventory.md`（清册）与 `docs/incensehub-transformation-plan.md`（方案）。
> 本批执行方案 §5.3 的 T2 队列**前 60 篇**（按清册 T2 优先级顺序），每篇按 §3 五段链轻量级改造 + §4 SEO/AIO 规范，并做主题内链与孤儿复核。剩余 T2 篇列 continuation 清单（不强行超量）。

---

## 1. 执行摘要

| 维度 | 结果 |
|---|---|
| T2 完成篇数 | **60 / 140**（本批 = T2 前 60 篇，全部为 ingredients 香材实体） |
| Continuation 清单 | **80 篇 content**（49 ingredients + 31 blog）+ 1 about 页 |
| 商业框架小节删除 | **118 段**（Our Industry View 60 · What buyers should look for 46 · Modern commercial applications 12） |
| 商业/买家框架中性化 | **50 篇**正文内嵌 buyer/sourcing-buyer/wholesale 框架句 → reader/identification/in trade 中性知识视角 |
| 机械 AI 腔命中 | **0**（However/It is important to/Moreover/Furthermore/Notably/notably/In conclusion 复扫 = 0） |
| 商业段残留（改造篇） | **0**（buyer/wholesale guide/sourcing buyer/Our Industry View/from a manufacturing = 0） |
| 断链 | **0**（60 篇内链目标逐一校验） |
| title 唯一性 | **60/60 唯一**（`title` 去重 = 0 重复） |
| 改造篇主题内链总数 | **568 条**（每篇 4–17 条，≥2 达标） |
| build | ✅ `npm run build` 282 页成功，0 error |

---

## 2. T2 前 60 篇清单（本批完成）

按清册 T2 优先级顺序（ingredients 字母序）取前 60：

```
agastache-rugosa, amber, amomum-villosum, angelica, angelica-sinensis, anise,
apricot-kernel, artemisia-annua, asarum, atractylodes, bamboo-leaves, basil,
bay-leaf, beeswax, bergamot, bletilla, borneol-oil, calamus, cardamom,
cassia-twig, castoreum, champaca, chrysanthemum, cinnamon, citron, citronella,
civet, clove, copaiba, coriander-seed, cubeb, cumin, cypress-seed, dill,
elsholtzia, eucalyptus, fennel, finger-citron, galangal, galbanum, gardenia,
ginger, ginkgo, grapefruit, honey, honeysuckle, jasmine, jasmine-grandiflorum,
juniper, katsumadai, kumquat, labdanum, lavender, lemon, licorice, ligusticum,
ligusticum-chuanxiong, lily-of-the-valley, litchi-husk, long-pepper
```

---

## 3. 五段链落地（每篇轻量级执行）

| 段 | 落地方式 | 验证 |
|---|---|---|
| **Information 事实分层** | 保留 `Key facts` 表 + `> Direct answer:` 块 + `Evidence & Sources` / `Evidence status` 分层（Established / Historically documented / Trade terminology / Practical screening） | 60/60 篇保留证据分层表 |
| **Analysis 机制链** | 每篇保留 ≥1 条「X→Y」机制链（如结香=伤口+真菌+时间；沉水=密度≠品质；命名共享=混淆风险；drying 转化 gingerol→shogaol） | 60/60 篇含机制链 |
| **Conclusion 每 H2 可摘取结论** | 每 H2 开头 `> **Direct answer:**` 黑体结论句 + 结尾 `## Summary` | 60/60 篇结构完整（Summary/FAQ/Evidence 三重校验通过） |
| **Author Viewpoint（误区/边界/实际意义）** | 保留 `Traditional use vs modern evidence`（边界）+ 命名/混淆段（误区）+ `Why is it used`（实际意义） | 60/60 篇含边界/误区标记段 |
| **Originality（视主题选做）** | 对比簇（anise vs fennel vs star anise、citron/finger-citron/bergamot、cinnamon vs cassia、borneol 晶体/油/合成、copaiba vs peru balsam 等）保留并作为原创资产 | 多篇含站内独有对比簇 |

---

## 4. 去商业化动作（§1.1 / §1.2）

1. **删除三个商业框架小节**（全 60 篇）：`Our Industry View` / `What buyers should look for` / `Modern commercial applications` —— 共 **118 段**。
2. **删除硬转化 CTA 句**：`See the [wholesale guide]...` 引导句 → 全部移除（60 篇内 wholesale-guide 引用 = 0）。
3. **中性化保留知识价值**（§1.2 转译）：
   - 「买家应该看什么」→「鉴别者应该看什么」：`buyer` → `reader`，`For powder buyers` → `For powder`，`the buyer evaluates the lot` → `the lot is judged by physical condition`。
   - 「批发/OEM 定制」→「产品分类与规格差异」：`sourcing buyer` → `sourcing`，保留 `Common forms` / 产品形态分类知识。
   - 「供应商/工厂审核」→「工艺与质量控制原理」：`from a manufacturing perspective` 段删除，`particle size / moisture / consistency` 知识保留为中性工艺变量。
   - 「商业视角」→「贸易/鉴别视角」：`commercially` → `in trade`，`defining commercial risk` → `defining identification risk`，`Commercial grading` → `Trade grading`。

> 知识价值（香材分类 / 香材差异 / 应用分析 / 命名辨析 / 机制链）全部保留，仅剥离「采购/买家/OEM」框架。

---

## 5. 主题内链 + 孤儿复核

- 改造篇主题内链总数 **568 条**，每篇 4–17 条，全部 ≥2（描述性锚文本，如 `[patchouli](/ingredients/patchouli/)`、`[how incense is made](/blog/how-incense-is-made/)`、`[scent guide](/blog/scent-guide/)`）。
- 主题聚类互链覆盖：香材实体↔香气家族（scent-guide / scent-wheel / aroma-family hubs）↔鉴别（substitution cross-reference / authentication database）↔工艺（how-incense-is-made / incense powder）↔文化（chinese-incense / 香乘）。
- **孤儿复核**：`scripts/orphan_detect.py` 重跑 → 全站孤儿页从历史 37 降至 **3 篇**（均为 T1 blog 对比页 `chinese-vs-indian-incense` / `chinese-vs-japanese-incense` / `sandalwood-vs-red-sandalwood`，属本批范围外）；本批 60 篇改造页 **0 孤儿**。
- `scripts/orphan_inbound.json` 已随重跑更新。

---

## 6. SEO / AIO 优化（改造篇）

| 项 | 落地 | 验证 |
|---|---|---|
| title | 唯一 + 意图匹配（`英文名 (中文) — 定位副标`，如 `Agastache (藿香) — Aromatic Herb`） | 60/60 唯一 |
| Meta Description | `directAnswer` 一句话价值+结论（`[中文] ([拼音]) is an [type] from [学名], with an aroma profile of [香调]`） | 60/60 渲染 |
| 首段 | 图片后 `> **Direct answer:**` 直答块（定义 + 一句话结论） | 60/60 |
| 摘要段 | `Key facts` 表格（中文/拼音/学名/来源/香调/风险） | 60/60 |
| H1–H2–H3 | H1 唯一主题 + H2 五段链分节（Aroma/Botanical identity/Terminology/Quality/Forms/Tradition/Evidence） | 60/60 |
| 自然实体覆盖 | 英文名 + 中文名 + 拼音 + 学名（植物类）+ 关联实体（混淆对/香气家族/工艺） | 60/60 |
| 无关键词堆砌 | 描述性锚文本内链，无精确匹配堆叠 | ✅ |
| 无机械 FAQ | FAQ 保留真实用户问题（`FAQPage` schema 仅抽取问句结尾 `?`） | ✅ |

---

## 7. 验证结果

| 检查 | 结果 |
|---|---|
| `npm run build` | ✅ 282 页，0 error（md-negotiation generated=275 skipped=7 missing=0） |
| T2 完成篇渲染抽验 | ✅ agastache-rugosa dist HTML：Direct answer ×12 · Summary · Traditional use vs modern evidence 均渲染 |
| 机械腔复扫 | ✅ 0 |
| 商业段残留复扫（改造篇） | ✅ 0 |
| 断链 | ✅ 0 |
| title 唯一 | ✅ 0 重复 |
| 孤儿（改造篇） | ✅ 0 |

---

## 8. Continuation 清单（剩余 T2，80 content + 1 about）

**T2 ingredients 剩余（49 篇）**：

```
lotus-flower, magnolia-flower, mastic, mint, mugwort, mulberry-leaf, mustard,
neroli, nutmeg, onycha, orange-peel, orchid, orris-root, osmanthus, oxyphylla,
patchouli, peony, pepper, peppermint, perilla, peru-balsam, pine-needles,
pine-resin, platycladus-leaves, plum-blossom, pomelo-peel, prickly-ash, quince,
rose, rosemary, sage, sand-ginger, schizonepeta, shellac, spearmint, star-anise,
styrax-resin, sweetgum, thuja, thyme, torreya, tree-peony, tsao-ko, tuberose,
valerian, vetiver, violet, wintersweet, ylang-ylang
```

**T2 blog 剩余（31 篇）**：

```
aromatherapy-beads, backflow-cones, boshan-censer, citrus-incense,
floral-aroma-family, gehuo-fenxiang-setup, how-to-choose-incense,
incense-aroma-families, incense-burn-time-format-matrix, incense-burners-tools,
incense-coils, incense-gift-guide, incense-holder-burner-guide, incense-powder-resin,
incense-powder-vs-wood-chips, incense-seal-zhuanxiang, incense-stick-vs-cone,
incense-sticks, incense-tools-utensils, indian-incense-agarbatti, lavender-incense,
lotus-incense, middle-eastern-incense, resinous-aroma-family, scent-guide,
scent-wheel, tibetan-incense, which-incense-format, woody-aroma-family,
world-incense-traditions, xuande-censer
```

**静态页**：`about`（T2 品牌去商业化改写，1 篇）。

> 后续批次按同一五段链 + 去商业 + 主题内链 + SEO/AIO 动作推进，无需改动本批脚本逻辑（`scripts/batch_c_decommercialize.py` / `scripts/batch_c_neutralize.py` 可复现）。

---

## 9. 复现脚本

- `scripts/batch_c_decommercialize.py`：确定性删除三商业框架小节 + 中性化 sourcing 段标题/CTA。
- `scripts/batch_c_neutralize.py`：买家/商业框架词 → 中性知识视角（reader/identification/in trade）+ 修悬空引用。
- 用法：`python3 scripts/batch_c_decommercialize.py <slug...>`（空参读 `/tmp/t2_60.txt`）。

---

**说明**：本批为内容改造（Markdown 层），未触碰 `incensehubdata` 数据层与 schema；品牌名 IncenseHub / 域名 incensehub.org 保持既有。
