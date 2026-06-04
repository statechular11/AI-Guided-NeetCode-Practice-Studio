# Architecture

This package has four layers: generated practice content, topic-level learning
materials, reusable tooling, and the bundled NeetCode Prep Coach skill.

## Generated Practice Content

- `problems/`: one folder per problem
- `study_plans/`: the ordered NeetCode 150 dashboard
- `tags/`: generated tag-to-problem mappings
- `indexes/`: machine-readable metadata and status files

Each problem folder owns the local practice experience for that problem.

## Topic-Level Learning Materials

- `technique_guides/`: standalone algorithm/data-structure guides generated one topic at a time.

Technique guides are derived from the corresponding problem set plus durable
learning history: problem notes, reference solutions, revisit items, and
Test/Debug/Review/Consolidate records. They should teach from first principles
before applying the technique to coding problems, and they should phrase durable
lessons as reusable sections such as "Practice Checkpoints", "Key Invariants",
and "Failure Modes to Guard Against". A guide index is intentionally created
only when requested.

## Tooling

- `common/lc_types.py`: LeetCode-style data structures and serializers
- `common/comparators.py`: output comparison helpers
- `common/runner.py`: loads `solution.py`, calls the right method/class, compares with reference output
- `tools/run_problem.py`: command-line entry point for one problem
- `tools/generate_indexes.py`: rebuilds index and tag files
- `tools/apply_macos_tags.py`: optional Finder tags
- `tools/fetch_and_generate.py`: generator for LeetCode metadata and folders
- `tools/stress_test_parser.py`: broad parser audit before larger expansions
- `tools/validate_tree.py`: local consistency checks

For convenience, generated `solution.py` templates and reference solutions that
use `ListNode`, `TreeNode`, or `Node` include the familiar LeetCode-style class
definitions as comments after the imports and before `class Solution`, with two
blank lines on both sides of the definition block. The executable classes still
come from `common/lc_types.py`, so the runner, serializers, and candidate
solutions all share the same runtime types.

## Metadata

`metadata.json` is the source of truth for each problem:

```json
{
  "id": 1,
  "title": "Two Sum",
  "slug": "two-sum",
  "folder": "0001_two_sum",
  "difficulty": "Easy",
  "tags": ["array", "hash-table"],
  "study_plans": ["neetcode-150"],
  "study_plan_orders": {
    "neetcode-150": 1
  },
  "sections_by_plan": {
    "neetcode-150": "Arrays & Hashing"
  },
  "function": {
    "class_name": "Solution",
    "method_name": "twoSum"
  },
  "status": "todo"
}
```

Generated indexes and tag pages should be derived from metadata, not edited by hand.

## Local Testing Model

For most problems, the runner:

1. imports `solution.py`
2. imports the reference solution
3. loads `tests/cases.json`
4. calls both implementations
5. compares normalized outputs

For special LeetCode formats, adapters handle linked lists, trees, design classes, in-place mutation, unordered outputs, and floating-point tolerance.

## Skill Layer

`skills/neetcode-prep-coach/` contains a movable Codex skill plus helper scripts.
The skill always initializes with a user-provided package root; it must not bake
in the current filesystem path. Installation instructions are in
`docs/SKILL_INSTALLATION.md`.
