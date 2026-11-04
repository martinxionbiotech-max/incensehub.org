# IncenseHub.org 内容改造 · 最终交付报告（Batch D · 全项目收口）

日期：2026-10-31 · 批次：Batch D · 品牌：IncenseHub · 技术栈：Astro 5（静态生成，282 渲染页）

> 承接 `docs/incensehub-inventory.md`（清册 266 内容篇）、`docs/incensehub-transformation-plan.md`（方案）、`docs/incensehub-batch-c-report.md` §8 continuation 清单。
> 本批为**收官批**：完成 T3 队列（72 篇）+ 剩余 T2 continuation（80 内容篇 + about 页）+ 全站终质检 + 交付报告。

---

## 1. 全项目四批总览

| 批次 | 处置 | 完成篇数 | 状态 |
|---|---|---|---|
| **Batch A** | T1 首批（19 blog + 1 首页） | 20 | ✅ 已落地（前置 commit） |
| **Batch B** | 平台重定位（nav/footer 去商业化、README、包名、中间件域名） | — | ✅ 已落地（前置 commit） |
| **Batch C** | T2 前 60 篇（ingredients 香材实体） | 60 | ✅ 已落地（前置 commit） |
| **Batch D（本批）** | T3 队列 + T2 continuation + KEEP 补清洗 + 全站终质检 | 166（见下） | ✅ 本批完成 |

清册处置口径：266 内容篇 = KEEP 21 · TRANSFORM·T1 19 · TRANSFORM·T2 140 · TRANSFORM·T3 72 · CUT 14。四批累计覆盖全部 231 篇 TRANSFORM（19+140+72）+ 13 篇 KEEP ingredients 补清洗，CUT 14 篇按方案降权（本批未删页未换 URL）。

### Batch D 完成明细

| 队列 | 篇数 | 完成 | backlog |
|---|---|---|---|
| **T3 队列**（28 ingredients + 44 blog） | 72 | **72 / 72** | 0 |
| **T2 continuation**（49 ingredients + 31 blog + 1 about） | 81 | **81 / 81** | 0 |
| **KEEP ingredients 补清洗**（13 篇，清册误标"无商业污染"） | 13 | **13 / 13** | 0 |
| **Batch C 残留 buying 框架补齐**（5 篇：cinnamon/civet/clove/copaiba/cumin） | 5 | **5 / 5** | 0 |
| **合计** | — | **171 篇内容操作** | **0** |

> **重要发现**：清册将 13 篇 KEEP ingredients 标为"已达标·无商业污染"，但实检发现这 13 篇（agarwood/ambergris/benzoin/borneol/camphor/cedar/dragons-blood/frankincense/jiangzhenxiang/musk/myrrh/red-sandalwood/sandalwood）仍完整保留 `Our Industry View` / `What buyers should look for` / `Modern commercial applications` 三个商业框架小节。本批一并清洗，使全站商业段残留归零。

---

## 2. 改造动作（Batch D 统一执行）

### 2.1 去商业化（§1.1 / §1.2）

1. **删除三个商业框架小节**（90 ingredients + 1 blog）：`Our Industry View` / `What buyers should look for` / `Modern commercial applications`，头至下一 `## ` 小节结构性删除。
2. **中性化买家/商业框架**（继承 Batch C 脚本，扩展至 blog）：
   - `buyer` → `reader`，`sourcing buyer` → `sourcing`，`commercially` → `in trade`，`Commercial grading` → `Trade grading`。
   - `buyer intelligence` / `buyer-intelligence` → `identification`（含 `(buyer intelligence)` 节标题去后缀、`reader-intelligence` 残留改写为 identification）。
   - `Key buying risk/note` → `Key identification risk/note`（对比表表头）。
   - `buying guide` → `selection guide`，`before buying` → `before choosing`，`what you are buying` → `what you are getting`。
3. **删除 wholesale-guide CTA 句**（8 篇 ingredients + blog 内嵌）：`See the [wholesale guide]... for the sourcing framework.` 全部移除。
4. **`incense-manufacturing-quality-control` 全文改写**：标题 `What Buyers Should Check` → `How Repeatability Is Actually Checked`，`search_intent` commercial_investigation → informational，删除 `Our Industry View` 小节 + wholesale-guide / request-a-quote CTA，buyer→reader 全文，作者观点段从 "wins the sourcing game" 改写为中性工艺判断。
5. **about 页改写**：删除 "manufacturer and supplier directory / Commercial services（wholesale·OEM·private label）/ supplier directory" 商业定位，重写为纯知识平台定位，保留法律主体披露（USCC/地址/邮箱），删除 OEM/private-label/wholesale/incense-manufacturer 商业页导航链接，`Is IncenseHub a store?` FAQ 从"商业经邮件协议安排"改为"知识平台"。

### 2.2 术语规范化（§3.1）

- 全部 150 ingredients `pinyin:` frontmatter 完整（0 缺失），中文名源真值内嵌保持既有。
- 无新增中文段落，无机械翻译腔；中文引文（香乘/本草）保留原文 + 英文意译，未直译拼接。
- 全文未引入任何 `[need-source]` 占位（0 处）；信息不足处维持既有 Evidence tier 分层表述，不虚构。

### 2.3 五段链复核（§3）

T3/T2-continuation 篇在移植时已携带五段链结构（Direct answer 直答块 + Key facts + Summary + FAQ + Evidence status），本批复核确认：

- **Information**：`Key facts` 表 + `> Direct answer:` 块 + `Evidence & Sources` 分层 —— 77/77 T2-cont+T3 ingredients 均含 Direct answer 与 Summary。
- **Conclusion**：每 H2 黑体结论句 + `## Summary` —— 77/77 达标（≥1 可摘取结论句）。
- **Author Viewpoint**：`Traditional use vs modern evidence` + 命名/误区段保留 —— 全量。
- **Originality**：对比簇（agarwood vs sandalwood / frankincense vs myrrh / borneol vs camphor / 藿香 vs 广藿香 等）保留。

### 2.4 机械腔清零

本批清理 4 处句首机械过渡 + 1 处 buyer 框架词：

| 文件 | 原文 | 改后 |
|---|---|---|
| banksia-rose.md | `Notably, the double...` | `The double...`（删过渡词） |
| paicao.md | `However, the classical...` | `The classical..., by contrast,...` |
| borneol.md | `However, much commercial borneol...` | `Much commercial borneol, though,...` |
| tuberose.md | `It is important to keep this straight:` | `To keep this straight:` |
| lanDeng-editorial-methodology.md | `buyer heuristics` | `trade heuristics` |

---

## 3. 修改页清单（124 文件）

### 3.1 ingredients（95 篇）

- **KEEP 补清洗（13）**：agarwood, ambergris, benzoin, borneol, camphor, cedar, dragons-blood, frankincense, jiangzhenxiang, musk, myrrh, red-sandalwood, sandalwood
- **T2 continuation（49）**：lotus-flower, magnolia-flower, mastic, mint, mugwort, mulberry-leaf, mustard, neroli, nutmeg, onycha, orange-peel, orchid, orris-root, osmanthus, oxyphylla, patchouli, peony, pepper, peppermint, perilla, peru-balsam, pine-needles, pine-resin, platycladus-leaves, plum-blossom, pomelo-peel, prickly-ash, quince, rose, rosemary, sage, sand-ginger, schizonepeta, shellac, spearmint, star-anise, styrax-resin, sweetgum, thuja, thyme, torreya, tree-peony, tsao-ko, tuberose, valerian, vetiver, violet, wintersweet, ylang-ylang
- **T3（28）**：aglaia, aromatic-turmeric, asafoetida, banksia-rose, blumea-balsamifera, chamomile, costus, cyperus, daphne, eupatorium, eupatorium-japonicum, fenugreek, lemon-balm, linglingxiang, litsea-cubeba, michelia-figo, paicao, rue, schisandra, silk-tree, sophora-flower, spikenard-nardostachys, tarragon, tree-peony-bark, turmeric, vanilla, yulan-magnolia, zedoary
- **Batch C 残留补齐（5）**：cinnamon, civet, clove, copaiba, cumin

### 3.2 blog（27 篇）

citrus-incense, floral-aroma-family, gehuo-fenxiang-setup, hand-rolled-vs-machine-made, how-incense-is-dried-and-cured, how-incense-is-made, how-incense-powder-is-made, how-to-choose-incense, incense-aroma-families, incense-burners-tools, incense-gift-guide, incense-ingredients-glossary, incense-manufacturing-quality-control（全文改写）, incense-materials-techniques-forms, incense-powder-vs-wood-chips, incense-terminology-reference, indian-incense-agarbatti, japanese-incense-kodo, lanDeng-editorial-methodology, lavender-incense, lotus-incense, makko-natural-binders, middle-eastern-incense, plant-sources-of-incense-scents, scent-guide, what-makes-incense-natural, xuande-censer

### 3.3 静态页 / 其他（2）

- `src/pages/about/index.astro`（T2 品牌去商业化改写）
- `scripts/orphan_inbound.json`（重跑更新）

### 3.4 新增脚本（2）

- `scripts/batch_d_neutralize_ingredients.py`（ingredients 残留框架清理）
- `scripts/batch_d_neutralize_blog.py`（blog buyer 框架清理）

---

## 4. 增删内容说明

- **删除**：90 ingredients + 1 blog 的 `Our Industry View` / `What buyers should look for` / `Modern commercial applications` 三个商业框架小节；8 处 wholesale-guide CTA 句；about 页商业服务小节与商业页导航链接；`incense-manufacturing-quality-control` 的 `Our Industry View` + request-a-quote CTA。总计净 **-2599 行**。
- **新增**：3 处孤儿页入链（见 §6）；`incense-manufacturing-quality-control` 改写（作者观点段 + 结论句保留）；`peony` 补回 schisandra 对照句（恢复被删小节内的有效知识链接）。净 **+438 行**。
- **未删任何页、未改任何 URL/文件名/slug/架构**。

---

## 5. 内链图谱（孤儿治理）

本批孤儿复核结果：

| 处置 | 页面 | 动作 |
|---|---|---|
| 新孤儿（本批引致） | `/ingredients/schisandra/` | `peony` 删商业小节时带走了唯一入链 → 在 `How is it used in fragrance?` 段补回对照句 `The same gap between fame and fragrance appears with [schisandra]...` |
| 历史孤儿（Batch C 遗留 3 篇 T1 对比页） | `/blog/chinese-vs-indian-incense/` | `indian-incense-agarbatti` FAQ 加 `the direct [Chinese vs Indian comparison]` 入链 |
| | `/blog/chinese-vs-japanese-incense/` | `japanese-incense-kodo` Kōdō vs Chinese 段加 `the side-by-side [Chinese vs Japanese comparison]` 入链 |
| | `/blog/sandalwood-vs-red-sandalwood/` | `red-sandalwood` naming 段加 `the shared-character trap unpacked in [sandalwood vs red sandalwood]` 入链 |

**孤儿最终：4 → 0。**

---

## 6. SEO / AIO 记录

| 项 | 结果 |
|---|---|
| title 唯一性 | **0 重复**（266 篇 title 去重） |
| Meta description | 由 BaseLayout 从 directAnswer/首段渲染，282 页均渲染 |
| 首段直答 | 全量 `Direct answer:` 块 + `Key facts` 表 |
| H1 唯一 | **单 H1 = 0 异常**（全站无多 H1/零 H1） |
| 自然实体覆盖 | 英文名 + 中文名 + 拼音 + 学名 + 关联实体（混淆对/香气家族/工艺） |
| 无关键词堆砌 | 描述性锚文本内链，无精确匹配堆叠 |
| JSON-LD / schema | 未触碰（数据层不在本批范围） |

---

## 7. 未验证信息清单

- `[need-source]` 占位标记：**0 处**（本批未引入任何未标注占位；既有内容以 Evidence tier 分层表述不确定性）。
- 未验证项集中为历史/传统记录（香乘/本草引文），以 `Historically documented` / `Traditional use` tier 标注，未升级为临床事实。
- 商业数据（MOQ/价格/产能/认证）：本批全部保持"确认 per inquiry / 不发布"口径，未新增任何商业数字。

---

## 8. 最终质量检查

| 检查 | 结果 |
|---|---|
| 机械腔（句首 However/Moreover/Furthermore/Notably/In conclusion/It is important to 等） | ✅ **0** |
| 商业段残留（buyer/wholesale guide/sourcing buyer/Our Industry View/from a manufacturing） | ✅ **0**（非 CUT 内容） |
| buyer-intelligence / reader-intelligence 残留 | ✅ **0** |
| 重复页相似度（对比簇 jaccard） | ✅ agarwood-vs-frankincense vs sandalwood-vs-frankincense 0.583 · agarwood-vs-frankincense vs agarwood-vs-sandalwood 0.510 · frankincense-vs-myrrh vs sandalwood-vs-frankincense 0.494 · agarwood-vs-sandalwood vs sandalwood-vs-red-sandalwood 0.247（对比簇已差异化，各自保留独立意图） |
| title 唯一性 | ✅ **0 重复** |
| 单 H1 | ✅ **0 异常** |
| 断链 | ✅ **0**（按 `slug:` frontmatter 派生 URL 校验） |
| 孤儿 | ✅ **0**（原 4 → 0） |
| 拼音 frontmatter | ✅ **150/150** 完整 |
| `npm run build` | ✅ **282 页，0 error** |
| sitemap | ✅ **281 locs**（282 页 − 404；sitemap-index → sitemap-0.xml 完整） |

---

## 9. backlog 清单

**T2 continuation / T3 队列：0 篇未完成**（72 + 81 全量完成，未触发容量降级）。

CUT 14 篇（`bulk-incense-ingredient-sourcing` / `custom-fragrance-development` / `factory-vetting-guide` / `how-to-buy-agarwood-for-incense-manufacturing` / `incense-export-considerations` / `incense-for-business` / `incense-spec-sheet-coa` / `incense-terminology-glossary` / `moq-pricing-guide` / `oem-private-label-guide` / `oem-vs-private-label` / `packaging-shipping-guide` / `samples-program` / `wholesale-guide`）+ 6 商业转化静态页，按方案 §5.1 属**降权/合并**处置，不在本批 TRANSFORM 范围，保留待后续 CUT 批次处理（不删页不换 URL）。

---

## 10. 复现脚本

- `scripts/batch_c_decommercialize.py`：确定性删除三商业框架小节 + 中性化 sourcing 标题/CTA。
- `scripts/batch_c_neutralize.py`：买家/商业框架词 → 中性知识视角。
- `scripts/batch_d_neutralize_ingredients.py`（新）：ingredients 残留 `(buyer intelligence)` 节标题、`Key buying`、buying→identification/sourcing、wholesale-guide CTA 清理。
- `scripts/batch_d_neutralize_blog.py`（新）：blog buyer/buying 框架 → reader/identification/selection。
- 用法：`python3 scripts/<name>.py <slug...>`（空参读 `/tmp` slug 清单）。

---

**说明**：本批为内容改造（Markdown + Astro 页层），未触碰 `incensehubdata` 数据层与 schema；品牌名 IncenseHub / 域名 incensehub.org 保持既有。全站商业框架归零、机械腔归零、孤儿归零、断链归零、build/sitemap 通过。
