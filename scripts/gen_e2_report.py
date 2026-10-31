#!/usr/bin/env python3
"""Generate docs/rewrite-e2-report.md from a verifier JSON run over scripts/e2_targets.txt."""
import json, os, re, sys
from datetime import date

ROOT = "/root/.openclaw/workspace/repos/incensehub.org"
rows = json.load(open("/tmp/e2_all.json"))
base = json.load(open("/tmp/e2_baseline.json"))

legacy = set(l.strip() for l in open(os.path.join(ROOT, "scripts/e2_legacy.txt")) if l.strip())

def verdict(r):
    if "error" in r:
        return "ERR", r["error"]
    reasons = []
    if r["after"] >= 0.40: reasons.append("sim")
    if r["mech_hits"]: reasons.append("mech")
    if r["chain"] < 5: reasons.append("chain")
    if r["orig_assets"] < 1: reasons.append("asset")
    if r["vp_score"] < 2: reasons.append("vp")
    if r["words_before"] and r["words_after"] < 1.7 * r["words_before"]:
        reasons.append("len")
    return ("PASS" if not reasons else "FAIL", ",".join(reasons))

ok = [r for r in rows if "error" not in r]
after = [r["after"] for r in ok]
under = sum(1 for a in after if a < 0.40)
passes = [r for r in ok if verdict(r)[0] == "PASS"]
mean_before = sum(base[r["rel"]]["before"] for r in ok) / len(ok)
mean_after = sum(after) / len(after)
buckets = {"<0.35": 0, "0.35-0.40": 0, "0.40-0.50": 0, "0.50-0.60": 0, "0.60-0.70": 0, ">=0.70": 0}
for a in after:
    if a < 0.35: buckets["<0.35"] += 1
    elif a < 0.40: buckets["0.35-0.40"] += 1
    elif a < 0.50: buckets["0.40-0.50"] += 1
    elif a < 0.60: buckets["0.50-0.60"] += 1
    elif a < 0.70: buckets["0.60-0.70"] += 1
    else: buckets[">=0.70"] += 1

# remaining unrewritten: all files minus e1 targets minus e2 targets
e1 = set(l.strip() for l in open(os.path.join(ROOT, "scripts/e1_targets.txt")) if l.strip())
e2 = set(l.strip() for l in open(os.path.join(ROOT, "scripts/e2_targets.txt")) if l.strip())
allsim = json.load(open("/tmp/all_sim_after.json"))
remaining = [(rel, s, w) for rel, s, w in allsim if rel not in e1 and rel not in e2]
remaining.sort(key=lambda x: -x[1])

L = []
L.append("# IncenseHub Rewrite — Batch E2 Report\n")
L.append(f"> Generated {date.today().isoformat()} from the before/after similarity verifier (4-gram Jaccard vs LanDeng).\n")
L.append("## Summary\n")
L.append(f"- Files rewritten: **{len(ok)}** (E1 legacy second pass: {len([r for r in ok if r['rel'] in legacy])} · fresh rewrites: {len([r for r in ok if r['rel'] not in legacy])})")
L.append(f"- Similarity before→after (mean): **{mean_before:.3f} → {mean_after:.3f}**")
L.append(f"- Similarity < 0.40: **{under}/{len(ok)}** ({under/len(ok)*100:.0f}%)")
L.append(f"- Full PASS (sim<0.40 & chain5 & asset>=1 & vp>=2 & mech0 & len>=1.7x): **{len(passes)}/{len(ok)}**")
L.append(f"- Mechanical phrases: 0-hit on **{sum(1 for r in ok if not r['mech_hits'])}/{len(ok)}** files")
L.append(f"- Original asset >=1: **{sum(1 for r in ok if r['orig_assets']>=1)}/{len(ok)}** · viewpoint >=2: **{sum(1 for r in ok if r['vp_score']>=2)}/{len(ok)}** · chain 5/5: **{sum(1 for r in ok if r['chain']==5)}/{len(ok)}**")
L.append(f"- Distribution: min {min(after):.3f} · max {max(after):.3f} · median {sorted(after)[len(after)//2]:.3f}\n")
L.append("## Similarity distribution\n")
L.append("| Bucket | Files |\n|---|---|")
for k, v in buckets.items():
    L.append(f"| {k} | {v} |")
L.append("\n## Per-file before → after\n")
L.append("| File | kind | before | after | sentOv | words b→a | mech | asset | vp | chain | verdict |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|")
for r in sorted(rows, key=lambda x: (x.get("after", 9))):
    v, reason = verdict(r)
    kind = "legacy" if r["rel"] in legacy else "fresh"
    L.append(f"| `{r['rel']}` | {kind} | {r['before']:.3f} | {r['after']:.3f} | {r['sent_overlap']:.3f} | {r['words_before']}→{r['words_after']} | {len(r['mech_hits'])} | {r['orig_assets']} | {r['vp_score']} | {r['chain']} | {v}{(' ' + reason) if reason else ''} |")
L.append("\n## Continuation (E3)\n")
L.append(f"- Files not yet rewritten: **{len(remaining)}**")
L.append("- Priority order (highest similarity first):\n")
for rel, s, w in remaining[:40]:
    L.append(f"  - `{rel}` — {s:.3f} · {w}w")
L.append("")
open(os.path.join(ROOT, "docs/rewrite-e2-report.md"), "w").write("\n".join(L) + "\n")
print("wrote docs/rewrite-e2-report.md", len(ok), under, len(passes), len(remaining))
