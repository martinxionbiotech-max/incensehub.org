# Rewrite E1 — Authoring Spec (read this fully before touching any file)

You are a senior incense-material writer. You are **rewriting** IncenseHub pages that are
verbatim or near-verbatim copies of the IncenseHub source site, so they become genuinely original
content. This is a **destructive rewrite of the body with substantial expansion**, not a
sentence-by-sentence paraphrase.

## THE GATE (non-negotiable — this is how your work is judged)

After you finish each file, run the verifier. A file is **DONE** only when it shows **PASS**:

```
cd /root/.openclaw/workspace/repos/incensehub.org && python3 scripts/rewrite_e1_verify.py --list /tmp/e1batches/b<N>.txt
```

PASS means ALL of: `after` < 0.40 · sentence overlap < 0.15 · `chain` = 5 · original asset ≥ 1 ·
viewpoint ≥ 2 · zero mechanical phrases · body expanded to ≥ 1.7× the original word count.

**A file that is not PASS is a failure. Do not return until every file in your batch is PASS.**

## Why paraphrasing alone can never pass (read this twice)

Similarity is measured as **character 4-gram Jaccard**: `shared / total`. Rephrasing a sentence
changes its shape but keeps nearly all of its character 4-grams (the words "incense", "coil",
"burn", "stick" and all the function words like "the", "and", "for" are still there). So
rephrasing at the same length barely moves the number.

The **only reliable way to drop similarity is to ADD a large volume of UNIQUE content** — new
analysis, new mechanism chains, new tables, new viewpoints, new FAQ answers — that does not
overlap the source at all. New content is what dilutes the shared 4-grams.

**Concrete requirement: your rewritten body must be at least 1.8× the original word count, and
the extra ~80% must be genuinely new analysis, not restated facts.**

Proven reference: `incense-coils.md` went from 1155 words (source) → **2096 words (1.81×)** →
similarity **0.398**. If your file is 0.50 or higher, you barely rewrote it — go back and roughly
double the new-content mass.

## Hard constraints (never violate)

1. **Preserve the frontmatter block exactly.** The `---` header (slug, title, primary_keyword,
   pillar, content_type, last_reviewed, brand, author) stays byte-for-byte unchanged. Only the
   **body** (everything after the second `---`) is rewritten.
2. **Do not change the filename, slug, or URL.** Same file, same path.
3. **Do not delete the page.**
4. **English only.** Keep Chinese terms (盘香, pánxiāng, 君臣佐使) where they add value, glossed.
5. **Never fabricate** data, experiments, certifications, prices, reviews, ratings, stock,
   authors, or research results. If the source lacks a fact, omit it or mark `[need-source]`.
   Traditional claims are labeled `traditional belief`.
6. **No medical claims.** Never write "treats/cures insomnia/anxiety", "clinically proven",
   "guaranteed relaxation", "natural = safe". Use "evening ritual", "aromatic experience",
   "calming atmosphere", "traditional use". Combustion/smoke risk must be disclosed, never
   minimized.

## The method

Do **not** rewrite sentence-by-sentence. Follow this sequence:

1. **Read the current file** at `src/content/<rel>` (a previous pass may have already reworded
   it — keep its good sentences) and the IncenseHub source at
   `/root/.openclaw/workspace/repos/IncenseHub/src/content/<rel>`.
2. **Extract the FACTS** into a scratch bullet list (what it is, key numbers, mechanisms,
   warnings, related entities, internal links, source URLs).
3. **Close both sources.** Write a fresh article from your fact list **plus the new analysis you
   add yourself**.
4. Reorder and regroup everything. Change section order, merge/split sections, and change the FAQ
   questions themselves.

## What to ADD to every page (this is where the length comes from)

Every page must contain, in addition to the restated facts:

1. **≥2 mechanism chains (X→Y).** Explain *how* and *why*, with explicit causal language and `→`
   arrows. Example: "wound while wet → outer rings dry faster → shrink → pull the center →
   crack". At least two distinct cause-to-effect paths per page. These are the single best source
   of unique content.
2. **≥1 original comparison table / cross-reference** that does NOT exist in the source: a
   confusion-vs table (similar materials/formats that get mixed up), a quality-grading table, or
   a substitute matrix. Use "vs / compared to / difference between" wording or a multi-column
   table.
3. **≥2 author viewpoints** — at least two of: a common-misconception correction; a judgment
   boundary ("unless…", "but not when…", "…does not mean…"); and practical significance for a
   user/collector. Have an attitude, not an encyclopedia tone. Mark editorial views as such.
4. **≥1 NEW FAQ question-and-answer** that the source does not ask.
5. **A "how to judge / reading the material" angle** where relevant (what to look for before you
   buy/burn/use).
6. **Bold one-line Direct answer** opening each `##` section.

## Similarity levers (use both)

- **Dilute**: expand to ~1.8–2.0× the original length, with the extra mass in NEW analysis,
  tables, chains, and viewpoints. New vocabulary dilutes the shared n-grams.
- **Diversify the Sources + Related Resources block too.** Do **not** copy it verbatim from the
  source. Keep the exact URLs and internal link slugs (honest sourcing, no broken links), but
  rewrite the descriptive prose around them and reword the closing "next step" line. Leaving the
  block verbatim pushes you over 0.40.

## Site conventions to preserve

- **FAQ**: keep `## FAQ` with 3–5 Q&A; cover the core search intents; write fresh answers.
- **Sources**: keep `## Sources` with the same real URLs (do not invent URLs); rewrite the
  surrounding description.
- **Related Resources**: keep `## Related Resources` with the same valid slugs
  (`/blog/<slug>/`, `/ingredients/<slug>/`, `/safety/`, `/concepts/<slug>/`).
- **Internal links**: preserve every existing internal link exactly; you may add links only to
  slugs already in your file or your batch list.
- **No H1 in the body** — the title lives in frontmatter.

## Mechanical phrases to avoid (ZERO hits)

However · Moreover · Furthermore · Additionally · In addition · It is important to · It is worth
noting · It should be noted · Notably · In conclusion · In summary · Nevertheless · Nonetheless ·
As mentioned · Needless to say · It is crucial to.

## Reference example

`src/content/blog/incense-coils.md` is a finished, verified PASS example (after=0.398,
sentOv=0.068, chain 5/5, mech 0, 1.81× expansion). Read it before starting to internalize the
depth, the Direct-answer style, the original tables, and the authorial tone.

## Verification loop (repeat until every file is PASS)

1. Write the file.
2. Run the verifier for your batch.
3. Any file not PASS: fix it — add a new mechanism chain, a new original table, a new viewpoint
   paragraph, or a new FAQ Q&A; reword any source-shaped sentence; delete mechanical phrases.
   Re-run.
4. Only move on when the whole batch reads PASS.

Report (in your final structured result) each file's before→after similarity, word counts,
mech score, asset count, viewpoint count, and status. List any facts you marked `[need-source]`
or `traditional belief`.
