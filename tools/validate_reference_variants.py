from __future__ import annotations

import json
import sys
import traceback
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from common.runner import (  # noqa: E402
    call_method,
    compare_case,
    expected_from_case,
    find_reference_file,
    load_module,
)


def test_variant(problem_dir: Path, variant_file: Path) -> list[str]:
    metadata = json.loads((problem_dir / "metadata.json").read_text())
    cases = json.loads((problem_dir / "tests" / "cases.json").read_text())["cases"]
    target_module = load_module(variant_file)
    primary_ref = find_reference_file(problem_dir, metadata)
    reference_module = target_module if primary_ref == variant_file else load_module(primary_ref)
    failures: list[str] = []

    for index, case in enumerate(cases, start=1):
        case_name = case.get("name", index)
        try:
            actual = call_method(target_module, metadata, deepcopy(case))
            explicit = expected_from_case(metadata, case)
            expected = explicit if explicit is not None else call_method(reference_module, metadata, deepcopy(case))
            if not compare_case(metadata, case, actual, expected):
                failures.append(
                    f"{problem_dir.name}/{variant_file.name} case {case_name}: "
                    f"actual={actual!r} expected={expected!r}"
                )
        except Exception as exc:
            failures.append(
                f"{problem_dir.name}/{variant_file.name} case {case_name} raised "
                f"{type(exc).__name__}: {exc}\n{traceback.format_exc(limit=3)}"
            )
    return failures


def main() -> None:
    failures: list[str] = []
    total = 0

    for problem_dir in sorted((ROOT / "problems").iterdir()):
        if not problem_dir.is_dir():
            continue
        for variant_file in sorted((problem_dir / "solutions").glob("solution*.py")):
            total += 1
            failures.extend(test_variant(problem_dir, variant_file))

    if failures:
        print(f"FAILED {len(failures)} failures across {total} reference variants")
        for failure in failures[:80]:
            print(f"- {failure}")
        raise SystemExit(1)

    print(f"PASSED all {total} reference variants")


if __name__ == "__main__":
    main()
