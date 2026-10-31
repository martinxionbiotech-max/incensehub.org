# IncenseHub.org 内容改造方案（Batch A — Transformation Plan）

> 配套文档：`docs/incensehub-inventory.md`（全量清册 + 逐篇处置）。
> 本方案定义改造**原则、结构、方法与批次**，不执行内容改写（改写为 Batch A 后续动作）。

---

## 0. 一句话定位

**IncenseHub.org = 独立的香材知识与香文化研究平台。** 它回答"这是什么香材、它为什么是、怎么判断真假好坏、为什么值得用"——而不是"去哪里买、起订量多少、如何询盘"。

当前仓库（`incensehub.org`）是**知识内容 + B2B 商业框架**的混合体：150 个香材实体页 100% 内嵌了"买家/批发/OEM"框架（Our Industry View / What Buyers Should Look For / Modern Commercial Applications），14 篇纯 B2B 博客 + 6 个商业转化静态页构成商业层。改造的目标是把"知识层"从"商业层"中剥离并强化，把商业层降权/合并，不删页、不换 URL。

---

## 1. 平台定位落实

### 1.1 删除（商业化内容，去推销/去询盘/去转化）

| 类别 | 处置 |
|---|---|
| 实体页内嵌商业框架小节 | 删除 `Our Industry View` / `What Buyers Should Look For` / `Modern Commercial Applications` 三个小节，以及 `Sourcing`/`Buying Guide` 段（150 实体页 + 7 博客页） |
| 硬转化 CTA 句 | 删除 `request a sample/quote`、`get a quote`、`MOQ`、`lead time`、`buy now` 引导（20 篇：12 纯 B2B CUT + 8 知识页内嵌） |
| 纯商业转化静态页（6） | `/incense-manufacturer/` `/oem/` `/private-label/` `/request-a-quote/` `/wholesale/` `/contact/` → CUT（降权重写/合并，不删页不换 URL） |
| 纯 B2B 博客（14） | `incense-for-business`、`moq-pricing-guide`、`wholesale-guide`、`oem-private-label-guide`、`oem-vs-private-label`、`factory-vetting-guide`、`bulk-incense-ingredient-sourcing`、`how-to-buy-agarwood-for-incense-manufacturing`、`custom-fragrance-development`、`packaging-shipping-guide`、`samples-program`、`incense-export-considerations`、`incense-spec-sheet-coa`、`incense-terminology-glossary` → CUT |

### 1.2 保留（知识价值，转为中性知识框架）

"买家应该看什么" → **"鉴别者应该看什么"**；"批发/OEM 定制" → **"产品分类与规格差异"**；"供应商/工厂审核" → **"工艺与质量控制原理"**。

保留并强化的知识价值内容：

- **香材分类**：实体分类（木/树脂/花/草本/果皮）、形态分类（粉/片/线香/盘香）、来源分类（本土/进口）。
- **香材差异**：对比页（agarwood vs sandalwood、frankincense vs myrrh、borneol vs camphor）是站内最高价值资产。
- **应用分析**：香气特征、焚燃方式、合香配伍、场景适配——全部中性化，无"采购"视角。

---

## 2. 内容结构体系（七大主题聚类 + 支柱设计）

现有内容已落在 13 个 pillar（P1–P12 + Commercial + Editorial）。改造按 **7 个主题域** 重新聚合，每个域一个**支柱页（hub）** + 若干**辐条页（spoke）**，形成可内链的簇。

| # | 主题域 | 支柱页（hub） | 内容范围 | 覆盖现状 |
|---|---|---|---|---|
| 1 | **香材实体** | `/chinese-incense/` + 150 实体页 | 沉香/檀香/降真香/乳香/没药/龙脑/麝香… 植物学身份、别名、产地、形态 | 150 实体页（13 KEEP 已达标，其余 T2/T3 需去商业化 + 差异化） |
| 2 | **鉴别与质量评价** | `incense-authentication-database` | 真假鉴别、等级体系（沉水/奇楠）、造假手段、质量因子 | `incense-substitution-cross-reference`、`natural-vs-synthetic-incense`、`qinan-buying-authentication`、`agarwood-grading-guide` |
| 3 | **形成原理** | `how-incense-is-made` 链 | 沉香结香机制、树脂形成、加工前处理 | 实体页 `How agarwood forms` 段 + 形成类内容（需补强为独立域） |
| 4 | **加工工艺** | `how-incense-is-made` / `incense-materials-techniques-forms` | 研磨/过筛/配伍/成型/干燥陈化 | P10 簇（12 篇 T2/T3） |
| 5 | **香气特征** | `scent-guide` + `scent-wheel` | 香气家族（10）、香气分子、氛围场景 | P2 簇（22 篇） |
| 6 | **香文化** | `what-is-chinese-incense` / `history-of-chinese-incense` | 历史、四般闲事、香谱、香道、地域传统、香方 | P1/P8/P9/P12 簇 |
| 7 | **行业认知** | `incense-terminology-reference` + 数据层 | 术语、分类体系、行业标准认知（去商业） | 术语 reference + data-landeng 8 数据集 |

**支柱设计原则**：
- 每个主题域一个 hub 页，承载"主题总览 + 全站该域内链入口"。
- spoke 页在首段与结尾互链回 hub 及同域相关 spoke（不做孤立页）。
- 七大域与 `data-landeng` 的 8 个数据集（ingredients/terminology/aroma/materials/comparisons/techniques/forms/relationships）一一呼应，叙事层引用数据层，数据层回链叙事层。

---

## 3. 每篇改造：五段链

每篇 TRANSFORM 页（无论 T1/T2/T3）按以下五段链重组，保证信息密度与原创性：

```
Information → Analysis → Conclusion → Originality → Author Viewpoint
（信息层）      （分析层）     （结论层）      （原创层）       （作者观点层）
```

| 段 | 做什么 | 完成判据 |
|---|---|---|
| **Information** | 准确可溯源的事实：是什么、植物学身份、来源、化学组分、历史记载；每句带证据分层（`FACT / TRADITIONAL_BELIEF / HISTORICAL_RECORD / SCIENTIFIC_FINDING…`） | 每个事实句可回溯到 Sources；无"无出处"的精确数字 |
| **Analysis** | 因素关系分析：什么机制导致什么结果（结香=伤口+真菌+时间；沉水=密度≠品质；合香=君臣佐使结构） | 至少 1 条明确的"X→Y"机制链，非属性罗列 |
| **Conclusion** | 可独立引用的判断句：每个 H2 有一个一句话站得住的核心结论（如"沉水是密度指标，不是品质指标"） | 每 H2 有黑体结论句，可被 AI 直接摘取 |
| **Originality** | 独有框架/综合/第一手数据/中文知识分析（非翻译）：君臣佐使的英文系统化、香谱源流综合、替代品交叉对照表、香气家族分类 | 有 ≥1 个站外不可复制的原创资产 |
| **Author Viewpoint** | 独立作者立场：常见误区纠正、判断边界（结论在何种条件下不成立）、实际意义（对使用者/收藏者意味着什么） | 无百科拼接、无模板 AI 腔；有明确编辑判断 |

**五段链与现有规范的关系**：它**细化**了 `AIO-STRATEGY.md` 的"direct answer → definition → key facts → detail → comparison → evidence → analysis → examples → related"与 `CONTENT-GOVERNANCE.md` 的 originality rule——不冲突，是二者的可执行拆解。

### 3.1 英文输出规范（语言转换策略）

清册结论：**当前 266 篇 = 194 EN + 72 MIX，0 纯中文页，无双语平行页。**

因此**不存在"中文→英文翻译"任务**；策略是**术语规范化**而非翻译：

1. **中文名作为"源真值"内嵌**：英文正文首次出现实体时给 `Chinese name (拼音)`，如 `Agarwood (沉香 chénxiāng)`。
2. **拼音一致性**：全站统一拼音标注（对照 `CHINESE-ENGLISH-GLOSSARY.md` 与 `data-landeng/terminology.json`）。
3. **中文引文保留原文 + 英文意译**：香谱/香乘引文保留原句 + 括号英译，不做直译拼接。
4. **禁机械翻译腔**：MIX 页的中文术语不是"翻译残留"，是"权威真值锚点"——保留，但不新增中文段落。

### 3.2 原创性标准（硬性红线）

- ❌ **不句子替换**：同义词替换现有句子 ≠ 原创。
- ❌ **不段落调整**：调换段落顺序 ≠ 原创。
- ❌ **不百科拼接**：把维基/百科条目拼成文章 ≠ 原创（维基仅作 discovery pointer）。
- ❌ **不模板化 AI 腔**：禁用"值得注意的是 / 综上所述 / 总而言之 / 首先其次最后"机械过渡；每段有实质判断而非填空。
- ✅ **重新分析整合**：基于源材料重新分析、重新综合，形成新判断。
- ✅ **独立作者观点**：有可辨识的编辑立场，敢下"对/错/边界"判断。
- ✅ **四要素齐全**：因素关系（X→Y）· 常见误区 · 判断边界 · 实际意义。
- ✅ **中文知识分析（非翻译）**：把中文一手资料（香谱、香乘、古籍）分析后形成英文原创，而非直译。

---

## 4. SEO / AIO 规范

| 维度 | 规范 |
|---|---|
| **核心意图** | 每页**一个** informational 核心意图；H1 直接回答该意图。禁止一页塞多个互斥意图 |
| **H1–H2–H3** | H1 = 唯一主题 + 核心关键词（含英文名 + 中文名/拼音）；H2 = 信息架构分节（按五段链）；H3 = 子主题；不跳级、不堆叠 |
| **自然实体覆盖** | 首次出现：英文名 + 中文名 + 拼音 + 学名（植物类）+ 别名 + 产地；关联实体自然引入（对照 `ENTITY-MODEL.md` / `CHINESE-ENGLISH-GLOSSARY.md`） |
| **主题关联内链** | 同域 hub↔spoke 双向；对比页互链（如 agarwood-vs-sandalwood ↔ sandalwood-vs-frankincense）；实体页 → 相关实体 + 所属主题 hub；不孤立页 |
| **可独立引用关键结论** | 每 H2 一个黑体结论句，语义自足、可被 AI 摘要直接摘取；关键结论句不依赖上下文 |
| **title / meta / 首段 / 摘要** | title ≤ 60 字符含核心词；meta description 150–160 字符直答意图；首段 = direct answer（定义 + 一句话结论）；摘要 = 结构化关键事实（列表/表格） |
| **无堆砌、无机械 FAQ** | 关键词自然分布（无堆砌）；FAQ 只保留真实用户问题（`FAQPage` schema 仅用于真实 Q&A）；删除模板化"Q&A"充数段 |

**AIO 叠加**：重要页走 AI 回答模式——`直答 → 定义 → 关键事实 → 详述 → 对比 → 证据/来源 → 原创分析 → 示例 → 相关实体`；保留 JSON-LD（Article / DefinedTerm / BreadcrumbList），数据层不在此批改动。

---

## 5. 批次计划

### 5.1 处置节奏总览

| 批次 | 篇数 | 内容 |
|---|---|---|
| **T1（首批）** | 19 篇 blog + 1 首页 | 最高搜索潜力 + 核心主题价值（见 5.2） |
| **T2（第二批）** | 140 篇（109 ingredients + 31 blog） + 1 about | 次核心实体/工艺/香气/地域 |
| **T3（第三批）** | 72 篇（28 ingredients + 44 blog） | 长尾香材/香方/场景/文化 |
| **KEEP** | 21 篇 + 7 静态页 | 已达标，仅品牌名替换（IncenseHub → IncenseHub） |
| **CUT** | 14 篇 blog + 6 静态页 | 降权重写/合并标注，不删页不换 URL |

### 5.2 T1 首批清单（19 篇，按搜索潜力 + 主题价值）

| 主题域 | T1 篇 | 改造要点 |
|---|---|---|
| **鉴别与质量评价** | `agarwood-grading-guide`（沉香等级/沉水/奇楠） | 沉水=密度≠品质的原创判断；等级体系图 |
| | `qinan-buying-authentication`（奇楠购买鉴别） | "buying"→"鉴别"视角；造假手段 + 判断边界 |
| | `incense-authentication-database`（真假鉴别） | 站内鉴别中枢 hub；补强为支柱页 |
| | `incense-substitution-cross-reference`（替代品交叉对照） | 标签陷阱对照表（原创资产） |
| | `natural-vs-synthetic-incense`（天然 vs 合成） | 判断边界：什么算"天然"；标签问题 |
| | `sandalwood-vs-red-sandalwood`（檀香 vs 紫檀） | 共享字符陷阱——独立作者观点样本 |
| | `borneol-vs-camphor`（龙脑 vs 樟脑） | 两种晶体不同植物；常见误区纠正 |
| **香材实体** | `agarwood-incense`（沉香） | 去商业化 + 结香机制分析 |
| | `sandalwood-incense`（檀香） | "Use vs Evidence"证据分层强化 |
| | `frankincense-incense`（乳香） | 树脂来源 + 应用分析 |
| | `qinan-kyara`（奇楠） | 多名同物；术语规范化样本 |
| **对比/差异** | `agarwood-vs-sandalwood` | 双参照木对比（最高价值对比页） |
| | `agarwood-vs-frankincense` | 木 vs 树脂对比 |
| | `sandalwood-vs-frankincense` | 对比簇（与上两篇互链 + 加区分度） |
| | `frankincense-vs-myrrh` | 双树脂对比 |
| **香气/应用** | `incense-material-comparison-matrix`（7 经典香材矩阵） | 矩阵表原创资产；AIO 结构化 |
| **工艺/配伍** | `hexiang-blending-system`（合香体系） | 君臣佐使英文系统化（核心原创） |
| **香文化/地域** | `chinese-vs-indian-incense`（中式 vs 印度） | 合香 vs Agarbatti 文化对比 |
| **形态/应用** | `agarwood-powder-vs-chips`（沉香粉 vs 片） | 形态决定用途；去"buying"视角 |

**+ 首页（index）**：T1 重定位——从商业首页改写为知识平台首页（主题域导航 + 支柱入口 + 数据层入口），删除询盘/产品推荐。

### 5.3 T2 / T3 队列（略表）

- **T2**：109 个次核心香材实体（clove/cinnamon/jasmine/rose/patchouli…）+ 31 篇 blog（香气家族、形态工具、地域传统、工艺）。统一动作：去商业框架三小节 + 差异化加深（消除模板骨架相似）+ 五段链补齐。
- **T3**：28 个长尾香材 + 44 篇 blog（香方 recipes、场景 use scenarios、安全 safety、文化 mindfulness、vs alternatives）。统一动作：去商业 + 五段链 + 术语规范化。
- **CUT 合并指引**：`oem-private-label-guide` + `oem-vs-private-label` 合并为单篇（保留后者 URL）；`incense-terminology-glossary` 并入 `incense-terminology-reference`；对比簇（agarwood-vs-frankincense / sandalwood-vs-frankincense / agarwood-vs-sandalwood）加区分度而非合并（各保留独立意图）。

---

## 6. 收口与可复现

- 清册生成：`python3 scripts/incensehub_inventory.py`（自包含，只读，可复现 T2/T3 批次重跑）。
- 本批不触碰 `data-landeng` 数据层；域名 `data.incensehub.org → data.incensehub.org` 与主站品牌替换在部署层执行。
- 改造执行（写内容）为 Batch A 后续动作，按 T1 → T2 → T3 → CUT 顺序推进。
