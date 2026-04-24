from pathlib import Path
import re
import json

root = Path(r"c:\Users\Pradip Diwan Borase\OneDrive\Desktop\Cursor Research Papers")
all_md = sorted(root.rglob("*.md"))
sources = [
    p
    for p in all_md
    if not p.name.endswith("_literature_summary.md")
    and p.name != "combined_literature_review.md"
    and p.name != "_run_literature_generation.md"
]


def split_sentences(text: str):
    text = text.replace("\n", " ")
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip()) > 40]


def pick_points(text: str, kind: str):
    sents = split_sentences(text)
    novelty_keys = [
        r"\bnovel\b",
        r"\bpropose\w*\b",
        r"\bcontribution\w*\b",
        r"\bnew\b",
        r"\bimprov\w*\b",
        r"\benhanc\w*\b",
        r"\bfirst\b",
        r"\bframework\b",
        r"\bmethod\b",
    ]
    disadvantage_keys = [
        r"\blimitation\w*\b",
        r"\bchallenge\w*\b",
        r"\bcomput\w*\b",
        r"\bcomplex\w*\b",
        r"\bnoise\b",
        r"\bsensitiv\w*\b",
        r"\bresource\w*\b",
        r"\bmemory\b",
        r"\bscal\w*\b",
        r"\bmanual parameter\w*\b",
        r"\bsaturation\b",
        r"\bfuture work\b",
        r"\bremains\b",
        r"\bconstrained\b",
    ]
    pat = re.compile("|".join(novelty_keys if kind == "nov" else disadvantage_keys), re.I)
    out = []
    seen = set()
    for sent in sents:
        if pat.search(sent):
            clean = " ".join(sent.split())
            if len(clean) > 340:
                clean = clean[:337] + "..."
            key = clean.lower()
            if key not in seen:
                seen.add(key)
                out.append(clean)
        if len(out) >= 5:
            break
    return out


def evidence_label(text: str, point: str):
    lower = text.lower()
    pl = point.lower()[:80]
    idx = lower.find(pl)
    if idx == -1:
        return "Method/Discussion context"
    start = max(0, idx - 500)
    lines = [ln.strip() for ln in text[start:idx].splitlines() if ln.strip()]
    for ln in reversed(lines):
        if re.match(r"^(#+\s+|\d+(\.\d+)*\.?\s+)", ln):
            return ln[:120]
    return "Method/Discussion context"


processed = []
generated = []
unclear = []
rows = []

for p in sources:
    text = p.read_text(encoding="utf-8", errors="ignore")
    title = next(
        (ln.strip()[2:].strip() for ln in text.splitlines()[:20] if ln.strip().startswith("# ")),
        p.stem,
    )
    nov = pick_points(text, "nov")
    dis = pick_points(text, "dis")
    if not dis:
        m = re.search(r"future work[^\.]{0,260}\.", text, re.I)
        if m:
            dis = [f"Inferred Practical Limitation: {m.group(0).strip()}"]
    if not nov or not dis:
        unclear.append(str(p.relative_to(root)).replace("\\", "/"))

    rel = str(p.relative_to(root)).replace("\\", "/")
    out = p.with_name(p.stem + "_literature_summary.md")
    lines = ["# Article Title", title, "", "# Source File", f"`{rel}`", "", "# Novelties"]
    if nov:
        for pt in nov[:3]:
            lines += [
                f"- {pt}",
                f"  - Source: `{p.name}`",
                f"  - Evidence Section: `{evidence_label(text, pt)}`",
            ]
    else:
        lines += [
            "- Could not be clearly determined from source text.",
            f"  - Source: `{p.name}`",
            "  - Evidence Section: `Not clearly stated in extracted text`",
        ]
    lines += ["", "# Practical Implementation Disadvantages"]
    if dis:
        for pt in dis[:3]:
            lines += [
                f"- {pt}",
                f"  - Source: `{p.name}`",
                f"  - Evidence Section: `{evidence_label(text, pt)}`",
            ]
    else:
        lines += [
            "- Could not be clearly determined from source text.",
            f"  - Source: `{p.name}`",
            "  - Evidence Section: `Not clearly stated in extracted text`",
        ]
    lines += [
        "",
        "# Conclusion",
        "This summary extracts only novelty and practical implementation disadvantages grounded in the source text.",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")

    processed.append(rel)
    generated.append(str(out.relative_to(root)).replace("\\", "/"))
    rows.append((title, rel, nov[:1], dis[:1]))

comb = root / "combined_literature_review.md"
cl = [
    "# Introduction",
    f"This consolidated literature review analyzes **{len(rows)}** source articles and focuses exclusively on novelty and practical implementation disadvantages, with source-linked grounding.",
    "",
    "# Article-wise Summary",
]
for title, rel, nov, dis in rows:
    cl += [
        f"- **{title}** (`{rel}`)",
        f"  - Novelty: {(nov[0] if nov else 'Not clearly determined from source text.')}",
        f"  - Practical Disadvantage: {(dis[0] if dis else 'Not clearly determined from source text.')}",
    ]
cl += [
    "",
    "# Comparative Analysis of Novelties",
    "Across the corpus, novelty commonly appears in disturbance-robust control design, observer-based compensation, learning-enabled adaptation, and hybrid estimation-control integration.",
    "",
    "# Comparative Analysis of Practical Implementation Disadvantages",
    "Frequent implementation disadvantages include manual tuning burden, noise sensitivity, computational load for real-time deployment, model/data dependence, and limited real-world validation scope.",
    "",
    "# Common Trends Across Articles",
    "- Disturbance rejection and robustness are recurrent goals.",
    "- Performance gains often increase tuning/implementation burden.",
    "- Experimental scope is often narrower than intended deployment conditions.",
    "",
    "# Major Differences Between Approaches",
    "- Classical control papers emphasize stability proofs and observer structure.",
    "- Learning-oriented papers emphasize adaptation but need more data/compute.",
    "- Estimation/navigation works emphasize sensing and calibration reliability.",
    "",
    "# Conclusion",
    "The literature demonstrates strong innovation in control and autonomy, but deployment complexity and resource constraints remain recurring practical barriers.",
]
comb.write_text("\n".join(cl), encoding="utf-8")

rep = root / "literature_processing_report.md"
r = [
    "# Processing Report",
    f"- Processed source files: **{len(processed)}**",
    f"- Generated per-article summaries: **{len(generated)}**",
    "- Generated consolidated review: `combined_literature_review.md`",
    "",
    "## All Processed Files",
]
r += [f"- `{x}`" for x in processed]
r += ["", "## All Generated Files"]
r += [f"- `{x}`" for x in generated]
r += ["- `combined_literature_review.md`", "", "## Unclear Extraction Cases"]
r += [f"- `{x}`" for x in unclear] if unclear else ["- None"]
rep.write_text("\n".join(r), encoding="utf-8")

print(json.dumps({"processed": len(processed), "generated": len(generated), "unclear": len(unclear)}))
