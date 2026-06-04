# Workflow

This is the operating manual for the standalone NeetCode 150 package.

## Daily Loop

1. Pick a section from `study_plans/neetcode_150.md`.
2. Work through that section in order, or use `tags/<tag>/problems.md` for a narrower drill.
3. Read `prompt.md`.
4. Code your attempt in `solution.py`.
5. Run local tests.
6. Debug failures.
7. Ask for Review once tests pass.
8. Consolidate durable lessons, status, and revisit items.

## Practice With The AI Coach

Install the bundled skill from `skills/neetcode-prep-coach/` using
[docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md), then initialize it:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

The skill keeps the practice loop disciplined:

```text
Pick Problem -> Code -> Test -> Debug -> Review -> Consolidate
```

Useful commands:

```text
Use $neetcode-prep-coach. Give me the next Sliding Window problem from study_plans/neetcode_150.md.
Use $neetcode-prep-coach. Work on 0128.
Use $neetcode-prep-coach. Test my current problem.
Use $neetcode-prep-coach. Debug my current problem.
Use $neetcode-prep-coach. Review my current solution.
Use $neetcode-prep-coach. Consolidate this problem.
Use $neetcode-prep-coach. Enrich references for my current problem.
Use $neetcode-prep-coach. Generate a technique guide for Heap / Priority Queue.
Use $neetcode-prep-coach. Add a revisit item for this problem: review the monotonic deque invariant.
```

### Mode Responsibilities

| Mode | Purpose | Writes |
| --- | --- | --- |
| Test | Runs the local judge and records evidence only: pass/fail, inputs, outputs, expected values, diffs, and runner stderr when present. No AI diagnosis is mixed into the result. | `test_history/` |
| Debug | Explains failing test evidence by connecting the mismatch to code, invariants, or edge cases. Reruns tests first when the latest evidence is stale. | `debug_history/` |
| Review | Acts as the quality gate after tests pass: checks hidden-risk edge cases, complexity, clarity, interview narration, performance gaps against optimized references, polish opportunities, and revisit signals. | `review_history/` |
| Consolidate | Converts the session into durable learning records: notes, status, revisit items, and regenerated progress views. | `notes.md`, `metadata.json`, `REVISIT.md`, generated views |

Review is read-only for durable package state. Consolidate is the step that
updates long-term records.

### Example: One Problem With The Skill

Suppose you want to start Arrays & Hashing.

```text
Use $neetcode-prep-coach. Give me the next Arrays & Hashing problem from study_plans/neetcode_150.md.
```

Mock response:

```text
Next problem: 0217_contains_duplicate
Difficulty: Easy
Section: Arrays & Hashing
Read: problems/0217_contains_duplicate/prompt.md
Code: problems/0217_contains_duplicate/solution.py
Test: python -B -m tools.run_problem problems/0217_contains_duplicate
References: solution_hash_set.py, solution_sorting.py
```

After you code your attempt:

```text
Use $neetcode-prep-coach. Test my current problem.
```

Mock passing output:

```text
PASSED 0217_contains_duplicate (4 cases)
```

Then ask for a quality gate:

```text
Use $neetcode-prep-coach. Review my current solution.
```

Mock review excerpt:

```text
Outcome: solid.

Correctness: the seen-set invariant is valid. Before processing each value,
seen contains exactly the values already scanned.

Complexity: O(n) time and O(n) space, matching the optimized reference.

Polish: the current names are clear. No revisit item needed unless duplicates
or set membership still feel shaky.
```

Finally:

```text
Use $neetcode-prep-coach. Consolidate this problem.
```

Mock consolidation excerpt:

```text
Updated notes.md with the seen-set invariant.
Marked metadata status as reviewed.
Synced study plan, tag pages, and indexes.
```

## Manual CLI

Use the CLI when you want direct control or when the skill is unavailable.

From the package root:

```bash
python -m tools.run_problem problems/0001_two_sum
```

Runs your current `solution.py` against local cases.

```bash
python -m tools.run_problem problems/0001_two_sum --reference
```

Runs the configured primary reference solution. Use this to confirm the local
test harness is healthy for a problem.

```bash
python -m tools.validate_tree
```

Checks package structure, required files, JSON validity, Python syntax, Markdown
links, generated index consistency, and publish-junk artifacts.

```bash
python -m tools.validate_tree --reference
```

Runs package validation plus a primary-reference test sweep across all problems.
This is slower, but it is the best package-wide smoke test.

```bash
python -m tools.validate_reference_variants
```

Runs every `solutions/solution*.py` variant against local cases. Use this after
reference-enrichment work because `validate_tree --reference` checks only the
configured primary reference for each problem.

Useful runner flags:

```bash
python -m tools.run_problem problems/0001_two_sum --no-color
python -m tools.run_problem problems/0001_two_sum --all-cases
python -m tools.run_problem problems/0001_two_sum --verbose
```

- `--no-color`: disable ANSI color in terminal output.
- `--all-cases`: print passed cases too, not only failures.
- `--verbose`: include raw normalized payloads and judge-mode details.
