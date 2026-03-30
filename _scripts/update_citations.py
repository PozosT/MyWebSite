"""
Fetch citation data from Google Scholar and update _data/citations.yml

Usage:
    python _scripts/update_citations.py

Requires: scholarly (pip install scholarly)
"""

import yaml
import os
import sys
import time
from pathlib import Path
from difflib import SequenceMatcher

try:
    from scholarly import scholarly
except ImportError:
    print("ERROR: scholarly not installed. Run: pip install scholarly")
    sys.exit(1)

SCHOLAR_ID = "C9PY5CwAAAAJ"
DATA_DIR = Path(__file__).resolve().parent.parent / "_data"
PUBLICATIONS_DIR = Path(__file__).resolve().parent.parent / "_publications"
OUTPUT_FILE = DATA_DIR / "citations.yml"


def normalize_title(title: str) -> str:
    """Normalize title for fuzzy matching."""
    return title.lower().strip().rstrip(".").replace("  ", " ")


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


def load_local_publications() -> list[dict]:
    """Load publication titles from _publications/*.md front matter."""
    pubs = []
    for md_file in sorted(PUBLICATIONS_DIR.glob("*.md")):
        if md_file.name == "alejandratp.bib":
            continue
        content = md_file.read_text(encoding="utf-8")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1])
                    if fm and "title" in fm:
                        pubs.append({
                            "file": md_file.stem,
                            "title": fm["title"],
                        })
                except yaml.YAMLError:
                    pass
    return pubs


def fetch_scholar_data() -> tuple[dict, list[dict]]:
    """Fetch author metrics and publication citations from Google Scholar."""
    print(f"Fetching Scholar profile for ID: {SCHOLAR_ID}...")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "publications"])

    metrics = {
        "name": author.get("name", ""),
        "h_index": author.get("hindex", 0),
        "i10_index": author.get("i10index", 0),
        "total_citations": author.get("citedby", 0),
        "last_updated": time.strftime("%Y-%m-%d"),
    }

    scholar_pubs = []
    for pub in author.get("publications", []):
        bib = pub.get("bib", {})
        scholar_pubs.append({
            "title": bib.get("title", ""),
            "citations": pub.get("num_citations", 0),
            "year": bib.get("pub_year", ""),
            "scholar_url": pub.get("author_pub_id", ""),
        })

    print(f"Found {len(scholar_pubs)} publications on Scholar")
    return metrics, scholar_pubs


def match_publications(local_pubs, scholar_pubs) -> list[dict]:
    """Match local publications with Scholar data using fuzzy title matching."""
    citations = []
    matched_count = 0

    for local in local_pubs:
        best_match = None
        best_score = 0.0

        for sp in scholar_pubs:
            score = similarity(local["title"], sp["title"])
            if score > best_score:
                best_score = score
                best_match = sp

        entry = {"key": local["file"], "title": local["title"]}
        if best_match and best_score >= 0.75:
            entry["citations"] = best_match["citations"]
            entry["scholar_title"] = best_match["title"]
            entry["match_score"] = round(best_score, 2)
            matched_count += 1
        else:
            entry["citations"] = 0
            entry["match_score"] = round(best_score, 2) if best_match else 0

        citations.append(entry)

    print(f"Matched {matched_count}/{len(local_pubs)} local publications")
    return citations


def main():
    local_pubs = load_local_publications()
    print(f"Loaded {len(local_pubs)} local publications")

    metrics, scholar_pubs = fetch_scholar_data()
    citations = match_publications(local_pubs, scholar_pubs)

    output = {
        "metrics": metrics,
        "publications": citations,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=120)

    print(f"\nWritten to {OUTPUT_FILE}")
    print(f"  h-index: {metrics['h_index']}")
    print(f"  i10-index: {metrics['i10_index']}")
    print(f"  Total citations: {metrics['total_citations']}")
    total_matched_cites = sum(p["citations"] for p in citations)
    print(f"  Sum of matched citations: {total_matched_cites}")


if __name__ == "__main__":
    main()
