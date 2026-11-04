# IncenseHub — Content & Database Focus

> 版本：2026-11-04
> 定位：知识内容 + 开放数据库，不做商业落地页，不做 LanDeng 镜像。

## 1. 三个项目，三种角色

| 项目 | 角色 | 主要内容 |
|---|---|---|
| **incensehub.org** | 内容层 | 长文、指南、历史、配方、安全、原料百科 |
| **data.incensehub.org** | 数据库层 | 实体、术语、关系、证据、JSON/CSV 下载 |
| **LanDeng（data.incenseherbs.com）** | 独立项目 | 不合并、不互相引用、不共享品牌主体 |

IncenseHub 的重点不是“再做一个 freight 式商业站”，而是：
- **内容**：可读、可引用、可追溯的英文知识库
- **数据库**：机器可读、可下载、可交叉验证的结构化数据

## 2. 当前资产

### 内容层
- 266 个页面：150 原料、115 blog、1 概念页、其他
- 已有：五层结构、原创资产、来源、FAQ、内链
- 全站相似度 259/266 <0.40；5 篇结构性下限 + 2 个元页面

### 数据库层
- 8 个数据集：ingredients 150 / terminology 249 / relationships 150 记录、806 边 / comparisons 17 / materials 15 / techniques 12 / forms 12 / aroma 10
- 205 个实体页；249 条术语目前只有索引
- JSON、CSV、DefinedTerm JSON-LD、Evidence Tier 1–6
- 已上线：`data.incensehub.org`

## 3. 内容层：下一步做什么

### 3.1 先减后加
- 合并/重写重复页，保留“每页有独有数据或判断”的页面
- 不追求页数；目标 280–320 个高质量页

### 3.2 五个内容簇
1. **Agarwood / 沉香**：分级、产地、造假、红海 vs 海湾贸易
2. **Sandalwood / 檀香**：物种、老山/新山、红檀混淆
3. **History & culture**：香道、宋代、日本接受史、香乘
4. **Materials & craft**：粘合剂、形态、炮制、合香
5. **Safety & buying**：烟、通风、宠物、认证、采购判断

### 3.3 每页标准
- 2,500–5,000 词；8+ 独有数据点
- 1 个 “Our read”；3–5 个失败模式
- 5+ 来源；`last reviewed`
- 句间重叠 <5%；不复制数据站全文

## 4. 数据库层：下一步做什么

### P1
1. **术语页**：249 条中字段足够的生成独立页；其余留在索引
2. **关系浏览**：按 type / entity / 反向边
3. **17 个对比页**：结构化表 + 数据短评
4. **Dataset JSON-LD**：每个数据集页补 Dataset schema
5. **搜索**：实体/术语/数据集可检索
6. **llms.txt + markdown**：AI 入口

### P2
7. **JSON Schema**：每个数据集一份，CI 校验
8. **Changelog / release**：版本、dateModified、变更记录
9. **证据/来源数据集**：把 citations 变成可查询数据
10. **数据短评**：6–10 篇，链回内容页

### 覆盖目标
- 205 实体页 → 覆盖 249 术语（按字段阈值）
- 806 边 → 增加反向边与类型
- 8 数据集 → 10–12（加 sources / evidence / versions）

## 5. 互补规则

- 内容页：叙事、判断、配方、历史；**不复制完整数据集**
- 数据页：定义、属性、关系、证据；**不写长文**
- 统一 `termCode`；内容页 `sameAs` → 实体；实体 `mainEntityOfPage` → 内容页
- 一个实体一个 canonical；不出现两个解释同一实体的页面
- 数据站不做商业页；内容站不做 JSON 大全

## 6. 30 天路线

**Week 1：审计与映射**
- 内容缺口审计：哪些页薄、重复、缺独有数据
- 建立 `termCode` ↔ 内容页映射
- 数据库 schema/关系缺口清单

**Week 2：内容加深**
- 10 篇高价值页重写/加深（沉香、檀香、历史、材料、安全）
- 每篇补 8 个独有数据点 + Our read

**Week 3：数据库补层**
- 术语页（按阈值）
- 关系浏览 + 17 对比页
- Dataset JSON-LD + 搜索 + llms.txt

**Week 4：互链与验收**
- 内容 ↔ 数据双向链接审计
- 断链、孤儿、重复、canonical 检查
- GSC 提交；记录 baseline

## 7. 验收指标
- 内容：280–320 页；80% ≥2,500 词；<0.40；0 orphan
- 数据库：205+ 实体页；249 术语可检索；806 边可浏览；17 对比页
- 互链：每个原料页至少 1 个实体链接；每个实体页至少 1 个内容链接
- AIO：llms.txt、markdown、Dataset/DefinedTerm JSON-LD 全量

## 8. 不做的事
- 不做商业落地页扩量（现有 noindex 页面保留，不进入内容路线）
- 不做 LanDeng 镜像或交叉引用
- 不为了页数生成模板页
- 不在数据站写长文，不在内容站堆 JSON
