from pathlib import Path
import sys

import fitz  # PyMuPDF


def sanitize_text(text: str) -> str:
    # Keep markdown readable while avoiding null bytes.
    return text.replace("\x00", "")


def pdf_to_md(pdf_path: Path, md_path: Path) -> None:
    with fitz.open(pdf_path) as doc:
        lines = [f"# {pdf_path.name}", ""]
        for page_index, page in enumerate(doc, start=1):
            text = page.get_text("text")
            lines.append(f"## Page {page_index}")
            lines.append("")
            lines.append(sanitize_text(text).strip())
            lines.append("")
        md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    pdfs = sorted(root.rglob("*.pdf"))
    success = 0
    failed = 0

    for idx, pdf in enumerate(pdfs, start=1):
        md = pdf.with_suffix(".md")
        try:
            pdf_to_md(pdf, md)
            success += 1
            print(f"[{idx}/{len(pdfs)}] OK {pdf.relative_to(root)} -> {md.name}", flush=True)
        except Exception as exc:
            failed += 1
            print(f"[{idx}/{len(pdfs)}] FAIL {pdf.relative_to(root)}: {exc}", flush=True)

    print(f"\nCompleted. Success: {success}, Failed: {failed}, Total PDFs: {len(pdfs)}")


if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
