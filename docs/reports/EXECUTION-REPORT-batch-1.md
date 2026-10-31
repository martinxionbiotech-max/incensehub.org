# IncenseHub 博客内容 — 第一批执行报告（中文）

日期：2026-09-09 · 批次：第一批（P1.0 / P1.1 / P2.1 / P2.2 / P2.3）

## Execution Summary
- **Created**：5 篇（输出到 `content/`，Markdown，slug 命名）
  1. `what-is-chinese-incense.md`（P1.0 What is Chinese incense）
  2. `history-of-chinese-incense.md`（P1.1 History）
  3. `sandalwood-incense.md`（P2.1 檀香）
  4. `agarwood-incense.md`（P2.2 沉香）
  5. `lavender-incense.md`（P2.3 薰衣草）
- **Updated**：无（复用既有研究笔记 R-001/R-002/R-003，未改动）
- **Skipped**：无
- **Reason**：品牌名/域名/产品线未定，正文以 `[BRAND]`、作者以 `[AUTHOR]` 占位，不阻塞内容生产（符合 prompt §1）

## Research
- **复用一手研究资产**：`docs/research/` 三份笔记（沉香 R-001、檀香 R-002、香道支柱 R-003），已含中英双语来源分级（S1–S5）。
- **新增检索**：薰衣草 1 次（英文 SERP 竞对实测，确认 overclaiming 模式 + Aauram 的合规诚实写法）。
- **Verified Facts**：沉香=「沉水」词源、Aquilaria 树脂形成机制、檀香 Santalum album 及替代种、香道历史时间线（商→宋→明→清→复兴）、四般闲事出处（吴自牧《梦粱录》）。
- **Conflicting Data（已披露，不擅自定论）**：
  - 奇楠词源 → 三说并存（Kāla/tagara/寺庙），标注「词源不确定」。
  - 奇楠五色分级是否独立等级 vs 绿棋老化阶段 → 源有分歧，标「传统分级，非定论」。
  - 「5000 年历史」→ 弃用，改用保守「约 3000 年（商甲骨文香）」。

## SEO
- **Primary keywords**：chinese incense / history of chinese incense / what is sandalwood incense / what is agarwood incense / lavender incense
- **Intent**：全 informational（第一批纯信息层，先建权威，符合 prompt §1 Content-First）
- **Target queries**：每篇 H1 + Direct Answer + 表格对齐搜索意图
- **Internal links**：5 篇互链（101 ↔ 历史 ↔ 檀香 ↔ 沉香 ↔ 薰衣草）+ 预留 `/natural-vs-synthetic-incense/` 等后续页 slug

## AIO / GEO
- **Direct Answers**：每篇顶部均有「Question → Answer → Key Facts」块，可被 AI 直接抽取。
- **Citation-worthy facts**：沉香沉水分级表、奇楠「油包木 vs 木包油」、檀香物种替代、香道非日本纠正、四般闲事出处。
- **Entities**：每篇明确主实体（Chinese incense / Sandalwood·Santalum / Agarwood·Aquilaria·奇楠 / Lavender·Lavandula）。

## Originality
- **Competitor Gaps**：英文 SERP 大量 overclaiming（檀香/薰衣草「治失眠/降皮质醇/平衡脉轮」等），中文核心知识（奇楠分级、沉水系统、隔火焚香、香谱谱系）英文几乎空白。
- **Original Insights**（每篇 2–5 条）：
  - 「香道非日本」纠正 + 四般闲事统一文化框架
  - 檀香「传统用途 vs 现代证据」诚实框架 + 物种替代买家情报
  - 奇楠 vs 沉香「油包木/木包油」英文稀缺解释 + 沉水分级 + 造假鉴别
  - 薰衣草「西方来源、非中式香谱正典」定位 + 「支持性仪式、非治疗」合规立场

## Quality（120 分制，均 ≥85 可交付）
| 文章 | Overall | 说明 |
|---|---|---|
| agarwood-incense | **102** | 信息增量最强（奇楠/沉水/造假） |
| what-is-chinese-incense | **100** | cornersto ne，纠偏 + 文化框架 |
| sandalwood-incense | **99** | 诚实证据框架 + 物种情报 |
| history-of-chinese-incense | **98** | 保守时间线，来源扎实 |
| lavender-incense | **95** | 合规立场 + 西方来源洞察 |

- **硬性阻断**：0（无虚构来源/数字/资质/评价，无医疗宣称，无重复主意图，无误导 schema）
- **合规红线**：0 触碰（全文 relax/calm/unwind/wellness 表述，无 sleep/treat/cure/anxiety/pain 宣称）

## Next Best Action（一项）
**第二批**：P7.1（incense vs essential oil diffuser，对比·商业调查意图）—— 它承接第一批建立的「中式香 vs 精油香薰」区分，是最早能承接商业意图、且与竞对（monianlife 功效表打法）形成差异化的高价值页面。

---
**说明**：本批为内容草稿（Markdown），尚未接线进 Astro 站点（content collection + 页面路由是后续 Codex 落地步骤）。待品牌 3 硬字段（公司名/域名/邮箱）确定后，替换 `[BRAND]`/`[AUTHOR]` 占位再上线。
