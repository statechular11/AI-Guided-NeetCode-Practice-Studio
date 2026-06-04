# AI-Guided NeetCode 150 Practice Studio

> A local NeetCode 150 workspace with an AI Prep Coach for testing, debugging, reviewing, note-taking, and smarter revisits.

**Stop losing the lesson after the solution passes.**

This repo turns NeetCode 150 into an AI-assisted interview-prep studio. You solve each problem locally in `solution.py`; the bundled `$neetcode-prep-coach` helps run tests, explain failures from evidence, review your approach against educational references, and consolidate the takeaways into notes and revisit items so future sessions build on your own learning history.

```text
read prompt.md -> code in solution.py -> Test -> Debug -> Review -> Consolidate
```

The goal is not just to grind through 150 answers. The goal is to build durable interview instincts: recognizing patterns faster, explaining invariants and tradeoffs clearly, avoiding repeat mistakes, and keeping a searchable learning trail across Arrays & Hashing, Sliding Window, Trees, Heaps, Graphs, Dynamic Programming, and the rest of the NeetCode roadmap.

## Why This Repo Exists

Most coding-interview practice has a memory problem:

1. You solve a problem today.
2. You understand the trick for a few hours.
3. Two weeks later, you remember the title but not the invariant, edge case, or bug pattern that mattered.

This workspace is designed to make practice compound. Every problem folder gives you a local place to attempt the problem, run tests, compare against enriched AI-authored references, and preserve the lesson. The AI Prep Coach then helps turn each session into durable notes, status updates, and revisit prompts.

Instead of asking, “Did I finish this problem?”, the repo helps you ask better interview-prep questions:

- Can I recognize the pattern again?
- Can I explain the invariant out loud?
- Do I know why this solution beats brute force?
- Did I record the edge case or API trap that caused trouble?
- Which topics deserve another focused drill?

## The AI Prep Coach Loop

The `$neetcode-prep-coach` skill is the centerpiece of the repo. It keeps the practice cycle disciplined while letting you code and test locally.

| Stage | What happens | Typical durable output |
| --- | --- | --- |
| Pick | Choose the next problem by study-plan section, tag, status, or specific ID. | Current problem context |
| Test | Run the local judge and report pass/fail evidence only: inputs, outputs, expected values, diffs, and runner errors. | `test_history/` |
| Debug | Explain failing evidence by connecting the mismatch to your code, invariants, or edge cases. | `debug_history/` |
| Review | After tests pass, check hidden-risk edge cases, complexity, clarity, interview narration, and gaps versus optimized references. | `review_history/` |
| Consolidate | Save the durable lesson, update status, sync progress views, and add revisit items when needed. | `notes.md`, `metadata.json`, `REVISIT.md`, generated views |

The important separation is intentional: **Test gives evidence, Debug explains failures, Review is the quality gate, and Consolidate updates long-term memory.** Passing local tests is only one step; the review and consolidation stages are what turn a solved problem into interview-ready learning.

## What Makes This Different

### AI-assisted, but still local-first

You write normal Python solutions in local files and run normal CLI commands. The AI coach wraps the workflow instead of replacing it: it helps select problems, interpret failures, review solution quality, and update learning records.

### Evidence-based debugging

When a solution fails, the local runner produces LeetCode-style failure reports. The coach is expected to reason from concrete evidence: the failing input, your output, the expected output, the diff, and the relevant code path.

### Review after the green check

A passing solution can still be weak for interviews. Review mode checks whether the approach is explainable, robust, idiomatic, and competitive with reference variants. It can flag edge cases, unclear invariants, avoidable complexity gaps, or places where your narration would be hard to defend.

### Personalized revisit memory

The repo includes `REVISIT.md` plus per-problem notes and history folders. When a bug pattern, concept, API, invariant, or problem deserves another pass, the coach can record it so later review sessions start from your real learning trail instead of a blank page.

### Enriched educational references

Reference solutions live under each problem’s `solutions/` folder. They are AI-authored educational implementations, often with explanatory headers, invariants, examples, pitfalls, and complexity notes. They are meant for learning and review, not copy-paste grinding.

### Topic-level learning support

The `technique_guides/` folder supports standalone guides for topics like Arrays & Hashing or Heap / Priority Queue. These guides are designed to teach from first principles, organize reusable patterns, show traces, name invariants, compare tradeoffs, and create interview-ready review material.

## Start Practicing

Clone the repo and run commands from the package root:

```bash
git clone https://github.com/statechular11/AI-Guided-NeetCode-Practice-Studio.git
cd AI-Guided-NeetCode-Practice-Studio

python -m tools.validate_tree
python -m tools.run_problem problems/0001_two_sum --reference
```

Then open the first attempt file:

```text
problems/0001_two_sum/solution.py
```

Code your solution and run it locally:

```bash
python -m tools.run_problem problems/0001_two_sum
```

Blank `solution.py` files are expected to fail until implemented.

## Use the AI Coach

The package includes the companion skill here:

```text
skills/neetcode-prep-coach/
```

Install it using the instructions in [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md), then initialize it with the package root you are using:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

After that, you can practice through natural commands like:

```text
Use $neetcode-prep-coach. Give me the next Arrays & Hashing problem from study_plans/neetcode_150.md.
Use $neetcode-prep-coach. Work on 0128.
Use $neetcode-prep-coach. Test my current problem.
Use $neetcode-prep-coach. Debug my current problem.
Use $neetcode-prep-coach. Review my current solution.
Use $neetcode-prep-coach. Consolidate this problem.
Use $neetcode-prep-coach. Generate a technique guide for Heap / Priority Queue.
Use $neetcode-prep-coach. Add a revisit item for this problem: review the monotonic deque invariant.
```

For the full day-to-day flow, see [WORKFLOW.md](WORKFLOW.md).

## Inside a Problem Folder

Each problem is meant to be a complete local practice unit:

```text
problems/0001_two_sum/
├── prompt.md              # problem statement, examples, constraints, signature
├── solution.py            # your blank/current attempt
├── tests/cases.json       # local test cases
├── solutions/             # AI-authored educational reference variants
├── notes.md               # durable lessons and review notes
├── metadata.json          # source, tags, status, function signature, references
├── test_history/          # created/updated by Test mode
├── debug_history/         # created/updated by Debug mode
├── review_history/        # created/updated by Review mode
└── consolidate_history/   # created/updated by Consolidate mode
```

A typical session looks like this:

```text
1. Read prompt.md.
2. Implement solution.py.
3. Run local tests.
4. Debug any failing evidence.
5. Review after tests pass.
6. Consolidate the lesson into notes, status, and revisit items.
```

## Practice by Plan, Tag, or Revisit Queue

Use the repo as a structured NeetCode roadmap or as a focused drill system:

- `study_plans/neetcode_150.md` gives the ordered NeetCode 150 progression by section.
- `tags/` lets you drill focused topics such as arrays, heap, graph, dynamic programming, intervals, or binary search.
- `indexes/` stores generated machine-readable views for problem metadata, tags, and status.
- `REVISIT.md` collects concepts, APIs, bug patterns, and problems that deserve another pass.
- `technique_guides/` can grow topic-level notes that connect individual problems into reusable interview patterns.

## Useful Commands

| Goal | Command |
| --- | --- |
| Validate package structure | `python -m tools.validate_tree` |
| Run your current solution | `python -m tools.run_problem problems/0001_two_sum` |
| Run the primary reference solution | `python -m tools.run_problem problems/0001_two_sum --reference` |
| Show all cases, including passed cases | `python -m tools.run_problem problems/0001_two_sum --all-cases` |
| Disable ANSI color | `python -m tools.run_problem problems/0001_two_sum --no-color` |
| Validate all reference variants | `python -m tools.validate_reference_variants` |
| Regenerate indexes and tag pages | `python -m tools.generate_indexes` |

## Repo Map

| Path | Purpose |
| --- | --- |
| `problems/` | One folder per NeetCode 150 problem |
| `study_plans/neetcode_150.md` | Ordered progress dashboard |
| `tags/` | Tag-to-problem lookup pages for focused drills |
| `indexes/` | Generated metadata, status, and tag indexes |
| `tools/` | Fetching, generation, running, validation, indexing, and tagging helpers |
| `common/` | LeetCode-style data structures, serializers, comparators, and runner support |
| `docs/` | Architecture, workflow, tooling, installation, and expansion docs |
| `skills/neetcode-prep-coach/` | Bundled companion skill and helper scripts |
| `technique_guides/` | Standalone topic guides generated over time |
| `REVISIT.md` | Package-level concepts and patterns to revisit |

## Who This Is For

This repo is useful if you are preparing for coding interviews and want more than a folder of completed answers. It is especially helpful if you want to:

- practice NeetCode 150 locally;
- get structured AI help without losing control of the code;
- debug from concrete test evidence;
- compare your solution against educational references;
- build better interview explanations;
- track repeated mistakes and revisit them intentionally;
- turn problem attempts into durable topic-level understanding.

## Source and Reference Notes

Problem statements link back to official source pages. Reference solutions are AI-authored educational implementations intended for learning, review, and comparison; they are not copied third-party solution code.

See [WORKFLOW.md](WORKFLOW.md) for the main operating manual and [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md) for skill setup.
