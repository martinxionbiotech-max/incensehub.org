# IncenseHub.org 全内容审计报告（五维 · AUDIT ONLY）

> 日期：2026-10-31 · 审计师：内容审计（只读）· 对比源站：`/root/.openclaw/workspace/repos/IncenseHub`（incensehub.org 原内容归档）
> 范围：266 内容文件（ingredients 150 · blog 115 · concepts 1）· 同路径可比 266/266
> **纪律：本次为纯审计，零内容修改，仅产出本报告 + 分析脚本（scripts/full_audit_5dim.py / full_audit_refine.py）。**

---

## 0. 执行摘要（一句话）

**四批改造（A/B/C/D）实际执行的是「去商业化 + 术语中性化」——即删除商业框架小节 + buyer→reader 等措辞替换——而非五维要求的「去重复 · 加深层次 · 增密度 · 提原创 · 立观点」。结果：266/266 篇与原站仍高度重复（文档级 N-gram 相似度 ≥0.80，均值 0.9409），51 篇逐字相同，句式重合均值 99.7%，总字数较原站 -10.00%（净减少而非增加），独有信息比 0.23%，强原创资产仅 44%。五维中四维 FAIL，一维 PARTIAL。**

---

## 1. 审计方法与口径（已验证 vs 假设分离）

### 1.1 已验证（脚本实测，可复现）

| 指标 | 方法 | 脚本 |
|---|---|---|
| 文档级重复 | 正文（去 frontmatter）字符 4-gram Jaccard 相似度 | full_audit_5dim.py |
| 段落级重复 | IH 每段对 LD 全段最佳 Jaccard 匹配，取均值 + 高/中/低段占比 | 同上 |
| 句式重合 | IH 句子（≥15 字符）对 LD 句子 4-gram Jaccard ≥0.70 视为重合 | 同上 |
| H 层级 | `## / ### / ####` 正则计数 | 同上 |
| 五段链 | 各要素正则命中（Direct answer / Key facts / Summary / FAQ / Evidence status / 机制链词 / 原创资产词 / 观点词） | 同上 |
| 字数 / 独有信息比 | `\S+` 计数；IH 段对 LD 段 Jaccard <0.40 判为「独有」 | 同上 |
| 原创资产 | 对比簇 / 交叉表 / 香气家族 / 君臣佐使 / 替代交叉引用 / 命名陷阱 正则命中 | 同上 + full_audit_refine.py |
| 观点密度 | 误区纠正 / 判断边界 / 实际意义 / 未证实声明 正则命中计数 | 同上 |

### 1.2 假设（需人工复核，非实测结论）

- 「机制链词命中 ≥2 即视为有 Analysis 段」是启发式，未做语义级 X→Y 因果链人工抽验（本批未逐句验语义，只验标记存在）。
- 「句式重合」用 4-gram 阈值 0.70，阈值本身是审计设定，非金标准。
- 「原创资产 = 正则命中」会把「继承自原站的资产」也计为命中——因此第 4 维进一步区分了「强资产（站外不可复制的自建框架）」与「弱资产（通用对比词）」，强资产命中率才是关键结论。
- 观点词命中数 ≠ 观点强度，仅表示「存在观点类表达」，强度分桶是相对分级。

---

## 2. 五维矩阵总览

| 维度 | 核心量化 | 判定 |
|---|---|---|
| **① 原站重复** | 文档级 N-gram 相似度 ≥0.80 的 266/266（100%）；≥0.90 的 194；逐字相同 51；句式重合均值 99.7% | **FAIL** |
| **② 层次加深** | H2 均值 15.3 / H3 均值 4.8；平铺页 0；五段链完整率 53.4%（但标记**继承自原站**） | **PARTIAL** |
| **③ 信息密度** | 字数均值 2055（中位 2257）；总字数较原站 **-10.00%**；独有信息比均值 **0.23%**；稀疏页 1 | **FAIL** |
| **④ 原创度** | 句式重合 99.7%；强原创资产达标率（hexiang/香气家族/命名陷阱/替代交叉引用）**44%**；且多继承自原站 | **FAIL** |
| **⑤ 态度观点** | 观点密度均值 4.21；≥1 篇占比 86%；中立百科腔页 37（14%）；但观点标记**多继承自原站** | **PARTIAL** |

---

## 3. 维度一：原站重复检测（FAIL）

### 3.1 文档级 N-gram 相似度分布（正文，266 篇）

| 相似度阈值 | 篇数 | 占比 |
|---|---|---|
| = 1.000（逐字相同） | 51 | 19.2% |
| ≥ 0.98 | 114 | 42.9% |
| ≥ 0.95 | 115 | 43.2% |
| ≥ 0.90 | 194 | 72.9% |
| ≥ 0.80 | 266 | 100% |
| ≥ 0.70（高重复阈值） | 266 | 100% |

- **min 0.8374 · max 1.0000 · mean 0.9409**
- 按任务口径（高 ≥0.7 / 中 0.4–0.7 / 低 <0.4）：**高重复 266 · 中 0 · 低 0**。

### 3.2 句式重合分布（句子级）

| 重合率阈值 | 文件数 |
|---|---|
| = 1.00（全部句子重合） | 212 |
| ≥ 0.95 | 264 |
| ≥ 0.90 | 265 |
| ≥ 0.80 | 266 |

- 均值 **99.69%**。即几乎每句都能在原站找到 ≥0.70 相似的对应句。

### 3.3 段落级（逐篇高/中/低段占比）

- IH 段落对 LD 段落最佳匹配：绝大多数篇目 **全部段落 ≥0.7**（high 段占比 ≈100%），逐篇 doc_dup 均值 0.94。
- 真正产生「低重合段」（<0.4）的篇目极少：唯一显著差异化的是 `blog/incense-manufacturing-quality-control.md`（doc_dup 0.900，含 5 高 + 3 低段，为全文改写的 T3 篇）。

### 3.4 结论

**改造并未去重。** 四批工作是在原站正文上做「减法」（删除商业小节）和「措辞替换」（buyer→reader 等），保留了原站正文的绝大部分句子原样。51 篇正文逐字未动。

---

## 4. 维度二：层次加深检测（PARTIAL）

### 4.1 H 层级深度

| 指标 | 全站 | ingredients(150) | blog(115) | concepts(1) |
|---|---|---|---|---|
| H2 总数 / 均值 | 4069 / 15.3 | 18.0 | 11.8 | 11.0 |
| H3 总数 / 均值 | 1282 / 4.8 | 4.1 | 5.7 | 0.0 |
| H4 总数 | 少量 | — | — | — |

- **单层平铺页（无 H3 且无机制链）：0 篇**（concepts/chinese-incense 无 H3，但含机制链 + 原创资产，不算平铺）。

### 4.2 五段链完整性

| 要素 | 全站命中率 | ingredients | blog |
|---|---|---|---|
| Information（Direct answer/Key facts/Evidence status） | 65.4% (174) | 100% | 21% |
| Analysis（机制链 ≥2） | 87.2% (232) | 83% | 93% |
| Conclusion（Summary/Key Takeaways） | 89.1% (237) | 100% | 76% |
| Originality（原创资产 ≥1） | 97.0% (258) | 100% | 93% |
| Author Viewpoint（观点 ≥1） | 86.1% (229) | 100% | 68% |
| **五段全中（完整率）** | **53.4% (142)** | — | — |

### 4.3 关键发现：五段链标记「继承自原站」，非本批新增

源站 IncenseHub 中，同样的标记早已存在：

| 标记 | 源站命中篇数 |
|---|---|
| `> **Direct answer:**` | 171 |
| `## Summary` | 150 |
| `## Evidence status` | 150 |
| `## Evidence & Sources` | 150 |
| `## FAQ` | 265 |
| `## Key facts` | 150 |

即：五段链结构在**移植前就已在源站正文中**，本批主要是「保留」而非「新建」。blog 段的 Information 命中率仅 21%（因 blog 用 `Key Takeaways` 而非 `Key facts`），说明部分篇目段落要素不齐，但这不是「加深」问题，而是「结构未被本批补齐」问题。

### 4.4 判定

结构层级（H2/H3）达标、无平铺页，**但「加深」是伪命题——层次是原站带来的，非改造新增**。故 PARTIAL。

---

## 5. 维度三：信息密度检测（FAIL）

### 5.1 字数分布

- 全站总字数 546,724；均值 2055；中位 2257；min 912；max 3817。
- 分布集中在 1100–2300 词区间，无空洞短页（除 1 篇稀疏页）。

### 5.2 与原站的信息增量（决定性证据）

| 指标 | 数值 |
|---|---|
| IH 总字数 | 546,724 |
| LD 总字数 | 607,459 |
| **字数差** | **−60,735（−10.00%）** |
| 字数减少的篇目 | 153 |
| 字数增加的篇目 | 2（各 +7） |
| 字数相等的篇目 | 111 |
| 段落差 | −1,410（151 篇减少 · 0 篇增加 · 115 篇相等） |
| **独有信息比（段级 Jaccard <0.40）均值** | **0.23%** |

### 5.3 稀疏页清单

| 页面 | 字数 | 表 | 对照 |
|---|---|---|---|
| `blog/incense-spec-sheet-coa.md` | 912 | 0 | 无 |

### 5.4 结论

**信息密度是「净减少」而非「更全面密集」。** 改造只删不增：总字数 -10%，段落 -1410，唯一的信息增量是措辞替换（+7 词级微调）。独有信息比 0.23% 意味着「新增事实 / 新增分析 / 新增对照表」几乎为零。明确 FAIL。

---

## 6. 维度四：原创度检测（FAIL）

### 6.1 站外可复制性

| 指标 | 数值 |
|---|---|
| 句式重合均值（vs 原站） | 99.69% |
| 模板骨架占比（样板词命中/正文长度） | 2.09%（低，因样板词稀疏，不代表原创） |

句式重合 99.7% 是决定性指标：**正文几乎逐句可追溯到原站**，站外可复制性极高。

### 6.2 原创资产统计

| 资产类型 | 命中篇数 | 说明 |
|---|---|---|
| 对比簇（vs/versus/difference between） | 248 | **弱资产**——通用对比词，站外可复制 |
| 交叉表（≥2 张表） | 188 | **弱资产**——表格结构常见 |
| 替代交叉引用（substitution/cross-reference） | 79 | 较强 |
| 君臣佐使英文系统化（hexiang/chief–minister–assistant–guide） | 30 | **强资产**（自建框架） |
| 命名陷阱（naming trap/confusion） | 16 | **强资产** |
| 香气家族分类（aroma family/scent wheel） | 15 | **强资产** |

### 6.3 每篇强原创资产 ≥1 达标率

- 弱口径（对比簇/交叉表也算）：258/266 = **97.0%**（虚高，因通用对比词泛滥）。
- **强口径（hexiang / 香气家族 / 命名陷阱 / 替代交叉引用 任一）：117/266 = 44.0%**。

### 6.4 关键发现：强资产也多为继承

源站中这些「自建框架」已存在：君臣佐使 15 篇、香气家族 10 篇、命名陷阱 13 篇、替代交叉引用 87 篇、对比簇 246 篇。即**本批几乎未新增原创资产**——强资产是移植时带过来的。

### 6.5 结论

句式重合 99.7% + 强原创资产达标率仅 44% 且多为继承 → **原创度 FAIL**。原站已存在的内容不构成「站外不可复制的原创资产」。

---

## 7. 维度五：态度观点检测（PARTIAL）

### 7.1 观点密度分布

| 强度分桶 | 篇数 | 占比 |
|---|---|---|
| zero（无观点） | 37 | 13.9% |
| low（1–2） | 66 | 24.8% |
| mid（3–5） | 81 | 30.5% |
| high（6+） | 82 | 30.8% |

- 观点密度均值 4.21；≥1 篇占比 229/266 = 86.1%。

### 7.2 中立百科腔页清单（无观点无立场，37 篇）

```
blog/aromatherapy-beads · backflow-cones · best-incense-for-small-room
chinese-incense-vs-essential-oils-candles · chinese-vs-indian-incense
custom-fragrance-development · floral-aroma-family · four-leisure-arts
history-of-chinese-incense · home-ambiance · how-to-choose-incense
huarui-furen-yamen-recipe · incense-aroma-families · incense-authentication-database
incense-burn-time-format-matrix · incense-burners-tools · incense-coils
incense-for-business · incense-holder-burner-guide · incense-in-daily-ritual
incense-stick-vs-cone · incense-sticks · incense-storage-longevity
incense-terminology-reference · incense-tools-utensils
incense-vs-reed-diffuser-wax-melts · indian-incense-agarbatti
jiangnan-lizhu-bedchamber-recipe · lanDeng-knowledge-map · lotus-incense
oem-private-label-guide · qinan-kyara · sandalwood-vs-red-sandalwood
scent-by-intention · shouyang-princess-plum-recipe · woody-aroma-family
world-incense-traditions
```

### 7.3 关键发现：观点标记也多为继承

源站中「not established」已命中 159 篇、「traditional belief」5 篇——即「未证实声明」「传统信念边界」这类作者立场在原站正文中已存在，本批主要是保留。真正由本批新增的观点性表达有限。

### 7.4 结论

86% 篇目有观点表达，但观点标记多继承自原站，且 37 篇仍是中立百科腔。综合判 **PARTIAL**。

---

## 8. P0 / P1 / P2 分级修复清单

> 分级依据：高重复（doc-ngram ≥0.90）为最重；叠加「逐字相同」「无观点」「薄」为复合问题优先。所有「发现→建议动作」均为审计建议，本次**未执行任何修改**。

### 8.0 总量

| 级别 | 篇数 | 判定口径 |
|---|---|---|
| **P0** | 41 | 逐字相同（=1.000）且（无观点 或 薄 <1600 词）——复合问题最重 |
| **P1** | 58 | 高重复（≥0.90）且（无观点 或 薄） |
| **P2** | 167 | 高重复但结构与观点尚可，需深化差异化 |

### 8.1 P0（41 篇）——逐字相同 + 无观点/薄

**P0a（逐字相同 + 无观点，20 篇）：**

| 页面 | 发现 | 建议动作 |
|---|---|---|
| `blog/best-incense-for-small-room` (1461w) | 逐字同源 + 零观点 | 重写并注入「小空间用香的剂量边界 + 通风判断」作者观点 |
| `blog/chinese-incense-vs-essential-oils-candles` (1156w) | 逐字同源 + 零观点 + 薄 | 补对比机制链 + 「为何传统合香≠芳香疗法」立场 |
| `blog/chinese-vs-indian-incense` (2296w) | 逐字同源 + 零观点 | 增「两大传统边界判断」段，降复制 |
| `blog/four-leisure-arts` (997w) | 逐字同源 + 零观点 + 薄 | 补 H3 分层 + 文化判断视角 |
| `blog/huarui-furen-yamen-recipe` (1183w) | 逐字同源 + 零观点 + 薄 | 加机制链（配伍逻辑）+ 适用边界 |
| `blog/incense-authentication-database` (1094w) | 逐字同源 + 零观点 + 薄 | 加「鉴别标准为何不可伪造」观点 |
| `blog/incense-burn-time-format-matrix` (1467w) | 逐字同源 + 零观点 + 薄 | 补「燃烧时长≠品质」判断 |
| `blog/incense-coils` (1155w) | 逐字同源 + 零观点 + 薄 | 加盘香 vs 线香适用边界 |
| `blog/incense-holder-burner-guide` (1229w) | 逐字同源 + 零观点 + 薄 | 加安全判断视角 |
| `blog/incense-in-daily-ritual` (1430w) | 逐字同源 + 零观点 + 薄 | 加「仪式感 vs 功效」边界 |
| `blog/incense-stick-vs-cone` (2047w) | 逐字同源 + 零观点 | 加选择判断结论 |
| `blog/incense-sticks` (1341w) | 逐字同源 + 零观点 + 薄 | 重写线香概览，注入质量判断 |
| `blog/incense-storage-longevity` (1172w) | 逐字同源 + 零观点 + 薄 | 加储存误区纠正 |
| `blog/incense-tools-utensils` (1153w) | 逐字同源 + 零观点 + 薄 | 加工具选择判断 |
| `blog/incense-vs-reed-diffuser-wax-melts` (1118w) | 逐字同源 + 零观点 + 薄 | 补对比机制链 + 立场 |
| `blog/jiangnan-lizhu-bedchamber-recipe` (1238w) | 逐字同源 + 零观点 + 薄 | 加配伍机制链 + 边界 |
| `blog/qinan-kyara` (1137w) | 逐字同源 + 零观点 + 薄 | 加奇楠鉴别判断 |
| `blog/sandalwood-vs-red-sandalwood` (1037w) | 逐字同源 + 零观点 + 薄 | 加命名陷阱立场（已删 buyer 段需补观点） |
| `blog/shouyang-princess-plum-recipe` (1182w) | 逐字同源 + 零观点 + 薄 | 加配方机制链 + 边界 |
| `blog/world-incense-traditions` (1292w) | 逐字同源 + 零观点 + 薄 | 加跨传统比较判断 |

**P0b（逐字相同 + 薄但已有观点，21 篇）：** 需重写降重 + 加深，但观点维度已过。
`baizi-incense-recipe · boshan-censer · calming-evening-ritual · chinese-incense-recipes · ersu-jiuju-recipe · how-aromatherapy-works · how-to-burn-incense-safely · incense-material-comparison-matrix · incense-pets-sensitivities · incense-powder-resin · incense-safety-guide · incense-seal-zhuanxiang · incense-smoke-air-quality-evidence · incense-sticks-vs-candles · incense-terminology-glossary · incense-ventilation-indoor-air · lotus-incense-recipe · plant-sources-of-incense-scents · qinan-buying-authentication · xiangpu-incense-manuals · xuezhong-chunxin-recipe`

### 8.2 P1（58 篇）——高重复（0.90–0.999）+ 无观点/薄

**P1a（≥0.90 + 无观点，17 篇）：**
`aromatherapy-beads · backflow-cones · custom-fragrance-development · floral-aroma-family · history-of-chinese-incense · home-ambiance · how-to-choose-incense · incense-aroma-families · incense-burners-tools · incense-for-business · incense-terminology-reference · indian-incense-agarbatti · lanDeng-knowledge-map · lotus-incense · oem-private-label-guide · scent-by-intention · woody-aroma-family`

**P1b（≥0.90 + 薄，41 篇）：** 主要为其余薄层 blog 篇，需深化差异化。

### 8.3 优先级排序（复合问题优先）

1. **P0a**（逐字 + 无观点 + 多为薄）——三重复合，最优先重写。
2. **P0b**（逐字 + 薄）——双重复合。
3. **P1a**（高重复 + 无观点）——缺立场。
4. **P1b**（高重复 + 薄）——缺深度。
5. **P2**（高重复但结构观点尚可）——需系统性降重 + 深化。

### 8.4 Top 10 修复清单（紧凑报告用）

| # | 页面 | 问题 | 动作 |
|---|---|---|---|
| 1 | `blog/four-leisure-arts` | 逐字 + 零观点 + 薄(997w) + 无H3 | 重写 + 分层 + 立场 |
| 2 | `blog/incense-authentication-database` | 逐字 + 零观点 + 薄(1094w) | 重写 + 鉴别判断 |
| 3 | `blog/qinan-kyara` | 逐字 + 零观点 + 薄(1137w) | 重写 + 奇楠鉴别立场 |
| 4 | `blog/sandalwood-vs-red-sandalwood` | 逐字 + 零观点 + 薄(1037w) | 重写 + 命名陷阱立场 |
| 5 | `blog/chinese-incense-vs-essential-oils-candles` | 逐字 + 零观点 + 薄(1156w) | 重写 + 对比机制 + 立场 |
| 6 | `blog/huarui-furen-yamen-recipe` | 逐字 + 零观点 + 薄(1183w) | 重写 + 配伍链 + 边界 |
| 7 | `blog/incense-tools-utensils` | 逐字 + 零观点 + 薄(1153w) | 重写 + 工具判断 |
| 8 | `blog/incense-coils` | 逐字 + 零观点 + 薄(1155w) | 重写 + 适用边界 |
| 9 | `blog/incense-spec-sheet-coa` | 稀疏(912w) + 无表 | 补表 + 加深 |
| 10 | `concepts/chinese-incense` | 无 H3 + 无 Conclusion 标记 | 补 H3 分层 + 结论段 |

---

## 9. 已验证 vs 假设分离（复核）

**已验证（脚本实测）：** 全部量化数字（相似度分布、字数差、段落差、H 层级、五段链命中率、观点密度分桶、原创资产命中率、逐字相同清单、中立页清单）。

**假设（需人工复核）：**
1. 「五段链标记继承自原站」——由源站正则命中数推断（Direct answer 171 等），未逐篇 diff 确认每一标记的 diff 来源。
2. 「强原创资产多为继承」——由源站框架命中数推断，未逐篇做框架级 diff。
3. 「机制链/观点 = 正则命中」是启发式，未做语义抽验。
4. 「句式重合 0.70 阈值」为审计设定。

---

## 10. 附：分析脚本

- `scripts/full_audit_5dim.py` — 主审计（五维 + 全量 JSON 输出至 /tmp/full_audit_5dim.json）
- `scripts/full_audit_refine.py` — 精炼指标（字数差 / 段落差 / H2 骨架 / 强弱资产）

**内容改动 = 0。**
