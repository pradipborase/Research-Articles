"""Merge all PDFs under this folder into All_Articles_Merged.pdf (pypdf PdfWriter)."""
import os
import shutil
import sys
import tempfile
from pathlib import Path

from pypdf import PdfWriter

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root = Path(__file__).resolve().parent
pdfs = sorted(root.rglob("*.pdf"))
pdfs = [p for p in pdfs if p.name.lower() != "all_articles_merged.pdf"]

out = root / "All_Articles_Merged.pdf"
errors = []
writer = PdfWriter()

for i, pdf_path in enumerate(pdfs, 1):
    try:
        writer.append(str(pdf_path))
        print(f"[{i}/{len(pdfs)}] OK {pdf_path.relative_to(root)}", flush=True)
    except Exception as e:
        errors.append((pdf_path, str(e)))
        print(f"[{i}/{len(pdfs)}] SKIP {pdf_path.relative_to(root)}: {e}", flush=True)

fd, tmp_path = tempfile.mkstemp(suffix=".pdf")
os.close(fd)
try:
    with open(tmp_path, "wb") as tmp_file:
        writer.write(tmp_file)
finally:
    writer.close()

try:
    if out.exists():
        out.unlink()
except OSError:
    pass
shutil.copy2(tmp_path, out)
os.unlink(tmp_path)

print(f"\nWritten: {out}")
print(f"Sources: {len(pdfs) - len(errors)} ok, {len(errors)} skipped")
if errors:
    for p, msg in errors:
        print(f"  {p.relative_to(root)}: {msg}")
