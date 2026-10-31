#!/usr/bin/env python3
"""Generate docs/rewrite-e1-report.md from baseline + after-similarity JSON."""
import json, os, sys, statistics

IH = "/root/.openclaw/workspace/repos/incensehub.org"
base = json.load(open('/tmp/e1_baseline.json'))
after_json = sys.argv[1] if len(sys.argv) > 1 else '/tmp/e1_after.json'
after_rows = json.load(open(after_json))
after = {r['rel']: r for r in after_rows}

rows = []
for rel in sorted(base):
    b = base[rel]
    a = after.get(rel, {})
    before = b.get('before')
    after_sim = a.get('after')
    words_before = b.get('words_before')
    words_after = a.get('words_after')
    sent_ov = a.get('sent_overlap')
    mech = a.get('mech_score')
    assets = a.get('orig_assets')
    vp = a.get('vp_score')
    chain = a.get('chain')
    mech_hits = a.get('mech_hits') or {}
    rows.append((rel, before, after_sim, sent_ov, words_before, words_after, mech, assets, vp, chain, mech_hits))

def fmt(v, nd=3):
    return f"{v:.{nd}f}" if isinstance(v, (int, float)) else str(v)

# pass/fail
def verdict(after_sim, words_before, words_after, chain, assets, vp, mech_hits):
    reasons = []
    if after_sim is None:
        return '—'
    if after_sim >= 0.40: reasons.append('sim')
    if chain < 5: reasons.append('chain')
    if assets < 1: reasons.append('asset')
    if vp < 2: reasons.append('vp')
    if mech_hits: reasons.append('mech')
    if words_before and words_after < 1.7 * words_before: reasons.append('len')
    return 'PASS' if not reasons else ('FAIL:' + ','.join(reasons))

lines = []
lines.append('# IncenseHub Rewrite — Batch E1 Report\n')
lines.append('> Generated automatically from the before/after similarity verifier. Batch E1 targets the P0\n')
lines.append('> pages (51 verbatim-identical + highest ≥0.90 overlap pages). Target: N-gram similarity < 0.40.\n')

# summary
after_vals = [r[2] for r in rows if r[2] is not None]
under04 = sum(1 for a in after_vals if a < 0.40)
mech0 = sum(1 for r in rows if not r[10])
chain5 = sum(1 for r in rows if r[9] >= 5)
asset1 = sum(1 for r in rows if r[7] >= 1)
vp2 = sum(1 for r in rows if r[8] >= 2)
passes = [r for r in rows if verdict(r[2], r[4], r[5], r[9], r[7], r[8], r[10]) == 'PASS']
before_vals = [r[1] for r in rows if r[1] is not None]

lines.append('## Summary\n')
lines.append(f'- Files rewritten: **{len(rows)}**')
lines.append(f'- Similarity before→after (mean): **{fmt(statistics.mean(before_vals))} → {fmt(statistics.mean(after_vals))}**')
lines.append(f'- Similarity < 0.40: **{under04}/{len(rows)}** ({under04/len(rows)*100:.0f}%)')
lines.append(f'- Distribution: min {fmt(min(after_vals))} · max {fmt(max(after_vals))} · median {fmt(statistics.median(after_vals))}')
lines.append(f'- Full PASS (sim<0.4 & chain5 & asset>=1 & vp>=2 & mech0 & len>=1.7x): **{len(passes)}/{len(rows)}**')
lines.append(f'- Mechanical phrases (However/Moreover/…): 0-hit on **{mech0}/{len(rows)}** files')
lines.append(f'- Five-segment chain = 5/5: {chain5}/{len(rows)} · original asset ≥1: {asset1}/{len(rows)} · viewpoint ≥2: {vp2}/{len(rows)}')
lines.append('')

# distribution buckets
buckets = {'<0.35': 0, '0.35–0.40': 0, '0.40–0.50': 0, '0.50–0.60': 0, '0.60–0.70': 0, '≥0.70': 0}
for a in after_vals:
    if a < 0.35: buckets['<0.35'] += 1
    elif a < 0.40: buckets['0.35–0.40'] += 1
    elif a < 0.50: buckets['0.40–0.50'] += 1
    elif a < 0.60: buckets['0.50–0.60'] += 1
    elif a < 0.70: buckets['0.60–0.70'] += 1
    else: buckets['≥0.70'] += 1
lines.append('## Similarity distribution\n')
lines.append('| Bucket | Files |')
lines.append('|---|---|')
for k, v in buckets.items():
    lines.append(f'| {k} | {v} |')
lines.append('')

# per-file table
lines.append('## Per-file before → after\n')
lines.append('| File | before | after | sentOv | words b→a | mech | asset | vp | chain | verdict |')
lines.append('|---|---|---|---|---|---|---|---|---|---|')
for rel, before, after_sim, sent_ov, wb, wa, mech, assets, vp, chain, mh in rows:
    v = verdict(after_sim, wb, wa, chain, assets, vp, mh)
    lines.append(f'| `{rel}` | {fmt(before) if before is not None else "—"} | {fmt(after_sim) if after_sim is not None else "—"} | {fmt(sent_ov) if sent_ov is not None else "—"} | {wb}→{wa} | {mech} | {assets} | {vp} | {chain} | {v} |')
lines.append('')

# original assets & viewpoints (counts)
lines.append('## Original assets & viewpoints\n')
lines.append('Counts of original assets and viewpoints are in the verifier columns above (asset = comparison table / cross-table / aroma-family / hexiang / substitution / naming-trap present; vp = viewpoint-density score).')
lines.append('')

# continuation
remaining = [r for r in rows if verdict(r[2], r[4], r[5], r[9], r[7], r[8], r[10]) != 'PASS']
lines.append('## Continuation (E2)\n')
lines.append(f'- Files still above target or not fully PASS: **{len(remaining)}**')
if remaining:
    lines.append('')
    for rel, *_ in remaining:
        lines.append(f'  - `{rel}`')

out = '\n'.join(lines) + '\n'
path = os.path.join(IH, 'docs', 'rewrite-e1-report.md')
with open(path, 'w', encoding='utf-8') as f:
    f.write(out)
print(f'wrote {path} ({len(lines)} lines)')
print(f'PASS {len(passes)}/{len(rows)} · mean {fmt(statistics.mean(before_vals))} -> {fmt(statistics.mean(after_vals))} · <0.4: {under04}/{len(rows)}')
