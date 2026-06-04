from __future__ import annotations

import argparse
import json
from pathlib import Path

from lib import REVIEWED_STATUSES, command_context, load_json, load_problem_records, package_root, problem_sort_key, status_of


def load_study_plan_folders(root: Path, study_plan: str | None) -> list[str] | None:
    if not study_plan:
        return None
    path = Path(study_plan).expanduser()
    if not path.is_absolute():
        path = root / study_plan
    if path.suffix == ".md":
        json_path = path.with_suffix(".json")
    else:
        json_path = path
    if not json_path.exists():
        raise SystemExit(f"Study-plan JSON not found: {json_path}")
    rows = load_json(json_path)
    if not isinstance(rows, list):
        raise SystemExit(f"Study-plan JSON should contain a list: {json_path}")
    return [row["folder"] for row in rows if "folder" in row]


def main() -> None:
    parser = argparse.ArgumentParser(description="Find the next problem by study plan, section, or tag.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--study-plan")
    parser.add_argument("--section")
    parser.add_argument("--tag")
    parser.add_argument("--include-status", action="append", default=[])
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    root = package_root(args.root)
    records = load_problem_records(root)
    by_folder = {record["folder"]: record for record in records}
    plan_folders = load_study_plan_folders(root, args.study_plan)
    if plan_folders is not None:
        ordered = [by_folder[folder] for folder in plan_folders if folder in by_folder]
    else:
        ordered = sorted(records, key=problem_sort_key)

    if args.section:
        needle = args.section.lower()
        ordered = [
            record
            for record in ordered
            if needle in str(record.get("section", "")).lower()
            or any(needle in str(value).lower() for value in record.get("sections_by_plan", {}).values())
        ]
    if args.tag:
        tag = args.tag.lower().replace(" ", "-")
        ordered = [record for record in ordered if tag in {item.lower() for item in record.get("tags", [])}]

    allowed = set(args.include_status)
    if allowed:
        ordered = [record for record in ordered if status_of(record) in allowed]
    else:
        ordered = [record for record in ordered if status_of(record) not in REVIEWED_STATUSES]

    context = command_context(root)
    results = []
    for record in ordered[: args.limit]:
        problem_dir = Path(record["_problem_dir"])
        rel_problem = problem_dir.relative_to(Path(context["cwd"]))
        results.append(
            {
                "folder": record["folder"],
                "id": record["id"],
                "title": record["title"],
                "difficulty": record.get("difficulty"),
                "section": record.get("section"),
                "tags": record.get("tags", []),
                "status": status_of(record),
                "problem_dir": str(problem_dir),
                "test_command": f"python -B -m {context['run_problem_module']} {rel_problem}",
            }
        )

    print(
        json.dumps(
            {
                "count": len(results),
                "command_cwd": context["cwd"],
                "results": results,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
