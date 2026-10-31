# IncenseHub 澜灯 (incensehub.org) 合规审计报告

- **站点**：incensehub.org（IncenseHub 澜灯 — Chinese Botanical Incense 内容站）
- **仓库**：repos/IncenseHub（Astro · 静态站 · 280 页）
- **主体**：Zhangjiakou Landeng Technology Co., Ltd.（张家口澜灯科技有限公司 · USCC 91130702MAKM4QXH5Q）
- **审计日期**：2026-10-18
- **审计师角色**：合规审计（广告法 / 医药宣称 / CITES 保护物种 / 消费者保护 / 隐私多法域）
- **方法**：逐页扫描 150 个原料实体 + 115 篇博客 + 16 个 Astro 页面 + 法律页 + BaseLayout 主体披露 + 商业页；全文 grep（中/英疗效词、绝对化用语、CITES、analytics/cookie、图片来源）。

---

## 总览（八维结果）

| 维度 | P0 违规 | P1 风险 | P2 建议 | 结论 |
|---|---|---|---|---|
| 1. 医药/疗效宣称 | 0 | 0 | 0 | ✅ 优秀——全站系统性「traditional use vs modern evidence」分层，无违规现代医疗宣称 |
| 2. 广告法（绝对化用语/虚假功效） | 0 | 0 | 1 | ✅ 优秀——零绝对化用语；「best」均为描述性/编辑性用法 |
| 3. CITES / 保护物种 | 0 | 0 | 2 | ✅ 优秀——所有 CITES 物种均附合法性/可持续来源声明 |
| 4. 产品安全披露 | 0 | 0 | 0 | ✅ 优秀——150/150 原料页均有 Safety 段 + 独立 /safety/ 页 |
| 5. 隐私与数据合规 | 0 | 2（已修 1） | 2 | ✅ 良好——已补 WhatsApp 数据收集披露；其余为 P2 |
| 6. 商业宣称核对 | 0 | 0 | 0 | ✅ 优秀——manufacturer/private-label 页「不虚构」原则贯彻彻底 |
| 7. 知识产权/商标 | 0 | 0 | 2 | ✅ 良好——品牌一致、数据集 CC BY-SA 4.0；图片来源声明缺失 |
| 8. 法域映射 | 0 | 0 | 1 | ✅ 良好——受众为英文国际 + 中国主体，法域清单见下 |

**合计：P0 = 0 · P1 = 2（1 项当场修复）· P2 = 8**

---

## 维度 1 — 医药/疗效宣称扫描（P0 重点）

**结论：零违规。** 本站内容质量极高，疗效语言已被系统性处理为三类并严格分层：

1. **纯粹植物学事实** — 独立陈述，无疗效暗示（如「乳香含 boswellic acids」「龙涎香为 ambrein 氧化产物」）。
2. **传统用途引用** — 全部标注「traditional materia-medica language, **not modern clinical evidence**」（如 agarwood 的「行气止痛/温中」、frankincense 的「活血止痛」、jiangzhenxiang 的「主天行时气」）。
3. **违规现代医疗宣称** — **未发现**。扫描了全部中英疗效词：

   - 英文 `therapeutic / treat / cure / heal / sedative / antibacterial / anti-inflammatory / sleep aid / insomnia / anxiety relief / lowers blood pressure / boosts immunity` → 全部命中均为「否认」语境（如 sandalwood FAQ「Does sandalwood help you sleep? — There is no established clinical evidence…」）。
   - 中文 `安神/助眠/抗菌/杀菌/治疗/缓解/消炎/止痛/抗癌/降压/增强免疫` → 仅 3 处命中，且全部是**引用古籍原文后紧接免责标注**（agarwood.md、agarwood-incense.md）。

**免责声明覆盖充分：**
- 每个原料页末有 `*…This is editorial knowledge content, not medical advice.*` 尾注。
- 每篇博客（aromatherapy/mood/sleep/meditation 类）有独立「Compliance Line / Verification Notes」段，明确「no sleep / no anxiety / no medical claims」。
- /safety/ 页有「Traditional use vs medical use」专节。
- 隐私页与 ToS §1 均含「not medical advice」。
- **本次新增 /disclaimer/ 页**，将「informational, not medical advice / traditional vs modern evidence / fragrance purposes only」集中成独立声明页（见「当场修复清单」）。

---

## 维度 2 — 广告法合规（中国广告法 + 国际口径）

**结论：零违规。**

- **绝对化用语**（最佳/第一/顶级/最好/最好/No.1/leading/世界第一/100%/纯天然保证）→ 全站扫描**零命中**为营销性绝对化用语。
- 出现「best」的 30+ 处经上下文核验，**全部为描述性/编辑性用法**，非广告法意义的「最佳」宣称：
  - 「the best material has a buttery smoothness」（品质描述，非「我们是最好」）
  - 「best *entry* recipe / best *documented* classical recipe / best known」（编辑性客观陈述）
  - 「best for」场景匹配（best incense for meditation → 文中明说「There is no single 'best'」）
- **manufacturer 页**主动声明「we make **no ranking claims** (we are not 'the best' or 'the leading' anything)」——广告法合规的反向标杆。
- **「纯天然/无添加/100%」** → 仅命中 2 处，且均为**拆穿性语境**（substitution-cross-reference：「'it's 100% natural' … they have substituted an adjective for a fact」；indian-incense：「'natural' is unregulated」）。
- 虚假功效暗示：无（见维度 1——所有功效类表述均已自证为否认语境）。

---

## 维度 3 — CITES / 保护物种合规（香类站点红线）

**结论：零违规。** 所有 CITES 物种页面均附「Sustainability & sourcing / Conservation」段，声明合法性 + 可持续来源。逐一核验：

| 物种 | 页面 | CITES/保护状态 | 来源声明 | 状态 |
|---|---|---|---|---|
| 沉香 Agarwood (*Aquilaria* spp.) | agarwood.md | CITES II（*A. malaccensis*；属整体列） | ✅「wild vs cultivated，文档化」 | 合规 |
| 檀香 Sandalwood (*Santalum album*) | sandalwood.md | CITES II + 中国二级保护 | ✅「plantation + Australian *S. spicatum*」 | 合规 |
| 红檀香 Red sandalwood (*Pterocarpus santalinus*) | red-sandalwood.md | CITES II（2019） | ✅「monitored and permitted」 | 合规 |
| 麝香 Musk (*Moschus*) | musk.md | CITES（鹿属） | ✅「historical reference only，现代为合成麝香」 | 合规 |
| 龙涎香 Ambergris (*Physeter*) | ambergris.md | CITES（抹香鲸） | ✅「restricted，现代为 ambroxide」 | 合规 |
| 灵猫香 Civet | civet.md | CITES App. III（印度/博茨瓦纳） | ✅「historical only，合成 civetone」 | 合规 |
| 海狸香 Castoreum | castoreum.md | 区域性保护（非 CITES） | ✅「national/regional protected，仅合成」 | 合规 |
| 木香 Costus (*Saussurea costus*) | costus.md | **CITES Appendix I** | ✅「wild trade heavily restricted，cultivated 主流」 | 合规 |
| 甘松 Spikenard (*Nardostachys*) | spikenard-nardostachys.md | CITES App. II | ✅「wild-harvest monitored，wild vs cultivated」 | 合规 |
| 乳香 Frankincense (*Boswellia sacra*) | frankincense.md | CITES checklist 引用 | ✅「over-tapping concern，物种/来源确认」 | 合规 |
| 降真香 Jiangzhenxiang | jiangzhenxiang.md | 提及 *Dalbergia odorifera* 混淆 | ✅ 物种争议显式披露 | 合规 |

**P2 建议（非违规，属完整性）：**
1. `sandalwood.md` 已写 CITES II，但**未明确点出「中国国家重点保护野生植物二级」**（中国境内口径）。建议在「Sustainability & sourcing」段补一句「in China, *Santalum album* is also a state-protected (Grade II) species」。
2. `frankincense.md` 提及 CITES checklist，但 *Boswellia* 部分物种（如 *B. sacra*）近年被建议列入 CITES App. II 的讨论可在来源中补注（非必须）。

---

## 维度 4 — 产品安全披露

**结论：零违规。**

- **150/150 原料页**均有 `## Safety` 段（脚本核验 `total=150 with_safety=150`）。
- 独立 `/safety/` 页内容完整：明火/通风/儿童宠物远离/呼吸道颗粒物提示；「Natural does not mean safe」原则；并集中列出 6 种高危材料（lily-of-the-valley 强心苷毒性、calamus β-asarone、asarum 马兜铃酸、apricot-kernel 苦杏仁苷/氰苷、star-anise 与毒八角混淆、camphor/borneol 不可内服）。
- 博客类焚香指南（how-to-burn-safely、incense-pets-sensitivities、ventilation、smoke-air-quality）均有安全提示并引用 ALA/EPA 室内空气质量来源。

---

## 维度 5 — 隐私与数据合规

**结论：良好，1 项 P1 已当场修复。**

法律页现状：
- ✅ `/privacy-policy/`（存在，2026-09-27）
- ✅ `/terms-of-service/`（存在，2026-09-27）
- ✅ 新增 `/disclaimer/`（本次）
- ⚠️ **无独立 Cookie Policy 页** —— 但因站内**实际零 cookie / 零统计脚本 / 零第三方追踪**（已 grep 源码 + public 全目录，仅 Google Fonts 与 wa.me 外链），「无 Cookie 页」在此语境下为 **P2**，隐私页已声明「No cookies, no trackers, no analytics」且属实。

**P1（已当场修复）：**
- 原隐私页声明「inquiries arrive by **email only**」「no online forms」，但全站头部/页脚/CTA 均有 WhatsApp 按钮（`wa.me/8613323237275`）+ 电话 `+86 13323237275`。原声明与站点实际数据收集渠道**不符**，且未披露 WhatsApp 作为第三方（Meta）处理者。
- **修复**：隐私页补充 WhatsApp/电话数据收集披露 + Meta 第三方条款提示（见「当场修复清单」）。

**P2 建议：**
1. 隐私页未显式提及 GDPR/CCPA。对「触达欧盟/加州受众的 B2B 站」建议补一节「Your rights (EEA/UK GDPR; California CCPA/CPRA)」——当前 email-only 采集规模下风险低，但合规隐私政策通常应具名法域与权利清单。
2. 隐私页词数偏薄（~250 词模板级）。虽与本「零追踪静态站」体量匹配，但若未来上线表单/统计（隐私页已承诺「会先更新本页」），需扩写至 1500+ 词。

---

## 维度 6 — 商业宣称核对

**结论：零违规。** 「不虚构原则」贯彻彻底：

- **manufacturer 页**：显式声明不发布产能/工厂规模/产线数、不宣称认证、不发布固定 MOQ/交期/价格（「confirmed per inquiry」）。并写「We publish **no invented credentials, no fabricated author, and no production statistics**」。
- **private-label 页**：资质宣称全部挂「verify against issuing body」，无证书图片/编号处一律「claims to verify, not badges to assume」。
- **OEM 页**：四步「buyer should verify」流程（sample/spec/documentation/QC process），无「保证/承诺」措辞。
- **wholesale 页**：「What a supplier claim alone cannot establish」段自曝边界。
- 价格/服务承诺措辞：均「on request / per inquiry / not a binding offer」，ToS §2 明确「Nothing on this site constitutes a binding offer」。
- 产能数字：无虚构；「company-provided information」在 manufacturer 页被显式标注来源。

---

## 维度 7 — 知识产权 / 商标

**结论：良好，2 项 P2。**

- **品牌一致性**：`IncenseHub`（285 次）/ `Landeng`（137，含邮箱域名、footer 法律名「Landeng Technology」）/ `landeng`（35，邮箱/URL 前缀）/ `澜灯`（8）——主品牌「IncenseHub」与法律实体「Zhangjiakou Landeng Technology」用法区分正确，无拼写漂移（相比 audit skill 中 DINWEYS 站的 Maju/Mayu 类问题，本站干净）。
- **数据集许可**：`data.incensehub.org` 下 8 个数据集均 CC BY-SA 4.0，knowledge-map / terminology-reference 页明示许可与版本。
- **古籍引用**：香乘（Xiang Cheng）/ 本草纲目（Bencao Gangmu）/ 梦粱录 等均链接 Wikisource / ctext 原文，ToS §3 声明引用规范。

**P2 建议：**
1. **图片来源声明缺失**。全站 200+ 张图片（`/images/*.webp`，含原料静物、工艺步骤图）为本地自产，但**无任何图片出处/生成方式声明**（无 seedream/AI 生成标注、无图注 credit）。按本站「来源透明」定位，建议在 ToS 或 disclaimer 增加一句「product/process images are illustrative still-life photography created for this site」。
2. footer 版权 `© IncenseHub` 与 ToS「© Zhangjiakou Landeng Technology Co., Ltd.」措辞可统一（P2 级一致性问题）。

---

## 维度 8 — 法域映射（合规地图）

**受众推断**：站点为**英文单语**（`grep 中文 src/pages` = 0 命中；原料页中文仅存于 frontmatter/术语字段，非中文站点版本）。故「四语」维度不适用——本站为面向**国际英文受众 + 中国法律主体**的 B2B 内容站。

**适用法域清单：**

| 法域 | 适用依据 | 本站状态 |
|---|---|---|
| 中国《广告法》 | 运营主体为张家口公司 | ✅ 无绝对化用语、无虚假功效 |
| 中国《消费者权益保护法》 | 主体属地 | ✅ 无虚假宣传、主体披露完整（USCC/地址/电话/邮箱） |
| 中国《药品/医疗广告》 | 疗效宣称风险 | ✅ 零医疗宣称，traditional vs modern 分层 |
| 中国《濒危野生动植物进出口管理条例》/《野生植物保护条例》 | CITES + 国家重点保护物种 | ✅ 全 CITES 物种附来源声明（S. album 国内二级保护建议补注 P2） |
| 中国《个人信息保护法》(PIPL) | 处理中国境内/主体个人信息 | ✅ 隐私页披露收集范围；email-only 低风险 |
| 美国 FTC（《联邦贸易委员会法》/健康宣称） | 英文内容触达美国受众 | ✅ 零疗效宣称，符合 FTC 健康宣称要求 |
| 美国 FDA（若产品出口美国） | 燃香/香薰消费品出口 | ✅ 无药品宣称；出口合规由 manufacturer 页「per shipment confirm」覆盖 |
| 欧盟 GDPR | 触达欧盟受众（WhatsApp/email 渠道） | ⚠️ P2：未具名 EEA 权利清单 |
| 美国 CCPA/CPRA | 触达加州受众 | ⚠️ P2：未具名加州权利 |
| 欧盟 CLP（香料过敏原，若产品出口欧盟） | 含精油/香料的产品出口 | ✅ 本站为 B2B 知识站未销售成品；出口考虑由 export-considerations 页覆盖（CLP 属产品合规，非本站内容页职责） |

---

## 当场修复清单（本次 commit）

> 仅补「声明 + 警示」类内容，未删改任何事实性内容。

1. **新增 `/disclaimer/` 页**（`src/pages/disclaimer/index.astro`）——集中法律免责声明：informational not medical advice / traditional vs modern evidence / fragrance purposes only / 燃香安全 / 商业信息非要约 / IP 许可。并在 BaseLayout footer「Compliance」导航加入口。
2. **修复隐私页 WhatsApp 数据披露**（`src/pages/privacy-policy/index.astro`）——原「email only」声明与站点实际 WhatsApp/电话渠道不符，已补：
   - 收集范围改为「by email, or through the WhatsApp / phone channels」；
   - 新增「WhatsApp / phone inquiries」条目，披露收集手机号+内容、用途仅限回复，并注明 WhatsApp 由第三方 Meta 运营、Meta 隐私条款适用。

---

## 待批宣称清单（需你决策后改）

**无。** 本次审计未发现任何需要删改的宣称类 P0 违规（疗效宣称 / 绝对化用语 / 保护物种缺失声明均为 0）。

以下为**可选 P2 增强项**（不改不违规，改则更完善）——是否执行请指示：

1. `sandalwood.md` 补「中国国家重点保护野生植物二级」注明（维度 3-P2-1）。
2. 隐私页补 GDPR/CCPA 权利清单（维度 5-P2-1）。
3. ToS 或 disclaimer 补图片来源/生成方式声明（维度 7-P2-1）。
4. footer 版权主体名统一（维度 7-P2-2）。

---

## 修复验证

- `npm run build` ✅ 280 页构建通过，`/disclaimer/` 已进入 sitemap。
- 隐私页 2 处替换 + footer 1 处替换已生效。

---

## 结论

IncenseHub 站点是**罕见的高合规内容站**：在疗效宣称、广告法、CITES、安全披露、商业宣称五个红线维度上实现了**系统性、零违规**的编辑纪律（「traditional use vs modern evidence」分层 + 「not medical advice」尾注 + 「不虚构」商业原则贯穿全部 280 页）。本次审计仅发现 2 项 P1（其中 WhatsApp 隐私披露已当场修复；另一项并入 GDPR P2 建议）与 8 项 P2 建议。无待批宣称删改项。
