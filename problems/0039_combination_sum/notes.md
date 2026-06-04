# Notes - 39. Combination Sum

## Core Idea

Recurse with the same index to allow reuse; advance index to avoid permutation duplicates.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_reuse_same_index.py` | primary solution | Exponential time; O(depth) space excl. output |
| `solution_choose_skip.py` | alternative backtracking reference | Time: exponential in target/min(candidates); Space: O(target/min(candidates)) excl. output |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
