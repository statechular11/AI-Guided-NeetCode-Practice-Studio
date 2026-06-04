# Sharing Checklist

Before sharing this package or copying it into another repository:

- Remove `.DS_Store`, `__pycache__`, `.pytest_cache`, and `*.pyc`.
- Run `python -m tools.validate_tree`.
- Run `python -m tools.validate_tree --reference`.
- Run one blank candidate, such as `python -m tools.run_problem problems/0001_two_sum --no-color`, and confirm the failure report is readable.
- Search for local paths, usernames, home directories, and temp paths.
- Confirm `technique_guides/` content phrases learning-history lessons as reusable checkpoints, not raw practice logs.
- Confirm `problems/*/solutions/` contains AI-authored references only, and `metadata.json` marks them with `reference_source_note: "AI-authored educational reference solutions."`.
- Confirm `THIRD_PARTY_NOTICES.md` does not claim legacy reference-solution attribution unless you intentionally add third-party code later.
- Decide and add an appropriate repository license in the shared copy.
- Keep generated prompts accurate, compact enough to read locally, and linked to official LeetCode pages.
- Avoid committing editor-specific settings unless they are examples.
