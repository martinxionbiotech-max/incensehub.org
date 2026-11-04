#!/usr/bin/env python3
"""
IncenseHub.org 全内容审计（五维 · AUDIT ONLY）
对比源站 LanDeng（incensehub.org 原内容归档）。

维度：
1. 原站重复检测（N-gram/Jaccard 段落级）
2. 层次加深检测（H2/H3 深度 + 五段链完整性）
3. 信息密度检测（字数 + 独有信息比 + 稀疏页）
4. 原创度检测（模板骨架占比 + 句式重合 + 原创资产）
5. 态度观点检测（作者观点段密度 + 中立百科腔页）

只读分析，不修改任何内容文件。输出 JSON + Markdown 报告。
"""
import os, re, json, hashlib, sys
from collections import Counter, defaultdict

IH = "/root/.openclaw/workspace/repos/incensehub.org"
LD = "/root/.openclaw/workspace/repos/LanDeng"
IH_CONTENT = os.path.join(IH, "src/content")
LD_CONTENT = os.path.join(LD, "src/content")

# ---------- helpers ----------
FRONT_RE = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)

def strip_frontmatter(text):
    return FRONT_RE.sub('', text, count=1)

def split_paragraphs(text):
    """Split body into paragraphs by blank lines; drop markdown table/code noise."""
    text = strip_frontmatter(text)
    paras = re.split(r'\n\s*\n', text)
    out = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        out.append(p)
    return out

def tokenize(text, n=3):
    """Character n-grams after normalization (lowercase, collapse whitespace)."""
    t = re.sub(r'\s+', ' ', text.lower())
    t = re.sub(r'[^a-z0-9\u4e00-\u9fff ]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) < n:
        return set(t)
    return set(t[i:i+n] for i in range(len(t)-n+1))

def jaccard(a, b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0

def ngram_similarity(t1, t2, n=4):
    s1 = tokenize(t1, n)
    s2 = tokenize(t2, n)
    return jaccard(s1, s2)

def load_file(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def rel(path):
    return os.path.relpath(path, IH_CONTENT)

def rel_ld(path):
    return os.path.relpath(path, LD_CONTENT)

# ---------- gather file lists ----------
ih_files = {}
for root, _, files in os.walk(IH_CONTENT):
    for fn in files:
        if fn.endswith('.md'):
            p = os.path.join(root, fn)
            ih_files[rel(p)] = p

ld_files = {}
for root, _, files in os.walk(LD_CONTENT):
    for fn in files:
        if fn.endswith('.md'):
            p = os.path.join(root, fn)
            ld_files[rel_ld(p)] = p

# ---------- structural parsing ----------
def parse_structure(text):
    """Extract headings (H1/H2/H3/H4), tables, direct-answer blocks, mechanisms, viewpoint markers."""
    body = strip_frontmatter(text)
    h2 = re.findall(r'^##\s+(.*)$', body, re.M)
    h3 = re.findall(r'^###\s+(.*)$', body, re.M)
    h4 = re.findall(r'^####\s+(.*)$', body, re.M)
    h1 = re.findall(r'^#\s+(.*)$', body, re.M)
    # tables: lines starting with | and containing |...|
    table_rows = [l for l in body.split('\n') if l.strip().startswith('|') and '|' in l[1:]]
    tables = []
    cur = []
    for l in body.split('\n'):
        if l.strip().startswith('|'):
            cur.append(l.strip())
        else:
            if cur:
                tables.append(cur)
                cur = []
    if cur:
        tables.append(cur)

    direct_answers = len(re.findall(r'>\s*\*\*Direct answer:\*\*', body, re.I))
    key_facts = 1 if re.search(r'##\s*Key facts', body, re.I) else 0
    summary = 1 if re.search(r'##\s*Summary', body, re.I) else 0
    faq = 1 if re.search(r'##\s*FAQ', body, re.I) else 0
    evidence_status = 1 if re.search(r'##\s*Evidence status', body, re.I) else 0
    evidence_sources = 1 if re.search(r'##\s*Evidence & Sources', body, re.I) else 0
    key_takeaways = 1 if re.search(r'##\s*Key Takeaways', body, re.I) else 0

    # mechanism chain: X→Y arrows, "because", "which is why", "this ... means", "mechanism"
    mech_arrows = len(re.findall(r'→', body))
    mech_because = len(re.findall(r'\bbecause\b', body, re.I))
    mech_why = len(re.findall(r'\b(which is why|this is why|that is why|is why)\b', body, re.I))
    mech_drives = len(re.findall(r'\b(drives|results in|leads to|explains why|means that|converts|catalyzes|forms? (when|through)|depends on)\b', body, re.I))
    mechanism_score = mech_arrows + mech_because + mech_why + mech_drives

    # originality assets
    comparison_cluster = 1 if re.search(r'\b(vs\.?|versus|compared to|difference between|comparison)\b', body, re.I) else 0
    cross_table = 1 if len(tables) >= 2 else 0
    aroma_family = 1 if re.search(r'\baroma famil|aroma wheel|scent wheel|fragrance famil|aromatic famil', body, re.I) else 0
    hexiang_system = 1 if re.search(r'君臣佐使|chief[–—-]minister[–—-]assistant[–—-]guide|hé xiāng|hexiang', body, re.I) else 0
    substitution_xref = 1 if re.search(r'\bsubstitut|one name, several|cross-reference|cross reference', body, re.I) else 0
    naming_trap = 1 if re.search(r'naming trap|naming (confusion|trap)|same (word|name).*(different|several)', body, re.I) else 0
    orig_assets = comparison_cluster + cross_table + aroma_family + hexiang_system + substitution_xref + naming_trap

    # viewpoint / attitude markers
    vp_not_established = len(re.findall(r'\bnot established\b|\bunverified\b|\btraditional belief\b|\bnot established clinical', body, re.I))
    vp_we_treat = len(re.findall(r'\bwe treat\b|\bwe do not claim\b|\bWhat we can say\b|\bWhat we do not claim\b', body, re.I))
    vp_boundary = len(re.findall(r'\bboundary\b|\bdistinction matters\b|\bthe line between\b|\bwhere the line\b|\brisk\b|\bbe read with skepticism\b|\bnot a triviality\b|\bnot medical advice\b|\bnot established medical', body, re.I))
    vp_significance = len(re.findall(r'\bpractical significance\b|\bwhy (this|it) matters\b|\bwhat this means\b|\bthe point is\b|\bin practice\b|\bactual meaning\b|\bmatters because\b', body, re.I))
    vp_misconception = len(re.findall(r'\bmisconception\b|\bcommon myth\b|\bmyth\b|\bmisleading\b|\bwrongly\b|\bfalse\b|\bmisunderstood\b', body, re.I))
    viewpoint_score = vp_not_established + vp_we_treat + vp_boundary + vp_significance + vp_misconception

    # five-segment chain presence
    info_hit = 1 if (key_facts or direct_answers or evidence_status) else 0
    analysis_hit = 1 if mechanism_score >= 2 else 0
    conclusion_hit = 1 if (summary or key_takeaways) else 0
    originality_hit = 1 if orig_assets >= 1 else 0
    viewpoint_hit = 1 if viewpoint_score >= 1 else 0

    words = len(re.findall(r'\S+', body))
    return {
        'h1': len(h1), 'h2': len(h2), 'h3': len(h3), 'h4': len(h4),
        'h2_titles': h2, 'h3_titles': h3,
        'tables': len(tables), 'table_rows': len(table_rows),
        'direct_answers': direct_answers,
        'key_facts': key_facts, 'summary': summary, 'faq': faq,
        'evidence_status': evidence_status, 'evidence_sources': evidence_sources,
        'key_takeaways': key_takeaways,
        'mech_arrows': mech_arrows, 'mech_because': mech_because, 'mech_why': mech_why, 'mech_drives': mech_drives,
        'mechanism_score': mechanism_score,
        'comparison_cluster': comparison_cluster, 'cross_table': cross_table,
        'aroma_family': aroma_family, 'hexiang_system': hexiang_system,
        'substitution_xref': substitution_xref, 'naming_trap': naming_trap,
        'orig_assets': orig_assets,
        'vp_not_established': vp_not_established, 'vp_we_treat': vp_we_treat,
        'vp_boundary': vp_boundary, 'vp_significance': vp_significance, 'vp_misconception': vp_misconception,
        'viewpoint_score': viewpoint_score,
        'info_hit': info_hit, 'analysis_hit': analysis_hit, 'conclusion_hit': conclusion_hit,
        'originality_hit': originality_hit, 'viewpoint_hit': viewpoint_hit,
        'words': words,
    }

# ---------- main analysis ----------
results = []
for relp in sorted(ih_files):
    ih_path = ih_files[relp]
    ih_text = load_file(ih_path)
    ih_body = strip_frontmatter(ih_text)
    ih_struct = parse_structure(ih_text)

    rec = {'rel': relp, 'section': relp.split('/')[0] if '/' in relp else 'root',
           'ih_words': ih_struct['words'], 'struct': ih_struct}

    # dim 1: duplicate vs LanDeng (paragraph-level n-gram)
    ld_path = ld_files.get(relp)
    if ld_path:
        ld_text = load_file(ld_path)
        ld_body = strip_frontmatter(ld_text)
        # paragraph-level similarity
        ih_paras = split_paragraphs(ih_text)
        ld_paras = split_paragraphs(ld_text)
        # compute per-ih-paragraph best match against all ld paragraphs
        para_sims = []
        for ip in ih_paras:
            ip_ng = tokenize(ip, 4)
            best = 0.0
            for lp in ld_paras:
                lp_ng = tokenize(lp, 4)
                s = jaccard(ip_ng, lp_ng)
                if s > best:
                    best = s
            para_sims.append(best)
        if para_sims:
            doc_dup = sum(para_sims) / len(para_sims)
        else:
            doc_dup = 0.0
        # document-level ngram
        doc_ng = ngram_similarity(ih_body, ld_body, 4)
        # high-duplicate paragraph fraction (para sim >= 0.7)
        high_para = sum(1 for s in para_sims if s >= 0.7)
        mid_para = sum(1 for s in para_sims if 0.4 <= s < 0.7)
        low_para = sum(1 for s in para_sims if s < 0.4)
        rec['ld_exists'] = True
        rec['doc_dup'] = doc_dup
        rec['doc_ngram'] = doc_ng
        rec['n_ih_paras'] = len(ih_paras)
        rec['n_ld_paras'] = len(ld_paras)
        rec['high_para'] = high_para
        rec['mid_para'] = mid_para
        rec['low_para'] = low_para
        # unique info ratio: paragraphs in ih not strongly present in ld (sim < 0.4)
        rec['unique_para'] = low_para
        rec['unique_ratio'] = low_para / len(ih_paras) if ih_paras else 0.0
        # sentence overlap (rough): sentences in ih body whose ngram appears in ld
        ih_sents = re.split(r'(?<=[.!?])\s+', ih_body)
        ld_sent_ngrams = [tokenize(s, 4) for s in re.split(r'(?<=[.!?])\s+', ld_body) if s.strip()]
        overlap_sents = 0
        for s in ih_sents:
            s = s.strip()
            if not s or len(s) < 15:
                continue
            ng = tokenize(s, 4)
            if any(jaccard(ng, lng) >= 0.7 for lng in ld_sent_ngrams if lng):
                overlap_sents += 1
        rec['n_ih_sents'] = len([s for s in ih_sents if len(s.strip()) >= 15])
        rec['overlap_sents'] = overlap_sents
        rec['sentence_overlap_ratio'] = overlap_sents / rec['n_ih_sents'] if rec['n_ih_sents'] else 0.0
    else:
        rec['ld_exists'] = False
        rec['doc_dup'] = 0.0
        rec['doc_ngram'] = 0.0
        rec['unique_ratio'] = 1.0
        rec['sentence_overlap_ratio'] = 0.0
        rec['n_ih_paras'] = len(split_paragraphs(ih_text))
        rec['n_ld_paras'] = 0
        rec['high_para'] = 0
        rec['mid_para'] = 0
        rec['low_para'] = 0
        rec['unique_para'] = 0

    # template skeleton ratio: fraction of body that is boilerplate
    boiler_markers = ['Direct answer:', 'Key facts', 'Summary', 'FAQ', 'Evidence & Sources',
                      'Evidence status', 'Key Takeaways', 'Sources', 'Safety', 'At a glance',
                      'Common forms', 'Where does', 'What determines', 'How is', 'Traditional use',
                      'Chinese name', 'Botanical identity', 'Aroma profile', 'Species:', 'In Chinese incense',
                      'Quality & authenticity', 'Sustainability']
    boiler_chars = 0
    for m in boiler_markers:
        boiler_chars += len(re.findall(re.escape(m), ih_body, re.I)) * len(m)
    rec['boiler_ratio'] = boiler_chars / max(1, len(ih_body))

    results.append(rec)

# ---------- aggregate ----------
def pct(n, d):
    return (n / d * 100) if d else 0.0

summary = {
    'total_files': len(results),
    'by_section': Counter(r['section'] for r in results),
    'ld_exists': sum(1 for r in results if r['ld_exists']),
}

# dim1 distribution
dup_buckets = {'high': 0, 'mid': 0, 'low': 0}
for r in results:
    d = r['doc_dup']
    if d >= 0.7: dup_buckets['high'] += 1
    elif d >= 0.4: dup_buckets['mid'] += 1
    else: dup_buckets['low'] += 1
summary['dup_distribution'] = dup_buckets

# dim2
summary['h2_total'] = sum(r['struct']['h2'] for r in results)
summary['h3_total'] = sum(r['struct']['h3'] for r in results)
summary['h2_avg'] = summary['h2_total'] / len(results)
summary['h3_avg'] = summary['h3_total'] / len(results)
five = ['info_hit', 'analysis_hit', 'conclusion_hit', 'originality_hit', 'viewpoint_hit']
for f in five:
    summary[f + '_count'] = sum(1 for r in results if r['struct'][f])
    summary[f + '_rate'] = pct(sum(r['struct'][f] for r in results), len(results))
chain_full = sum(1 for r in results if all(r['struct'][f] for f in five))
summary['chain_full'] = chain_full
summary['chain_full_rate'] = pct(chain_full, len(results))
# flat pages: no H3 and no mechanism
flat_pages = [r for r in results if r['struct']['h3'] == 0 and r['struct']['mechanism_score'] < 2]
summary['flat_pages'] = len(flat_pages)

# dim3
words_all = [r['ih_words'] for r in results]
summary['words_total'] = sum(words_all)
summary['words_avg'] = sum(words_all) / len(words_all)
summary['words_min'] = min(words_all)
summary['words_max'] = max(words_all)
summary['words_median'] = sorted(words_all)[len(words_all)//2]
uniq_ratios = [r['unique_ratio'] for r in results if r['ld_exists']]
summary['unique_ratio_avg'] = sum(uniq_ratios) / len(uniq_ratios) if uniq_ratios else 0.0
# sparse pages: words < 1200 and no table and no comparison
sparse = [r for r in results if r['ih_words'] < 1200 and r['struct']['tables'] == 0 and r['struct']['comparison_cluster'] == 0]
summary['sparse_pages'] = len(sparse)

# dim4
summary['boiler_ratio_avg'] = sum(r['boiler_ratio'] for r in results) / len(results)
sent_ov = [r['sentence_overlap_ratio'] for r in results if r['ld_exists']]
summary['sentence_overlap_avg'] = sum(sent_ov) / len(sent_ov) if sent_ov else 0.0
orig_asset_counts = [r['struct']['orig_assets'] for r in results]
summary['orig_assets_total'] = sum(orig_asset_counts)
summary['orig_assets_avg'] = sum(orig_asset_counts) / len(results)
summary['orig_asset_gte1'] = sum(1 for r in results if r['struct']['orig_assets'] >= 1)
summary['orig_asset_gte1_rate'] = pct(sum(1 for r in results if r['struct']['orig_assets'] >= 1), len(results))
# asset type distribution
for k in ['comparison_cluster', 'cross_table', 'aroma_family', 'hexiang_system', 'substitution_xref', 'naming_trap']:
    summary['asset_' + k] = sum(1 for r in results if r['struct'][k])

# dim5
vp_scores = [r['struct']['viewpoint_score'] for r in results]
summary['vp_total'] = sum(vp_scores)
summary['vp_avg'] = sum(vp_scores) / len(results)
summary['vp_gte1'] = sum(1 for r in results if r['struct']['viewpoint_score'] >= 1)
summary['vp_gte1_rate'] = pct(sum(1 for r in results if r['struct']['viewpoint_score'] >= 1), len(results))
neutral = [r for r in results if r['struct']['viewpoint_score'] == 0]
summary['neutral_pages'] = len(neutral)
# viewpoint intensity buckets
vp_buckets = {'zero': 0, 'low(1-2)': 0, 'mid(3-5)': 0, 'high(6+)': 0}
for r in results:
    s = r['struct']['viewpoint_score']
    if s == 0: vp_buckets['zero'] += 1
    elif s <= 2: vp_buckets['low(1-2)'] += 1
    elif s <= 5: vp_buckets['mid(3-5)'] += 1
    else: vp_buckets['high(6+)'] += 1
summary['vp_distribution'] = vp_buckets

out = {
    'summary': summary,
    'results': results,
    'flat_pages': [r['rel'] for r in flat_pages],
    'sparse_pages': [r['rel'] for r in sparse],
    'neutral_pages': [r['rel'] for r in neutral],
}

with open('/tmp/full_audit_5dim.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# print summary
print(json.dumps(summary, ensure_ascii=False, indent=2))
print("\n=== flat pages (%d) ===" % len(flat_pages))
for r in flat_pages[:50]:
    print("  ", r['rel'], "h3=%d mech=%d" % (r['struct']['h3'], r['struct']['mechanism_score']))
print("\n=== neutral pages (%d) ===" % len(neutral))
for r in neutral[:50]:
    print("  ", r['rel'], "vp=%d" % r['struct']['viewpoint_score'])
print("\n=== sparse pages (%d) ===" % len(sparse))
for r in sparse[:50]:
    print("  ", r['rel'], "words=%d tables=%d" % (r['ih_words'], r['struct']['tables']))
