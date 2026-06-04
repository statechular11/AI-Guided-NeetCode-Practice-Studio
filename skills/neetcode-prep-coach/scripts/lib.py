from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


REVIEWED_STATUSES = {"reviewed", "mastered"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def package_root(raw: str | Path) -> Path:
    root = Path(raw).expanduser().resolve()
    required = [
        root / "problems",
        root / "study_plans",
        root / "tags",
        root / "tools" / "run_problem.py",
        root / "tools" / "validate_tree.py",
        root / "WORKFLOW.md",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit("Not a valid NeetCode Prep Kit root; missing: " + ", ".join(missing))
    return root


def command_context(root: Path) -> dict[str, str]:
    cwd = root
    prefix = "tools"
    return {
        "cwd": str(cwd),
        "module_prefix": prefix,
        "run_problem_module": f"{prefix}.run_problem",
        "validate_tree_module": f"{prefix}.validate_tree",
    }


def problem_metadata_paths(root: Path) -> list[Path]:
    return sorted((root / "problems").glob("*/metadata.json"))


def load_problem_records(root: Path) -> list[dict[str, Any]]:
    records = []
    for path in problem_metadata_paths(root):
        item = load_json(path)
        item["_metadata_path"] = str(path)
        item["_problem_dir"] = str(path.parent)
        records.append(item)
    return records


def normalize_query(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def resolve_problem(root: Path, query: str) -> tuple[Path, dict[str, Any]]:
    raw = query.strip()
    candidate = Path(raw).expanduser()
    if candidate.exists():
        problem_dir = candidate.resolve()
        if problem_dir.is_file():
            problem_dir = problem_dir.parent
        metadata = problem_dir / "metadata.json"
        if metadata.exists():
            return problem_dir, load_json(metadata)

    rel = (root / raw).resolve()
    if rel.exists():
        problem_dir = rel if rel.is_dir() else rel.parent
        metadata = problem_dir / "metadata.json"
        if metadata.exists():
            return problem_dir, load_json(metadata)

    records = load_problem_records(root)
    exact = []
    normalized = normalize_query(raw)
    numeric = raw.lstrip("0")
    for record in records:
        folder = record.get("folder", "")
        title = record.get("title", "")
        slug = record.get("slug", "")
        rid = str(record.get("id", ""))
        if raw == folder or raw == slug or raw == title or numeric == rid:
            exact.append(record)
        elif normalized and normalized in {
            normalize_query(folder),
            normalize_query(title),
            normalize_query(slug),
        }:
            exact.append(record)
    if len(exact) == 1:
        return Path(exact[0]["_problem_dir"]), strip_private_keys(exact[0])
    if len(exact) > 1:
        raise SystemExit("Ambiguous problem query; matches: " + ", ".join(item["folder"] for item in exact))

    fuzzy = []
    for record in records:
        haystack = " ".join(
            [
                normalize_query(record.get("folder", "")),
                normalize_query(record.get("title", "")),
                normalize_query(record.get("slug", "")),
            ]
        )
        if normalized and normalized in haystack:
            fuzzy.append(record)
    if len(fuzzy) == 1:
        return Path(fuzzy[0]["_problem_dir"]), strip_private_keys(fuzzy[0])
    if fuzzy:
        raise SystemExit("Ambiguous problem query; matches: " + ", ".join(item["folder"] for item in fuzzy[:20]))
    raise SystemExit(f"Could not resolve problem: {query}")


def strip_private_keys(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if not key.startswith("_")}


def markdown_table(rows: list[list[str]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def status_of(record: dict[str, Any]) -> str:
    return str(record.get("status") or "todo")


def problem_sort_key(record: dict[str, Any]) -> tuple[int, int, str]:
    order = record.get("order")
    try:
        order_value = int(order)
    except Exception:
        order_value = 10**9
    return order_value, int(record.get("id", 10**9)), record.get("folder", "")


def write_status_csv(root: Path, records: list[dict[str, Any]]) -> None:
    path = root / "indexes" / "status.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "title", "difficulty", "section", "tags", "status", "last_reviewed"])
        for record in sorted(records, key=problem_sort_key):
            writer.writerow(
                [
                    record.get("id", ""),
                    record.get("title", ""),
                    record.get("difficulty", ""),
                    record.get("section", ""),
                    "|".join(record.get("tags", [])),
                    status_of(record),
                    record.get("last_reviewed", ""),
                ]
            )
