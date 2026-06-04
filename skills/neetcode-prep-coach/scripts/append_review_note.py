from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from lib import package_root, resolve_problem


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a review note to a problem notes.md.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--title", default="Review")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--status")
    parser.add_argument("--test-result")
    args = parser.parse_args()

    if not args.body and not args.body_file:
        raise SystemExit("Provide --body or --body-file")
    body = args.body
    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    body = (body or "").strip()
    if not body:
        raise SystemExit("Review body is empty")

    root = package_root(args.root)
    problem_dir, metadata = resolve_problem(root, args.problem)
    notes_path = problem_dir / "notes.md"
    text = notes_path.read_text(encoding="utf-8") if notes_path.exists() else f"# Notes - {metadata['id']}. {metadata['title']}\n\n"
    if "## Review Log" not in text:
        text = text.rstrip() + "\n\n## Review Log\n"

    stamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    extra = []
    if args.status:
        extra.append(f"Status: {args.status}")
    if args.test_result:
        extra.append(f"Tests: {args.test_result}")
    suffix = f" ({'; '.join(extra)})" if extra else ""
    entry = f"\n### {stamp} - {args.title}{suffix}\n\n{body}\n"
    notes_path.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print(json.dumps({"notes": str(notes_path), "appended": True}, indent=2))


if __name__ == "__main__":
    main()
