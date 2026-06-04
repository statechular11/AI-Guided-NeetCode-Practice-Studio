# AI Prompts

These prompts are assistant-agnostic. Replace `<PACKAGE_ROOT>` with the folder that contains this package.

## Use The Local Skill

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

Useful follow-ups:

```text
Use $neetcode-prep-coach. Give me the next Sliding Window problem from study_plans/neetcode_150.md.
Use $neetcode-prep-coach. Work on 0128.
Use $neetcode-prep-coach. Test my current problem.
Use $neetcode-prep-coach. Debug my current problem.
Use $neetcode-prep-coach. Review my current solution.
Use $neetcode-prep-coach. Consolidate this problem.
Use $neetcode-prep-coach. Enrich references for my current problem with meaningful different solution variants.
Use $neetcode-prep-coach. Generate a technique guide for Heap / Priority Queue.
```

## Reproduce A Similar Package From Scratch

```text
Build a standalone coding-interview practice package from scratch for this problem set:
<PROBLEM_SET_LINKS_OR_STRUCTURED_LIST>

Goals:
- One folder per problem with `README.md`, `prompt.md`, `metadata.json`, blank `solution.py`, `notes.md`, `solutions/`, `tests/cases.json`, and `tests/test_solution.py`.
- A study-plan dashboard that tracks order, section, difficulty, and status.
- Tag pages for tag -> problem lookup with status.
- A local runner for normal methods, in-place mutation, prefix-return problems, design classes, linked lists, trees, graphs, random-pointer lists, codecs, unordered outputs, and custom comparators.
- Local Test/Debug/Review/Consolidate history files.
- A revisit queue for concepts, APIs, and bug patterns.
- Tools to fetch or regenerate problem metadata, prompts, examples, tags, similar questions, tests, study plans, indexes, and package validation.
- AI-authored reference solutions with meaningful variants. Each non-trivial reference must have a header-style docstring explaining the variant role, core idea, invariant, walkthrough, pitfalls, complexity, and when to choose it.
- Docs for workflow, tooling, architecture, adding problem sets, troubleshooting, and skill installation.

Prompt requirements:
- Preserve source formatting for problem descriptions, examples, explanations, constraints, and follow-up text.
- A local `prompt.md` must be sufficient to solve the problem without opening the source page.
- If source pages cannot be fetched or sample problems are unavailable, stop and ask the user to provide sample problem data before generating at scale. The tools must be tested on sample problems before broad generation.

Implementation requirements:
- Keep `solution.py` blank except imports, signatures/classes, and `pass`.
- Do not copy third-party solution code. Use external pages only for strategy discovery when allowed, then author original references.
- Use metadata as the source of truth and regenerate indexes/tags/study-plan views from metadata.
- Avoid hard-coded local package paths so the package can be moved.
- Include validation and run it before delivery.

Before editing, show a short implementation checklist. After editing, report validation results and limitations.
```

## Create A Companion Prep-Coach Skill From Scratch

```text
Create a Codex skill named `<package-name>-prep-coach` for a local coding-interview practice package.

The skill should:
- initialize with a user-provided package root path and verify required files
- resolve current, next, or specific problems by id, folder, title, or slug
- support study-plan and tag navigation
- implement Test, Debug, Review, and Consolidate modes
- ensure Review checks correctness beyond local tests, edge cases, complexity, clarity, interview explainability, performance gaps against optimized references, polish opportunities, and revisit recommendations
- ensure Consolidate reads Test/Debug/Review history, updates `notes.md`, status metadata, progress views, and `REVISIT.md`
- support reference enrichment with AI-authored solution variants and rich header docstrings
- support standalone technique-guide generation from first principles, using problem notes, references, and learning history, with a draft -> critique -> improve loop by default
- support revisit queue add/list commands
- include helper scripts for resolving problems, running tests, reading latest tests, appending history, updating notes/status, syncing views, auditing, and listing revisit items

The skill must not bake in a specific package root path. It should always accept `--root <PACKAGE_ROOT>` or infer it from explicit user context.
```

## Review A Solution Without The Skill

```text
Please review this coding interview solution.

Problem folder: <PACKAGE_ROOT>/problems/<PROBLEM_FOLDER>
Solution file: <PACKAGE_ROOT>/problems/<PROBLEM_FOLDER>/solution.py
Notes file: <PACKAGE_ROOT>/problems/<PROBLEM_FOLDER>/notes.md

Please check correctness, missed edge cases, complexity, clarity, interview explainability, performance gaps against `solutions/`, polish opportunities, and whether the problem or related concepts should be revisited. Propose concise additions to notes.md under Review Log, but do not overwrite existing notes.
```
