# AI-Guided NeetCode 150 Practice Studio

Imagine practicing NeetCode with an AI coach sitting beside the code: it runs
your local tests, explains failures from evidence, reviews your solution against
optimized references, notices recurring bug patterns, and turns each attempt
into durable learning notes. Weeks later, when you want to revisit Sliding
Window, heaps, graph BFS, or one stubborn problem, the package can pull from
your own learning trail instead of asking you to reconstruct everything from
memory.

This workspace is built for that loop:

```text
read prompt.md -> code in solution.py -> Test -> Debug -> Review -> Consolidate
```

The point is not just to solve 150 problems. The point is to leave every session
with sharper instincts, better notes, and a searchable map of what needs another
pass.

## What You Get

- 150 NeetCode problem folders in a clean `todo` state
- blank attempt files in `solution.py`
- enriched AI-authored reference solutions under `solutions/`
- local tests with LeetCode-style failure reports
- a strict all-reference validator for checking every solution variant
- `study_plans/neetcode_150.md` for progress by section
- `tags/` for focused drills by data structure or technique
- `REVISIT.md` for concepts, APIs, bug patterns, and problems to drill again
- reusable tools for running, validating, fetching, regenerating, and expanding
- bundled `$neetcode-prep-coach` skill for the Test/Debug/Review/Consolidate loop
- standalone technique-guide support for topic-level learning notes

## Quick Start

Run commands from the package root:

```bash
cd <PACKAGE_ROOT>
python -m tools.validate_tree
python -m tools.run_problem problems/0001_two_sum --reference
```

Then open `problems/0001_two_sum/solution.py`, code your attempt, and run:

```bash
python -m tools.run_problem problems/0001_two_sum
```

Blank attempt files are expected to fail until implemented.

## Use The AI Coach

The package includes a companion skill at:

```text
skills/neetcode-prep-coach/
```

Install it with [docs/SKILL_INSTALLATION.md](docs/SKILL_INSTALLATION.md), then
initialize it with the package root you are using:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

The skill handles package initialization, study-plan navigation, specific
problem selection, Test, Debug, Review, Consolidate, reference enrichment,
technique-guide generation, and revisit tracking.

For the full day-to-day flow, see [WORKFLOW.md](WORKFLOW.md). That file is the
main operating manual for practicing with the skill and the local CLI.

## Main Folders

- `problems/`: one folder per NeetCode 150 problem
- `study_plans/neetcode_150.md`: ordered progress dashboard
- `tags/`: tag-to-problem lookup pages
- `tools/`: fetch, generate, run, validate, and tagging helpers
- `common/`: runner support for LeetCode-style data structures and comparisons
- `docs/`: architecture, workflow prompts, tooling, installation, and expansion docs
- `skills/neetcode-prep-coach/`: bundled companion skill
- `technique_guides/`: standalone topic guides generated over time
- `REVISIT.md`: package-level concepts and patterns to revisit

## Notes

Problem statements link back to official source pages. Reference solutions are
AI-authored educational implementations intended for learning, not copied
third-party code.
