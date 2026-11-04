---
slug: "incensehub-editorial-methodology"
title: "How IncenseHub Researches Chinese Incense"
primary_keyword: "chinese incense research methodology"
search_intent: "informational"
pillar: "Editorial & Data"
content_type: "authority_reference"
cluster_role: "authority_reference"
last_reviewed: "2026-09-22"
brand: "IncenseHub"
author: "IncenseHub Editorial Team"
---

**At a glance:** IncenseHub documents Chinese botanical incense in English, but the Chinese term is always the source of truth. Every ingredient entry is built through a fixed eight-step method: establish the Chinese name, verify the botanical identity, normalize the English term, identify the historical source, separate modern scientific evidence, label trade terminology, mark uncertain claims, and review before publication. Traditional knowledge and scientific evidence are never merged.

**Key facts:** This page describes how we work, what sources we accept, how we tier evidence, how we correct errors, and who the "IncenseHub Editorial Team" byline actually is. There is no fabricated author, credential, or review board behind it.

---

## The Eight-Step Research Method

> Every IncenseHub entity page follows the same eight steps, in order. The point is not speed — it is that a reader, a search engine, or an AI system can trace any sentence back to one of these steps and see what kind of claim it is.

### Step 1 — Establish the Chinese term

Each ingredient begins with its Chinese name, written in characters, with pinyin. The English page is a translation layer on top of the Chinese term, not a replacement for it. If multiple Chinese names exist for one material (for example, a classical name and a modern market name), both are recorded and the relationship between them is stated.

### Step 2 — Verify the botanical identity

The next step is to confirm what the material actually is. For a plant, this means the scientific name and family — *Aquilaria* for agarwood, *Santalum album* for true sandalwood. For an animal-derived or mineral material, it means naming the source organism or substance without glossing over it. Where the botanical identity is contested or genuinely uncertain, that uncertainty is kept rather than papered over with a confident name.

### Step 3 — Normalize the English terminology

English names for Chinese incense materials are inconsistent across the trade. One Chinese word can map to several English words, and one English word can point at several different materials. IncenseHub fixes a single preferred English translation per term and records the alternates, so a reader can tell what we mean and where the naming risk lies. The canonical glossary is published in the terminology dataset.

### Step 4 — Identify the historical source

Where a material has a classical record — 本草纲目 (Compendium of Materia Medica), 香乘 (the Xiangpu incense manuals), or another historical text — we name the source and quote the traditional use as a historical claim. The historical record is reported as history, not as a claim about what the material does today.

### Step 5 — Separate modern scientific evidence

Modern evidence — peer-reviewed research, botanical databases, government checklists — is handled separately from the historical record. A traditional description is never silently upgraded into a scientific finding. Where there is scientific evidence (for example, on smoke, air quality, or species distribution), it is cited with its source and evidence tier; where there is none, the page says so instead of implying one.

### Step 6 — Label trade terminology

Grading vocabulary, market names, and trade heuristics (沉水 "sinking", 奇楠 qínán, grade names, adulteration signals) are labeled as trade terminology. These are the practical language of the Chinese incense market, and they are useful — but they are industry convention, not laboratory measurement. We keep the two apart.

### Step 7 — Mark uncertain claims

Claims that cannot be verified, or that rest on conflicting sources, are marked rather than asserted. Common markers are "traditionally believed to", "sources disagree on", "proportions unverified", and "trade practice, not a laboratory standard". An open question is shown as an open question.

### Step 8 — Review before publication

A page is not published until it has passed a factual review: every claim is either sourced or labeled as traditional, editorial, or unverified; no statistic, certification, price, review, or customer case appears that cannot be traced; and the page satisfies a real question rather than padding a template.

The pre-publication checklist is explicit:

1. **Source check** — every factual claim carries a source that resolves, lives on the allow-list (botanical databases, primary text repositories, government checklists), and actually supports the sentence it sits behind.
2. **Evidence-tier check** — traditional knowledge, modern evidence, trade terminology, and uncertain claims are each labeled with their own tier; none is presented as another.
3. **Dataset consistency** — mirrored counts, term codes, and records match the data-site datasets (ingredients.json, terminology.json, relationships.json).
4. **Relationship integrity** — every related[] edge points at a live slug, and reciprocity is confirmed.
5. **Commercial-claims check** — no fabricated MOQ, capacity, pricing, certification, or customer case; anything commercial is confirmed-per-inquiry.
6. **Date truthfulness** — last_reviewed changes only when a substantive review happened, never as a freshness stamp.

Post-publication, pages are re-reviewed on the cadence in the freshness policy (T1 90 days / T2 180 days / T3 trigger-based), and every change — including a no-change review — is logged in the change ledger.

---

## Source Policy

> IncenseHub accepts sources by subject, not by search rank. A page that ranks well is not a source; a primary record, an academic institution, or a regulatory body is.

The source policy follows the subject of the claim, with a strict preference order:

- **Botanical** — botanical databases, peer-reviewed papers, authoritative botanical references, and herbarium or university sources.
- **Historical** — academic publications, museum sources, the classical texts themselves, and university resources.
- **Scientific** — peer-reviewed research, academic institutions, and scientific databases.
- **Regulation** — government agencies, official regulatory bodies, and recognized standards organizations.
- **Industry** — manufacturer and technical documentation, trade organizations, and industry publications.

Low-quality SEO content is not used as primary evidence, and a source is never cited merely because it ranks well. External links in our pages are restricted to an allow-list of authoritative hosts (botanical and taxonomic databases, primary text repositories, and government checklists), so a citation is always to a stable, checkable record.

---

## Evidence Tiers

> Every source is assigned one of six evidence tiers, by the nature of the source — not by how convenient it is. The tier is published with the citation so a reader or an AI system can tell fact from tradition from editorial view.

| Tier | Label | Source nature |
|---|---|---|
| Tier 1 | Scientific / Government | Government checklists and regulatory lists (e.g. CITES) |
| Tier 2 | Academic / Museum / Institutional | Botanical and taxonomic institutions (e.g. GBIF, Flora of China) |
| Tier 3 | Historical primary source | Classical Chinese texts (本草纲目, 香乘 on Wikisource) |
| Tier 4 | Industry / Trade terminology | Trade and industry sources |
| Tier 5 | Traditional knowledge | Traditional-knowledge sources |
| Tier 6 | Editorial synthesis | IncenseHub's own editorial pages |

The same six tiers are applied in the open datasets on the data site, so a claim carries the same evidence level whether it is read in prose or pulled from JSON.

---

## Correction Policy

> Errors are corrected in place, the page's review date is updated, and dataset changes are recorded in a changelog. We do not silently rewrite and we do not delete retired entities.

The correction process is simple and traceable:

1. When an error is identified — by a reader, a source update, or an internal review — the claim is corrected at its source, not patched around.
2. The page's `last_reviewed` date is updated so the correction is visible in the record.
3. If a dataset changes, the minor version is bumped and the change is logged in the dataset's `changelog`.
4. An entity that is wrong is not deleted and orphaned; it is marked `deprecated`, or pointed at its replacement with `supersededBy`, so existing links keep resolving.
5. Corrections are never dressed up with a fabricated "reviewed by" attribution.

Content is updated only when there is a reason: new evidence, a new source, new industry information, a correction, a new relationship, or a real improvement to search intent. Pages are not rewritten on a schedule to look fresh.

---

## Who Writes IncenseHub

> IncenseHub's content is published under a single collective byline — "IncenseHub Editorial Team" — rather than a named individual. There is no fabricated PhD, expert title, or review board behind any page.

The byline is honest about what it is: a team entity, not a person. We do not invent an author name, a credential, a photograph, or a biography. The site's own editorial rule is stated on the homepage: no fake reviews, ratings, prices, or authors.

What the byline represents is the method described above — the eight-step research process, the source policy, the evidence tiers, and the correction policy. Authority on this site comes from the traceability of each claim, not from a name attached to it. If you need to attribute a IncenseHub page, cite "IncenseHub Editorial Team" as the publisher and the page as the source.

### Publisher

IncenseHub is an independent knowledge platform. The "IncenseHub Editorial Team" byline is the site's editorial team.


---

## What We Will Not Do

These are the editorial lines the site holds, stated plainly:

- We do not convert "traditionally believed to" into "scientifically proven to".
- We do not make medical claims, and we do not describe incense as a treatment, a sleep aid, or an anxiety remedy.
- We do not invent statistics, certifications, production capacity, or customer cases.
- We do not cite a source because it ranks highly.
- We do not publish a named author or expert that does not exist.

---

## FAQ

### Q: Why does IncenseHub publish under a team byline instead of a named author?
A: Because there is no single named person behind the site to claim authorship, and inventing one would be exactly the kind of fake authority the site is built to avoid. A collective "IncenseHub Editorial Team" byline is honest: it signals that the content follows a defined editorial process without attaching a fabricated name or credential to it. Authority here rests on source traceability and the eight-step method, which any reader can audit page by page.

### Q: How can I tell whether a claim on a IncenseHub page is fact or tradition?
A: Look at the labels and the evidence tier. Traditional use is introduced as traditional, historical record as history, trade terminology as market convention, and scientific evidence as scientific, with its source and tier cited. When a claim is uncertain, the page says so directly. The evidence tier — from Tier 1 (scientific/government) to Tier 6 (editorial synthesis) — is attached to the source, not buried in prose.

### Q: What happens when IncenseHub gets something wrong?
A: The error is corrected at its source and the page's review date is updated. If a dataset is involved, the version is bumped and the change is logged in the changelog. A wrong entity is marked deprecated or pointed at its successor rather than silently deleted, so existing links keep working. Corrections are not announced with a fake reviewer attribution.

### Q: What sources does IncenseHub accept?
A: Sources are matched to the subject of the claim — botanical databases and papers for botanical facts, the classical texts and academic work for history, peer-reviewed research for science, government and standards bodies for regulation, and industry documentation for trade practice. Low-quality SEO content is never used as primary evidence, and external links are limited to an allow-list of authoritative hosts.

---

## Sources

- [IncenseHub Editorial Methodology (this page)](/blog/incensehub-editorial-methodology/)
- [IncenseHub Knowledge Map](/blog/incensehub-knowledge-map/) — the entity and dataset map this method feeds.
- [IncenseHub Terminology dataset](https://data.incensehub.org/datasets/terminology.json) — the canonical Chinese–English glossary referenced in step 3.
- [IncenseHub Ingredient dataset](https://data.incensehub.org/datasets/ingredients.json) — the structured, evidence-tiered ingredient definitions.
- 本草纲目 and 香乘 — classical primary texts, cited in the pages where they are the source.

## Related Resources

- [The Xiangpu Incense Manuals](/blog/xiangpu-incense-manuals/) — the classical manuals used as a historical source.
- [IncenseHub Knowledge Map](/blog/incensehub-knowledge-map/)
- [Ingredient Encyclopedia](/ingredients/)
- [Open Datasets](https://data.incensehub.org)
- [llms.txt](/llms.txt) — the machine-readable site summary.
