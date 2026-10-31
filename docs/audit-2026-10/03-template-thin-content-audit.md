# 03 — 模板化与薄内容审计（Template & Thin Content）

## 一、方法

- **全量程序化扫描**：266 个内容源（150 ingredients + 115 blog + 1 concept）的正文词数、H2 章节数、FAQ/Sources/Evidence 存在性、共享样板块出现率。
- **深度阅读**：6 个 ingredient 页（agarwood 木/树脂、sandalwood 木、clove 香料、ambergris 动物源、calamus 安全警示、paicao 冷门草本）逐段核对独立价值与重复部分。
- 判断依据：独立价值 / 重复段落 / 仅替换名称 / 不可验证声明 / 内容稀薄 / 是否回答问题，结合语义重复度、事实差异、信息增量、搜索意图——**不只看字数**。

---

## 二、全量量化结论（先给数字，再给逐页）

| 集合 | 页数 | 平均词数 | 词数区间 | 最薄页 |
|---|---|---|---|---|
| ingredients | 150 | 2,761 | 2,076–4,389 | schizonepeta（2,076） |
| blog | 115 | 1,654 | 912–3,021 | incense-spec-sheet-coa（912） |
| concept | 1 | ~2,500 | — | chinese-incense |

**关键：全站最薄页为 912 词，无 <500 词的"薄页"。** 不存在内容稀薄这一结构性风险。

### 共享模板块出现率（150 ingredient 页）

| 块 | 出现率 | 解读 |
|---|---|---|
| `> **Direct answer:**` 直答块 | 150/150 | 结构统一，**内容逐页唯一**（每页实体名+学名+香气不同） |
| `## FAQ` | 150/150 | 结构统一 |
| `## Summary` | 150/150 | 结构统一 |
| `## Evidence & Sources` | 150/150 | 结构统一 |
| `## Evidence status` | 150/150 | 结构统一 |
| `## Our Industry View` | 150/150 | 结构统一 |
| `## Traditional use vs modern evidence` | 149/150 | 结构统一 |
| `not medical advice`（页脚免责） | 148/150 | 页脚统一 |
| `## What determines… quality` | 135/150 | 按材质有质量维度差异 |
| `## What buyers should look for` | 122/150 | 部分页面并入他节 |
| `[how incense is made]` 链接 | 42/150 | 仅工艺相关页 |
| `See the [wholesale guide]` | 34/150 | 仅采购相关页 |
| `## Sustainability` / `## Sustainability & sourcing` | 22/150 + 22/150 | 仅野生/CITES 敏感材质 |

### Safety 正文重复度（关键指标）

- `## Safety` 段落全文去重后 **40 种不同文本**（150 页）。
- 最常被共享的 Safety 文本（55 页共享）是 **Evidence & Sources 节内**的标准安全条目："*Source: incense combustion produces smoke and particulate matter; burn in a well-ventilated space. Evidence type: Established.*"——这是**证据分层条目**，不是正文替换。
- 逐页 Safety 正文多数带**材质特定警示**（例：clove 加"eugenol 强刺激勿未稀释使用"；calamus 加"β-asarone 摄入限制"；ambergris 加"多为合成物"）。

**结论：模板是"编辑框架统一、内容逐页个性化"，不是"仅替换名称的 doorway 页"。**

---

## 三、逐页审计（6 篇深度 + 全量代表）

### 1. /ingredients/agarwood/（4,389 词，全站最长）
- **主要独立信息**：沉香是"木质状态而非物种"；沉水三等级（沉/栈/黄熟）引自 香乘；奇楠"木包油 vs 油包木"结构差异；四结（熟结/生结/脱落/虫漏）；CITES + 种植沉香；掺假三手段（染色白木/杂木/注油）；"烧白烟见油"筛查法。
- **重复部分**：与 /blog/agarwood-grading-guide/、/blog/qinan-kyara/ 存在术语级重叠，但此处为实体页、他处为专题指南，各有独立意图。
- **缺失事实**：无具体价格区间（合理——避免不可验证数字）。
- **风险等级**：低。**建议**：KEEP。

### 2. /ingredients/sandalwood/
- **主要独立信息**：檀香 vs 紫檀（*Pterocarpus santalinus*）命名陷阱；四种 *Santalum* 物种区分；半寄生性；"油 vs 木"替代风险；明确"助眠/降压/免疫"为传统或未验证主张、不做疗效声明。
- **重复部分**：命名陷阱在 /blog/sandalwood-vs-red-sandalwood/ 有展开，属正常 hub-spoke。
- **风险等级**：低。**建议**：KEEP。

### 3. /ingredients/clove/
- **主要独立信息**：丁香=丁香 vs 欧丁香（*Syringa* 丁香）双义；eugenol 香气来源；"exhausted cloves"（已提油）质量陷阱；五香粉成员；FDA/刺激警示。
- **风险等级**：低。**建议**：KEEP。

### 4. /ingredients/ambergris/（动物源，非植物）
- **主要独立信息**：龙涎香=抹香鲸消化分泌（非植物）；"found not farmed"海源定位；ambrein→ambrox 氧化化学；CITES + 合成替代（ambroxide/ambreine）；龙涎香 vs 麝香对比表。
- **亮点**：主动声明"这是唯一非植物条目""'botanical incense'含龙涎香是在拉伸定义"——诚实的范畴边界处理。
- **风险等级**：低。**建议**：KEEP。

### 5. /ingredients/calamus/（安全警示型）
- **主要独立信息**：菖蒲=*Acorus calamus* 根茎；**β-asarone 致癌（啮齿）**、FDA 1968 食品禁用、EC 限值；二倍体 vs 四倍体差异；菖蒲 vs 鸢尾根混淆；端午节+艾草民俗。
- **亮点**：YMYL 处理到位——明确"摄入限制 ≠ 燃烧烟雾"，"不声称燃烧菖蒲无害"。这是教科书级的安全页。
- **风险等级**：低。**建议**：KEEP。

### 6. /ingredients/paicao/（冷门草本）
- **主要独立信息**：排草=*Lysimachia capillipes*；香乘原文逐字引用（"白色状如细柳根""人多伪杂之"）；古典"根" vs 现代"全草"的**身份差异提示**；与零陵香同属异种区分；Flora of China 形态数据（40–60cm、叶片 1.5–7cm）。
- **亮点**：最冷门条目仍含中文古籍原文 + 植物学数据 + 身份歧义提示，证明"长尾页也有真实独立价值"。
- **风险等级**：低。**建议**：KEEP。

### 全量代表（程序化，未逐字）
- 最薄 5 ingredient（schizonepeta/daphne/aglaia/michelia-figo/tuberose，2,076–2,248 词）均含 14–15 个 H2、FAQ、Sources、Evidence——**结构完整、非空洞**。
- 全 150 页直答块内容互不重复（前端 directAnswer 由 中文名+拼音+type+学名+香气 五字段生成，语义唯一）。

---

## 四、是否"仅替换名称"？（关键判定）

**否。** 判据：
1. 每页直答块、香气描述、中文名/术语陷阱、加工方式、质量维度、掺假方式、FAQ 答案均为**材质特定事实**（例：agarwood 讲"沉水测试"，calamus 讲"β-asarone"，ambergris 讲"氧化老化"，paicao 讲"根 vs 全草"）。
2. 共享部分仅限**编辑框架**（标题层级、证据分级、"传统 vs 证据"声明、页脚免责），这些是**质量信号而非重复内容**。
3. Safety 正文 40 种变体，非复制粘贴。

---

## 五、风险等级汇总与建议

| 页 | 风险 | 建议 |
|---|---|---|
| 150 ingredient 页 | 低 | KEEP（全部保留） |
| 115 blog 页 | 低 | KEEP（个别见 04 号意图重叠建议） |
| 1 concept 页 | 低 | KEEP |

**未发现任何"IMPROVE 以下"级别的薄页/模板页。** 无需合并、重定向、noindex 或删除（符合"禁止把相似自动等同垃圾"红线）。

---

## 六、一个可改善点（非降权风险）

150 ingredient 页与 1 concept 页**无日期信号**（无 `last_reviewed`，schema 无 `dateModified`），与 115 blog 页（有 `last_reviewed`）不一致。这是新鲜度信号的一致性问题（P1），不是内容质量问题。详见 09/10 号文档。
