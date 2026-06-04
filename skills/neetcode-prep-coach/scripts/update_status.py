from __future__ import annotations

import argparse
import json
from datetime import datetime

from lib import package_root, resolve_problem, write_json


ALLOWED = {"todo", "attempted", "passed-local", "reviewed", "needs-redo", "mastered"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Update a problem status in metadata.json.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--status", required=True, choices=sorted(ALLOWED))
    parser.add_argument("--tests", choices=["passed", "failed", "not-run"])
    parser.add_argument("--quality", choices=["solid", "needs-work", "not-reviewed"])
    parser.add_argument("--summary", default="")
    args = parser.parse_args()

    root = package_root(args.root)
    problem_dir, metadata = resolve_problem(root, args.problem)
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    metadata["status"] = args.status
    if args.status in {"reviewed", "mastered"}:
        metadata["last_reviewed"] = now
    metadata.setdefault("review_history", [])
    metadata["review_history"].append(
        {
            "timestamp": now,
            "status": args.status,
            "tests": args.tests or "",
            "quality": args.quality or "",
            "summary": args.summary,
        }
    )
    write_json(problem_dir / "metadata.json", metadata)
    print(json.dumps({"metadata": str(problem_dir / "metadata.json"), "status": args.status}, indent=2))


if __name__ == "__main__":
    main()
