# 09 — URL 整改清单（Remediation Plan）

## 一、执行原则（红线）

- 只读审计，**本清单为计划，不执行任何发布/删页/noindex/改源码**。
- 不批量删页、不批量 noindex、不合并 URL，除非逐页证据支持。
- 每个问题一个任务，字段：ID / 严重程度 / 证据 URL / 问题与原文证据 / 为何影响用户价值或搜索质量 / 需修改字段或段落 / 推荐整改方法 / 预期效果 / 风险副作用 / 验收标准 / 是否需 GSC 或上线后验证。
- 禁止把低流量页标删除；禁止把相似自动等同垃圾。

---

## 二、P0 立即排查（抓取/索引/规范化）

**结论：无 P0 项。** 抓取/索引/规范化均健康（robots 全允许、sitemap 279 URL、canonical 正确、无 noindex、meta description 0 重复、抽查页全 200）。

---

## 三、P1 优先改善（2 项）

### P1-01 补齐 ingredient/concept 页日期信号
- **严重程度**：High
- **证据 URL**：/ingredients/{任意 slug}/（150 页）、/chinese-incense/（concept）
- **问题与证据**：150 ingredient 与 1 concept 页 frontmatter 无 `last_reviewed`，页面 schema 无 `dateModified`/`datePublished`；而 115 blog 页有 `last_reviewed` 且 blog/[slug].astro 输出 `dateModified`。→ 全站日期信号不一致。
- **为何影响**：新鲜度信号是 Google 对信息型内容信任的组成部分；缺失日期会让"常青知识页"无法体现维护痕迹（对 YMYL 邻近内容尤甚）。
- **需改字段**：ingredient/concept frontmatter 增加 `last_reviewed`（**如实填写实际审核日期，不得伪造**）；[slug].astro 输出 `dateModified`。
- **推荐方法**：参照 docs/content-freshness-policy.md，按 Tier 回填真实审核日期（T1=90 天、T2=180 天、T3=触发式），**不批量统一刷同一个假日期**。
- **预期效果**：新鲜度信号一致；利于 E-E-A-T。
- **风险副作用**：若回填日期不真实，反而违反"日期真实性"（政策明令禁止）。**必须逐页真实审核后回填。**
- **验收标准**：150 ingredient + 1 concept 页 schema 出现真实 `dateModified`；无"统一假日期"。
- **是否需验证**：否（技术侧改动，构建即可见）；但建议 GSC 观察收录趋势。

### P1-02 部署与 GitHub 仓库同步
- **严重程度**：Medium
- **证据 URL**：线上 /disclaimer/（200）、线上 robots.txt（含十余 AI bot Allow）；本地 `grep -rl disclaimer src/` 为空、`public/robots.txt` 仅有 `User-agent: * Allow: /`
- **问题与证据**：生产环境领先于 origin/main（/disclaimer/ 页 + robots.txt 未入库）。git 分支 "up to date with origin/main"，说明这些变更是**未提交/未推送**的。
- **为何影响**：部署治理风险——无法用 Git 还原线上状态，回滚会丢失 disclaimer 页；也影响后续审计的源码-线上一致性。
- **需改**：把线上 /disclaimer/ 页与 robots.txt 变更提交到仓库（属运维动作，非本审计执行）。
- **推荐方法**：核对线上 dist 与 Cloudflare Pages 部署源，把 disclaimer.astro 页面 + 更新后的 robots.txt 提交并推送。
- **预期效果**：仓库与生产一致，可审计可回滚。
- **风险副作用**：低（纯同步）。
- **验收标准**：`git status` 干净且 origin/main 含 disclaimer 页与完整 robots.txt。
- **是否需验证**：否。

---

## 四、P2 长期建设（4 项）

### P2-01 powder-vs-chips 组差异化加固
- **严重程度**：Medium
- **证据 URL**：/blog/incense-powder-vs-wood-chips/ 与 /blog/agarwood-powder-vs-chips/
- **问题与证据**：两页共用"同材两形/表面积决定释放/粉=制香、片=品香"框架，段落结构相似度高于其他组（最接近重复的一组）。
- **为何影响**：可能被误判为近似页，稀释两页各自排名潜力。
- **推荐方法**：generic 页开头加一句明确的层级指引（"沉香专项见 agarwood-powder-vs-chips"）；agarwood 页强化"奇楠粉末=诈骗信号"这一独占增量，减少与 generic 页的框架性重复段落。
- **预期效果**：两页意图边界更清晰。
- **风险副作用**：低。
- **验收标准**：两页标题/首段/FAQ 明确指向各自材质范围，无大段同构。
- **是否需验证**：否（内容改动）。

### P2-02 E-E-A-T 署名信号强化
- **严重程度**：Medium
- **证据 URL**：全部 115 blog 页 `author: "Landeng Tech Team"`；/blog/landeng-editorial-methodology/
- **问题与证据**：作者统一为团队名，无个人署名/资质/方法论作者。这不是虚假（是诚信），但 E-E-A-T 署名信号偏弱。
- **推荐方法**：增设"编辑团队"页说明真实团队构成与专业背景（**真实、不虚构个人**）；方法论页补"审核流程 + 来源准入标准"。
- **预期效果**：强化 E-E-A-T，不引入虚假资历。
- **风险副作用**：若虚构专家身份则反而违规——**必须真实**。
- **验收标准**：新增编辑团队/方法页，内容真实可核。
- **是否需验证**：否。

### P2-03 "natural ≠ smoke-free" 观点复用去重
- **严重程度**：Low
- **证据 URL**：/blog/incense-safety-guide/、/blog/incense-smoke-air-quality-evidence/、/blog/incense-pets-sensitivities/、3 个 vs 对比页
- **问题与证据**："自然≠无烟"这一纠偏框架在 5+ 页重复展开。
- **为何影响**：轻度冗余（非重复内容、非蚕食），仅增加维护面。
- **推荐方法**：指定 smoke-air-quality 页为该观点的权威出处，其余页改为一句+内链引用，不再逐页大段展开。
- **预期效果**：降低冗余、强化权威页。
- **风险副作用**：低。
- **验收标准**：非权威页该观点收敛为一句话+内链。
- **是否需验证**：否。

### P2-04 外链/权威积累（配合冷启动诊断）
- **严重程度**：Medium
- **证据 URL**：无 GSC/外链数据（见 11 号）
- **问题与证据**：新域名缺乏权威与反链，是曝光趋零的最可能主因（非内容）。
- **推荐方法**：内容之外，规划高质量外链获取（行业目录、香料/植物学社群、B2B 平台、数据站 citation 反向传播）。
- **预期效果**：缓解冷启动。
- **风险副作用**：若用机械外链/垃圾外链则触发反效果——**必须白帽**。
- **验收标准**：GSC 中外链与权威指标改善。
- **是否需验证**：是（需 GSC 数据）。

---

## 五、逐 URL 操作结论

| 范围 | 操作 | 数量 |
|---|---|---|
| 150 ingredient 页 | KEEP | 150 |
| 115 blog 页 | KEEP（其中 powder-vs-chips 组 2 页 P2 微调） | 115 |
| 1 concept 页 | KEEP | 1 |
| 静态页 | KEEP | 14 |
| **REMOVE** | 无 | 0 |
| **NOINDEX** | 无 | 0 |
| **REDIRECT** | 无 | 0 |
| **MERGE** | 无 | 0 |

**无任何 URL 需要删除、noindex、重定向或合并。** 这符合"禁止把低流量页标删除、禁止把相似自动等同垃圾"的红线。
