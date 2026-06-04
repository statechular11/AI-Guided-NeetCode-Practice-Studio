from __future__ import annotations

import argparse
import json
import plistlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def tag_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def set_tags(path: Path, tags: list[str], dry_run: bool = False) -> None:
    encoded = [f"{tag}\n0" for tag in tags]
    data = plistlib.dumps(encoded, fmt=plistlib.FMT_BINARY)
    if dry_run:
        print(f"{path}: {', '.join(tags)}")
        return
    subprocess.run(
        ["xattr", "-w", "-x", "com.apple.metadata:_kMDItemUserTags", data.hex(), str(path)],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--folders-only", action="store_true")
    args = parser.parse_args()

    for metadata_path in sorted((ROOT / "problems").glob("*/metadata.json")):
        metadata = json.loads(metadata_path.read_text())
        tags = [
            "leetcode",
            "interview-prep",
            "project:neetcode",
            f"lcid:{int(metadata['id']):04d}",
            f"lc:{metadata['difficulty'].lower()}",
            f"section:{tag_slug(metadata['section'])}",
            f"status:{metadata['status']}",
        ]
        for plan in metadata.get("study_plans", []):
            tags.append(f"plan:{plan}")
            tags.append(f"plan:{plan.replace('-', '_')}")
        tags.extend(f"tag:{tag}" for tag in metadata["tags"])
        problem_dir = metadata_path.parent
        set_tags(problem_dir, tags, args.dry_run)
        if not args.folders_only:
            for name in ["prompt.md", "solution.py", "notes.md"]:
                path = problem_dir / name
                if path.exists():
                    set_tags(path, tags, args.dry_run)


if __name__ == "__main__":
    main()
