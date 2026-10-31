#!/usr/bin/env python3
"""
Rewrite E1 verifier — per-file before→after similarity + quality checks.
Compares IncenseHub body vs LanDeng body (4-gram Jaccard, sentence overlap),
and reports the five-segment chain, mechanical-phrase hits, original assets,
viewpoint density and word counts.

Usage:
  python3 scripts/rewrite_e1_verify.py [--list scripts/e1_targets.txt] [--json /tmp/e1_after.json]
If --list omitted, reads scripts/e1_targets.txt (one relative path per line).
Baseline (before) values are read from /tmp/e1_baseline.json.
"""
import os, re, json, sys, argparse
from collections import defaultdict

IH = "/root/.openclaw/workspace/repos/incensehub.org"
LD = "/root/.openclaw/workspace/repos/LanDeng"

FRONT_RE = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)

def strip_frontmatter(text):
    return FRONT_RE.sub('', text, count=1)

def tokenize(text, n=4):
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

def load(p):
    with open(p, encoding='utf-8') as f:
        return f.read()

def ngram_similarity(t1, t2, n=4):
    return jaccard(tokenize(t1, n), tokenize(t2, n))

MECH = [
    r'\bhowever\b', r'\bmoreover\b', r'\bfurthermore\b', r'\badditionally\b',
    r'\bin addition\b', r'\bit is important to\b', r'\bit is worth noting\b',
    r'\bit should be noted\b', r'\bnotably\b', r'\bin conclusion\b',
    r'\bnevertheless\b', r'\bnonetheless\b', r'\bas mentioned\b',
    r'\bneedless to say\b', r'\bit is crucial to\b',
]

def parse(body):
    h2 = len(re.findall(r'^##\s+', body, re.M))
    h3 = len(re.findall(r'^###\s+', body, re.M))
    h4 = len(re.findall(r'^####\s+', body, re.M))
    tables = 0
    cur = False
    for l in body.split('\n'):
        s = l.strip()
        if s.startswith('|'):
            if not cur:
                tables += 1
                cur = True
        else:
            if s and not s.startswith('|'):
                cur = False
    direct_answer = len(re.findall(r'>\s*\*\*Direct answer:\*\*|\*\*Direct answer:\*\*', body, re.I))
    key_facts = 1 if re.search(r'##\s*Key facts', body, re.I) else 0
    summary = 1 if re.search(r'##\s*(Summary|Key Takeaways)', body, re.I) else 0
    evidence_status = 1 if re.search(r'##\s*(Evidence status|Evidence & Sources)', body, re.I) else 0

    mech_arrows = len(re.findall(r'→', body))
    mech_because = len(re.findall(r'\bbecause\b', body, re.I))
    mech_why = len(re.findall(r'\b(which is why|this is why|that is why|is why)\b', body, re.I))
    mech_drives = len(re.findall(r'\b(drives|results in|leads to|explains why|means that|converts|catalyzes|forms? (when|through)|depends on|so that|causing|yields|in turn)\b', body, re.I))
    mech_score = mech_arrows + mech_because + mech_why + mech_drives

    comparison = 1 if re.search(r'\b(vs\.?|versus|compared to|difference between|comparison)\b', body, re.I) else 0
    cross_table = 1 if tables >= 2 else 0
    aroma_family = 1 if re.search(r'\baroma famil|aroma wheel|scent wheel|fragrance famil|aromatic famil', body, re.I) else 0
    hexiang = 1 if re.search(r'君臣佐使|chief[–—-]minister[–—-]assistant[–—-]guide|hé xiāng|hexiang', body, re.I) else 0
    substitution = 1 if re.search(r'\bsubstitut|one name, several|cross-reference|cross reference', body, re.I) else 0
    naming_trap = 1 if re.search(r'naming trap|naming (confusion|trap)|same (word|name).*(different|several)', body, re.I) else 0
    orig_assets = comparison + cross_table + aroma_family + hexiang + substitution + naming_trap

    vp_ne = len(re.findall(r'\bnot established\b|\bunverified\b|\btraditional belief\b|\bnot established clinical', body, re.I))
    vp_we = len(re.findall(r'\bwe treat\b|\bwe do not claim\b|\bwhat we can say\b|\bwhat we do not claim\b', body, re.I))
    vp_bd = len(re.findall(r'\bboundary\b|\bdistinction matters\b|\bthe line between\b|\bwhere the line\b|\bdoes not mean\b|\bdoesn.t mean\b|\bunless\b|\bbut not\b', body, re.I))
    vp_sig = len(re.findall(r'\bpractical significance\b|\bwhy (this|it) matters\b|\bwhat this means\b|\bthe point is\b|\bin practice\b|\bactual meaning\b|\bmatters because\b|\bfor a collector\b|\bfor a buyer\b|\bfor the user\b', body, re.I))
    vp_misc = len(re.findall(r'\bmisconception\b|\bcommon myth\b|\bmyth\b|\bmisleading\b|\bwrongly\b|\bfalse\b|\bmisunderstood\b|\bmistake\b|\boverstated\b|\boverrated\b', body, re.I))
    vp_score = vp_ne + vp_we + vp_bd + vp_sig + vp_misc

    info_hit = 1 if (key_facts or direct_answer or evidence_status) else 0
    analysis_hit = 1 if mech_score >= 2 else 0
    conclusion_hit = 1 if summary else 0
    orig_hit = 1 if orig_assets >= 1 else 0
    vp_hit = 1 if vp_score >= 1 else 0
    chain = info_hit + analysis_hit + conclusion_hit + orig_hit + vp_hit

    words = len(re.findall(r'\S+', body))

    mech_hits = {}
    for m in MECH:
        n = len(re.findall(m, body, re.I))
        if n:
            mech_hits[m.strip(r'\\b')] = n

    return {
        'words': words, 'h2': h2, 'h3': h3, 'h4': h4, 'tables': tables,
        'direct_answer': direct_answer, 'key_facts': key_facts,
        'summary': summary, 'evidence_status': evidence_status,
        'mech_score': mech_score, 'orig_assets': orig_assets,
        'vp_score': vp_score, 'chain': chain,
        'info_hit': info_hit, 'analysis_hit': analysis_hit,
        'conclusion_hit': conclusion_hit, 'orig_hit': orig_hit, 'vp_hit': vp_hit,
        'mech_hits': mech_hits,
        'assets_detail': {'comparison': comparison, 'cross_table': cross_table,
                          'aroma_family': aroma_family, 'hexiang': hexiang,
                          'substitution': substitution, 'naming_trap': naming_trap},
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list', default='scripts/e1_targets.txt')
    ap.add_argument('--json', default='/tmp/e1_after.json')
    args = ap.parse_args()

    with open(args.list) as f:
        targets = [l.strip() for l in f if l.strip() and not l.startswith('#')]

    baseline = {}
    if os.path.exists('/tmp/e1_baseline.json'):
        baseline = json.load(open('/tmp/e1_baseline.json'))

    rows = []
    for relp in targets:
        ih_p = os.path.join(IH, 'src/content', relp)
        ld_p = os.path.join(LD, 'src/content', relp)
        if not os.path.exists(ih_p):
            rows.append({'rel': relp, 'error': 'ih missing'})
            continue
        ih_text = load(ih_p)
        ih_body = strip_frontmatter(ih_text)
        ld_body = ''
        if os.path.exists(ld_p):
            ld_body = strip_frontmatter(load(ld_p))
        after = ngram_similarity(ih_body, ld_body) if ld_body else 0.0
        # sentence overlap
        ih_sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', ih_body) if len(s.strip()) >= 15]
        ld_sents = [tokenize(s, 4) for s in re.split(r'(?<=[.!?])\s+', ld_body) if s.strip()]
        overlap = 0
        for s in ih_sents:
            ng = tokenize(s, 4)
            if any(jaccard(ng, lng) >= 0.7 for lng in ld_sents if lng):
                overlap += 1
        sent_ov = overlap / len(ih_sents) if ih_sents else 0.0
        st = parse(ih_body)
        b = baseline.get(relp, {})
        rows.append({
            'rel': relp,
            'before': b.get('before'),
            'after': round(after, 4),
            'sent_overlap': round(sent_ov, 4),
            'words_before': b.get('words_before'),
            'words_after': st['words'],
            'mech_score': st['mech_score'],
            'orig_assets': st['orig_assets'],
            'vp_score': st['vp_score'],
            'chain': st['chain'],
            'mech_hits': st['mech_hits'],
            'tables': st['tables'],
            'h2': st['h2'],
        })

    json.dump(rows, open(args.json, 'w'), ensure_ascii=False, indent=1)

    # table with PASS/FAIL gate
    def verdict(r):
        if 'error' in r:
            return ('ERR', r['error'])
        reasons = []
        if r['after'] >= 0.40:
            reasons.append('sim>=0.4')
        if r['mech_hits']:
            reasons.append('mechphrases')
        if r['chain'] < 5:
            reasons.append('chain<5')
        if r['orig_assets'] < 1:
            reasons.append('noasset')
        if r['vp_score'] < 2:
            reasons.append('vp<2')
        if r['words_before'] and r['words_after'] < 1.7 * r['words_before']:
            reasons.append(f"underexpand({r['words_after']}/{r['words_before']})")
        if reasons:
            return ('FAIL', ','.join(reasons))
        return ('PASS', '')

    print(f"{'rel':<55} {'before':>7} {'after':>7} {'sentOv':>6} {'wBef':>5} {'wAft':>5} {'mech':>4} {'asset':>5} {'vp':>3} {'chain':>5}  verdict")
    for r in rows:
        if 'error' in r:
            print(f"{r['rel']:<55} ERROR {r['error']}")
            continue
        v, reason = verdict(r)
        mh = r['mech_hits']
        mhstr = ','.join(f"{k}:{v}" for k, v in list(mh.items())[:2]) if mh else '0'
        print(f"{r['rel']:<55} {str(r['before']):>7} {str(r['after']):>7} {r['sent_overlap']:>6} {str(r['words_before']):>5} {r['words_after']:>5} {r['mech_score']:>4} {r['orig_assets']:>5} {r['vp_score']:>3} {r['chain']:>5}  {v} {reason}")

    # summary stats
    ok = [r for r in rows if 'error' not in r]
    if ok:
        after_vals = [r['after'] for r in ok]
        under04 = sum(1 for a in after_vals if a < 0.4)
        mech0 = sum(1 for r in ok if r['mech_hits'])
        chain5 = sum(1 for r in ok if r['chain'] >= 5)
        asset1 = sum(1 for r in ok if r['orig_assets'] >= 1)
        vp2 = sum(1 for r in ok if r['vp_score'] >= 2)
        passes = [r for r in ok if verdict(r)[0] == 'PASS']
        print(f"\n=== SUMMARY (n={len(ok)}) ===")
        print(f"PASS (sim<0.4 & chain5 & asset>=1 & vp>=2 & mech0 & expand>=1.7x): {len(passes)}/{len(ok)}")
        print(f"similarity <0.4: {under04}/{len(ok)} ({under04/len(ok)*100:.0f}%)  mean_after={sum(after_vals)/len(after_vals):.4f}")
        print(f"mechanical-phrase 0 hits: {len(ok)-mech0}/{len(ok)}")
        print(f"chain=5/5: {chain5}/{len(ok)}  orig_asset>=1: {asset1}/{len(ok)}  vp>=2: {vp2}/{len(ok)}")

if __name__ == '__main__':
    main()
