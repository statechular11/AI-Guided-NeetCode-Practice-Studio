from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path


sys.dont_write_bytecode = True

from common.runner import run_problem

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PROBLEM_FILES = [
    "README.md",
    "prompt.md",
    "metadata.json",
    "solution.py",
    "notes.md",
    "tests/cases.json",
    "tests/test_solution.py",
]

REQUIRED_GITIGNORE_PATTERNS = [
    "__pycache__/",
    "*.pyc",
    ".pytest_cache/",
    ".DS_Store",
]

FORBIDDEN_TEXT = [
    "leetcode_" + "prep_kit_public",
    "/" + "private" + "/tmp",
    "/" + "private" + "/var",
]

FORBIDDEN_PATTERNS = [re.compile(re.escape(pattern)) for pattern in FORBIDDEN_TEXT]
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
URL_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
PUBLISH_JUNK_NAMES = {".DS_Store", "__pycache__", ".pytest_cache"}


def iter_text_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".py", ".md", ".json", ".toml", ".csv"}:
            yield path


def check_no_publish_junk(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if path.name in PUBLISH_JUNK_NAMES or path.suffix == ".pyc":
            errors.append(f"Publish-junk artifact present: {path.relative_to(ROOT)}")


def check_gitignore(errors: list[str]) -> None:
    gitignore_path = ROOT / ".gitignore"
    if not gitignore_path.exists():
        errors.append("Missing .gitignore")
        return
    ignored = set(gitignore_path.read_text(encoding="utf-8").splitlines())
    for pattern in REQUIRED_GITIGNORE_PATTERNS:
        if pattern not in ignored:
            errors.append(f".gitignore should include {pattern}")


def check_no_local_paths(errors: list[str]) -> None:
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"Local path assumption in {path.relative_to(ROOT)}: {pattern.pattern}")


def check_text_format(errors: list[str]) -> None:
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        if "\r\n" in text:
            errors.append(f"CRLF line endings in {path.relative_to(ROOT)}")
        if "\ufffd" in text:
            errors.append(f"Unicode replacement character in {path.relative_to(ROOT)}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip(" \t") != line:
                errors.append(f"Trailing whitespace in {path.relative_to(ROOT)}:{line_number}")
        if path.suffix == ".md" and text.count("```") % 2:
            errors.append(f"Unbalanced Markdown code fences in {path.relative_to(ROOT)}")


def check_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or target.startswith("#") or URL_PATTERN.match(target):
                continue
            target = target.strip("<>")
            if not (path.parent / target).exists():
                line_number = text[: match.start()].count("\n") + 1
                errors.append(f"Broken Markdown link in {path.relative_to(ROOT)}:{line_number}: {match.group(1)}")


def check_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_python_syntax(errors: list[str]) -> None:
    for path in ROOT.rglob("*.py"):
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")


def check_problem_files(errors: list[str]) -> list[dict]:
    problems = []
    for problem_dir in sorted((ROOT / "problems").iterdir()):
        if not problem_dir.is_dir():
            continue
        for rel in REQUIRED_PROBLEM_FILES:
            if not (problem_dir / rel).exists():
                errors.append(f"Missing {problem_dir.relative_to(ROOT)}/{rel}")
        metadata_path = problem_dir / "metadata.json"
        if metadata_path.exists():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            problems.append(metadata)
            if metadata.get("folder") != problem_dir.name:
                errors.append(f"Folder mismatch in {problem_dir.name}: metadata folder={metadata.get('folder')}")
    return problems


def check_indexes(errors: list[str], problems: list[dict]) -> None:
    index_path = ROOT / "indexes" / "problems.json"
    if not index_path.exists():
        errors.append("Missing indexes/problems.json")
        return
    indexed = json.loads(index_path.read_text(encoding="utf-8"))
    problem_folders = sorted(p["folder"] for p in problems)
    indexed_folders = sorted(p["folder"] for p in indexed)
    if problem_folders != indexed_folders:
        errors.append("indexes/problems.json does not match problems/*/metadata.json")

    tags_path = ROOT / "indexes" / "tags.json"
    if tags_path.exists():
        tags = json.loads(tags_path.read_text(encoding="utf-8"))
        for tag, folders in tags.items():
            tag_page = ROOT / "tags" / tag / "problems.md"
            if not tag_page.exists():
                errors.append(f"Missing tag page for {tag}")
            for folder in folders:
                if folder not in problem_folders:
                    errors.append(f"Tag {tag} references unknown folder {folder}")


def check_reference_sweep(errors: list[str]) -> None:
    for problem_dir in sorted((ROOT / "problems").iterdir()):
        if problem_dir.is_dir():
            rc = run_problem(problem_dir, use_reference=True)
            if rc:
                errors.append(f"Reference test failed: {problem_dir.name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", action="store_true", help="Run all reference solutions against local tests")
    args = parser.parse_args()

    errors: list[str] = []
    check_gitignore(errors)
    check_no_publish_junk(errors)
    check_no_local_paths(errors)
    check_text_format(errors)
    check_markdown_links(errors)
    check_json(errors)
    check_python_syntax(errors)
    problems = check_problem_files(errors)
    check_indexes(errors, problems)
    if args.reference:
        check_reference_sweep(errors)

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"VALIDATION PASSED: {len(problems)} problem folders checked")


if __name__ == "__main__":
    main()
