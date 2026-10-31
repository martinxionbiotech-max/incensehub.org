# 01 — 执行摘要（Executive Summary）

审计对象：https://incensehub.org（IncenseHub 澜灯，中国植物香材英文知识站）
审计日期：2026-10-18
审计性质：只读审计（未发布、未删页、未改 canonical/robots、未改任何源码）
执行者：IncenseHerbs.com 内容质量与 Google 算法风险审计

---

## 一、一句话结论

**本站内容质量高、证据链完整、无薄内容/无重复页面/无虚构声明；曝光趋近零的最可能解释是"新域名冷启动"（缺权威与反链、仍在初期索引阶段），而非内容质量触发的算法处罚。** 无法用内容层面证据证明 2026-10-11 后的曝光下降由内容质量导致；反之，内容层面证据强有力地排除了"内容质量差"这一常见降权诱因。

---

## 二、关键证据概览

| 维度 | 结论 | 关键证据 |
|---|---|---|
| 站点年代 | 全新站点 | Git 全 36 次提交均在 2026-09-27 至 2026-09-29；线上 /disclaimer/ 页标注 2026-10-18 |
| 内容规模 | 266 内容源 + 16 页面 | 150 ingredients + 115 blog + 1 concept；sitemap 279 URL |
| 内容厚度 | 无薄页 | ingredient 平均 2,761 词（区间 2,076–4,389）；blog 平均 1,654 词（最薄 912 词） |
| 模板化 | 结构统一、内容逐页个性化 | 150/150 有直答+证据分级+FAQ+Summary；Safety 正文 40 种变体，非"仅替换名称" |
| 意图重叠 | 无关键词蚕食 | 8 组候选对全部已差异化（hub-and-spoke / glossary-vs-index / 对比-vs-流程） |
| 科学/安全声明 | 严谨、可溯源 | 引用 PMC/ALA/EPA/CPSC/NFPA；明确"相关≠因果""传统≠疗效"；无编造文献 |
| 原创性 | 高（中文源情报+植物分类+鉴别分级） | 逐页引用 香乘/本草纲目/夢粱录 原文 + Flora of China/GBIF 分类 |
| 虚假声明 | 无 | 无伪造作者/专家/资质/检测/引用；作者统一为 "Landeng Tech Team" |
| 抓取/索引 | 健康 | robots 全允许 + sitemap 279 URL + canonical 正确 + meta description 0 重复 |
| 部署 | 轻微漂移 | 线上有 /disclaimer/ 页 + 更完整 robots.txt，本地 origin/main 无（生产领先于仓库） |

---

## 三、核心判断（区分已验证事实 / 风险信号 / 待验证假设）

### 已验证事实
1. 内容质量高、无薄页、无重复页、无虚构声明（全量程序化扫描 + 6 页深度阅读 + 8 组重叠候选对比 + 4 页科学/安全页逐句核对）。
2. 站点为全新域名，Git 提交集中在 2026-09 下旬，10 月无仓库级内容变更（线上另有 /disclaimer/ 于 10-18 更新）。
3. 抓取/索引配置健康：robots 全允许、sitemap 279 URL、canonical 正确、无 noindex、meta description 零重复。

### 风险信号（非降权证据）
1. **新域名零权威**：无 GSC 数据，无法确认外链/权威积累；新站曝光趋零是常态而非异常。
2. **部署与仓库漂移**：/disclaimer/ 页与更完整 robots.txt 未进入 GitHub 仓库（origin/main 落后于生产）。
3. **日期信号薄弱**：150 ingredient + 1 concept 页无 `last_reviewed`、无 `dateModified` schema（blog 页有）。
4. **轻度内容冗余**："natural ≠ smoke-free" 框架在 5+ 页重复出现（非重复内容，属观点复用）。

### 待验证假设
1. "曝光下降由内容质量导致" —— **无证据支持**；时间关联（10-08 Spam Update 结束、10-11 下降）仅作线索，不构成因果。
2. 是否存在技术性抓取异常 / 索引延迟 —— 需 GSC 数据才能判定（无权限，未编造）。

---

## 四、已确认问题（Top 列表，详细证据见 02/03/04/06/07）

| 级别 | 问题 | 证据 URL |
|---|---|---|
| P1 | ingredient/concept 页无日期信号（无 last_reviewed/dateModified） | 150 ingredient + 1 concept 源码 schema 均无 dateModified；blog 页有 |
| P1 | 部署与 GitHub 仓库漂移（disclaimer/robots 未入库） | 线上 /disclaimer/ 200；本地 `grep -rl disclaimer src/` 为空 |
| P2 | 意图最接近的重复组：incense-powder-vs-wood-chips 与 agarwood-powder-vs-chips（结构相似、范围不同） | 两页均用"同材两形/表面积"框架 |
| P2 | E-E-A-T 作者信号弱（统一 "Landeng Tech Team"，无署名方法论/资质） | 全部 115 blog frontmatter `author: "Landeng Tech Team"` |
| P2 | "natural ≠ smoke-free" 观点在多页复用（轻度冗余，非重复内容） | safety-guide / smoke-air-quality / pets / 3 个对比页 |

**无 Critical 问题**：未发现抓取阻断、规范化错误、批量重复、虚构声明、医疗越界等 Critical 级风险。

---

## 五、整改任务统计（详见 09/10）

- **P0（立即排查）**：0 项（抓取/索引/规范化均健康，无阻断性问题）
- **P1（优先改善）**：2 项（日期信号补齐；部署与仓库同步）
- **P2（长期建设）**：4 项（powder-vs-chips 组差异化加固；E-E-A-T 署名；观点复用去重；外链/权威积累）

---

## 六、最终结论（详见 12）

内容质量**不是**曝光下降的可能实质贡献因素；站点核心短板是**新域名冷启动与权威积累**，而非内容。建议不删除、不批量 noindex、不合并 URL；优先做"补日期信号 + 仓库同步 + 外链建设 + 权威沉淀"。

> 本报告不声称能确定 Google 内部算法判断；无 GSC 数据，曝光下降原因仅能给出"最可能解释"，不能确认处罚。
