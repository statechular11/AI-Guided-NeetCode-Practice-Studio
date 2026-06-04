---
name: neetcode-prep-coach
description: "Use when working with a NeetCode Prep Kit package: initialize the package root, pick the next problem by study plan section or tag, run local tests, review a candidate solution, enrich reference-solution variants, generate standalone technique guides, append observations to notes.md, capture revisit/TODO items, update problem status, sync study-plan/tag/index progress views, or audit the package."
metadata:
  short-description: Coach NeetCode Prep Kit practice
---

# NeetCode Prep Coach

Use this skill to guide coding practice in a standalone NeetCode 150 prep package.

## Package Root

On init, ask for or infer the package root, then verify it contains:

- `problems/`
- `study_plans/`
- `tags/`
- `tools/run_problem.py`
- `tools/validate_tree.py`
- `WORKFLOW.md`

Remember the root for the current thread. If the user later says "current problem", use the most recently resolved problem in this thread.

Two package layouts are supported:

- Standalone package: run commands from `<PACKAGE_ROOT>` with `python -m tools...`
- Embedded packages inside a larger Python workspace: run commands from the
  workspace root with that package's documented module path.

Resolve `scripts/...` relative to this skill directory when running helper scripts. The package itself runs from `<PACKAGE_ROOT>` with `python -m tools...` and can be moved freely.

## Single-Problem Loop

1. Resolve the problem:

   ```bash
   python scripts/resolve_problem.py --root <PACKAGE_ROOT> --problem <ID_OR_FOLDER_OR_TITLE>
   ```

2. Read `prompt.md`, `metadata.json`, `notes.md`, and the current `solutions/` inventory. Summarize only what helps the user start coding: problem, signature, constraints, examples, available reference variants, and test command.

3. Do a lightweight reference-health check for the active problem unless the user is only browsing:

   - `prompt.md` has a usable problem statement, examples, constraints, and source link.
   - `metadata.json` has source/study-plan/tags/reference metadata.
   - `solutions/` has at least one meaningful AI-authored reference.
   - Existing references pass local tests when reference health is explicitly requested.

4. Use the four-command loop below:

   ```text
   Test -> Debug -> Review -> Consolidate
   ```

   If tests pass immediately, the usual path is:

   ```text
   Test -> Review -> Consolidate
   ```

Do not mark a problem `reviewed` merely because tests passed. `reviewed` is assigned during Consolidate after a passing Review.

## Test Mode

Trigger Test when the user asks to test, run, judge, or check the current solution.

Test mode is evidence-only:

- Run tests with `scripts/run_tests.py`.
- Print only the runner output.
- Do not explain why the solution failed.
- Record:
  - `test_history/latest.json`
  - `test_history/history.jsonl`

Command shape:

```bash
python scripts/run_tests.py --root <PACKAGE_ROOT> --problem <PROBLEM>
```

`run_tests.py` prints the summary first. By default, a plain Test request expands failed cases only, including inputs, outputs, expected values, and diffs. Use `--all-cases` only when the user explicitly wants passed-case detail too.

## Debug Mode

Trigger Debug when the user asks to debug, explain the failure, diagnose, or asks where the solution went wrong.

Debug mode explains failing evidence:

1. Resolve the problem.
2. Read the latest recorded test:

   ```bash
   python scripts/latest_test.py --root <PACKAGE_ROOT> --problem <PROBLEM>
   ```

3. If there is no latest test record, or if `stale` is true because `solution.py` changed since the latest test, first run:

   ```bash
   python scripts/run_tests.py --root <PACKAGE_ROOT> --problem <PROBLEM> --all-cases --no-color
   ```

4. Read `solution.py`, `prompt.md`, `metadata.json`, relevant `notes.md`, references under `solutions/`, and `test_history/latest.json`.
5. Explain the failure using the latest recorded inputs, output, expected output, and diff. Keep the explanation grounded in the code line or invariant that caused the mismatch.
6. Store the debug result:

   ```bash
   python scripts/append_history.py --root <PACKAGE_ROOT> --problem <PROBLEM> --kind debug --title "Debug" --body-file <DEBUG_BODY_FILE> --outcome failed-tests --tests failed --summary "<SHORT_SUMMARY>"
   ```

7. Do not update `notes.md`, status, or progress views during Debug unless the user explicitly asks to Consolidate.

## Review Mode

Trigger Review when the user asks to review, quality-check, or judge whether the solution is solid.

Review is the quality gate:

1. Ensure test evidence is fresh using `latest_test.py`.
2. If missing or stale, run Test first.
3. If tests fail:
   - automatically run Debug,
   - show the Debug result,
   - store a Review history entry with outcome `blocked-by-failing-tests`,
   - do not mark the problem reviewed.
4. If tests pass:
   - review correctness beyond local tests,
   - check edge cases, complexity, clarity, and interview explainability,
   - spot performance gaps against the optimized reference solution, including
     asymptotic gaps and meaningful constant-factor/data-structure gaps,
   - compare against `solutions/` for simpler invariants or cleaner
     formulations,
   - suggest polish opportunities, such as clearer names, simpler branching,
     tighter invariants, more idiomatic APIs, or easier interview narration,
   - store a Review history entry.
5. Apply the revisit recommendation check:
   - If the user explicitly says they struggled, had no clue, relied on a reference, wants to remember something, or wants the problem revisited, include a `## Revisit Recommendation` section in the Review body.
   - If history shows a clear struggle signal, such as multiple failed/stale test rounds, a Debug finding tied to a core invariant, or repeated Review comments about the same pattern, include a `## Revisit Recommendation` section in the Review body.
   - Do not update `REVISIT.md` during Review. Consolidate is responsible for turning recommendations into durable revisit items.

Store Review history with:

```bash
python scripts/append_history.py --root <PACKAGE_ROOT> --problem <PROBLEM> --kind review --title "Review" --body-file <REVIEW_BODY_FILE> --outcome solid --tests passed --quality solid --summary "<SHORT_SUMMARY>"
```

Review should not directly mutate `notes.md`, `metadata.json`, `REVISIT.md`, or progress views. Leave durable package updates to Consolidate.

## Consolidate Mode

Trigger Consolidate when the user asks to update files, update notes/status, summarize learning, commit the lesson, or consolidate the current problem.

Consolidate turns raw history into durable learning artifacts:

1. Read:
   - `test_history/latest.json`
   - `debug_history/history.jsonl` when present
   - `review_history/history.jsonl` when present
   - `notes.md`
   - `metadata.json`
   - relevant references under `solutions/`
2. Extract durable lessons:
   - repeated bug patterns
   - misunderstood invariants
   - edge cases that repeatedly failed
   - significant optimization gaps
   - Python APIs/modules or data-structure patterns worth revisiting
3. Update `notes.md` via `append_review_note.py`.
4. Update `metadata.json` via `update_status.py`:
   - `reviewed` only when tests passed and Review found the solution solid
   - `passed-local` when tests passed but Review has concerns
   - `needs-redo` when there is a major correctness, complexity, or explainability issue
5. Add `REVISIT.md` items via `add_revisit_item.py` when history shows a repeated struggle, when Review history contains a `Revisit Recommendation`, or when an unfamiliar concept is worth drilling later. Skip duplicates if the same problem/topic is already present.
6. Store a Consolidate history entry with `append_history.py`.
7. Run `sync_progress_views.py`.
8. Run `audit_package.py`; use `--reference` only when the user asks for a full reference sweep.

Consolidate is the only normal mode that updates learning/progress records.

## Study-Plan Loop

When the user chooses a study plan and an algorithm/data-structure focus, use:

```bash
python scripts/next_problem.py --root <PACKAGE_ROOT> --study-plan <STUDY_PLAN_MD_OR_JSON> --section "<SECTION>"
```

For tag-driven practice:

```bash
python scripts/next_problem.py --root <PACKAGE_ROOT> --tag <TAG>
```

Default next-problem selection excludes `reviewed` and `mastered` problems. Use `--include-status` if the user wants redo/review behavior.

After selecting a problem, continue with the Single-Problem Loop.

## Technique Guide Generation

Trigger this mode when the user asks to generate, create, write, draft, or update
a technique guide, learning material, fundamentals guide, algorithm/data
structure guide, or similar topic-level study note. Treat this as a specific
command distinct from Reference Enrichment and single-problem Consolidate.

Use this mode for requests such as:

- "Generate a technique guide for Arrays & Hashing"
- "Create the Linked List Pointer Rewiring guide"
- "Write learning materials for monotonic stack"
- "Update the bit manipulation technique guide"

Default output location:

```text
<PACKAGE_ROOT>/technique_guides/<topic_slug>.md
```

Do not create or update a technique-guide index unless the user explicitly asks for it.

Generation workflow:

1. Resolve the package root and create `technique_guides/` if needed.
2. Identify the relevant technique/topic name and a stable lowercase filename
   slug, for example `arrays_and_hashing.md`, `two_pointers.md`, or
   `linked_list_pointer_rewiring.md`.
3. Review the sample technique guides before drafting. Read the package-local
   samples first:
   - `<PACKAGE_ROOT>/technique_guides/sample_guides/arrays_and_hashing.md`
   - `<PACKAGE_ROOT>/technique_guides/sample_guides/heap_priority_queue.md`

   Treat these samples as a foundational blueprint and quality floor, not a
   ceiling and not a source to copy. Extract their underlying teaching
   philosophy:
   - first-principles decomposition: break the topic into primitive mechanics
     before advanced applications
   - mental-model-first teaching: name the design question that makes the code
     feel inevitable
   - pattern taxonomy: organize by reusable problem shapes, not just problem
     names
   - mechanics-level depth: explain what is stored, when it changes, and what
     guarantee it gives
   - state and invariant discipline: make state meaning and correctness claims
     explicit
   - design worksheets: force key choices such as key/value, priority/payload,
     scope, update rule, validity, and stop condition
   - detailed traces and diagrams: show variables and data structures evolving
     on concrete examples
   - tradeoff awareness: compare neighboring tools and say when this technique
     is not the best choice
   - failure modes: teach common wrong models, update-order bugs, edge cases,
     and Python-specific traps
   - interview explanation scripts: help the learner explain and defend the
     solution aloud
   - progressive mastery: move from mechanics to recognition, variants,
     tradeoffs, and advanced applications
   - quick-review material: end with checklists, templates, and decision prompts

   Do not copy literal content, phrasing, examples, or structure mechanically.
   If the new topic needs additional sections, deeper explanation, or different
   examples, expand beyond the samples.
4. Inspect the corresponding coding-problem set:
   - `indexes/status.csv` for reviewed/attempted problems in the section/tag
   - relevant `problems/<ID>_*/metadata.json`
   - relevant `problems/<ID>_*/notes.md`
   - relevant reference solutions under `solutions/` when they contain teaching
     details worth lifting to the topic level
5. Inspect the user's learning arc for this topic:
   - `test_history/history.jsonl` and `latest.json` when relevant
   - `debug_history/history.jsonl` when present
   - `review_history/history.jsonl` when present
   - `consolidate_history/history.jsonl` when present
   - package-level `REVISIT.md`
6. Distill that history into shareable learning material. Incorporate durable
   lessons as neutral sections such as "Practice Checkpoints", "Failure Modes to
   Guard Against", "Key Invariants", or "Interview Signals". Do not phrase the
   guide as a record of the user's mistakes or use wording like "you previously
   struggled with this".
7. Before drafting, define the guide's quality bar and teaching spine:
   - The guide should be sufficient for a motivated reader to succeed in an
     interview that relies on this technique without opening external notes.
   - Start from the primitive operation or representation, not from named
     problem patterns. Explain what the technique can and cannot answer quickly.
   - Answer the first-principles questions explicitly: what problem the
     technique fundamentally solves, what brute-force behavior it avoids, what
     operation/state/invariant makes it powerful, and what smallest useful
     mental model should guide solution design.
   - Begin with the idea that makes the code obvious, not with code. Define the
     topic's version of questions like "What fact do I need to answer quickly?"
     or "What frontier and priority should I expose?"
   - Identify the topic's core state-design questions, such as key/value,
     priority/payload, source/position, scope, update timing, validity/staleness,
     or boundary ownership. Include a worksheet-style table when it helps.
   - Decide which adjacent tools must be compared, such as sorting, two
     pointers, sliding windows, heaps, binary search, bitmasks, tries,
     union-find, monotonic stacks/deques, or dynamic programming. A strong guide
     explicitly says when this technique is not the final tool.
   - Select the highest-value traces/diagrams before writing: internal
     mechanics, boundary-sensitive updates, duplicate/count handling,
     lazy/stale state, encoding/decoding, grid/box formulas, or frontier
     advancement.
8. Generate the guide from first principles:
   - introduce basics, core concepts, and mental models before advanced
     applications
   - explain non-trivial ideas explicitly, whether basic or advanced
   - include any relevant internal mechanics or representation details, for
     example heap array/tree layout, hash-table key/hash/equality lookup,
     pointer ownership, bit positions, stack/deque direction, graph state, or DP
     state meaning
   - use examples, small traces, tables, and diagrams when they clarify the idea
   - include step-by-step walkthroughs for boundary-sensitive or invariant-heavy
     patterns
   - make phase splits explicit, such as build full set then scan starts, count
     then select, seed frontier then advance, expand right then shrink left, or
     write left state then merge right state
   - avoid over-explaining truly trivial details
9. Cover the technique organically before applying it to coding problems. The
   reader should be able to understand the concept, why it works, common
   variants, and typical interview applications without opening problem files.
10. Use this general guide structure unless the topic calls for a better
    organization:
   - what the technique is
   - core mental model
   - mechanics and complexity basics
   - design worksheet or state-definition checklist
   - recognition signals
   - fundamental patterns
   - detailed applications with traces
   - correctness invariants
   - failure modes and edge cases
   - tooling and implementation details, especially Python details when useful
   - tradeoffs and neighboring techniques
   - typical interview applications
   - practice progression
   - interview explanation templates
   - mastery checklist
   - quick reference
11. For every major pattern, prefer this teaching shape when applicable:
   - problem shape and recognition signal
   - core question the data structure answers quickly
   - when to use it and when not to use it
   - state representation or entry design
   - invariant before/after each iteration or operation
   - implementation template or concise pseudocode
   - worked trace with concrete values
   - correctness reason or proof sketch
   - complexity with variables named clearly
   - failure modes and edge cases
   - representative interview problems
   - when to choose this pattern versus a nearby alternative
12. Include practical interview material:
   - recognition signals
   - templates or pseudocode where useful
   - correctness invariants
   - complexity discussion
   - edge cases and failure modes
   - problem progression and practice checkpoints
   - concise interview explanation templates
13. Add topic-level Python/API guidance when relevant:
   - exact standard-library APIs and their gotchas
   - mutation and aliasing traps
   - hashability/comparability constraints
   - sign conventions, sentinel values, counters/tie-breakers, integer masks, or
     other representation details that commonly cause correct-looking bugs
14. Run one content-quality loop by default:
   - generate the first draft
   - critique it as an independent reviewer against the quality bar above:
     missing primitive mechanics, weak state-design worksheet, insufficient
     diagrams/traces, unclear invariants, missing proof sketches, broken
     progression, missing "when not to use this" tradeoffs, over-explaining or
     under-explaining, overly specific wording, and missing learning-arc lessons
   - compare the draft against the sample guides' teaching depth and ask whether
     it is at least as clear, structured, example-rich, and interview-ready
   - improve the guide based on that critique
   Skip this critique/improvement loop only when the user explicitly asks for
   pure content generation.
15. Verify the final guide:
   - no broken relative links; use plain problem names when a note should remain
     portable across copied packages
   - no accidental technique-guide index unless requested
   - no wording that exposes raw practice-history details; phrase lessons as
     reusable checkpoints
   - Markdown headings are coherent and ordered
   - examples/code blocks render cleanly
   - local package content is internally consistent after the guide is updated
   - the final guide contains enough first-principles explanation, state
     design, worked traces, invariants, tradeoffs, and practice checkpoints to be
     at least comparable to the strongest existing technique guides in the
     package
   - a learner could use it to recognize the technique, choose the right
     variant, implement cleanly, explain the solution aloud, prove correctness
     with invariants, analyze complexity, avoid common bugs, compare
     alternatives, and progress from beginner mechanics to interview mastery

## Reference Enrichment

Trigger this mode when the user says things like:

- "enrich references"
- "add missing variants"
- "find more representative solutions"
- "deep reference pass"
- "compare NeetCode/LeetCode solution ideas"
- "this problem needs more solution directions"

Reference enrichment is opt-in because it can take time and may require browsing. Use source pages for idea discovery only; do not copy proprietary or third-party solution code. The final `solutions/*.py` files must be AI-authored, tested locally, and written in the package's style.

For the active problem:

1. Resolve the problem and inspect `prompt.md`, `metadata.json`, `notes.md`, and `solutions/`.
2. Run the existing references with the local reference command.
3. Identify whether current references cover the meaningful different approaches:
   - brute force or baseline, when educationally useful
   - primary interview-ready approach
   - optimized asymptotic approach
   - alternative data-structure/state representation, such as bitmask, heap, trie, union-find, DP state compression, monotonic stack/deque, binary search on answer, or graph traversal variant
4. If coverage is probably incomplete, inspect:
   - NeetCode solution page: `https://neetcode.io/problems/<neetcode-slug>/solution`
   - LeetCode solutions page: `https://leetcode.com/problems/<leetcode-slug>/solutions/`
5. Distill only the representative strategy categories. Avoid copying code or long prose from those pages.
6. Add only genuinely different implementations. Do not add variants that differ only by syntax, minor loop shape, or naming.
7. Name new files descriptively, for example `solution_bitmask.py`, `solution_heap.py`, `solution_prefix_suffix.py`, or `solution_dp_state_compression.py`.
8. Each non-trivial reference must include a high-quality module-level header docstring at the top of the script, before imports and before `class Solution`. Prefer this over method-level docstrings for reference files. The header should be teaching-oriented, close in depth to a good interview note, and include:
   - problem/variant role in the title
   - core idea and the key invariant
   - why the algorithm works, including important identities or state meaning
   - step-by-step walkthrough or mechanics
   - one concrete example or mental trace when helpful
   - explanations of important constants, masks, sentinels, or edge-case handling
   - common pitfalls for the variant
   - complexity
   - when to choose this variant in an interview
   Keep the implementation itself concise after the header; use inline comments only where the code is still non-obvious.
9. Update `metadata.json` `reference_solutions`, keep `reference_source_note: "AI-authored educational reference solutions."`, update `notes.md` to summarize the variants, and sync progress views.
10. Run the active problem's reference tests. If imports or runner behavior changed, run package validation.

## Revisit Queue

When the user says they want to remember, revisit, drill, TODO, or compile a concept later, append it to package-level `REVISIT.md` instead of burying it only in one problem note.

Use the current problem when the reminder came from an active problem:

```bash
python scripts/add_revisit_item.py --root <PACKAGE_ROOT> --problem <PROBLEM> --topic "<SHORT_TOPIC>" --note "<WHAT_TO_REVISIT>" --tag <TAG>
```

For longer notes, write the body to a temporary file and pass `--body-file <FILE>`.

To list or compile revisit items later:

```bash
python scripts/list_revisit_items.py --root <PACKAGE_ROOT>
python scripts/list_revisit_items.py --root <PACKAGE_ROOT> --tag heap
python scripts/list_revisit_items.py --root <PACKAGE_ROOT> --status todo
```

During Review, write a `Revisit Recommendation` when the user explicitly mentions struggle/no-clue/reference reliance or when repeated history makes the struggle signal clear. Consolidate is responsible for writing `REVISIT.md`.

## Status Values

Prefer these statuses:

- `todo`: untouched or ready to attempt
- `attempted`: user has tried but not passed/reviewed
- `passed-local`: local tests pass, review not complete
- `reviewed`: local tests pass and review found no major issue
- `needs-redo`: important bug, weak explanation, or missed pattern
- `mastered`: reviewed and later redone cleanly

`metadata.json` is the source of truth. Study-plan markdown, tag pages, and indexes are derived views; sync them with `sync_progress_views.py`.

## Review Note Style

Append concise, useful observations under `## Review Log` in `notes.md`:

- what went wrong or what was strong
- invariant or edge case to remember
- complexity and interview explanation notes
- meaningful optimization gaps versus `solutions/` references
- redo trigger if applicable

Avoid overwriting existing notes unless the user explicitly asks.

## Installation Note

Install this skill by copying `skills/neetcode-prep-coach/` into `~/.codex/skills/`, then restart Codex. Always initialize with `Use $neetcode-prep-coach with package root <PACKAGE_ROOT>` after moving or cloning the package.
