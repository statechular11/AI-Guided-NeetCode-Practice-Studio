# Adding Problem Sets

The package is metadata-driven. To add more problems, create or fetch problem metadata, generate missing folders, then regenerate indexes and tags.

## Expansion Principles

- Preserve existing `solution.py` files.
- Preserve existing `notes.md` review logs.
- Keep new `solution.py` files blank except imports, signatures, and `pass`.
- Add reference solutions only when you can legally use and attribute them.
- Preserve the key problem information in `prompt.md`: description, examples with expected output and explanation when available, constraints, follow-up, signature, and official links.
- Regenerate indexes from metadata instead of editing tag pages by hand.

## Human Checklist

1. Decide the new set: study-plan slug, list of slugs, CSV, or custom JSON.
2. Fetch metadata for each problem: id, title, slug, difficulty, tags, signature, description, examples, constraints, follow-up, similar questions, and study-list membership.
3. Create missing folders under `problems/`.
4. Fill `README.md`, `prompt.md`, `metadata.json`, `notes.md`, `tests/`, and `solutions/`.
5. Run `python -m tools.generate_indexes`.
6. Run `python -m tools.validate_tree`.
7. Run `python -m tools.validate_tree --reference` if reference solutions exist.

## Prompt Your AI Assistant Can Use

```text
I have a local NeetCode prep package at <PACKAGE_ROOT>.

Please expand it to include this problem set:
<PROBLEM_SET_DESCRIPTION_OR_PROBLEM_SLUGS>

Requirements:
1. Inspect the existing package structure, metadata schema, runner behavior, and generated indexes before editing.
2. Preserve all existing user-written solutions, notes, review logs, and status fields.
3. Create one folder per missing problem under <PACKAGE_ROOT>/problems using the existing naming convention.
4. Fetch current LeetCode metadata where available: id, title, slug, difficulty, topic tags, Python signature, metadata, and example test cases.
5. Keep each new solution.py blank except for imports, class/method signature, and pass.
6. Add `prompt.md` as a semantically complete local prompt with official links, study-list membership, signature, problem description, examples including output and explanation when available, constraints, follow-up, and local test notes.
7. Add notes.md with core idea, mental model, common pitfalls, edge cases, complexity discussion, and an empty Review Log.
8. Add tests/cases.json and tests/test_solution.py compatible with the existing runner.
9. Prefer AI-authored reference solutions with rich explanations and matching notes.md. If any third-party code is included during migration, include attribution and update THIRD_PARTY_NOTICES.md.
10. Regenerate study plans, tag mappings, indexes, and status.csv from metadata. Use explicit study-plan slugs such as `leetcode-top-interview-150` and `neetcode-150`; overlapping problems should keep both memberships.
11. Run validation: required files, JSON parsing, Python compilation, tag-index consistency, and reference test sweep if references exist.
12. Respect the local package root above; do not introduce unrelated absolute paths, temp paths, or assumptions about other repository layouts.

Before editing, produce a short implementation checklist. After editing, summarize files changed, validation results, and limitations.
```

## Common Expansion Sources

- LeetCode study-plan slug
- curated slug list
- NeetCode or another curated problem list
- company-tagged problem set
- CSV exported from a tracker
- AI-curated list for a target role

When in doubt, use a plain text slug list because it is easy to inspect and version.
