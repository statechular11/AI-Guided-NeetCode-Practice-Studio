from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from lib import package_root, resolve_problem


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Read the latest recorded test run for a problem.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    args = parser.parse_args()

    root = package_root(args.root)
    problem_dir, _metadata = resolve_problem(root, args.problem)
    latest_path = problem_dir / "test_history" / "latest.json"
    if not latest_path.exists():
        print(json.dumps({"exists": False, "stale": True}, indent=2))
        return

    record = json.loads(latest_path.read_text(encoding="utf-8"))
    solution_path = problem_dir / "solution.py"
    current_hash = file_sha256(solution_path) if solution_path.exists() else ""
    recorded_hash = record.get("target_sha256", "")
    stale = record.get("target") != "solution" or recorded_hash != current_hash
    payload = {
        "exists": True,
        "stale": stale,
        "latest": record,
        "current_solution_sha256": current_hash,
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
