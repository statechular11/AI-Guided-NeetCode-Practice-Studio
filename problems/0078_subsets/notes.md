# Notes - 78. Subsets

## Core Idea

Subsets are a binary decision tree: include or exclude each value.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_cascading.py` | primary concise solution | Time: O(n*2^n); Space: O(n*2^n) |
| `solution_include_exclude.py` | backtracking pattern | Time: O(n*2^n); Space: O(n) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
