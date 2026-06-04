from __future__ import annotations

import argparse
import json
from pathlib import Path

from lib import command_context, package_root, resolve_problem


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve a NeetCode Prep Kit problem identifier.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--problem", required=True)
    args = parser.parse_args()

    root = package_root(args.root)
    problem_dir, metadata = resolve_problem(root, args.problem)
    context = command_context(root)
    rel_problem = problem_dir.relative_to(Path(context["cwd"]))
    run_base = f"python -B -m {context['run_problem_module']} {rel_problem}"
    payload = {
        "package_root": str(root),
        "problem_dir": str(problem_dir),
        "problem_dir_from_command_cwd": str(rel_problem),
        "command_cwd": context["cwd"],
        "metadata": metadata,
        "files": {
            "prompt": str(problem_dir / "prompt.md"),
            "solution": str(problem_dir / "solution.py"),
            "notes": str(problem_dir / "notes.md"),
            "metadata": str(problem_dir / "metadata.json"),
            "tests": str(problem_dir / "tests" / "cases.json"),
        },
        "commands": {
            "test": run_base,
            "test_reference": run_base + " --reference",
        },
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
