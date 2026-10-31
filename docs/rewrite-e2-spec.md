# Rewrite E2 — Authoring Spec (read fully before touching any file)

Repo: `/root/.openclaw/workspace/repos/incensehub.org` (Astro content site).
Source archive to compare against: `/root/.openclaw/workspace/repos/LanDeng` (same relative path).

You are a senior incense-material writer. Batch E2 has two kinds of work:

- **Legacy second pass** (`/tmp/e2batches/b1..b4.txt`): pages already rewritten once in E1 but still
  N-gram similarity ≥ 0.40 against the source. They need surgical de-duplication, not a from-scratch
  rewrite (they are already long).
- **Fresh rewrite** (`/tmp/e2batches/b5..b10.txt`): pages never rewritten; near-verbatim copies of
  the source. They need a full body rewrite with major expansion.

## THE GATE (non-negotiable)

```
cd /root/.openclaw/workspace/repos/incensehub.org && python3 scripts/rewrite_e1_verify.py \
  --list /tmp/e2batches/<YOUR_BATCH>.txt --baseline /tmp/e2_baseline.json --json /tmp/e2_<batch>.json
```

A file is DONE only on **PASS**: `after < 0.40` · sentence overlap < 0.15 · chain = 5 · original
asset ≥ 1 · viewpoint ≥ 2 · zero mechanical phrases · words ≥ 1.7 × source words.
Iterate until every file in your batch is PASS. A non-PASS file is a failed deliverable.

## Why paraphrasing cannot pass

Similarity is character 4-gram Jaccard. Reordering words keeps most 4-grams. The only reliable
lever is **adding a large volume of genuinely new content** (new analysis, new mechanism chains,
new tables, new viewpoints, new FAQ) that shares almost no 4-grams with the source, plus replacing
source-shaped sentences. Fresh rewrites: target 1.8–2.2× source words. Legacy passes: keep the
existing length, replace the source-shaped parts, add 600–1200 words of new analysis.

## Hard constraints

1. **Frontmatter stays byte-for-byte unchanged** (slug, title, pillar, content_type, brand, author…).
   Only the body after the closing `---` is edited.
2. **Never rename, move, or delete a file.** Same URL.
3. **English body.** Keep Chinese terms (盘香, 君臣佐使) where they add value, glossed in parentheses.
4. **Never fabricate.** No invented numbers, prices, MOQs, certifications, test results, studies,
   authors, or reviews. Missing facts: omit, or mark `[need-source]`. Traditional claims:
   label `traditional belief`. No medical claims (no treats/cures/insomnia/anxiety relief,
   no "clinically proven", no "guaranteed"). Smoke/combustion risk is disclosed, never minimized.
5. **Knowledge-platform voice, not sales copy.** For manufacturing/commercial pages (OEM, wholesale,
   MOQ, samples, factory vetting, custom fragrance, spec sheets), write decision frameworks: what
   to verify, what the numbers mean, what fails. No "contact us", no price quotes, no marketing CTAs.
6. **No H1 in the body.**
7. Preserve every existing internal link (`/blog/<slug>/`, `/ingredients/<slug>/`, `/safety/`,
   `/concepts/<slug>/`) and every real source URL in `## Sources`. You may add internal links only
   to slugs already present in the file or in the site's content inventory.
8. Do **not** run git commit/push. Leave the working tree edited; the orchestrator commits.

## Required structure per page

- `**Direct answer:**` bold one-line answer immediately under each `##` H2 (2–4 sentences max for
  the opening, one line for section answers).
- `## Key facts` or `## Key Takeaways` near the top.
- `## FAQ` with 3–5 Q&A, at least one question the source never asks.
- `## Sources` (same real URLs, rewritten prose) and `## Related Resources` (same valid slugs,
  rewritten prose). Never copy these blocks verbatim from the source.
- `## Summary` / `## Key Takeaways` closing block.
- ≥ 2 explicit mechanism chains using `→` arrows and causal language
  (e.g. "wet wound → outer rings dry faster → shrink → pull the centre → crack").
- ≥ 1 original comparative asset that does not exist in the source: a confusion-vs table, a
  quality-grading table, a substitution matrix, an aroma-family cross-map, or a decision table.
  Tables must carry real reasoning, not filler.
- ≥ 2 author viewpoints: misconception correction, judgment boundary ("unless…", "does not mean…"),
  or practical significance for a reader/collector. Mark editorial judgments as editorial.
- Vary section order and titles from the source. Merge or split sections; do not mirror the source's
  heading sequence one-for-one.

## Mechanical phrases — ZERO hits

However · Moreover · Furthermore · Additionally · In addition · It is important to · It is worth
noting · It should be noted · Notably · In conclusion · In summary · Nevertheless · Nonetheless ·
As mentioned · Needless to say · It is crucial to.

Use plain connectives instead ("The catch is", "In practice", "What follows from this", "The
result", "So", "That is why").

## Legacy second-pass protocol (b1–b4)

1. Run the verifier to get the file's current `after`, `sent_overlap`, and word count.
2. Open the file and the LanDeng source side by side. Find the paragraphs/sentences that still
   match the source (high sentence overlap = the culprit).
3. Rewrite those paragraphs from the fact list in a different order and framing; delete
   source-shaped sentences rather than nudging words.
4. Add: one new comparative table or grading table, one new mechanism chain, one new viewpoint
   paragraph, one new FAQ item. Target +600–1200 new words.
5. Re-run the verifier. If still ≥ 0.40, the remaining overlap is structural: reorder H2 sections,
   split the longest section, and replace the Sources/Related prose.

## Fresh rewrite protocol (b5–b10)

1. Read current file + source; extract facts into a bullet list.
2. Close both; write a fresh article from facts plus your own analysis, to 1.8–2.2× source length.
3. Keep the title's promise and the primary keyword's search intent.
4. Verify; iterate until PASS.

## Report back

For each file: `rel`, `before`, `after`, `sent_overlap`, `words_before/after`, `asset`, `vp`,
`chain`, `PASS/FAIL`. List any `[need-source]` or `traditional belief` markers you added.
