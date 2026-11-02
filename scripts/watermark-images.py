#!/usr/bin/env python3
"""Watermark IncenseHub content images with 'incensehub.org' at the bottom.

Skips brand assets, favicons, social cards and SVGs. Re-encodes in place
(WebP q=88 / JPEG q=90 / PNG optimized) while preserving dimensions.
"""
import os, sys, glob
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "public", "images")
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TEXT = "incensehub.org"

SKIP_DIRS = {"brand"}
SKIP_PREFIXES = ("favicon", "og-image", "logo")

def should_skip(path):
    rel = os.path.relpath(path, IMG_DIR)
    parts = rel.split(os.sep)
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return True
    name = parts[-1].lower()
    if name.endswith(".svg"):
        return True
    return name.startswith(SKIP_PREFIXES)

def watermark(path, out=None):
    im = Image.open(path)
    fmt = im.format
    base = im.convert("RGBA")
    w, h = base.size
    band = max(36, int(round(h * 0.065)))
    font_size = max(20, int(round(band * 0.55)))
    font = ImageFont.truetype(FONT_BOLD, font_size)
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rectangle([0, h - band, w, h], fill=(10, 10, 10, 185))
    bbox = d.textbbox((0, 0), TEXT, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (w - tw) / 2 - bbox[0]
    y = h - band + (band - th) / 2 - bbox[1]
    d.text((x, y), TEXT, font=font, fill=(255, 255, 255, 240), stroke_width=1, stroke_fill=(0, 0, 0, 200))
    out_img = Image.alpha_composite(base, overlay)
    target = out or path
    if fmt == "WEBP":
        out_img.convert("RGB").save(target, "WEBP", quality=88, method=6)
    elif fmt == "JPEG":
        out_img.convert("RGB").save(target, "JPEG", quality=90, optimize=True, progressive=True)
    elif fmt == "PNG":
        out_img.save(target, "PNG", optimize=True)
    else:
        out_img.save(target)
    return (w, h, band, font_size)

def main():
    samples = sys.argv[1:]
    if samples:
        outdir = "/tmp/wm-samples"
        os.makedirs(outdir, exist_ok=True)
        for p in samples:
            out = os.path.join(outdir, os.path.basename(p))
            print(p, "->", out, watermark(p, out))
        return
    count = 0
    for p in sorted(glob.glob(os.path.join(IMG_DIR, "**", "*"), recursive=True)):
        if not os.path.isfile(p) or should_skip(p):
            continue
        try:
            watermark(p)
            count += 1
        except Exception as e:
            print("FAIL", p, e)
    print(f"watermarked {count} images")

if __name__ == "__main__":
    main()
