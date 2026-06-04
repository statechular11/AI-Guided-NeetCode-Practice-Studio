# Tooling

Run commands from the package root:

```bash
cd <PACKAGE_ROOT>
```

The package is intentionally movable. Do not rely on the current local path in
commands, docs, or skills.

## Codex Skill Shortcut

For normal practice, prefer the installed `$neetcode-prep-coach` skill:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

The skill wraps problem resolution, testing, debugging, reviewing, note/status
updates, revisit tracking, progress-view syncing, audits, reference enrichment,
and standalone technique-guide generation.

To call the bundled helper scripts before installing the skill, use paths under
the package:

```bash
python skills/neetcode-prep-coach/scripts/run_tests.py --root <PACKAGE_ROOT> --problem 0001
python skills/neetcode-prep-coach/scripts/latest_test.py --root <PACKAGE_ROOT> --problem 0001
python skills/neetcode-prep-coach/scripts/list_revisit_items.py --root <PACKAGE_ROOT>
```

After installing the skill into `~/.codex/skills`, the same scripts live under
that installed skill directory. See [SKILL_INSTALLATION.md](SKILL_INSTALLATION.md).

## Run A Problem

```bash
python -m tools.run_problem problems/0001_two_sum
```

Run the primary reference solution:

```bash
python -m tools.run_problem problems/0001_two_sum --reference
```

Useful flags:

```bash
python -m tools.run_problem problems/0001_two_sum --verbose
python -m tools.run_problem problems/0001_two_sum --no-color
python -m tools.run_problem problems/0001_two_sum --all-failures
python -m tools.run_problem problems/0001_two_sum --all-cases
```

- `--verbose`: include judge mode and raw normalized payloads.
- `--no-color`: disable ANSI color.
- `--all-failures`: print every failing case; this is the default unless
  `--all-cases` is used.
- `--all-cases`: print every case, including passed cases.

Runner output is LeetCode-style: summary first, then failing input, output,
expected output, compact diff, and mismatch reason.

## Regenerate Indexes

```bash
python -m tools.generate_indexes
```

This rebuilds:

- `indexes/problems.json`
- `indexes/tags.json`
- `indexes/status.csv`
- `tags/*/problems.md`

Generated views derive from `metadata.json`; do not hand-edit tag pages or
status tables.

## Fetch And Generate

The generator can refresh factual problem metadata, prompts, examples, tags,
similar questions, and study-plan data from the available source pages/APIs:

```bash
python -m tools.fetch_and_generate
```

Use this before expanding or rebuilding at scale only after testing on a small
sample. If source pages cannot be fetched or examples cannot be parsed, pause and
provide sample problem data instead of generating a weak package.

The generator preserves AI-authored educational reference solutions when
`metadata.json` contains:

```json
{
  "reference_source_note": "AI-authored educational reference solutions.",
  "reference_solutions": []
}
```

For new problems, author high-quality references under `solutions/` and reflect
their variants in `notes.md`. Do not vendor third-party solution code.

## Stress Test Parser

Before expanding to a much larger set, stress test the content parser:

```bash
python -m tools.stress_test_parser --limit 1000
```

The tool checks source problem pages for descriptions, examples, constraints,
follow-up detection, and similar-question parsing, then writes
`indexes/parser_stress_report.json`.

## Apply macOS Finder Tags

Optional macOS-only helper:

```bash
python -m tools.apply_macos_tags --dry-run
python -m tools.apply_macos_tags
```

Finder tags are a convenience only. Metadata remains the source of truth.

## Validate

```bash
python -m tools.validate_tree
```

Use `--reference` to run every problem's primary reference solution against
local cases:

```bash
python -m tools.validate_tree --reference
```

This is slower, but it is the strongest package-level smoke test for runner
adapters and reference imports.

## Skill History Helpers

The skill records mode history in problem folders:

- `test_history/latest.json`
- `test_history/history.jsonl`
- `debug_history/`
- `review_history/`
- `consolidate_history/`

Append a revisit item directly:

```bash
python skills/neetcode-prep-coach/scripts/add_revisit_item.py \
  --root <PACKAGE_ROOT> \
  --problem 0347 \
  --topic "heapq API and size-k heap pattern" \
  --note "Review heapq.heapify, heappush, heappop, and size-k min-heap usage." \
  --tag heap
```
