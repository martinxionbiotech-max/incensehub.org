#!/usr/bin/env python3
"""Refinement metrics for the 5-dim audit."""
import os, re, json
from collections import Counter, defaultdict

IH = "/root/.openclaw/workspace/repos/incensehub.org"
LD = "/root/.openclaw/workspace/repos/IncenseHub"
IHC = os.path.join(IH, "src/content")
LDC = os.path.join(LD, "src/content")
FRONT_RE = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)

def strip(t): return FRONT_RE.sub('', t, count=1)
def load(p):
    with open(p, encoding='utf-8') as f: return f.read()

def tokenize(text, n=4):
    t = re.sub(r'\s+', ' ', text.lower())
    t = re.sub(r'[^a-z0-9\u4e00-\u9fff ]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) < n: return set(t)
    return set(t[i:i+n] for i in range(len(t)-n+1))
def jac(a,b):
    if not a and not b: return 1.0
    if not a or not b: return 0.0
    u = len(a|b)
    return len(a&b)/u if u else 0.0

files = []
for root,_,fs in os.walk(IHC):
    for fn in fs:
        if fn.endswith('.md'):
            p = os.path.join(root, fn)
            files.append(os.path.relpath(p, IHC))

# 1. document-level ngram distribution + IH vs LD word/para counts
doc_ng = []
word_delta = []
para_delta = []
sent_ov = []
for relp in sorted(files):
    ih_t = load(os.path.join(IHC, relp)); ih_b = strip(ih_t)
    ld_t = load(os.path.join(LDC, relp)); ld_b = strip(ld_t)
    doc_ng.append(ng4 := jac(tokenize(ih_b), tokenize(ld_b)))
    ih_w = len(re.findall(r'\S+', ih_b)); ld_w = len(re.findall(r'\S+', ld_b))
    word_delta.append((ih_w, ld_w, ih_w - ld_w))
    ih_p = [x.strip() for x in re.split(r'\n\s*\n', ih_b) if x.strip()]
    ld_p = [x.strip() for x in re.split(r'\n\s*\n', ld_b) if x.strip()]
    para_delta.append((len(ih_p), len(ld_p), len(ih_p)-len(ld_p)))
    # sentence overlap
    ih_s = [s.strip() for s in re.split(r'(?<=[.!?])\s+', ih_b) if len(s.strip())>=15]
    ld_sng = [tokenize(s) for s in re.split(r'(?<=[.!?])\s+', ld_b) if s.strip()]
    ov = sum(1 for s in ih_s if any(jac(tokenize(s), l)>=0.7 for l in ld_sng if l))
    sent_ov.append((ov, len(ih_s), ov/len(ih_s) if ih_s else 0))

doc_ng.sort()
print("=== doc-level ngram similarity distribution (all 266) ===")
for th in [1.0, 0.99, 0.98, 0.97, 0.95, 0.90, 0.80, 0.70]:
    print("  >=%.2f: %d" % (th, sum(1 for x in doc_ng if x >= th)))
print("  min: %.4f  max: %.4f  mean: %.4f" % (min(doc_ng), max(doc_ng), sum(doc_ng)/len(doc_ng)))

print("\n=== word count delta (IH - LD) ===")
tot_ih = sum(a for a,b,c in word_delta); tot_ld = sum(b for a,b,c in word_delta)
print("  IH total words: %d  LD total words: %d  delta: %+d (%.2f%%)" % (tot_ih, tot_ld, tot_ih-tot_ld, (tot_ih-tot_ld)/tot_ld*100))
neg = sum(1 for a,b,c in word_delta if c < 0); pos = sum(1 for a,b,c in word_delta if c > 0); zero = sum(1 for a,b,c in word_delta if c==0)
print("  files with fewer words than LD: %d | more words: %d | equal: %d" % (neg,pos,zero))

print("\n=== paragraph count delta (IH - LD) ===")
totp_ih = sum(a for a,b,c in para_delta); totp_ld = sum(b for a,b,c in para_delta)
print("  IH total paras: %d  LD total paras: %d  delta: %+d" % (totp_ih, totp_ld, totp_ih-totp_ld))
negp = sum(1 for a,b,c in para_delta if c<0); posp = sum(1 for a,b,c in para_delta if c>0); zerop = sum(1 for a,b,c in para_delta if c==0)
print("  files with fewer paras: %d | more paras: %d | equal: %d" % (negp,posp,zerop))

print("\n=== sentence overlap distribution ===")
ovs = sorted(c for a,b,c in sent_ov)
for th in [1.0, 0.95, 0.90, 0.80, 0.70, 0.50]:
    print("  >=%.2f: %d files" % (th, sum(1 for x in ovs if x>=th)))

# 2. common H2 skeleton across ingredients
print("\n=== ingredient H2 title frequency (skeleton) ===")
h2_counter = Counter()
for relp in files:
    if not relp.startswith('ingredients/'): continue
    b = strip(load(os.path.join(IHC, relp)))
    for h in re.findall(r'^##\s+(.*)$', b, re.M):
        h2_counter[h.strip().lower()] += 1
tot_ing = 150
common = [(h,c) for h,c in h2_counter.most_common() if c >= tot_ing*0.8]
print("  H2 titles appearing in >=80%% of ingredient pages (skeleton): %d" % len(common))
for h,c in common:
    print("    %3d  %s" % (c, h))

# 3. strong vs weak original assets
print("\n=== original asset type distribution ===")
assets = defaultdict(int)
for relp in files:
    b = strip(load(os.path.join(IHC, relp)))
    if re.search(r'君臣佐使|chief[–—-]minister[–—-]assistant[–—-]guide|hé xiāng|hexiang', b, re.I): assets['hexiang_system'] += 1
    if re.search(r'aroma famil|aroma wheel|scent wheel|fragrance famil|aromatic famil', b, re.I): assets['aroma_family'] += 1
    if re.search(r'naming trap|naming (confusion|trap)|same (word|name).*(different|several)', b, re.I): assets['naming_trap'] += 1
    if re.search(r'substitut|one name, several|cross-reference|cross reference', b, re.I): assets['substitution_xref'] += 1
for k,v in sorted(assets.items(), key=lambda x:-x[1]):
    print("  %-20s %d files" % (k, v))
strong = 0
for relp in files:
    b = strip(load(os.path.join(IHC, relp)))
    cnt = 0
    for pat in ['君臣佐使','hé xiāng','hexiang','aroma famil','scent wheel','aroma wheel','naming trap','substitut','cross-reference','cross reference','one name, several']:
        if re.search(pat, b, re.I): cnt += 1
    if cnt >= 1: strong += 1
print("  files with >=1 STRONG asset (hexiang/aroma-family/naming-trap/substitution-xref): %d / 266 (%.1f%%)" % (strong, strong/266*100))
