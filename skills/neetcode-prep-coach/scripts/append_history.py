from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from lib import package_root, resolve_problem


ALLOWED_KINDS = {"debug", "review", "consolidate"}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8").strip()
    return (args.body or "").strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Append Debug/Review/Consolidate history for a problem.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--kind", required=True, choices=sorted(ALLOWED_KINDS))
    parser.add_argument("--title", default="")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--outcome", default="")
    parser.add_argument("--tests", default="")
    parser.add_argument("--quality", default="")
    parser.add_argument("--summary", default="")
    args = parser.parse_args()

    body = read_body(args)
    if not body:
        raise SystemExit("Provide --body or --body-file")

    root = package_root(args.root)
    problem_dir, metadata = resolve_problem(root, args.problem)
    solution_path = problem_dir / "solution.py"
    solution_hash = file_sha256(solution_path) if solution_path.exists() else ""
    latest_test_path = problem_dir / "test_history" / "latest.json"
    latest_test = json.loads(latest_test_path.read_text(encoding="utf-8")) if latest_test_path.exists() else None

    now = datetime.now(timezone.utc).astimezone()
    title = args.title or args.kind.title()
    record = {
        "timestamp": now.isoformat(timespec="seconds"),
        "kind": args.kind,
        "problem": metadata.get("folder"),
        "id": metadata.get("id"),
        "title": metadata.get("title"),
        "history_title": title,
        "outcome": args.outcome,
        "tests": args.tests,
        "quality": args.quality,
        "summary": args.summary,
        "solution_sha256": solution_hash,
        "latest_test_timestamp": latest_test.get("timestamp") if isinstance(latest_test, dict) else "",
        "latest_test_sha256": latest_test.get("target_sha256") if isinstance(latest_test, dict) else "",
        "latest_test_passed": latest_test.get("passed") if isinstance(latest_test, dict) else None,
        "body": body,
    }

    history_dir = problem_dir / f"{args.kind}_history"
    history_dir.mkdir(exist_ok=True)
    latest_md = history_dir / "latest.md"
    latest_json = history_dir / "latest.json"
    history_jsonl = history_dir / "history.jsonl"

    front = [
        f"# {args.kind.title()} - {metadata.get('id')}. {metadata.get('title')}",
        "",
        f"- Timestamp: {record['timestamp']}",
        f"- Outcome: {args.outcome or 'unspecified'}",
        f"- Tests: {args.tests or 'unspecified'}",
        f"- Quality: {args.quality or 'unspecified'}",
        f"- Summary: {args.summary or 'unspecified'}",
        "",
        "## Notes",
        "",
        body,
        "",
    ]
    latest_md.write_text("\n".join(front), encoding="utf-8")
    latest_json.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    with history_jsonl.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(
        json.dumps(
            {
                "history_dir": str(history_dir),
                "latest_md": str(latest_md),
                "latest_json": str(latest_json),
                "appended": str(history_jsonl),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
