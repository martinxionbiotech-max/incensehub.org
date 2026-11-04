# IncenseHub (incensehub.org) 合规页面检查 + 优化批

- **站点**：incensehub.org（IncenseHub IncenseHub — Chinese Botanical Incense 内容站）
- **仓库**：repos/IncenseHub（Astro · 静态站 · 282 页）
- **主体**：IncenseHub（张家口IncenseHub科技有限公司 · USCC 91130702MAKM4QXH5Q）
- **日期**：2026-10-23
- **角色**：合规法律内容编辑 + 技术 SEO
- **任务**：对齐六页基线（about/contact/privacy/terms/cookies/disclaimer 条款级 1500–2200 · 主体一致 · 零虚构）

---

## 一、检查结果（六页矩阵）

| 页面 | 状态 | 词数（正文去标签） | 主体披露 | 条款覆盖 | 追踪脚本如实 |
|---|---|---|---|---|---|
| about | **新建** | 1504 | ✅ Zhangjiakou Landeng + USCC + 地址 + 联系 | ✅ 平台定位 / 商业服务 / 编辑团队与方法论 / 编辑红线 / 配图声明 | — |
| contact | **增厚**（157→1538） | 1538 | ✅ 法律实体 + USCC + 地址 | ✅ 四类询价 / 三渠道 / 响应预期 / 纠错通道 / 不做什么 | — |
| privacy-policy | 已有（10-21 深化） | 1532 | ✅ | ✅ 13 条（收集/不收集/cookie/第三方/留存/跨境/权利/儿童/安全/变更/联系） | ✅ 无追踪（grep 实测 0 命中） |
| terms-of-service | 已有（10-21 深化） | 1524 | ✅ | ✅ 13 条（接受/性质/知识产权/行为/商业/链接/免责/责任/赔偿/终止/变更/法域/可分割） | — |
| cookies | **新建** | 1503 | ✅（邮箱） | ✅ 无追踪 cookie / 单一 webfont 请求 / 日志 / DNT / 浏览器管理 / 法域 / FAQ | ✅ 无追踪 cookie（如实） |
| disclaimer | 已有（10-21 深化） | 1564 | ✅ | ✅ 12 条（范围/非医疗/传统vs证据/非专业建议/责任/准确性/链接/版权/商业/配图/法域/纠错） | — |

**追踪脚本实扫**：`grep -rniE "gtag|googletagmanager|analytics|plausible|fathom|matomo|umami|hotjar|fbq|clarity|facebook" src public` → **0 命中**（`clarity` 命中均为原料页英文单词 "clarity"，非追踪脚本）。站内唯一第三方请求 = Google Fonts（`fonts.googleapis.com` / `fonts.gstatic.com`）+ Cloudflare 托管（`public/_headers` 实据）。

**与 10-21 深化版不冲突不回归**：disclaimer/privacy/terms/safety 四页仅改日期（10-21→10-23）+ 补互链 + 统一「六页法律公司集」口径（原「four legal pages」表述已合并为单段六页表述），未改动既有条款实质。

---

## 二、优化项清单

### 1. contact 增厚（157 → 1538 词）
- 询价/商业联系主渠道：Email（incensehubltd@gmail.com，主渠道）+ WhatsApp/电话/WeChat（+86 13323237275，如实注明 Meta 条款适用）——**如实沿用站点现有触点**。
- 新增：语言/时区、四类询价明细、各商业路径入口（wholesale/OEM/private-label/samples）、「写信后流程」、编辑纠错通道（含「纠正≠删除」声明）、「不做什么」（含「不编造客户案例/证言」）、FAQ（MOQ/sample/store）。
- 互链：六页 + request-a-quote + 商业页。

### 2. 新建 cookies 页（1503 词）
- 如实分类：**无追踪/分析/广告/功能 cookie**、无社交 widget → 无 cookie 横幅、无需同意。
- 单一第三方请求 = Google Fonts webfont（如实说明非我方所设 cookie，Google 隐私政策适用）；Cloudflare 访问日志（server-side，非 cookie）。
- 管理方式：浏览器设置路径（Chrome/Firefox/Safari/Edge）+ 私密模式 + 阻断 webfont 时优雅降级系统字体。
- 与 privacy §4 交叉引用（privacy 已补 cookies 页链接）。

### 3. 新建 about 页（1504 词）
- 平台定位：知识平台 + 制造商/供应商目录（如实：品牌/产品目录/私人定制 = wholesale/OEM/private-label 三路径）。
- **主体披露**：IncenseHub（张家口IncenseHub科技有限公司）+ USCC + 完整地址 + 邮箱 + 电话（与 BaseLayout Organization schema、footer、manufacturer 页三处一致）。
- 编辑团队与方法论：集体 byline「IncenseHub Editorial Team」、无虚构作者/专家、八步法 + 六档证据层级 → 互链 `/blog/incensehub-editorial-methodology/`。
- 互链：contact / methodology / manufacturer / 六页。

### 4. 一致性
- 六页口径/主体/联系/日期（2026-10-23）统一；互链齐全（每页 Related pages 含其余页）。
- 页脚 nav：Company 组加 About；Compliance 组加 Cookie Policy。
- schema Organization 与真实主体一致（未回归）：legalName / USCC / 地址 / incensehubltd@gmail.com / +86 13323237275。
- AI 配图声明保持（disclaimer §10 + about 专节）。

---

## 三、零虚构核对

- ✅ **主体**：全部沿用 IncenseHub + USCC 91130702MAKM4QXH5Q + 完整地址（与 footer/schema/methodology 一致）。
- ✅ **联系**：沿用站点现有 incensehubltd@gmail.com / +86 13323237275 / wa.me/8613323237275。**未引入外部提供的 joanna@dinweys.com / +8615153588090**（该值属姊妹站 DINGWEY battery，非本站在用值——已按「以站点现有为准」原则弃用，全站 grep 无 dinweys/joanna 残留）。
- ✅ **追踪**：cookies 页如实写「无追踪 cookie」（grep 实测 0 命中），未虚构 cookie 页/横幅/同意机制。
- ✅ **无虚构**：无编造作者/专家/证书/产能/客户案例/MOQ 固定值；无编造仲裁机构；责任上限按真实口径（免费信息免责 + 交易实付金额上限 + 法定不可排除不排除）。
- ✅ **争议解决**：协商优先 + 运营地法院（张家口），无虚构仲裁机构。

---

## 四、build / commit

- `npm run build`：✅ **282 页**构建成功（exit 0，`[build] Complete!`），`about`/`cookies`/`contact` 三页均渲染。
- 渲染验证：七页 h1 + `Last updated: 2026-10-23` 一致；footer nav 含 About + Cookie Policy；sitemap 含 `/about/`、`/cookies/`、`/contact/`。
- 逐页 commit + push：见 git 记录。
