import sys
from pathlib import Path

import yaml
from scholarly import scholarly

AUTHOR_ID = "FPfGzxoAAAAJ"
OUTPUT_PATH = Path("_data/publications.yml")
MAX_PUBLICATIONS = 6


def _coerce_year(value: str | None) -> int | None:
    if not value:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def fetch_publications() -> list[dict]:
    author = scholarly.search_author_id(AUTHOR_ID)
    author = scholarly.fill(author, sections=["publications"])

    publications: list[dict] = []
    seen_titles: set[str] = set()
    for publication in author.get("publications", []):
        filled = scholarly.fill(publication)
        bib = filled.get("bib", {})
        title = bib.get("title")
        if not title or title in seen_titles:
            continue
        seen_titles.add(title)

        venue = (
            bib.get("journal")
            or bib.get("venue")
            or bib.get("conference")
            or bib.get("publisher")
            or ""
        )
        year = _coerce_year(bib.get("pub_year") or bib.get("year"))
        publications.append({
            "title": title,
            "venue": venue,
            "year": year,
        })

    publications.sort(key=lambda item: item.get("year") or 0, reverse=True)
    return publications[:MAX_PUBLICATIONS]


def write_publications(publications: list[dict]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        yaml.safe_dump(publications, file, sort_keys=False, allow_unicode=True)


def main() -> int:
    try:
        publications = fetch_publications()
    except Exception as exc:  # pragma: no cover - network/runtime issues
        print(f"Error fetching publications: {exc}", file=sys.stderr)
        return 1

    if not publications:
        print("No publications fetched.", file=sys.stderr)
        return 1

    write_publications(publications)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
