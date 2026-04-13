# /// script
# dependencies = ["pikepdf", "Pillow"]
# requires-python = ">=3.9"
# ///
"""Recompress images inside a PDF without touching vector content."""
import sys
from io import BytesIO
from pathlib import Path

import pikepdf
from PIL import Image

MAX_DIM = 2400
JPEG_QUALITY = 80
MIN_SIZE_KB = 50


def fmt(size: int) -> str:
    return f"{size / 1048576:.1f} MB" if size > 1048576 else f"{size / 1024:.0f} KB"


def squeeze(input_path: Path, output_path: Path) -> bool:
    pdf = pikepdf.Pdf.open(input_path)

    images = []
    for i in range(len(pdf.objects)):
        try:
            obj = pdf.get_object((i, 0))
            if not isinstance(obj, pikepdf.Stream):
                continue
            if obj.get("/Subtype") != pikepdf.Name.Image:
                continue
            w = int(obj.get("/Width", 0))
            h = int(obj.get("/Height", 0))
            raw_len = len(obj.read_raw_bytes())
            if w < 10 or h < 10 or raw_len < MIN_SIZE_KB * 1024:
                continue
            images.append((i, obj, w, h, raw_len))
        except Exception:
            continue

    compressed = 0
    for _, obj, w, h, orig_len in images:
        try:
            pil_img = pikepdf.PdfImage(obj).as_pil_image()

            scale = min(MAX_DIM / max(w, h), 1.0)
            if scale < 1.0:
                pil_img = pil_img.resize(
                    (int(w * scale), int(h * scale)), Image.LANCZOS
                )

            if pil_img.mode in ("RGBA", "LA", "P"):
                pil_img = pil_img.convert("RGB")
            elif pil_img.mode == "1":
                pil_img = pil_img.convert("L")

            buf = BytesIO()
            if pil_img.mode == "L":
                pil_img.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
                cs = pikepdf.Name.DeviceGray
            else:
                if pil_img.mode != "RGB":
                    pil_img = pil_img.convert("RGB")
                pil_img.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
                cs = pikepdf.Name.DeviceRGB

            new_data = buf.getvalue()
            if len(new_data) >= orig_len:
                continue

            obj.write(new_data, filter=pikepdf.Name.DCTDecode)
            obj[pikepdf.Name.Width] = pil_img.width
            obj[pikepdf.Name.Height] = pil_img.height
            obj[pikepdf.Name.ColorSpace] = cs
            obj[pikepdf.Name.BitsPerComponent] = 8

            for key in ["/SMask", "/DecodeParms", "/Decode"]:
                if key in obj:
                    del obj[key]

            compressed += 1
        except Exception:
            continue

    pdf.save(
        output_path,
        linearize=True,
        object_stream_mode=pikepdf.ObjectStreamMode.generate,
    )
    pdf.close()

    orig_size = input_path.stat().st_size
    comp_size = output_path.stat().st_size
    pct = (1 - comp_size / orig_size) * 100
    print(f"{input_path.name}  {fmt(orig_size)} → {fmt(comp_size)}  ({pct:.1f}% smaller)")
    return True


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: pdfsqueeze <file.pdf> [file2.pdf ...] [-o output.pdf]")
        sys.exit(0)

    output = None
    files = []
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "-o" and i + 1 < len(args):
            output = args[i + 1]
            i += 2
        else:
            files.append(Path(args[i]))
            i += 1

    if output and len(files) > 1:
        print("Error: -o can only be used with a single input file")
        sys.exit(1)

    for f in files:
        if not f.exists():
            print(f"File not found: {f}")
            continue
        out = Path(output) if output else f.with_stem(f.stem + ".squeezed")
        squeeze(f, out)


if __name__ == "__main__":
    main()
