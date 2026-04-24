from pathlib import Path
import re
from datetime import datetime

ROOT = Path(r"c:\Users\Pradip Diwan Borase\OneDrive\Desktop\Cursor Research Papers")

EXCLUDED = {
    "combined_literature_review.md",
    "all_206_articles_literature_summary.md",
    "literature_processing_report.md",
    "All_Merged_PDFs.md",
    "All_Articles_Merged.md",
    "All_Articles_Merged_Light.md",
}


def is_article_md(path: Path) -> bool:
    if path.name in EXCLUDED or path.name.endswith("_literature_summary.md"):
        return False
    rel = path.relative_to(ROOT).as_posix()
    return any(k in rel for k in ["Cluster", "IEEE", "DIOB", "Cursor 6"])


def first_heading(text: str) -> str:
    for line in text.splitlines()[:40]:
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    return "Unknown Title"


def pick_points(text: str, keywords, n=4):
    sent = re.split(r"(?<=[.!?])\s+", text.replace("\n", " "))
    out = []
    seen = set()
    for s in sent:
        s = " ".join(s.split())
        if len(s) < 70:
            continue
        noisy = (
            s.startswith("#")
            or "©" in s
            or "doi.org" in s.lower()
            or "accepted for publication" in s.lower()
            or "keywords:" in s.lower()
            or "citation:" in s.lower()
        )
        if noisy:
            continue
        if any(re.search(k, s, re.I) for k in keywords):
            if s not in seen:
                out.append(s[:500] + ("..." if len(s) > 500 else ""))
                seen.add(s)
        if len(out) >= n:
            break
    return out


def evidence_section(text: str, point: str) -> str:
    idx = text.lower().find(point[:80].lower())
    if idx < 0:
        return "Method/Results discussion"
    window = text[max(0, idx - 800):idx]
    lines = [ln.strip() for ln in window.splitlines() if ln.strip()]
    for ln in reversed(lines):
        if re.match(r"^(#+\s+|\d+(\.\d+)*\.?\s+)", ln):
            return ln[:120]
    return "Method/Results discussion"


novelty_keys = [
    r"\bnovel\b",
    r"\bpropose\w*\b",
    r"\bcontribution\w*\b",
    r"\bframework\b",
    r"\bimprov\w*\b",
    r"\benhanc\w*\b",
    r"\bhybrid\b",
    r"\bcompar\w*\b",
]

disadvantage_keys = [
    r"\blimitation\w*\b",
    r"\bchallenge\w*\b",
    r"\bcomput\w*\b",
    r"\breal-time\b",
    r"\bnoise\b",
    r"\bsaturation\b",
    r"\bresource\w*\b",
    r"\bmemory\b",
    r"\bconverg\w*\b",
    r"\bdynamic environment\b",
    r"\bfuture work\b",
]

articles = [p for p in sorted(ROOT.rglob("*.md")) if is_article_md(p)][:10]
timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")

for path in articles:
    text = path.read_text(encoding="utf-8", errors="ignore")
    title = first_heading(text)
    nov = pick_points(text, novelty_keys, n=3)
    dis = pick_points(text, disadvantage_keys, n=3)

    if not dis:
        fw = re.search(r"future work[^.]{0,250}\.", text, re.I)
        if fw:
            dis = [f"Inferred Practical Limitation: {fw.group(0).strip()}"]

    # Make novelty/practical sections detailed and implementation-focused.
    nov = [f"Detailed novelty: {x}" for x in nov]
    dis = [f"Detailed practical implementation disadvantage: {x}" for x in dis]

    lines = [
        f"Generated on: `{timestamp}`",
        "",
        "# Article Title",
        title,
        "",
        "# Source File",
        f"`{path.relative_to(ROOT).as_posix()}`",
        "",
        "# Novelties",
    ]
    if nov:
        for p in nov:
            lines += [f"- {p}", f"  - Evidence Section: `{evidence_section(text, p)}`"]
    else:
        lines += ["- Could not be clearly determined from source text.", "  - Evidence Section: `Not clearly stated`"]

    lines += ["", "# Practical Implementation Disadvantages"]
    if dis:
        for p in dis:
            lines += [f"- {p}", f"  - Evidence Section: `{evidence_section(text, p)}`"]
    else:
        lines += ["- Could not be clearly determined from source text.", "  - Evidence Section: `Not clearly stated`"]

    lines += ["", "# Conclusion", "Detailed pilot summary focused on novelty and practical implementation disadvantages."]
    out = path.with_name(path.stem + "_literature_summary.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

combined = ROOT / "combined_literature_review_10_articles.md"
body = [
    f"Generated on: `{timestamp}`",
    "",
    "# Introduction",
    "This document consolidates detailed novelty and practical implementation disadvantages for 10 pilot research articles.",
    "",
    "# Article-wise Summary",
]
for p in articles:
    s = p.with_name(p.stem + "_literature_summary.md")
    body += [f"## `{p.relative_to(ROOT).as_posix()}`", s.read_text(encoding="utf-8", errors="ignore"), ""]

combined.write_text("\n".join(body), encoding="utf-8")
print(f"Generated {len(articles)} detailed summaries and combined_literature_review_10_articles.md")
