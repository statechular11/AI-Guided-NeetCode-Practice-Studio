# Workflow

This is the operating manual for the AI-Guided NeetCode 150 Practice Studio.
The `$neetcode-prep-coach` skill is the recommended way to use the repo because
it keeps testing, debugging, review, consolidation, revisit tracking, reference
enrichment, and technique-guide generation in separate, disciplined modes.

```text
Problem loop: read prompt.md -> code solution.py -> Test -> Debug -> Review -> Consolidate
Topic loop: shaky technique -> Generate Technique Guide -> revisit with a stronger mental model
```

## Install and Initialize the AI Prep Coach

Install the bundled skill from:

```text
skills/neetcode-prep-coach/
```

See [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md), then initialize it
with the package root you are using:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

After initialization, you can use natural commands:

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

## Daily Practice Loop

1. Pick a section from `study_plans/neetcode_150.md`, or choose a focused drill
   from `tags/<tag>/problems.md`.
2. Ask the coach to resolve the next problem, a specific problem, or your current
   problem.
3. Read the problem's `prompt.md`.
4. Code your attempt in `solution.py`.
5. Ask the coach to Test the current problem.
6. If tests fail, ask the coach to Debug the current problem.
7. Once tests pass, ask the coach to Review your solution.
8. Ask the coach to Consolidate the problem so notes, status, progress views,
   and revisit items are updated.
9. When a topic still feels fuzzy, ask the coach to Generate a Technique Guide.
10. Revisit weak patterns later using `REVISIT.md`, tags, generated guides, and
    per-problem notes.

## Coach Modes at a Glance

| Mode | Purpose | Writes |
| --- | --- | --- |
| Pick / Navigate | Resolve the current, next, or requested problem by study-plan section, tag, ID, title, or folder. | Current problem context only |
| Test | Run the local judge and record evidence only: pass/fail, inputs, outputs, expected values, diffs, and runner stderr when present. No AI diagnosis is mixed into the result. | `test_history/` |
| Debug | Explain failing test evidence by connecting the mismatch to code, invariants, edge cases, or incorrect assumptions. Rerun tests first when evidence is stale. | `debug_history/` |
| Review | Act as the quality gate after tests pass: check hidden-risk edge cases, complexity, clarity, interview narration, performance gaps against optimized references, and revisit signals. | `review_history/` |
| Consolidate | Convert the session into durable learning records: notes, status, revisit items, and regenerated progress views. | `notes.md`, `metadata.json`, `REVISIT.md`, generated views |
| Technique Guide Generation | Create or update a standalone topic guide for a reusable algorithm or data-structure technique. | `technique_guides/<topic>.md` |
| Reference Enrichment | Add meaningful AI-authored reference variants when a problem needs more representative solution directions. | `solutions/`, `metadata.json`, `notes.md` |
| Revisit Queue | Add or list concepts, APIs, bug patterns, and problems worth drilling again. | `REVISIT.md` |

Review is read-only for durable package state. Consolidate is the normal step
that updates long-term records. Technique Guide Generation is a separate
topic-level command; it is not just a single-problem consolidation note.

## Example: One Problem With the Skill

Suppose you want to start Arrays & Hashing.

```text
Use $neetcode-prep-coach. Give me the next Arrays & Hashing problem from study_plans/neetcode_150.md.
```

Example response:

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

Example passing output:

```text
PASSED 0217_contains_duplicate (4 cases)
```

Then ask for the quality gate:

```text
Use $neetcode-prep-coach. Review my current solution.
```

Example review excerpt:

```text
Outcome: solid.
Correctness: the seen-set invariant is valid. Before processing each value,
seen contains exactly the values already scanned.
Complexity: O(n) time and O(n) space, matching the optimized reference.
Polish: the current names are clear.
No revisit item needed unless duplicates or set membership still feel shaky.
```

Finally, consolidate the durable lesson:

```text
Use $neetcode-prep-coach. Consolidate this problem.
```

Example consolidation excerpt:

```text
Updated notes.md with the seen-set invariant.
Marked metadata status as reviewed.
Synced study plan, tag pages, and indexes.
```

## Technique Guide Generation

Technique Guide Generation is the coach's topic-level learning mode. Use it when
you want to generate, create, draft, or update a standalone study guide for a
reusable algorithm or data-structure technique.

Use it when:

- a section like Sliding Window, Heap / Priority Queue, Graph BFS, Backtracking,
  or Dynamic Programming feels fragmented;
- you keep missing the same pattern across multiple problems;
- you want a first-principles explanation before attempting harder problems;
- you want quick-review material before an interview.

Example commands:

```text
Use $neetcode-prep-coach. Generate a technique guide for Monotonic Stack.
Use $neetcode-prep-coach. Generate a technique guide for Graph BFS.
Use $neetcode-prep-coach. Create the Linked List Pointer Rewiring guide.
Use $neetcode-prep-coach. Update the bit manipulation technique guide.
Use $neetcode-prep-coach. Generate a technique guide for Dynamic Programming state design.
```

Generated guides are written under:

```text
technique_guides/<topic_slug>.md
```

The repo includes sample technique guides here:

```text
technique_guides/sample_guides/arrays_and_hashing.md
technique_guides/sample_guides/heap_priority_queue.md
```

Use generated guides before starting a topic, after struggling with a cluster of
related problems, or as interview quick-review material. After more practice,
you can ask the coach to update a guide with newly discovered invariants, edge
cases, failure modes, or tradeoffs.

## Reference Enrichment

Reference Enrichment is different from Technique Guide Generation. Use it when a
specific problem needs more meaningful solution variants under `solutions/`.

Example:

```text
Use $neetcode-prep-coach. Enrich references for my current problem with meaningful different solution variants.
```

Reference enrichment should add genuinely different approaches, such as a brute
force baseline, primary interview-ready approach, optimized asymptotic approach,
or alternative data-structure variant. The final reference files should be
AI-authored educational implementations and should pass local tests.

## Revisit Queue

Use the revisit queue when something deserves another pass later.

Examples:

```text
Use $neetcode-prep-coach. Add a revisit item for this problem: review the monotonic deque invariant.
Use $neetcode-prep-coach. Add a revisit item for Heap / Priority Queue: practice lazy deletion with stale indexes.
```

The coach should write durable revisit items to package-level `REVISIT.md`. When
review history shows repeated struggle, Review can recommend a revisit item, but
Consolidate is responsible for writing it.

## Optional Manual CLI Use

The companion skill is the recommended way to practice. The CLI is useful when
you want direct control, automation, or a quick smoke test. Run commands from
the package root.

Run your current `solution.py` against local cases:

```bash
python -m tools.run_problem problems/0001_two_sum
```

Run the configured primary reference solution:

```bash
python -m tools.run_problem problems/0001_two_sum --reference
```

Use this to confirm the local test harness is healthy for a problem before
starting your own attempt.

Validate package structure:

```bash
python -m tools.validate_tree
```

This checks package structure, required files, JSON validity, Python syntax,
Markdown links, generated index consistency, and publish-junk artifacts.

Run package validation plus a primary-reference test sweep:

```bash
python -m tools.validate_tree --reference
```

This is slower, but it is the best package-wide smoke test.

Run every reference variant against local cases:

```bash
python -m tools.validate_reference_variants
```

Use this after reference-enrichment work because `validate_tree --reference`
checks only the configured primary reference for each problem.

Useful runner flags:

```bash
python -m tools.run_problem problems/0001_two_sum --no-color
python -m tools.run_problem problems/0001_two_sum --all-cases
python -m tools.run_problem problems/0001_two_sum --verbose
```

- `--no-color`: disable ANSI color in terminal output.
- `--all-cases`: print passed cases too, not only failures.
- `--verbose`: include raw normalized payloads and judge-mode details.

## When to Use Each Learning Artifact

| Artifact | Best use |
| --- | --- |
| `solution.py` | Your current attempt |
| `prompt.md` | Local problem statement, examples, constraints, and signature |
| `solutions/` | Educational reference variants after attempting or during review |
| `notes.md` | Durable lessons for one problem |
| `test_history/` | Raw evidence from local tests |
| `debug_history/` | Explanations of failing evidence |
| `review_history/` | Post-pass quality gate records |
| `consolidate_history/` | Durable session summaries |
| `REVISIT.md` | Package-level queue for concepts, APIs, bug patterns, and problems to drill again |
| `technique_guides/` | Topic-level guides that connect many problems into reusable interview patterns |
| `technique_guides/sample_guides/` | Sample technique guides |

## Good Practice Habits

- Write your own attempt before reading references.
- Treat local tests as evidence, not as the finish line.
- Ask for Review after tests pass.
- Ask for Consolidate before moving on.
- Add revisit items when a bug pattern or invariant is worth drilling.
- Generate a Technique Guide when a topic feels fragmented across individual
  problems.
- Update a guide after more practice if new attempts reveal better mental
  models, failure modes, edge cases, or tradeoffs.
