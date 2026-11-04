# Image inventory — IncenseHub

Generated 2026-11-02. Source: IncenseHub archive (`public/images`), identical SHA-256 set to the pre-import archive.

## Summary

- Files: **206** (11.7 MB)
- Referenced in pages: **186**
- Unused but retained: **20**
- Exact duplicates (SHA-256): **0**
- Near-duplicates (dHash ≤ 6): **0 content images**; the only near matches are the intentional brand logo variants (mono / transparent / standard)
- Watermarked: **195 content images** with `incensehub.org` in a bottom band; skipped: brand logos, favicons, social card, SVGs
- ALT coverage: **193/193 rendered images have descriptive ALT**; the header logo uses `alt=""` + `aria-hidden="true"` inside a link with `aria-label="IncenseHub home"` (correct decorative pattern)

## ALT policy

- Every rendered image carries a unique, descriptive ALT (0 duplicate ALT strings).
- Unused images have suggested ALT text in `docs/image-inventory.csv` for future use.
- Decorative logo: empty ALT is intentional.

## Watermark

`scripts/watermark-images.py` — bottom band, height 6.5% (min 36 px), white text with 1 px dark stroke, band alpha 185. Re-encoded WebP q88 / JPEG q90 / PNG optimized; dimensions preserved.

## Full list

See `docs/image-inventory.csv` (206 rows).
