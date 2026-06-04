from __future__ import annotations

import argparse
import json
import subprocess

from lib import command_context, package_root


def main() -> None:
    parser = argparse.ArgumentParser(description="Run package validation.")
    parser.add_argument("--root", required=True)
    parser.add_argument("--reference", action="store_true")
    args = parser.parse_args()

    root = package_root(args.root)
    context = command_context(root)
    command = ["python", "-B", "-m", context["validate_tree_module"]]
    if args.reference:
        command.append("--reference")
    proc = subprocess.run(command, cwd=context["cwd"], text=True, capture_output=True)
    print(
        json.dumps(
            {
                "command": " ".join(command),
                "cwd": context["cwd"],
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            },
            indent=2,
        )
    )
    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
