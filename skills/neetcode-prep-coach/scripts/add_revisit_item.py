from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from lib import package_root, resolve_problem


def read_body(args: argparse.Namespace) -> str:
    parts = []
    if args.note:
        parts.append(args.note.strip())
    if args.body_file:
        parts.append(Path(args.body_file).read_text(encoding="utf-8").strip())
    return "\n\n".join(part for part in parts if part)


def ensure_revisit_file(path: Path) -> None:
    if path.exists():
        return
    path.write_text(
        "# Revisit Queue\n\n"
        "Use this file to collect concepts, APIs, bug patterns, and drills worth returning to later.\n\n"
        "## Open Items\n\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Append a revisit/TODO item to REVISIT.md.")
    parser.add_argument("--root", required=True, help="NeetCode Prep Kit package root")
    parser.add_argument("--topic", required=True, help="Short topic or reminder title")
    parser.add_argument("--problem", help="Optional problem id, folder, slug, title, or path")
    parser.add_argument("--note", help="Optional note body")
    parser.add_argument("--body-file", help="Optional file containing a longer note body")
    parser.add_argument("--tag", action="append", default=[], help="Optional tag; repeat for multiple tags")
    parser.add_argument("--status", default="todo", help="Item status, default: todo")
    args = parser.parse_args()

    root = package_root(args.root)
    revisit_path = root / "REVISIT.md"
    ensure_revisit_file(revisit_path)

    problem_line = "- Problem: None"
    if args.problem:
        problem_dir, metadata = resolve_problem(root, args.problem)
        rel = problem_dir.relative_to(root).as_posix()
        problem_line = f"- Problem: [{metadata.get('id'):04d} {metadata.get('title')}]({rel}/)"

    tags = ", ".join(args.tag) if args.tag else "None"
    body = read_body(args) or "TBD"
    topic_title = f"### TODO: {args.topic.strip()}"
    entry = (
        f"{topic_title}\n\n"
        f"- Status: {args.status}\n"
        f"- Created: {date.today().isoformat()}\n"
        f"{problem_line}\n"
        f"- Tags: {tags}\n\n"
        f"{body}\n\n"
    )
    text = revisit_path.read_text(encoding="utf-8")
    if topic_title in text and (not args.problem or problem_line in text):
        print(f"Revisit item already exists in {revisit_path}")
        return
    if "## Open Items" not in text:
        text = text.rstrip() + "\n\n## Open Items\n\n"
    text = text.rstrip() + "\n\n" + entry
    revisit_path.write_text(text, encoding="utf-8")
    print(f"Appended revisit item to {revisit_path}")


if __name__ == "__main__":
    main()
