from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from lib import load_json, load_problem_records, markdown_table, package_root, problem_sort_key, status_of, strip_private_keys, write_json, write_status_csv


def title_from_existing_md(path: Path, fallback: str) -> str:
    if path.exists():
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return fallback


def sync_study_plans(root: Path, records_by_folder: dict[str, dict]) -> list[str]:
    changed = []
    for json_path in sorted((root / "study_plans").glob("*.json")):
        if json_path.name.endswith("_raw.json"):
            continue
        rows = load_json(json_path)
        if not isinstance(rows, list):
            continue
        new_rows = []
        table_rows = []
        for row in rows:
            folder = row.get("folder")
            record = records_by_folder.get(folder)
            if not record:
                new_rows.append(row)
                continue
            updated = dict(row)
            updated.setdefault("id", record.get("id"))
            updated.setdefault("title", record.get("title"))
            updated.setdefault("section", record.get("section"))
            updated["status"] = status_of(record)
            new_rows.append(updated)
            table_rows.append(
                [
                    str(updated.get("order", record.get("order", ""))),
                    f"{int(record['id']):04d}",
                    f"[{record['title']}](../problems/{record['folder']})",
                    record.get("difficulty", ""),
                    updated.get("section") or record.get("section", ""),
                    status_of(record),
                ]
            )
        write_json(json_path, new_rows)
        md_path = json_path.with_suffix(".md")
        title = title_from_existing_md(md_path, json_path.stem.replace("_", " ").title())
        md_path.write_text(
            f"# {title}\n\n" + markdown_table(table_rows, ["Order", "ID", "Problem", "Difficulty", "Section", "Status"]) + "\n",
            encoding="utf-8",
        )
        changed.extend([str(json_path), str(md_path)])
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate progress views from metadata.json.")
    parser.add_argument("--root", required=True)
    args = parser.parse_args()

    root = package_root(args.root)
    records = [strip_private_keys(record) for record in load_problem_records(root)]
    records = sorted(records, key=problem_sort_key)
    records_by_folder = {record["folder"]: record for record in records}

    (root / "indexes").mkdir(exist_ok=True)
    write_json(root / "indexes" / "problems.json", records)

    tag_map = defaultdict(list)
    for record in records:
        for tag in record.get("tags", []):
            tag_map[tag].append(record)
    write_json(root / "indexes" / "tags.json", {tag: [record["folder"] for record in items] for tag, items in sorted(tag_map.items())})
    write_status_csv(root, records)

    changed = [
        str(root / "indexes" / "problems.json"),
        str(root / "indexes" / "tags.json"),
        str(root / "indexes" / "status.csv"),
    ]

    for tag, items in sorted(tag_map.items()):
        tag_dir = root / "tags" / tag
        tag_dir.mkdir(parents=True, exist_ok=True)
        rows = []
        for record in sorted(items, key=lambda item: (item.get("difficulty", ""), int(item.get("id", 10**9)))):
            rows.append(
                [
                    f"{int(record['id']):04d}",
                    f"[{record['title']}](../../problems/{record['folder']})",
                    record.get("difficulty", ""),
                    record.get("section", ""),
                    status_of(record),
                ]
            )
        path = tag_dir / "problems.md"
        path.write_text(f"# {tag.replace('-', ' ').title()}\n\n" + markdown_table(rows, ["ID", "Problem", "Difficulty", "Section", "Status"]) + "\n", encoding="utf-8")
        changed.append(str(path))

    changed.extend(sync_study_plans(root, records_by_folder))
    print(json.dumps({"changed_count": len(changed), "changed": changed}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
