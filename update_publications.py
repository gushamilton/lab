#!/usr/bin/env python3
import argparse
import datetime as dt
import sys
from typing import Any, Dict, List

import yaml
from scholarly import ProxyGenerator, scholarly


AUTHOR_ID = "FPfGzxoAAAAJ"
DEFAULT_OUTPUT = "_data/publications.yml"


def _best_url(pub: Dict[str, Any]) -> str:
    return pub.get("pub_url") or pub.get("eprint_url") or ""


def _normalize_pub(pub: Dict[str, Any]) -> Dict[str, Any]:
    bib = pub.get("bib", {})
    title = bib.get("title", "").strip()
    venue = bib.get("venue", "").strip()
    year = bib.get("year", "").strip()
    url = _best_url(pub)
    return {
        "title": title,
        "venue": venue,
        "year": year,
        "url": url,
    }


def _year_key(pub: Dict[str, Any]) -> int:
    try:
        return int(pub.get("year") or 0)
    except ValueError:
        return 0


def fetch_publications(max_items: int) -> List[Dict[str, Any]]:
    pg = ProxyGenerator()
    scholarly.use_proxy(pg)
    author = scholarly.search_author_id(AUTHOR_ID)
    author = scholarly.fill(author, sections=["publications"])

    publications: List[Dict[str, Any]] = []
    for pub in author.get("publications", []):
        try:
            filled = scholarly.fill(pub)
        except Exception:
            filled = pub
        normalized = _normalize_pub(filled)
        if normalized["title"]:
            publications.append(normalized)

    publications.sort(key=_year_key, reverse=True)
    if max_items:
        publications = publications[:max_items]
    return publications


def main() -> int:
    parser = argparse.ArgumentParser(description="Update publications from Google Scholar.")
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--max", type=int, default=50)
    args = parser.parse_args()

    publications = fetch_publications(args.max)
    payload: List[Dict[str, Any]] = publications

    with open(args.output, "w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, sort_keys=False, allow_unicode=False)

    print(f"Wrote {len(publications)} publications to {args.output} on {dt.date.today().isoformat()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
