# 02 — URL 清单（URL Inventory）

## 一、来源与交叉

URL 清单来自三条独立来源，交叉核验：
1. **线上 sitemap**：https://incensehub.org/sitemap-index.xml → sitemap-0.xml（200）
2. **线上 robots.txt**：https://incensehub.org/robots.txt（200，全允许 + sitemap 声明）
3. **本地源码仓库**：/home/openclaw/IncenseHub（Astro，`src/content/` + `src/pages/` + `astro.config.mjs`）

---

## 二、URL 总数与分类统计

| 分类 | 数量 | 说明 |
|---|---|---|
| **A 香材实体页（ingredients）** | 150 | /ingredients/{slug}/，Agarwood→Zedoary |
| **B/C/D/E/F 知识/教程/安全/对比/B2B（blog）** | 115 | /blog/{slug}/ |
| **G 目录/索引页** | 3 | /、/ingredients/、/blog/ |
| **H 首页/分类辅助页（静态）** | 11 | /chinese-incense/ /contact/ /incense-manufacturer/ /oem/ /privacy-policy/ /private-label/ /request-a-quote/ /safety/ /terms-of-service/ /wholesale/ /disclaimer/ |
| **合计（线上 sitemap）** | **279** | 150 + 115 + 14 静态（含 /disclaimer/） |

> 本地仓库可生成 URL = **278**（无 /disclaimer/，因为 `src/pages/` 无 disclaimer 页面）。差异 1 条，见「sitemap 与仓库差异」。

### blog 115 篇按内容类型粗分（依据 frontmatter `content_type`/`pillar`/标题）
- 比较/购买指南（E）：约 25 篇（vs 系列、对比矩阵、如何选购、礼赠指南等）
- 安全/健康/宠物（D）：约 12 篇（safety-guide、smoke-air-quality、pets、ventilation、burn-safely、storage 等）
- 历史文化术语（B）：约 20 篇（history、four-leisure-arts、boshan-censer、xiangpu-manuals、terminology 等）
- 教程/燃烧方法（C）：约 20 篇（how-to-burn、how-incense-is-made、gehuo-fenxiang、seal、formats 等）
- 制造/OEM/B2B（F）：约 15 篇（oem、private-label、wholesale、factory-vetting、moq、packaging、spec-sheet、sourcing 等）
- 香材专题（A/B 交叉）：约 20 篇（agarwood-incense、sandalwood-incense、qinan、lavender、frankincense 等）

> 上述粗分为人工归类，用于体量判断，非精确台账；精确逐页字段见下方抽查表与 working 目录。

---

## 三、抓取/验证结果

- sitemap-index.xml：HTTP 200
- sitemap-0.xml：HTTP 200，含 279 个 `<loc>`
- robots.txt：HTTP 200，全允许（并显式 Allow Google-Extended/GPTBot/OAI-SearchBot/ClaudeBot/PerplexityBot 等）
- 线上抽查代表页（均 200，canonical 正确）：

| URL | HTTP | Title | Meta description（首段） | Canonical |
|---|---|---|---|---|
| / | 200 | IncenseHub IncenseHub — Chinese Botanical Incense Knowledge | A research-led English-language knowledge platform… | https://incensehub.org/ |
| /ingredients/agarwood/ | 200 | Agarwood (沉香) — Grades & Fakes — IncenseHub Ingredients | 沉香 (chénxiāng) is an ingredient from Aquilaria spp., with an aroma profile of woody, resinous, sweet… | https://incensehub.org/ingredients/agarwood/ |
| /blog/incense-smoke-air-quality-evidence/ | 200 | Incense Smoke & Air Quality: The Evidence — IncenseHub | At a glance: Yes, incense smoke measurably degrades indoor air — and the honest headline number… | https://incensehub.org/blog/incense-smoke-air-quality-evidence/ |
| /disclaimer/ | 200 | Disclaimer — IncenseHub | （正文页） | — |

- data 子站：data.incensehub.org（200）、/ingredients/（200）、/datasets/terminology.json（200）
- 重定向：/data/ingredients.json → data.incensehub.org/datasets/ingredients.json（301，_redirects 生效）

---

## 四、sitemap 与仓库差异（关键发现）

1. **线上 sitemap 含 `/disclaimer/`，本地仓库无此页**：`grep -rl "disclaimer" src/` 返回空；`src/pages/` 无 disclaimer。→ 生产环境领先于 GitHub 仓库（origin/main 落后于生产）。
2. **线上 robots.txt 比本地 `public/robots.txt` 更完整**：本地仅有 `User-agent: * Allow: /`；线上额外显式列出十余个 AI bot 的 Allow 指令。→ 同上，生产有未入库的 robots.txt 更新。
3. 二者均不影响抓取/索引（都是允许抓取），但**是部署治理风险**（详见 08/09）。

---

## 五、规范化与索引信号（全站级）

- **robots**：无 Disallow，无 noindex；显式 Allow AI 爬虫（正向）。
- **X-Robots-Tag（_headers）**：`index, follow, max-snippet:-1, max-image-preview:large`（全站，无 noindex）。
- **canonical**：BaseLayout 统一生成 `new URL(pathname, site)`，抽查 3 页均正确。
- **meta description**：三种来源（ingredient 的 directAnswer / blog 的正文提炼 / 静态页手写），此前审计（docs/aio-audit.md G13）确认 **262 页 0 重复**。
- **结构化数据**：Organization + WebSite（BaseLayout 全站）；ingredient 页 DefinedTerm+BreadcrumbList+FAQPage；blog 页 Article+BreadcrumbList+FAQPage。无 Product/Review/AggregateRating（无虚构评分）。

---

## 六、HTTP 状态 / 重定向 / noindex 汇总

| 项 | 结果 |
|---|---|
| 失败抓取数 | 0（抽查的线上 URL 全部 200） |
| 重定向 | 4 条（/data → data 子站，_redirects 声明，正常） |
| noindex 页面 | 0 |
| 404 | 仅 /404.html（正常） |

> 说明：本次为**抽样抓取**（代表页 4 个 + data 子站 3 个 + 重定向 1 个），未对 279 URL 全量逐条抓取（受节流约束）。正文逐字核查覆盖 6 ingredient + 12 blog + 1 concept = 19 篇 + 全量程序化扫描 266 内容源。具体抽样范围与"未逐页抓取"的边界在 11 号文档如实记录。
