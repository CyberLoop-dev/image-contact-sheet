#!/usr/bin/env python3
"""Build a labeled contact sheet from images in a directory."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

SUPPORTED = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif", ".tiff"}

def build_contact_sheet(source: Path, output: Path, columns: int, thumb_width: int, thumb_height: int):
    files = sorted(p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED and p.resolve() != output.resolve())
    cell_height, cell_width = thumb_height + 46, thumb_width + 24
    rows = max(1, (len(files) + columns - 1) // columns)
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), "#101827")
    draw, written, failed = ImageDraw.Draw(sheet), 0, 0
    for index, path in enumerate(files):
        try:
            with Image.open(path) as original:
                image = ImageOps.exif_transpose(original).convert("RGB")
                image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
                x = (index % columns) * cell_width + (thumb_width - image.width) // 2 + 12
                y = (index // columns) * cell_height + (thumb_height - image.height) // 2 + 8
                sheet.paste(image, (x, y))
                label = path.name if len(path.name) <= 28 else path.name[:25] + "..."
                draw.text(((index % columns) * cell_width + 12, (index // columns) * cell_height + thumb_height + 16), label, fill="#e5edf7")
                written += 1
        except (OSError, ValueError): failed += 1
    if written == 0: raise ValueError("No readable supported images were found.")
    output.parent.mkdir(parents=True, exist_ok=True); sheet.save(output)
    return written, failed

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path); parser.add_argument("-o", "--output", type=Path, default=Path("contact-sheet.jpg"))
    parser.add_argument("--columns", type=int, default=4); parser.add_argument("--thumb-width", type=int, default=220)
    parser.add_argument("--thumb-height", type=int, default=150); args = parser.parse_args()
    if not args.folder.is_dir(): parser.error(f"folder does not exist: {args.folder}")
    if min(args.columns, args.thumb_width, args.thumb_height) < 1: parser.error("columns and thumbnail dimensions must be positive")
    try: written, failed = build_contact_sheet(args.folder, args.output, args.columns, args.thumb_width, args.thumb_height)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr); return 2
    print(f"Contact sheet: {args.output} ({written} images, {failed} unreadable)"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
