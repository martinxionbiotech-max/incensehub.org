# SEO-EXPERIMENTS.md — IncenseHub

Experiment ledger. Changes that are measurable are recorded as experiments before rollout.

## Schema

| Field | Meaning |
|---|---|
| Experiment ID | E-### |
| Question | hypothesis |
| Page | target page(s) |
| Baseline | current metric |
| Change | what changed |
| Start date | date |
| Measurement period | window |
| Result | outcome |
| Decision | keep / revert / iterate |
| Rollout status | testing / rolled out / reverted |

## Candidate experiment surfaces

- Title / meta description
- Direct-answer block
- Internal links
- Comparison tables
- FAQ
- Entity presentation
- CTA placement
- Content structure
- Visual structure

## Loop

```
Observe → Hypothesis → Change → Measure → Learn → Roll out → Document
```

> **Never assume.** Record successful patterns; do not blindly replicate failed ones. No experiment rows yet — populate as tests actually run.
