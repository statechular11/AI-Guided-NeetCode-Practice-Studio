from __future__ import annotations

import argparse
import re

from lib import package_root


def item_matches(block: str, status: str | None, tag: str | None) -> bool:
    lowered = block.lower()
    if status:
        match = re.search(r"^- Status:\s*(.+)$", block, flags=re.MULTILINE)
        if not match or match.group(1).strip().lower() != status.lower():
            return False
    if tag and tag.lower() not in lowered:
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="List revisit/TODO items from REVISIT.md.")
    parser.add_argument("--root", required=True, help="NeetCode Prep Kit package root")
    parser.add_argument("--status", help="Filter by status, for example todo")
    parser.add_argument("--tag", help="Filter by tag or keyword")
    args = parser.parse_args()

    root = package_root(args.root)
    path = root / "REVISIT.md"
    if not path.exists():
        print(f"No revisit queue yet: {path}")
        return
    text = path.read_text(encoding="utf-8")
    chunks = re.split(r"(?=^### )", text, flags=re.MULTILINE)
    header = chunks[0].strip()
    matches = [chunk.strip() for chunk in chunks[1:] if item_matches(chunk, args.status, args.tag)]
    if not matches:
        print("No matching revisit items.")
        return
    print(header)
    print()
    print("\n\n".join(matches))


if __name__ == "__main__":
    main()
