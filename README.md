# AI-Guided NeetCode 150 Practice Studio

![AI Coach](https://img.shields.io/badge/AI%20Coach-Test%20%7C%20Debug%20%7C%20Review%20%7C%20Consolidate-purple)
![Technique Guides](https://img.shields.io/badge/Technique%20Guides-Topic%20Level%20Learning-orange)
![Local Practice](https://img.shields.io/badge/Practice-Local%20NeetCode%20150-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> **TL;DR**: A local NeetCode 150 workspace with an AI Prep Coach for testing,
> debugging, reviewing, note-taking, smarter revisits, and interview-ready
> technique-guide generation.

AI-assisted NeetCode 150 practice with a bundled `$neetcode-prep-coach` skill
that does the note-taking for you: solve problems locally, get guided through
Test, Debug, Review, and Consolidate, and let the coach grow personalized notes
so future sessions build on your own learning trail.

Most practice repos stop at "here are the problems." This one is built for the
part that actually changes interview performance: recognizing patterns faster,
explaining invariants and tradeoffs clearly, avoiding repeat mistakes, and
turning every attempt into durable review material.

```text
Problem loop: read prompt.md -> code solution.py -> Test -> Debug -> Review -> Consolidate
Topic loop: shaky technique -> Generate Technique Guide -> revisit with a stronger mental model
```

The goal is not just to finish 150 problems. The goal is to leave every session
with sharper instincts, better notes, stronger explanations, and a searchable map
of what deserves another pass.

## Why This Repo Exists

Coding interview prep has a memory problem. You may solve a problem today,
understand the trick for a few hours, and then forget the invariant, edge case,
API detail, or bug pattern two weeks later.

This studio is designed to make practice compound:

- You solve in local `solution.py` files instead of only reading explanations.
- Local tests produce LeetCode-style pass/fail evidence.
- The AI coach explains failures from actual inputs, outputs, diffs, and code.
- Review checks correctness, complexity, clarity, edge cases, and interview
  narration after tests pass.
- Consolidation updates notes, status, progress views, and revisit items.
- Technique Guide Generation turns topic-level weak spots into standalone study
  guides for patterns like Sliding Window, Monotonic Stack, Heap / Priority
  Queue, Graph BFS, Dynamic Programming, and more.

Instead of asking only, "Did I finish this problem?", the repo helps you ask the
questions that matter in interviews:

- Can I recognize this pattern again?
- Can I explain the invariant out loud?
- Do I know why this beats brute force?
- Do I know when this technique is not the right tool?
- Did I record the edge case, state update, or Python API trap that caused
  trouble?
- Which topics deserve another focused drill or a full technique guide?

## The AI Prep Coach Is the Core Feature

Start by installing the bundled skill with
[docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md). The skill lives at:

```text
skills/neetcode-prep-coach/
```

After installation, initialize it with the package root you are using:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

For the full day-to-day operating manual, use [WORKFLOW.md](WORKFLOW.md). The
README gives the overview; `WORKFLOW.md` explains the recommended practice loop,
coach commands, technique-guide flow, revisit tracking, and manual CLI fallback.

| Coach mode | What it does | Durable output |
| --- | --- | --- |
| Pick / Navigate | Chooses the next problem by study-plan section, tag, status, or specific ID. | Current problem context |
| Test | Runs the local judge and reports pass/fail evidence only. | `test_history/` |
| Debug | Explains failing evidence by connecting the mismatch to your code, invariants, or edge cases. | `debug_history/` |
| Review | Acts as the quality gate after tests pass: correctness, edge cases, complexity, clarity, and interview narration. | `review_history/` |
| Consolidate | Turns the session into durable learning records and progress updates. | `notes.md`, `metadata.json`, `REVISIT.md`, generated views |
| Technique Guide Generation | Creates or updates standalone guides for reusable algorithm and data-structure techniques. | `technique_guides/<topic>.md` |
| Reference Enrichment | Adds meaningful AI-authored reference variants when a problem needs more representative solution directions. | `solutions/`, `metadata.json`, `notes.md` |
| Revisit Queue | Records concepts, APIs, bug patterns, and problems worth drilling again. | `REVISIT.md` |

Use the coach like this:

```text
Use $neetcode-prep-coach. Give me the next Sliding Window problem from study_plans/neetcode_150.md.
Use $neetcode-prep-coach. Work on 0128.
Use $neetcode-prep-coach. Test my current problem.
Use $neetcode-prep-coach. Debug my current problem.
Use $neetcode-prep-coach. Review my current solution.
Use $neetcode-prep-coach. Consolidate this problem.
Use $neetcode-prep-coach. Generate a technique guide for Heap / Priority Queue.
Use $neetcode-prep-coach. Add a revisit item for this problem: review the monotonic deque invariant.
```

The separation is intentional: **Test gives evidence, Debug explains failures,
Review is the quality gate, and Consolidate updates long-term memory.** Passing
local tests is not the finish line; interview-ready learning comes from the full
loop.

## Generate Interview-Ready Technique Guides

Technique Guide Generation is the coach's topic-level learning mode. Use it when
a whole technique feels fuzzy, when several problems share the same pattern, or
when you want a first-principles study guide before an interview.

Example commands:

```text
Use $neetcode-prep-coach. Generate a technique guide for Monotonic Stack.
Use $neetcode-prep-coach. Generate a technique guide for Graph BFS.
Use $neetcode-prep-coach. Create the Linked List Pointer Rewiring guide.
Use $neetcode-prep-coach. Update the bit manipulation technique guide.
```

Generated guides belong in:

```text
technique_guides/<topic_slug>.md
```

The repo includes two sample technique guides:

```text
technique_guides/sample_guides/arrays_and_hashing.md
technique_guides/sample_guides/heap_priority_queue.md
```

They are useful examples of the depth and teaching style of the topic-level
guides this repo is designed to produce. For the recommended guide-generation
flow, see [WORKFLOW.md](WORKFLOW.md).

## What Makes It Different From a Solutions Repo

| Usual practice repo | This studio |
| --- | --- |
| Static solution files | Blank attempts plus enriched AI-authored reference variants |
| Manual memory | Notes, histories, revisit queue, generated progress views, and generated technique guides |
| "It passed" as the finish line | Review checks correctness, complexity, clarity, edge cases, and interview narration |
| One-off debugging | Evidence-driven Debug mode tied to local test failures |
| Topic review from scratch | Technique Guide Generation creates standalone first-principles guides for reusable patterns |
| Flat problem list | Study-plan sections, tag drill pages, status views, and revisit queues for targeted practice |

## Recommended Coach-First Practice Flow

1. Install the skill with [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md).
2. Initialize the coach with your package root.
3. Ask the coach for the next problem by section, tag, status, ID, or title.
4. Read the local `prompt.md` and code your attempt in `solution.py`.
5. Ask the coach to Test the current problem.
6. If tests fail, ask for Debug.
7. Once tests pass, ask for Review.
8. Ask for Consolidate to update notes, status, revisit items, and progress
   views.
9. When a topic still feels fuzzy, ask for a Technique Guide.
10. Revisit weak patterns later using your own notes, generated guides, tags,
    and `REVISIT.md`.

## Project Map

| Path | Purpose |
| --- | --- |
| `problems/` | One folder per NeetCode 150 problem, with prompt, attempt file, tests, references, notes, and metadata |
| `study_plans/` | Ordered NeetCode 150 progress dashboard |
| `tags/` | Generated tag-to-problem lookup pages for focused drills |
| `indexes/` | Machine-readable metadata, status, and generated lookup files |
| `tools/` | Local runner, validators, index generation, fetching, and regeneration helpers |
| `common/` | LeetCode-style data structures, serializers, comparators, and runner support |
| `skills/neetcode-prep-coach/` | Bundled companion skill and helper scripts |
| `technique_guides/sample_guides/` | Sample technique guides |
| `technique_guides/` | Generated topic-level learning guides |
| `docs/` | Architecture, workflow prompts, tooling, installation, troubleshooting, and expansion docs |
| `templates/` | Reusable generated-file templates |
| `tests/` | Package-level tests and runner checks |
| `REVISIT.md` | Package-level queue for concepts, APIs, bug patterns, and problems worth another pass |

## Optional Manual CLI Reference

The companion skill is the recommended way to practice. The CLI remains useful
when you want direct control, automation, or a quick smoke test.

Run your current solution:

```bash
python -m tools.run_problem problems/0001_two_sum
```

Run the primary reference solution:

```bash
python -m tools.run_problem problems/0001_two_sum --reference
```

Validate the package structure:

```bash
python -m tools.validate_tree
```

Run a package-wide primary-reference smoke test:

```bash
python -m tools.validate_tree --reference
```

Run every reference variant against local cases:

```bash
python -m tools.validate_reference_variants
```

Useful runner flags:

```bash
python -m tools.run_problem problems/0001_two_sum --verbose
python -m tools.run_problem problems/0001_two_sum --no-color
python -m tools.run_problem problems/0001_two_sum --all-cases
```

## Documentation

- [WORKFLOW.md](WORKFLOW.md): day-to-day operating manual for practicing with
  the Prep Coach skill
- [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md): install the bundled
  Prep Coach skill
- [docs/TOOLING.md](docs/TOOLING.md): local runner, validators, generators, and
  helper scripts
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): package structure and design
  model
- [docs/AI_PROMPTS.md](docs/AI_PROMPTS.md): reusable prompts for using or
  recreating the workflow

## Notes

Problem statements link back to official source pages. Reference solutions are
AI-authored educational implementations intended for learning, not copied
third-party code.
