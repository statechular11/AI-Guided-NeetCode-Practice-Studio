# Troubleshooting

## Codex Skill Does Not Trigger

Use the exact skill name:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

If Codex has lost track of the current problem, include the folder explicitly:

```text
Use $neetcode-prep-coach. Test <PACKAGE_ROOT>/problems/0001_two_sum.
```

## Module Import Fails

Run commands from the package root:

```bash
cd <PACKAGE_ROOT>
python -m tools.run_problem problems/0001_two_sum
```

If you run from another directory, set `PYTHONPATH` to `<PACKAGE_ROOT>` or
return to the package root before invoking `python -m tools...`.

## My Blank solution.py Fails Tests

That is expected until you implement it. To confirm the local runner works, run:

```bash
python -m tools.run_problem problems/0001_two_sum --reference
```

## Local Tests Pass But LeetCode Fails

Local tests are not hidden tests. Add the failing edge case to `tests/cases.json` and update `notes.md` with the lesson.

## Design Problems Behave Differently

Design problems such as caches, stacks, tries, and data streams use operation sequences. Inspect `tests/cases.json` to see the constructor and method calls.

## macOS Tags Do Not Work

Finder tags are optional and macOS-specific. The package works without them.

## __pycache__ Folders Appear

That is normal Python behavior and is harmless. The program will still run correctly if you delete those folders, and it is also fine to leave them locally.

The package `.gitignore` excludes `__pycache__/` and `*.pyc`, so these cache files should stay out of your repository.

## Regenerated Files Overwrite My Work

The generator should preserve user work, but check generated changes before committing. For important attempts, keep your work in `solution.py` and rely on version control before large regeneration tasks.
