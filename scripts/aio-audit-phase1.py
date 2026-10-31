#!/usr/bin/env python3
"""Phase 1 AIO audit: all ingredient pages + all blog pages.

Checks per page (4 AIO criteria from §11/§13/§25):
  1. Direct answer blockquote ("> **Direct answer:** ...") present after an H2.
  2. First 100 words directly answer "what is it" (definitional lead).
  3. Has a FAQ section.
  4. Has >=1 AI-extractable definition sentence.

Outputs a Markdown report with per-page score table, gap stats, and a
search-value-ranked fix list.
"""
import os, re, json, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ING = os.path.join(ROOT, "src", "content", "ingredients")
BLOG = os.path.join(ROOT, "src", "content", "blog")
OUT = "/root/.openclaw/workspace/phase2/optimization-reports/aio-audit-phase1.md"

# §33 priority entities (highest search value) — phase-1 priority list.
PRIORITY = [
    "agarwood", "sandalwood", "frankincense", "benzoin", "borneol", "borneol-oil",
    "mugwort", "rose", "jasmine", "osmanthus", "patchouli", "myrrh", "vetiver",
    "clove", "cinnamon", "cardamom", "star-anise", "pine-resin", "cedar",
    "champaca", "spikenard", "spikenard-nardostachys",
]

def read_body(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text

def strip_frontmatter(text):
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    if m:
        return text[m.end():]
    return text

def strip_markdown(text):
    # remove images, links (keep text), bold/italic, code, tables pipes minimal
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`>#|]", " ", text)
    return text

def first_words(text, n=100):
    body = strip_frontmatter(text)
    body = strip_markdown(body)
    words = body.split()
    return " ".join(words[:n])

def has_direct_answer_blockquote(text):
    # blockquote line starting "> **Direct answer:" (the deepened format)
    return bool(re.search(r"^>\s*\*\*Direct answer:", text, re.M))

def has_faq(text):
    return bool(re.search(r"^#{2,3}\s*FAQ\b", text, re.M))

def has_definition_sentence(text):
    body = strip_frontmatter(text)
    body = strip_markdown(body)
    # entity-defining patterns
    pats = [
        r"\bis\s+(?:a|an|the)\s+",
        r"\bare\s+(?:a|an|the)\s+",
        r"\brefers\s+to\b",
        r"\bmeans\s+\"",
        r"\u2014\s+[^\n]{0,120}?\u2014\s+is\s+",   # "X — ... — is ..."
        r"\u2014\s+is\s+",
    ]
    for p in pats:
        if re.search(p, body):
            return True
    return False

def first_100_answers_what(body_text):
    w = first_words(body_text, 100)
    # a lead answering "what is it" typically names the entity then "is ..."
    return bool(re.search(r"\bis\s+(?:a|an|the)\b|\b(?:is|are)\s+(?:an?\s+)?(?:the\s+)?", w)) and len(w) > 30

def opening_label(text):
    body = strip_frontmatter(text)
    m = re.search(r"^\s*\*\*([A-Za-z ]+):\*\*", body)
    if m:
        return m.group(1).strip()
    m = re.search(r"^\s*\*\*([A-Za-z ]+)\*\*", body)
    if m:
        return m.group(1).strip()
    return ""

def first_h2s(text):
    body = strip_frontmatter(text)
    return re.findall(r"^##\s+(.+)$", body, re.M)[:5]

def word_count(text):
    body = strip_frontmatter(text)
    body = strip_markdown(body)
    return len(body.split())

def faq_count(text):
    body = strip_frontmatter(text)
    return len(re.findall(r"^\*\*[^\n]{3,}\?\*\*", body, re.M))

def internal_links(text):
    return len(re.findall(r"\]\(/", text))

def primary_keyword(text):
    m = re.search(r'primary_keyword:\s*"([^"]+)"', text)
    return m.group(1) if m else ""

def search_value(path, text, name):
    score = 0
    if name in PRIORITY:
        score += 100
    if primary_keyword(text):
        score += 20
    score += min(faq_count(text), 10) * 2
    score += min(internal_links(text), 15)
    score += min(word_count(text) // 300, 20)
    return score

def audit_page(path, kind):
    text = read_body(path)
    name = os.path.splitext(os.path.basename(path))[0]
    r = {
        "name": name,
        "kind": kind,
        "da_blockquote": has_direct_answer_blockquote(text),
        "first100": first_100_answers_what(text),
        "faq": has_faq(text),
        "def_sentence": has_definition_sentence(text),
        "words": word_count(text),
        "faq_n": faq_count(text),
        "links": internal_links(text),
        "label": opening_label(text),
        "h2s": first_h2s(text),
        "pk": primary_keyword(text),
    }
    r["score"] = sum([r["da_blockquote"], r["first100"], r["faq"], r["def_sentence"]])
    r["sv"] = search_value(path, text, name)
    return r

def main():
    pages = []
    for f in sorted(os.listdir(ING)):
        if f.endswith(".md"):
            pages.append(audit_page(os.path.join(ING, f), "ingredient"))
    for f in sorted(os.listdir(BLOG)):
        if f.endswith(".md"):
            pages.append(audit_page(os.path.join(BLOG, f), "blog"))

    n_ing = [p for p in pages if p["kind"] == "ingredient"]
    n_blog = [p for p in pages if p["kind"] == "blog"]

    lines = []
    w = lines.append
    w("# AIO 全站复检报告 — Phase 1（任务①阶段A）\n")
    w("> 生成脚本：`scripts/aio-audit-phase1.py`。检查范围：全部 150 个原料页 + 全部 %d 个 blog 页。\n" % len(n_blog))
    w("> 4 项 AIO 指标（§11/§13/§25）：① Direct answer blockquote（`> **Direct answer:**`）② 开篇 100 词直接回答「是什么」③ 有 FAQ 节 ④ 有 ≥1 句可被 AI 抽取的定义句。\n")

    def tally(ps, key):
        return sum(1 for p in ps if p[key])

    def line(tag, tot, yes):
        w(f"| {tag} | {tot} | {yes} | {tot - yes} |")

    w("\n## 缺口统计\n")
    w("| 指标 | 总数 | 通过 | 缺口 |")
    w("|---|---|---|---|")
    for kind, ps, label in [("ingredient", n_ing, "原料页"), ("blog", n_blog, "Blog 页")]:
        w(f"### {label}（{len(ps)} 页）")
        line("① Direct answer blockquote", len(ps), tally(ps, "da_blockquote"))
        line("② 开篇100词回答「是什么」", len(ps), tally(ps, "first100"))
        line("③ FAQ 节", len(ps), tally(ps, "faq"))
        line("④ 定义句", len(ps), tally(ps, "def_sentence"))
        w("")

    # score distribution
    w("\n## 得分分布（4 项全通过=4 分）\n")
    for kind, ps in [("原料页", n_ing), ("Blog 页", n_blog)]:
        dist = collections.Counter(p["score"] for p in ps)
        w(f"- **{kind}**：{dict(sorted(dist.items()))}")

    # per-page score table
    w("\n## 分页得分表\n")
    w("| 页面 | 类型 | ①DA块 | ②100词 | ③FAQ | ④定义句 | 得分 | 搜索价值 | 词数 | 开篇标签 |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for p in sorted(pages, key=lambda x: (-x["sv"], x["name"])):
        ck = lambda b: "✅" if b else "❌"
        w(f"| {p['name']} | {p['kind']} | {ck(p['da_blockquote'])} | {ck(p['first100'])} | {ck(p['faq'])} | {ck(p['def_sentence'])} | {p['score']} | {p['sv']} | {p['words']} | {p['label']} |")

    # fix list: ingredient pages missing DA blockquote, ranked by search value
    missing = [p for p in n_ing if not p["da_blockquote"]]
    missing.sort(key=lambda x: -x["sv"])
    w("\n## 修复清单（缺 Direct answer 块的原料页，按搜索价值排序）\n")
    w(f"共 **{len(missing)}** 页缺 Direct answer blockquote。\n")
    w("| # | 页面 | 搜索价值 | 开篇标签 | 首个 H2 | 主关键词 |")
    w("|---|---|---|---|---|---|")
    for i, p in enumerate(missing, 1):
        w(f"| {i} | {p['name']} | {p['sv']} | {p['label']} | {p['h2s'][0] if p['h2s'] else '—'} | {p['pk'][:40]} |")

    # blog pages missing DA blockquote (informational)
    blog_missing = [p for p in n_blog if not p["da_blockquote"]]
    w(f"\n## Blog 页缺 Direct answer 块（信息，共 {len(blog_missing)} 页）\n")
    w("阶段B范围限定为**原料页**（150 页）。blog 页在此仅审计，不纳入本轮补块。\n")
    for p in sorted(blog_missing, key=lambda x: -x["sv"]):
        w(f"- {p['name']}（sv={p['sv']}）")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {OUT}")
    print(f"ingredient pages: {len(n_ing)}, blog pages: {len(n_blog)}")
    print(f"ingredient missing DA blockquote: {len(missing)}")
    print(f"blog missing DA blockquote: {len(blog_missing)}")

    # also dump machine-readable fix list
    dump = {"missing_ingredients": [p["name"] for p in missing]}
    with open("/root/.openclaw/workspace/phase2/optimization-reports/aio-fixlist.json", "w") as f:
        json.dump(dump, f, indent=2)
    print("Wrote aio-fixlist.json")

if __name__ == "__main__":
    main()
