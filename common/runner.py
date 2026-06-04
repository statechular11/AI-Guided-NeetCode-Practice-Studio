from __future__ import annotations

import argparse
import difflib
import importlib.util
import json
import os
import sys
from copy import deepcopy
from pathlib import Path

from common.comparators import compare_values
from common.lc_types import (
    build_graph,
    build_list,
    build_list_with_cycle,
    build_next_tree,
    build_random_list,
    build_tree,
    find_tree_node,
    graph_to_adjacency,
    list_to_values,
    next_tree_to_levels,
    quad_tree_to_values,
    random_list_to_values,
    tree_to_values,
)


class TerminalStyle:
    def __init__(self, enabled: bool):
        self.enabled = enabled

    def color(self, text: str, code: str) -> str:
        if not self.enabled:
            return text
        return f"\033[{code}m{text}\033[0m"

    def red(self, text: str) -> str:
        return self.color(text, "31;1")

    def green(self, text: str) -> str:
        return self.color(text, "32;1")

    def yellow(self, text: str) -> str:
        return self.color(text, "33;1")

    def dim(self, text: str) -> str:
        return self.color(text, "2")

    def bold(self, text: str) -> str:
        return self.color(text, "1")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem + "_local", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def convert_arg(slug, raw, lc_type):
    if slug == "clone-graph":
        return build_graph(raw)
    if slug == "copy-list-with-random-pointer":
        return build_random_list(raw)
    if slug == "populating-next-right-pointers-in-each-node-ii":
        return build_next_tree(raw)
    if lc_type == "ListNode[]":
        return [build_list(values) for values in raw]
    if lc_type == "ListNode":
        return build_list(raw)
    if lc_type == "TreeNode":
        return build_tree(raw)
    if lc_type == "Node":
        if slug == "clone-graph":
            return build_graph(raw)
        if slug == "copy-list-with-random-pointer":
            return build_random_list(raw)
        return build_next_tree(raw)
    return deepcopy(raw)


def serialize(slug, value, lc_type=None):
    if value is None:
        return None
    if slug == "clone-graph":
        return graph_to_adjacency(value)
    if slug == "copy-list-with-random-pointer":
        return random_list_to_values(value)
    if slug == "populating-next-right-pointers-in-each-node-ii":
        return next_tree_to_levels(value)
    if slug == "construct-quad-tree":
        return quad_tree_to_values(value)
    if lc_type == "ListNode" or hasattr(value, "next") and hasattr(value, "val") and slug not in {"populating-next-right-pointers-in-each-node-ii"}:
        return list_to_values(value)
    if lc_type == "TreeNode" or (hasattr(value, "left") and hasattr(value, "right") and slug not in {"construct-quad-tree", "populating-next-right-pointers-in-each-node-ii"}):
        return tree_to_values(value)
    if isinstance(value, list):
        return [serialize(slug, item) for item in value]
    if isinstance(value, tuple):
        return [serialize(slug, item) for item in value]
    return value


def prepare_args(metadata, case):
    slug = metadata["slug"]
    params = metadata.get("function", {}).get("params", [])
    raw_args = case.get("args", {})
    if slug == "linked-list-cycle":
        return [build_list_with_cycle(raw_args["head"], raw_args["pos"])]
    if slug in {"lowest-common-ancestor-of-a-binary-tree", "lowest-common-ancestor-of-a-binary-search-tree"}:
        root = build_tree(raw_args["root"])
        return [root, find_tree_node(root, raw_args["p"]), find_tree_node(root, raw_args["q"])]
    return [convert_arg(slug, raw_args[param["name"]], param["type"]) for param in params]


def serialize_args(metadata, args):
    params = metadata.get("function", {}).get("params", [])
    return [
        serialize(metadata["slug"], arg, param.get("type"))
        for arg, param in zip(args, params)
    ]


def call_method(module, metadata, case):
    slug = metadata["slug"]
    func = metadata["function"]
    if metadata["judge"]["mode"] == "codec":
        raw_args = case.get("args", {})
        values = raw_args.get("dummy_input") or raw_args.get("strs") or next(iter(raw_args.values()))
        klass = getattr(module, func.get("class_name", "Solution"))
        obj = klass()
        encoded = obj.encode(deepcopy(values))
        decoded = obj.decode(encoded)
        return {"return": serialize(slug, decoded), "encoded": encoded}
    if metadata["judge"]["mode"] == "tree_codec":
        raw_args = case.get("args", {})
        root = build_tree(raw_args["root"])
        codec = getattr(module, "Codec")()
        encoded = codec.serialize(root)
        decoded = codec.deserialize(encoded)
        return {"return": tree_to_values(decoded), "encoded": encoded}
    if metadata["judge"]["mode"] == "design":
        return call_design(module, metadata, case)
    args = prepare_args(metadata, case)
    klass = getattr(module, func.get("class_name", "Solution"))
    method = getattr(klass(), func["method_name"])
    result = method(*args)
    ret_type = func.get("return_type")
    payload = {"return": serialize(slug, result, ret_type)}
    if metadata["judge"]["mode"] in {"returned_prefix", "in_place"}:
        payload["args"] = serialize_args(metadata, args)
    return payload


def expected_from_case(metadata, case):
    if "expected" not in case:
        return None
    expected = deepcopy(case["expected"])
    if isinstance(expected, dict) and (
        "return" in expected
        or "args" in expected
        or "reference_exception" in expected
    ):
        return expected
    judge = metadata["judge"]["mode"]
    if judge in {"return", "codec", "tree_codec"}:
        ret_type = metadata.get("function", {}).get("return_type")
        return {"return": serialize(metadata["slug"], expected, ret_type)}
    if judge == "design":
        return {"return": expected}
    raise ValueError(
        "Explicit expected values for this judge mode must use the normalized "
        "payload shape, such as {'return': ..., 'args': ...}."
    )


def call_design(module, metadata, case):
    class_name = metadata["function"]["class_name"]
    cls = getattr(module, class_name)
    operations = case["operations"]
    arguments = case["arguments"]
    obj = None
    outputs = []
    live_set = set()
    random_checks = []
    for op, args in zip(operations, arguments):
        if op == class_name:
            if class_name == "BSTIterator":
                args = [build_tree(args[0])]
            obj = cls(*args)
            outputs.append(None)
        else:
            if obj is None:
                raise AssertionError("Design test called a method before constructor")
            result = getattr(obj, op)(*args)
            outputs.append(serialize(metadata["slug"], result))
            if class_name == "RandomizedSet":
                if op == "insert":
                    expected = args[0] not in live_set
                    live_set.add(args[0])
                    random_checks.append(result == expected)
                elif op == "remove":
                    expected = args[0] in live_set
                    if expected:
                        live_set.remove(args[0])
                    random_checks.append(result == expected)
                elif op == "getRandom":
                    random_checks.append(result in live_set)
    return {"return": outputs, "randomized_set_checks": random_checks}


def find_reference_file(problem_dir, metadata):
    ref = metadata.get("reference_solution")
    if ref:
        return problem_dir / ref
    candidates = sorted((problem_dir / "solutions").glob("solution_*.py"))
    return candidates[0] if candidates else None


def compare_case(metadata, case, actual, expected):
    slug = metadata["slug"]
    judge = metadata["judge"]
    raw_args = case.get("args", {})
    if judge["mode"] == "design":
        if metadata["function"]["class_name"] == "RandomizedSet":
            return all(actual.get("randomized_set_checks", []))
        return compare_values(slug, actual["return"], expected["return"], raw_args)
    if judge["mode"] == "codec":
        return compare_values(slug, actual["return"], expected["return"], raw_args)
    if judge["mode"] == "tree_codec":
        return compare_values(slug, actual["return"], expected["return"], raw_args)
    if judge["mode"] == "returned_prefix":
        idx = judge["arg_index"]
        ak = actual["return"]
        ek = expected["return"]
        if ak != ek:
            return False
        return compare_values(slug, actual["args"][idx][:ak], expected["args"][idx][:ek], raw_args)
    if judge["mode"] == "in_place":
        idx = judge["arg_index"]
        return compare_values(slug, actual["args"][idx], expected["args"][idx], raw_args)
    return compare_values(slug, actual["return"], expected["return"], raw_args)


def format_value(value):
    compact = compact_value(value)
    if "\n" not in compact and len(compact) <= 120:
        return compact
    return json.dumps(value, indent=2, ensure_ascii=False, default=str)


def compact_value(value):
    return json.dumps(value, ensure_ascii=False, default=str)


def format_input(case):
    lines = []
    if "args" in case:
        for name, value in case["args"].items():
            lines.append(f"{name} =")
            lines.append(format_value(value))
    else:
        lines.append("operations =")
        lines.append(format_value(case.get("operations", [])))
        lines.append("arguments =")
        lines.append(format_value(case.get("arguments", [])))
    return "\n".join(lines)


def output_sections(metadata, actual, expected):
    judge = metadata["judge"]["mode"]
    slug = metadata["slug"]
    if isinstance(actual, dict) and "exception" in actual:
        return [("Error", actual["exception"]), ("Expected", readable_expected(metadata, expected))]
    if isinstance(expected, dict) and "reference_exception" in expected:
        return [("Output", readable_expected(metadata, actual)), ("Reference Error", expected["reference_exception"])]
    if judge == "returned_prefix":
        idx = metadata["judge"]["arg_index"]
        actual_k = actual["return"]
        expected_k = expected["return"]
        return [
            ("Output", actual_k),
            ("Expected", expected_k),
            ("Output Prefix", actual["args"][idx][:actual_k] if isinstance(actual_k, int) else actual["args"][idx]),
            ("Expected Prefix", expected["args"][idx][:expected_k] if isinstance(expected_k, int) else expected["args"][idx]),
        ]
    if judge == "in_place":
        idx = metadata["judge"]["arg_index"]
        return [
            ("Output", actual["args"][idx]),
            ("Expected", expected["args"][idx]),
        ]
    if judge == "design":
        return [
            ("Output", actual["return"]),
            ("Expected", expected["return"]),
        ]
    return [("Output", actual["return"]), ("Expected", expected["return"])]


def readable_expected(metadata, expected):
    if isinstance(expected, dict) and "return" in expected:
        return expected["return"]
    return expected


def mismatch_reason(metadata, actual, expected):
    judge = metadata["judge"]["mode"]
    if isinstance(actual, dict) and "exception" in actual:
        return "Candidate solution raised an exception."
    if isinstance(expected, dict) and "reference_exception" in expected:
        return "Reference solution raised an exception while computing expected output."
    if judge == "returned_prefix":
        idx = metadata["judge"]["arg_index"]
        if actual["return"] != expected["return"]:
            return "Returned prefix length differs."
        if actual["args"][idx][: actual["return"]] != expected["args"][idx][: expected["return"]]:
            return "Returned length matches, but the accepted prefix differs."
    if judge == "in_place":
        return "Mutated argument differs from the expected final state."
    if judge == "design":
        if metadata["function"]["class_name"] == "RandomizedSet":
            return "One or more randomized-set operation invariants failed."
        actual_outputs = actual.get("return", [])
        expected_outputs = expected.get("return", [])
        for i, (a, e) in enumerate(zip(actual_outputs, expected_outputs)):
            if a != e:
                return f"First differing operation output at index {i}."
        if len(actual_outputs) != len(expected_outputs):
            return "Number of operation outputs differs."
    return "Return value differs from expected output."


def color_inline_diff(actual_text, expected_text, style):
    matcher = difflib.SequenceMatcher(a=actual_text, b=expected_text)
    actual_parts = []
    expected_parts = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        actual_chunk = actual_text[i1:i2]
        expected_chunk = expected_text[j1:j2]
        if tag == "equal":
            actual_parts.append(actual_chunk)
            expected_parts.append(expected_chunk)
        elif tag == "delete":
            actual_parts.append(style.red(actual_chunk))
        elif tag == "insert":
            expected_parts.append(style.green(expected_chunk))
        elif tag == "replace":
            actual_parts.append(style.red(actual_chunk))
            expected_parts.append(style.green(expected_chunk))
    return "".join(actual_parts), "".join(expected_parts)


def diff_block(actual, expected, style):
    actual_text = compact_value(actual)
    expected_text = compact_value(expected)
    if isinstance(actual, str) and isinstance(expected, str) and style.enabled:
        marked_actual, marked_expected = color_inline_diff(actual_text, expected_text, style)
        return "\n".join([f"Output:   {marked_actual}", f"Expected: {marked_expected}"])
    actual_lines = format_value(actual).splitlines()
    expected_lines = format_value(expected).splitlines()
    diff = []
    for line in difflib.unified_diff(actual_lines, expected_lines, fromfile="Output", tofile="Expected", lineterm=""):
        if line.startswith("+") and not line.startswith("+++"):
            diff.append(style.green(line))
        elif line.startswith("-") and not line.startswith("---"):
            diff.append(style.red(line))
        elif line.startswith("@@"):
            diff.append(style.yellow(line))
        else:
            diff.append(line)
    return "\n".join(diff[:80])


def should_use_color(no_color):
    if no_color or os.environ.get("NO_COLOR"):
        return False
    return sys.stdout.isatty()


def print_section(title, body, style):
    print()
    print(style.dim(title))
    print(body if isinstance(body, str) else format_value(body))


def print_failure_report(metadata, case, actual, expected, index, total_failures, total_cases, style, verbose):
    has_exception = isinstance(actual, dict) and "exception" in actual
    has_reference_exception = isinstance(expected, dict) and "reference_exception" in expected
    if has_exception:
        title = "Runtime Error"
    elif has_reference_exception:
        title = "Reference Error"
    else:
        title = "Wrong Answer"
    case_label = case.get("name", f"case_{index}")
    print(style.red(title))
    print(style.dim(f"{metadata['id']}. {metadata['title']}"))
    print(style.dim(f"{metadata['folder']} | case {case_label} | failure {index}/{total_failures} | {total_failures}/{total_cases} cases failed"))
    print_section("Input", format_input(case), style)
    print_section("Use Testcase", case_label, style)
    sections = output_sections(metadata, actual, expected)
    for section_title, section_value in sections:
        print_section(section_title, section_value, style)
    if len(sections) >= 2 and not has_exception and not has_reference_exception:
        print_section("Diff", diff_block(sections[0][1], sections[1][1], style), style)
    print_section("Reason", mismatch_reason(metadata, actual, expected), style)
    if verbose:
        print_section("Judge Mode", metadata["judge"], style)
        print_section("Raw Actual", actual, style)
        print_section("Raw Expected", expected, style)


def print_case_report(metadata, case, actual, expected, index, total_cases, passed, style, verbose):
    has_exception = isinstance(actual, dict) and "exception" in actual
    has_reference_exception = isinstance(expected, dict) and "reference_exception" in expected
    if passed:
        title = style.green("Accepted")
    elif has_exception:
        title = style.red("Runtime Error")
    elif has_reference_exception:
        title = style.red("Reference Error")
    else:
        title = style.red("Wrong Answer")
    case_label = case.get("name", f"case_{index}")
    print(title)
    print(style.dim(f"{metadata['id']}. {metadata['title']}"))
    print(style.dim(f"{metadata['folder']} | case {case_label} | {index}/{total_cases}"))
    print_section("Input", format_input(case), style)
    print_section("Use Testcase", case_label, style)
    sections = output_sections(metadata, actual, expected)
    for section_title, section_value in sections:
        print_section(section_title, section_value, style)
    if not passed and len(sections) >= 2 and not has_exception and not has_reference_exception:
        print_section("Diff", diff_block(sections[0][1], sections[1][1], style), style)
    if passed:
        print_section("Reason", "Output matched expected result.", style)
    else:
        print_section("Reason", mismatch_reason(metadata, actual, expected), style)
    if verbose:
        print_section("Judge Mode", metadata["judge"], style)
        print_section("Raw Actual", actual, style)
        print_section("Raw Expected", expected, style)


def run_problem(
    problem_dir: Path,
    use_reference: bool = False,
    *,
    verbose: bool = False,
    no_color: bool = False,
    all_failures: bool = False,
    all_cases: bool = False,
) -> int:
    metadata = json.loads((problem_dir / "metadata.json").read_text())
    cases = json.loads((problem_dir / "tests" / "cases.json").read_text())["cases"]
    target_file = find_reference_file(problem_dir, metadata) if use_reference else problem_dir / "solution.py"
    reference_file = find_reference_file(problem_dir, metadata)
    if target_file is None or not target_file.exists():
        raise FileNotFoundError(f"No target solution file found for {problem_dir}")
    if reference_file is None or not reference_file.exists():
        raise FileNotFoundError(f"No reference solution file found for {problem_dir}")
    target_module = load_module(target_file)
    reference_module = target_module if use_reference else load_module(reference_file)
    failures = []
    results = []
    for case_number, case in enumerate(cases, start=1):
        explicit_expected = expected_from_case(metadata, case)
        try:
            actual = call_method(target_module, metadata, deepcopy(case))
        except Exception as exc:
            if explicit_expected is not None:
                expected = explicit_expected
            else:
                try:
                    expected = call_method(reference_module, metadata, deepcopy(case))
                except Exception as reference_exc:
                    expected = {"reference_exception": f"{type(reference_exc).__name__}: {reference_exc}"}
            failures.append((case_number, case, {"exception": f"{type(exc).__name__}: {exc}"}, expected))
            results.append((case_number, case, {"exception": f"{type(exc).__name__}: {exc}"}, expected, False))
            continue
        if explicit_expected is not None:
            expected = explicit_expected
        else:
            try:
                expected = call_method(reference_module, metadata, deepcopy(case))
            except Exception as reference_exc:
                expected = {"reference_exception": f"{type(reference_exc).__name__}: {reference_exc}"}
                failures.append((case_number, case, actual, expected))
                results.append((case_number, case, actual, expected, False))
                continue
        if not compare_case(metadata, case, actual, expected):
            failures.append((case_number, case, actual, expected))
            results.append((case_number, case, actual, expected, False))
        else:
            results.append((case_number, case, actual, expected, True))
    if all_cases:
        style = TerminalStyle(should_use_color(no_color))
        if failures:
            print(style.red(f"FAILED {metadata['folder']} ({len(failures)}/{len(cases)} cases failed)"))
        else:
            print(style.green(f"PASSED {metadata['folder']} ({len(cases)} cases)"))
        for display_index, (case_number, case, actual, expected, passed) in enumerate(results, start=1):
            print()
            if display_index > 1:
                print("\n" + style.dim("-" * 72) + "\n")
            print_case_report(metadata, case, actual, expected, case_number, len(cases), passed, style, verbose)
        if failures:
            return 1
        return 0
    if failures:
        style = TerminalStyle(should_use_color(no_color))
        print(style.red(f"FAILED {metadata['folder']} ({len(failures)}/{len(cases)} cases failed)"))
        selected = failures
        for display_index, (case_number, case, actual, expected) in enumerate(selected, start=1):
            print()
            if display_index > 1:
                print("\n" + style.dim("-" * 72) + "\n")
            print_failure_report(metadata, case, actual, expected, display_index, len(failures), len(cases), style, verbose)
        return 1
    print(f"PASSED {metadata['folder']} ({len(cases)} cases)")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", help="Problem folder path, e.g. problems/0001_two_sum")
    parser.add_argument("--reference", action="store_true", help="Run the generated reference solution instead of solution.py")
    parser.add_argument("--verbose", action="store_true", help="Print judge mode and raw normalized payloads on failure")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI color in failure output")
    parser.add_argument("--all-failures", action="store_true", help="Print every failing case; this is the default unless --all-cases is used")
    parser.add_argument("--all-cases", action="store_true", help="Print every case, including passed cases, with input/output/expected")
    args = parser.parse_args()
    problem_dir = Path(args.problem)
    if not problem_dir.exists():
        root = Path(__file__).resolve().parents[1]
        candidates = [
            root / args.problem,
            root / "problems" / args.problem,
        ]
        for candidate in candidates:
            if candidate.exists():
                problem_dir = candidate
                break
    raise SystemExit(
        run_problem(
            problem_dir.resolve(),
            args.reference,
            verbose=args.verbose,
            no_color=args.no_color,
            all_failures=args.all_failures,
            all_cases=args.all_cases,
        )
    )


if __name__ == "__main__":
    main()
