from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    problems = []
    tag_map = defaultdict(list)
    for metadata_path in sorted((ROOT / "problems").glob("*/metadata.json")):
        metadata = json.loads(metadata_path.read_text())
        problems.append(metadata)
        for tag in metadata["tags"]:
            tag_map[tag].append(metadata)

    (ROOT / "indexes").mkdir(exist_ok=True)
    (ROOT / "indexes" / "problems.json").write_text(json.dumps(problems, indent=2) + "\n")
    (ROOT / "indexes" / "tags.json").write_text(json.dumps({k: [p["folder"] for p in v] for k, v in tag_map.items()}, indent=2) + "\n")

    with (ROOT / "indexes" / "status.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "difficulty", "section", "tags", "status", "last_reviewed"])
        for p in problems:
            writer.writerow([p["id"], p["title"], p["difficulty"], p["section"], "|".join(p["tags"]), p["status"], ""])

    for tag, items in tag_map.items():
        tag_dir = ROOT / "tags" / tag
        tag_dir.mkdir(parents=True, exist_ok=True)
        rows = ["| ID | Problem | Difficulty | Section | Status |", "| --- | --- | --- | --- | --- |"]
        for p in sorted(items, key=lambda x: x["id"]):
            rows.append(f"| {p['id']:04d} | [{p['title']}](../../problems/{p['folder']}) | {p['difficulty']} | {p['section']} | {p['status']} |")
        (tag_dir / "problems.md").write_text(f"# {tag.replace('-', ' ').title()}\n\n" + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
