from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from lib import command_context, package_root, resolve_problem


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run and record a NeetCode Prep Kit problem test.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--reference", action="store_true")
    parser.add_argument("--all-cases", action="store_true", help="Print every case, including passed cases.")
    parser.add_argument("--compact", action="store_true", help="Deprecated compatibility flag; the compact failed-only report is now the default.")
    parser.add_argument("--all-failures", action="store_true", help="Print every failing case without passed cases; this is the default.")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--no-color", action="store_true")
    args = parser.parse_args()

    root = package_root(args.root)
    problem_dir, metadata = resolve_problem(root, args.problem)
    context = command_context(root)
    rel_problem = problem_dir.relative_to(Path(context["cwd"]))

    command = ["python", "-B", "-m", context["run_problem_module"], str(rel_problem)]
    if args.reference:
        command.append("--reference")
    if args.all_cases:
        command.append("--all-cases")
    if args.all_failures:
        command.append("--all-failures")
    if args.verbose:
        command.append("--verbose")
    if args.no_color:
        command.append("--no-color")

    target = problem_dir / ("solution.py" if not args.reference else metadata.get("reference_solution", ""))
    target_hash = file_sha256(target) if target.exists() and target.is_file() else ""

    proc = subprocess.run(command, cwd=context["cwd"], text=True, capture_output=True)

    # Test mode is intentionally plain: print the runner's evidence only.
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="")

    now = datetime.now(timezone.utc).astimezone()
    try:
        target_file = str(target.relative_to(root))
    except ValueError:
        target_file = str(target)

    record = {
        "timestamp": now.isoformat(timespec="seconds"),
        "problem": metadata.get("folder"),
        "id": metadata.get("id"),
        "title": metadata.get("title"),
        "target": "reference" if args.reference else "solution",
        "target_file": target_file,
        "target_sha256": target_hash,
        "command": " ".join(command),
        "cwd": "<PACKAGE_ROOT>",
        "returncode": proc.returncode,
        "passed": proc.returncode == 0,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }

    history_dir = problem_dir / "test_history"
    history_dir.mkdir(exist_ok=True)
    latest_path = history_dir / "latest.json"
    jsonl_path = history_dir / "history.jsonl"
    latest_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with jsonl_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
