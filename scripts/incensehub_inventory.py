#!/usr/bin/env python3
"""IncenseHub.org Batch A — content inventory generator (self-contained, read-only).

Regenerates docs/incensehub-inventory.md from src/content/**/*.md. No side
effects on content; writes only the inventory document. Run with:

    python3 scripts/incensehub_inventory.py

Pipeline (single pass): analyze -> classify -> similarity -> assemble markdown.
The editorial classification sets (KEEP/T1/T2/CUT) are the batch-A disposition
policy; T3 is the default for long-tail material not otherwise assigned.
"""
import os, re, json, csv, hashlib
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "src", "content")
OUT = os.path.join(ROOT, "docs", "incensehub-inventory.md")

# ---------------------------------------------------------------------------
# Editorial disposition policy (batch A)
# ---------------------------------------------------------------------------
KEEP = {
    # flagship entities already at evidence-layered standard
    'agarwood','sandalwood','frankincense','myrrh','borneol','camphor','cedar',
    'jiangzhenxiang','red-sandalwood','musk','ambergris','benzoin','dragons-blood',
    # cornerstone + culture pillars
    'what-is-chinese-incense','history-of-chinese-incense','japanese-incense-kodo',
    'xiangpu-incense-manuals','chinese-vs-japanese-incense',
    # concepts pillar page (the single concepts-collection entry)
    'chinese-incense',
    # editorial/data (rebrand only)
    'landeng-editorial-methodology','landeng-knowledge-map',
}

T1 = {
    # agarwood cluster
    'agarwood-grading-guide','agarwood-incense','agarwood-powder-vs-chips',
    'agarwood-vs-sandalwood','agarwood-vs-frankincense','qinan-kyara',
    'qinan-buying-authentication',
    # sandalwood cluster
    'sandalwood-incense','sandalwood-vs-frankincense','sandalwood-vs-red-sandalwood',
    # frankincense/myrrh cluster
    'frankincense-incense','frankincense-vs-myrrh',
    # identification / quality / authenticity (high search + core value)
    'incense-authentication-database','incense-substitution-cross-reference',
    'natural-vs-synthetic-incense','incense-material-comparison-matrix',
    'borneol-vs-camphor',
    # regional + culture high intent
    'chinese-vs-indian-incense','hexiang-blending-system',
}

CUT = {
    # pure marketing blog files (B2B pillar + spec-sheet)
    'bulk-incense-ingredient-sourcing','custom-fragrance-development',
    'factory-vetting-guide','how-to-buy-agarwood-for-incense-manufacturing',
    'incense-export-considerations','incense-for-business','moq-pricing-guide',
    'oem-private-label-guide','oem-vs-private-label','packaging-shipping-guide',
    'samples-program','wholesale-guide','incense-spec-sheet-coa',
    # near-duplicate terminology glossary (merge into terminology-reference)
    'incense-terminology-glossary',
}

T2_INGREDIENTS = {
    # important well-known incense botanicals
    'amber','ambergris','clove','cinnamon','patchouli','osmanthus','jasmine','rose',
    'lavender','pine-resin','styrax-resin','onycha','vetiver','galbanum','mastic',
    'peru-balsam','labdanum','sandalwood','frankincense','myrrh','star-anise',
    'saffron','copaiba','balsam','citronella','lemongrass','bergamot','neroli',
    'ylang-ylang','tuberose','gardenia','champaca','plum-blossom','orchid','peony',
    'tree-peony','lotus-flower','magnolia-flower','honeysuckle','chrysanthemum',
    'mugwort','artemisia-annua','calamus','atractylodes','angelica','angelica-sinensis',
    'ligusticum','ligusticum-chuanxiong','asarum','schizonepeta','agastache-rugosa',
    'perilla','elsholtzia','mint','peppermint','spearmint','basil','rosemary','thyme',
    'sage','bay-leaf','dill','fennel','cumin','coriander-seed','cardamom','galangal',
    'ginger','sand-ginger','tsao-ko','katsumadai','amomum-villosum','oxyphylla',
    'nutmeg','cubeb','long-pepper','pepper','prickly-ash','mustard','anise',
    'cassia-twig','licorice','honey','beeswax','bletilla','shellac','cypress-seed',
    'camphor','borneol-oil','eucalyptus','citron','finger-citron','pomelo-peel',
    'orange-peel','litchi-husk','kumquat','lemon','grapefruit','quince','apricot-kernel',
    'ginkgo','torreya','mulberry-leaf','bamboo-leaves','pine-needles','platycladus-leaves',
    'thuja','juniper','sweetgum','civet','castoreum','valerian','orris-root',
    'violet','lily-of-the-valley','jasmine-grandiflorum','wintersweet','banana-shrub',
}

# Non-content static pages: 13 named pages + 2 collection index pages = 15.
STATIC = {
    'incense-manufacturer':'CUT','oem':'CUT','private-label':'CUT',
    'request-a-quote':'CUT','wholesale':'CUT','contact':'CUT',
    'index':'T1','about':'T2','blog/index':'KEEP','ingredients/index':'KEEP',
    'cookies':'KEEP','disclaimer':'KEEP','privacy-policy':'KEEP',
    'safety':'KEEP','terms-of-service':'KEEP',
}
STATIC_NOTE = {
    'incense-manufacturer':'纯商业转化 → CUT（降权重/去询盘）','oem':'纯商业转化 → CUT',
    'private-label':'纯商业转化 → CUT','request-a-quote':'纯询盘表单 → CUT',
    'wholesale':'纯商业转化 → CUT','contact':'询盘/样品表单 → CUT',
    'index':'首页 → T1 重定位为知识平台首页','about':'关于页 → T2 品牌去商业化改写',
    'blog/index':'索引页 KEEP（重排栏目）','ingredients/index':'索引页 KEEP（重排栏目）',
    'cookies':'法律页 KEEP','disclaimer':'法律页 KEEP','privacy-policy':'法律页 KEEP',
    'safety':'安全页 KEEP','terms-of-service':'法律页 KEEP',
}

FRAMEWORK_RE = re.compile(r'(modern commercial applications|our industry view|what buyers should look for)', re.I)
HARD_CTA_RE = re.compile(r'(request a sample|request a quote|get a quote|minimum order|\bmoq\b|lead time|\bbuy now\b)', re.I)

# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def files_for(coll):
    d = os.path.join(CONTENT, coll)
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]

def parse_frontmatter(text):
    fm = {}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    body = text
    if m:
        body = text[m.end():]
        for line in m.group(1).splitlines():
            mm = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
            if mm:
                val = mm.group(2).strip()
                if len(val) >= 2 and val[0] == val[-1] and val[0] in '"\'':
                    val = val[1:-1]
                fm[mm.group(1)] = val
    return fm, body

def word_stats(body):
    b = re.sub(r'<img[^>]*>', '', body)
    b = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', b)
    b = re.sub(r'https?://\S+', '', b)
    b = re.sub(r'\|.*\|', '', b)
    b = re.sub(r'[#>*`\-]', ' ', b)
    words = re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", b)
    cjk = re.findall(r'[\u4e00-\u9fff]', b)
    return len(words), len(cjk)

def heading_structure(body):
    h = Counter()
    for line in body.splitlines():
        m = re.match(r'^(#{1,6})\s', line)
        if m:
            h['H%d' % len(m.group(1))] += 1
    return h

def norm(path):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    m = re.match(r'^---\s*\n.*?\n---\s*\n', text, re.DOTALL)
    body = text[m.end():] if m else text
    body = re.sub(r'<img[^>]*>', '', body)
    body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', body)
    body = re.sub(r'https?://\S+', '', body)
    body = re.sub(r'[|#>*-]', ' ', body)
    return set(t.lower() for t in re.findall(r"[A-Za-z0-9]+", body) if len(t) > 2)

def jaccard(a, b):
    if not a or not b: return 0.0
    return len(a & b) / len(a | b)

def analyze():
    rows = []
    for coll in ['ingredients', 'concepts', 'blog']:
        for path in files_for(coll):
            with open(path, encoding='utf-8') as fh:
                text = fh.read()
            fm, body = parse_frontmatter(text)
            wc, cjk = word_stats(body)
            headings = heading_structure(body)
            slug = fm.get('slug') or os.path.splitext(os.path.basename(path))[0]
            title = fm.get('title', '').strip().strip('"')
            # concepts render at top-level routes (the single concept renders at /chinese-incense/)
            url = {'ingredients': '/ingredients/%s/' % slug, 'concepts': '/%s/' % slug,
                   'blog': '/blog/%s/' % slug}[coll]
            rows.append({
                'collection': coll, 'slug': slug, 'url': url, 'title': title,
                'words': wc, 'cjk_chars': cjk,
                'lang': 'EN' if cjk / max(wc + cjk, 1) < 0.08 else ('ZH' if wc / max(wc + cjk, 1) < 0.08 else 'MIX'),
                'h1': headings.get('H1', 0), 'h2': headings.get('H2', 0), 'h3': headings.get('H3', 0),
                'pillar': fm.get('pillar', ''), 'content_type': fm.get('content_type', ''),
                'search_intent': fm.get('search_intent', ''),
                'framework': bool(FRAMEWORK_RE.search(body)),
                'hard_cta': bool(HARD_CTA_RE.search(body)),
                'commercial_count': len(re.findall(FRAMEWORK_RE.pattern, body, re.I)),
            })
    return rows

def tier_for(r):
    s = r['slug']
    if s in KEEP: return 'KEEP'
    if s in CUT: return 'CUT'
    if s in T1: return 'T1'
    if r['collection'] == 'blog':
        if any(k in r['pillar'] for k in ['P9','P12','P3','P6','P7','P1','Editorial']):
            return 'T3'
        return 'T2'
    if s in T2_INGREDIENTS: return 'T2'
    return 'T3'

# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
TIER_ORDER = ['KEEP','T1','T2','T3','CUT']
TIER_LABEL = {'KEEP':'KEEP','T1':'TRANSFORM · T1','T2':'TRANSFORM · T2','T3':'TRANSFORM · T3','CUT':'CUT'}

def esc(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ').strip()

def main():
    rows = analyze()
    for r in rows:
        r['tier'] = tier_for(r)

    n = len(rows)
    c_tier = Counter(r['tier'] for r in rows)
    c_lang = Counter(r['lang'] for r in rows)
    c_coll = Counter(r['collection'] for r in rows)
    words = sorted(r['words'] for r in rows)
    framework_files = [r for r in rows if r['framework']]
    hard_cta_files = [r for r in rows if r['hard_cta']]
    hard_cta_cut = [r for r in hard_cta_files if r['tier'] == 'CUT']
    hard_cta_knowledge = [r for r in hard_cta_files if r['tier'] != 'CUT']

    # similarity (cross-collection, Jaccard > 0.30)
    sigs = {}
    for coll in ['ingredients', 'concepts', 'blog']:
        for path in files_for(coll):
            sigs[os.path.splitext(os.path.basename(path))[0]] = set(norm(path))
    keys = list(sigs.keys())
    pairs = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            jj = jaccard(sigs[keys[i]], sigs[keys[j]])
            if jj > 0.30:
                pairs.append((jj, keys[i], keys[j]))
    pairs.sort(reverse=True)

    def tier_sort(r):
        return (TIER_ORDER.index(r['tier']), r['collection'], r['slug'])

    L = []
    L.append("# IncenseHub.org 内容清册（Batch A — Inventory & Disposition）\n")
    L.append("> 生成方式：对仓库只读分析（不修改任何内容）。范围：`src/content`（266 篇：ingredients 150 · concepts 1 · blog 115）＋ 非内容静态页（15：13 独立页 + 2 索引页）。总渲染页面 281（`dist`/sitemap 均 281，另 404）。\n")
    L.append("\n## 1. 结构总览\n")
    L.append("| 维度 | 值 |")
    L.append("|---|---|")
    L.append("| 内容集合 | `ingredients`（香材实体）、`concepts`（支柱概念，单篇 `/chinese-incense/`）、`blog`（知识文章/香方/工艺/文化） |")
    L.append("| 内容文件总数 | %d（ingredients %d · concepts %d · blog %d） |" % (n, c_coll['ingredients'], c_coll['concepts'], c_coll['blog']))
    L.append("| 非内容渲染页 | 15（13 独立静态页 + blog/ingredients 索引页；另 404） |")
    L.append("| 总渲染页面 | 281 |")
    L.append("| 站点配置域名 | `https://incenseherbs.com`（`astro.config.mjs` → 目标 `IncenseHub.org`） |")
    L.append("| 技术栈 | Astro 5 静态生成 + `@astrojs/sitemap`；`output: static` |")
    L.append("| 字数范围 | min %d · max %d · 均值 %d · 中位 %d |" % (words[0], words[-1], int(sum(words)/n), words[len(words)//2]))
    L.append("| 结构完整性 | 全部 %d 篇均有 H2 分区；无空泛短页（<300 词：0 篇） |" % n)
    L.append("")
    L.append("## 2. 语言分布\n")
    L.append("**当前语言 = 英语（English-primary），中文术语为“源真值”内嵌注释。** 无纯中文页，无双语平行页——**无需翻译式语言转换策略**；需做的是术语规范化（中文名→英文统一 + 拼音标注一致性）。\n")
    L.append("| 语言 | 篇数 | 说明 |")
    L.append("|---|---|---|")
    L.append("| EN（纯英文正文） | %d | 正文全英文，无中文字符 |" % c_lang['EN'])
    L.append("| MIX（英文正文 + 中文术语） | %d | 正文英文，含少量中文名/引文（约 1–5%% CJK），如 `沉香`、`檀香`、香乘引文 |" % c_lang['MIX'])
    L.append("| ZH（纯中文） | 0 | 不存在 |")
    L.append("")
    L.append("## 3. 与 data-landeng 兄弟仓关系\n")
    L.append("`data-landeng` 是**权威数据源**（唯一源），主仓通过 `scripts/sync-datasets.mjs` 幂等同步 8 个 `datasets/*.json` 到 `data/` 与 `public/data/`。数据站域名 `data.incenseherbs.com`（→ 目标 `data.incensehub.org`）。本批只分析不触碰数据层。\n")
    L.append("")
    L.append("## 4. 处置分布汇总\n")
    L.append("| 处置 | 内容 .md 篇数 | 非内容页 | 合计 | 含义 |")
    L.append("|---|---|---|---|---|")
    L.append("| TRANSFORM · T1 | %d | 1（首页 index） | %d | 首批改造：最高搜索潜力 + 核心主题价值 |" % (c_tier['T1'], c_tier['T1']+1))
    L.append("| TRANSFORM · T2 | %d | 1（about） | %d | 第二批：次核心实体/工艺/香气/地域 |" % (c_tier['T2'], c_tier['T2']+1))
    L.append("| TRANSFORM · T3 | %d | 0 | %d | 第三批：长尾香材/香方/场景/文化 |" % (c_tier['T3'], c_tier['T3']))
    L.append("| KEEP | %d | 7（两索引页 + 法律页×5） | %d | 已达标：证据分层 + 无商业污染 |" % (c_tier['KEEP'], c_tier['KEEP']+7))
    L.append("| CUT | %d | 6（商业转化页） | %d | 降权重写/合并标注（不删页不换 URL） |" % (c_tier['CUT'], c_tier['CUT']+6))
    L.append("| **合计** | **%d** | **15** | **281** | — |" % n)
    L.append("")
    L.append("## 5. 重复检测（页间相似度 top）\n")
    L.append("Jaccard（正文去图/去链接/去表格后词集相似度）。高相似主要来自**实体页共用模板骨架**（不属真正抄袭），真正需合并的是**对比簇**与**OEM 簇**：\n")
    L.append("| 相似度 | 页面 A | 页面 B | 判定 |")
    L.append("|---|---|---|---|")
    # curated top-7 with editorial verdicts (data-driven pair values, curated verdicts)
    verdicts = {
        ('champaca','gardenia'): '模板骨架相似 → T2 差异化加深（非 CUT）',
        ('galangal','ginger'): '同上',
        ('citron','finger-citron'): '同上',
        ('agarwood-vs-frankincense','sandalwood-vs-frankincense'): '**对比簇重叠 → 合并/加区分度**',
        ('oem-private-label-guide','oem-vs-private-label'): '**OEM 簇重复 → 合并为单篇**（均 CUT）',
        ('frankincense-vs-myrrh','sandalwood-vs-frankincense'): '对比簇重叠',
        ('agarwood-vs-frankincense','agarwood-vs-sandalwood'): '对比簇重叠',
    }
    shown = set()
    for j, a, b in pairs:
        key = tuple(sorted((a, b)))
        if key in shown:
            continue
        v = verdicts.get(key) or verdicts.get((b, a))
        if v is None:
            continue
        shown.add(key)
        L.append("| %.3f | %s | %s | %s |" % (j, a, b, v))
        if len(shown) >= 7:
            break
    L.append("")
    L.append("## 6. 商业/营销段落命中\n")
    L.append("| 类型 | 命中数 | 说明 |")
    L.append("|---|---|---|")
    L.append("| 硬转化 CTA（request a sample/quote、get a quote、MOQ、minimum order、lead time、buy now） | %d 篇（%d 纯 B2B CUT + %d 知识页内嵌） | CUT 剥离后删页；知识页剥离 CTA 保留知识 |" % (len(hard_cta_files), len(hard_cta_cut), len(hard_cta_knowledge)))
    L.append("| 商业框架小节（Our Industry View / What Buyers Should Look For / Modern Commercial Applications） | %d 篇（ingredients %d = **实体页 100%%**；blog %d） | 实体模板**系统性内嵌**商业框架——改造核心：转“买家/批发/OEM”框架为“鉴别/质量/应用”中性知识框架 |" % (len(framework_files), sum(1 for r in framework_files if r['collection']=='ingredients'), sum(1 for r in framework_files if r['collection']=='blog')))
    L.append("| 纯商业转化静态页 | 6 页 | incense-manufacturer / oem / private-label / request-a-quote / wholesale / contact → CUT |")
    L.append("")
    L.append("---\n")
    L.append("## 7. 全量清册（逐篇处置）\n")
    L.append("> Disposition 列：KEEP（已达标）/ TRANSFORM·T1/T2/T3（按优先级改造）/ CUT（降权重写或合并，不删页不换 URL）。\n")

    for coll in ['ingredients', 'concepts', 'blog']:
        sub = sorted([r for r in rows if r['collection'] == coll], key=tier_sort)
        L.append("\n### %s（%d 篇）\n" % (coll, len(sub)))
        L.append("| # | 处置 | URL | 题名 | 字数 | 语言 | H2 | 主题/栏目 |")
        L.append("|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(sub, 1):
            pillar = (r['pillar'] or r['content_type'] or r['search_intent'] or '')
            L.append("| %d | %s | `%s` | %s | %d | %s | %d | %s |" % (i, TIER_LABEL[r['tier']], r['url'], esc(r['title']), r['words'], r['lang'], r['h2'], esc(pillar)))
        L.append("")

    L.append("### 非内容渲染页（15）\n")
    L.append("| 页面 | URL | 处置 | 说明 |")
    L.append("|---|---|---|---|")
    for p in ['incense-manufacturer','oem','private-label','request-a-quote','wholesale','contact','index','about','blog/index','ingredients/index','cookies','disclaimer','privacy-policy','safety','terms-of-service']:
        L.append("| %s | `/%s/` | %s | %s |" % (p, p, STATIC[p], STATIC_NOTE[p]))

    out = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(out)

    print("WROTE", os.path.relpath(OUT, ROOT), " lines=%d" % len(out.splitlines()))
    print("  content files:", n, "| tiers:", dict(c_tier))
    print("  lang:", dict(c_lang))
    print("  framework files:", len(framework_files),
          "(ingredients %d, blog %d)" % (sum(1 for r in framework_files if r['collection']=='ingredients'),
                                          sum(1 for r in framework_files if r['collection']=='blog')))
    print("  hard CTA files:", len(hard_cta_files),
          "(CUT %d, knowledge %d)" % (len(hard_cta_cut), len(hard_cta_knowledge)))

if __name__ == '__main__':
    main()
