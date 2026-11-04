# 07 — 内容架构审计（Content Architecture）

## 一、主题定位与覆盖

本站主题定位清晰，六大主题方向（对照审计规格 E）：

| 主题 | 覆盖 | 载体 |
|---|---|---|
| 中国植物香材 + 物种分类 | 150 ingredient 页，每页 GBIF/Flora of China 分类 + 中文名/拼音/学名 | ingredients 集合 |
| 香材历史与合香 | history、four-leisure-arts、xiangpu-manuals、hexiang-blending-system、多篇香方 | blog |
| 鉴别分级 | agarwood-grading、qinan-kyara、authentication-database、substitution-cross-reference | blog |
| 制作使用 | how-incense-is-made、powder/chips、burners-tools、seal、formats | blog |
| 燃烧安全科学 | smoke-air-quality、ventilation、safety-guide、pets、burn-safely | blog + /safety/ |
| OEM B2B | oem、private-label、wholesale、factory-vetting、moq、spec-sheet、sourcing | blog + 5 个静态页 |

主题聚焦、无"无关主题铺页面"。**未发现**为凑量而做的偏离主题页面。

---

## 二、核心页与内链合理性

- **核心 hub 页**：/（首页）、/chinese-incense/（支柱）、/ingredients/（百科索引）、/safety/（安全）、/wholesale/ /oem/ /private-label/ /incense-manufacturer/（B2B）。
- **内链类型**：
  - **知识关系链**：ingredient 页通过 `related[]` 互链（如 agarwood↔sandalwood↔frankincense），且内容正文内用「See [x]」指向真正相关的页。
  - **hub-spoke 链**：safety-guide 页底有完整 cluster directory（5 个安全相关页互链）；vs-candles hub 链到 4 个对比页。
  - **实体↔专题链**：ingredient 页链到对应 blog 专题（agarwood→agarwood-grading/incense），blog 反向链回实体页。
- **机械互链检测**：`[how incense is made]` 链接仅出现在 42/150 页（工艺相关），`[wholesale guide]` 仅 34/150（采购相关）——说明内链是**按相关性触发**，非全站机械互链。
- **数据层链**：每 ingredient 页链到 `data.incensehub.org/ingredients/#{slug}`（机器可读实体记录）；页脚链到 data 子站 8 数据集。

**结论：内链为知识关系型 + hub-spoke 型，非机械互链。**

---

## 三、商业页真实性（F 类 B2B）

抽查 /oem/ /wholesale/ 对应的 blog 页（oem-vs-private-label、oem-private-label-guide、wholesale-guide、factory-vetting、moq、spec-sheet）：

- **真实服务**：明确区分 OEM（按规格开发）vs Private Label（贴牌现有产品）vs Wholesale（批量采购），服务描述具体、可落地。
- **无虚假采购信号**：**明确声明"无价目表、无固定 MOQ、按项目报价"**（多页重复），并明示"本页无伪造资质/认证/产量/客户案例"（见 /disclaimer/ 第 4 条）。
- **采购实务知识真实**：配方所有权、打样迭代、brief 清单、供应商验厂——为真实 B2B 实务，非虚饰。

**结论：商业页真实、无虚假资质/案例。** 组织信息（公司名/地址/统一社会信用代码 91130702MAKM4QXH5Q/电话/邮箱）在 BaseLayout Organization schema 与页脚一致，具备企业实体可信度（E-E-A-T 正向）。

---

## 四、作者/编辑方法/参考/修订可信度

- **作者署名**：统一 "IncenseHub Editorial Team"（115 blog）+ 页脚企业实体。**不伪造专家/个人作者/头衔/经历**——这是诚信（但 E-E-A-T 署名信号偏弱，见 P2）。
- **编辑方法**：/blog/incensehub-editorial-methodology/ 明确声明"传统/证据/贸易术语分层 + 来源透明 + 不伪造评分"。方法可审计。
- **参考**：逐页 "Evidence & Sources" + "Sources" + 证据分层表（Established / Historically documented / Trade terminology / Practical screening / Requires testing / Not established）。
- **修订可信度**：blog 页有 `last_reviewed` 日期；docs/content-freshness-policy.md 定义分 Tier 复审节奏与 6 类触发条件，并**明令"不得为刷新而刷日期"**。→ 诚信的更新治理。
- **缺失**：ingredient/concept 页无日期信号（P1，见 09）。

---

## 五、夸大资历 / 伪造经验检测

- 无"X 年经验""权威专家""获奖""检测报告编号"等虚构资历。
- 无伪造客户案例、销量、产能数字。
- "The Author's Take" 段落统一标注"*This is the author's editorial view…not a verified fact.*"，把观点与事实严格隔离。

**结论：无夸大资历、无伪造经验。**

---

## 六、架构层面的改进建议

| 级别 | 建议 |
|---|---|
| P1 | 补齐 ingredient/concept 页日期信号（dateModified/datePublished），与 blog 页一致 |
| P2 | 增设署名方法论页的"编辑团队资质"说明（真实团队，非虚构个人），强化 E-E-A-T |
| P2 | 首页/支柱页增加"更新日期 + 编辑方法"的可视信任信号 |

架构层面**无阻断性问题**。主题聚焦、内链合理、商业页真实、方法论可审计。
