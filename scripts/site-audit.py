#!/usr/bin/env python3
"""Site audit: SEO / AIO / structure metrics over dist HTML.

Usage: python3 scripts/site-audit.py [--json out.json]
"""
import os, re, json, sys, statistics, html as htmllib
from collections import Counter, defaultdict

DIST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dist")
TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"<(script|style|svg)\b[\s\S]*?</\1>", re.I)
LD_RE = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>([\s\S]*?)</script>', re.I)

def text_of(html):
    t = SCRIPT_STYLE_RE.sub(" ", html)
    t = TAG_RE.sub(" ", t)
    t = htmllib.unescape(t)
    return re.sub(r"\s+", " ", t).strip()

def words(t):
    return len(re.findall(r"[A-Za-z0-9’'\-]+", t))

def ld_types(obj, out):
    if isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, str): out.append(t)
        elif isinstance(t, list): out.extend([x for x in t if isinstance(x, str)])
        for v in obj.values(): ld_types(v, out)
    elif isinstance(obj, list):
        for v in obj: ld_types(v, out)

def audit_page(path, html):
    text = text_of(html)
    title = re.search(r"<title[^>]*>([\s\S]*?)</title>", html, re.I)
    desc_tag = re.search(r'<meta[^>]+name=["\']description["\'][^>]*>', html, re.I)
    desc_val = re.search(r"content=([\"'])(.*?)\1", desc_tag.group(0), re.S) if desc_tag else None
    can = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)["\']', html, re.I)
    robots = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']*)["\']', html, re.I)
    lang = re.search(r'<html[^>]+lang=["\']([^"\']+)["\']', html, re.I)
    og = {k: (re.search(r'<meta[^>]+property=["\']og:'+k+r'["\'][^>]+content=["\']([^"\']*)["\']', html, re.I) or [None, None])[1]
          for k in ("title", "description", "image", "type", "url")}
    tw = re.search(r'<meta[^>]+name=["\']twitter:card["\'][^>]+content=["\']([^"\']*)["\']', html, re.I)
    viewport = re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.I)
    imgs = re.findall(r"<img\b[^>]*>", html, re.I)
    img_total = len(imgs)
    img_missing_alt = sum(1 for i in imgs if not re.search(r'\balt\s*=', i, re.I))
    img_empty_alt = sum(1 for i in imgs if re.search(r'\balt\s*=\s*["\']\s*["\']', i, re.I))
    h1 = len(re.findall(r"<h1\b", html, re.I))
    h2 = len(re.findall(r"<h2\b", html, re.I))
    tables = len(re.findall(r"<table\b", html, re.I))
    internal = len(re.findall(r'href=["\'](/[^"\'#?]*)', html))
    external = len(re.findall(r'href=["\']https?://', html))
    lds = LD_RE.findall(html)
    types = []
    ld_errors = 0
    for raw in lds:
        try:
            ld_types(json.loads(raw), types)
        except Exception:
            ld_errors += 1
    lower = text.lower()
    return {
        "path": path,
        "title": htmllib.unescape(title.group(1)).strip() if title else "",
        "title_len": len(htmllib.unescape(title.group(1)).strip()) if title else 0,
        "desc": htmllib.unescape(desc_val.group(2)).strip() if desc_val else "",
        "desc_len": len(htmllib.unescape(desc_val.group(2)).strip()) if desc_val else 0,
        "canonical": can.group(1) if can else "",
        "robots": (robots.group(1) if robots else "").lower(),
        "lang": lang.group(1) if lang else "",
        "words": words(text),
        "h1": h1, "h2": h2, "tables": tables,
        "imgs": img_total, "img_missing_alt": img_missing_alt, "img_empty_alt": img_empty_alt,
        "internal_links": internal, "external_links": external,
        "ld_blocks": len(lds), "ld_errors": ld_errors, "ld_types": sorted(set(types)),
        "og_title": bool(og["title"]), "og_desc": bool(og["description"]), "og_image": bool(og["image"]),
        "twitter_card": bool(tw), "viewport": bool(viewport),
        "has_faq": ("faq" in lower) or ("Frequently asked" in text),
        "has_sources": bool(re.search(r"\bSources\b", text)),
        "has_direct_answer": "Direct answer" in text,
        "has_traditional_label": "traditional belief" in lower or "Traditional practice" in text,
        "need_source_marks": len(re.findall(r"\[need-source\]", text)),
        "images_section": bool(re.search(r"Images?|Photo|Figure", text)),
    }

def main():
    pages = []
    for root, _, files in os.walk(DIST):
        if "_astro" in root or "_md" in root: continue
        for f in files:
            if f == "index.html":
                p = os.path.join(root, f)
                rel = "/" + os.path.relpath(os.path.dirname(p), DIST).replace(os.sep, "/")
                rel = "/" if rel == "/." else rel + "/"
                pages.append((rel, p))
    out = []
    for rel, p in sorted(pages):
        with open(p, encoding="utf-8", errors="ignore") as fh:
            out.append(audit_page(rel, fh.read()))
    result = {"pages": out, "count": len(out)}
    json.dump(result, open("/tmp/audit_html.json", "w"), ensure_ascii=False, indent=1)

    n = len(out)
    def pct(k, cond):
        return round(100 * sum(1 for r in out if cond(r)) / n, 1)
    titles = [r["title"] for r in out]
    descs = [r["desc"] for r in out]
    words = [r["words"] for r in out]
    ld_types = Counter(t for r in out for t in r["ld_types"])
    summary = {
        "pages": n,
        "with_title": pct("title", lambda r: bool(r["title"])),
        "title_30_65": pct("t", lambda r: 30 <= r["title_len"] <= 65),
        "unique_titles": len(set(titles)),
        "with_desc": pct("d", lambda r: bool(r["desc"])),
        "desc_120_165": pct("d2", lambda r: 120 <= r["desc_len"] <= 165),
        "unique_descs": len(set(descs)),
        "canonical": pct("c", lambda r: bool(r["canonical"])),
        "robots_noindex": sum(1 for r in out if "noindex" in r["robots"]),
        "lang_en": pct("l", lambda r: r["lang"] == "en"),
        "h1_exactly_one": pct("h1", lambda r: r["h1"] == 1),
        "jsonld_pages": pct("ld", lambda r: r["ld_blocks"] > 0),
        "jsonld_errors": sum(r["ld_errors"] for r in out),
        "og_complete": pct("og", lambda r: r["og_title"] and r["og_desc"] and r["og_image"]),
        "twitter_card": pct("tw", lambda r: r["twitter_card"]),
        "viewport": pct("vp", lambda r: r["viewport"]),
        "img_missing_alt": sum(r["img_missing_alt"] for r in out),
        "img_empty_alt": sum(r["img_empty_alt"] for r in out),
        "faq_coverage": pct("f", lambda r: r["has_faq"]),
        "sources_coverage": pct("s", lambda r: r["has_sources"]),
        "direct_answer_coverage": pct("da", lambda r: r["has_direct_answer"]),
        "need_source_marks": sum(r["need_source_marks"] for r in out),
        "words_mean": round(statistics.mean(words), 1),
        "words_median": statistics.median(words),
        "words_p10": sorted(words)[max(0, int(0.1*n)-1)],
        "pages_under_600w": sum(1 for w in words if w < 600),
        "tables_total": sum(r["tables"] for r in out),
        "tables_pages": pct("t2", lambda r: r["tables"] > 0),
        "internal_links_mean": round(statistics.mean([r["internal_links"] for r in out]), 1),
        "internal_links_median": statistics.median([r["internal_links"] for r in out]),
        "external_links_mean": round(statistics.mean([r["external_links"] for r in out]), 1),
        "ld_types": dict(ld_types.most_common()),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
