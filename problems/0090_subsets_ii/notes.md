# Notes - 90. Subsets II

## Core Idea

Sort first, then skip duplicate values only at the same recursion depth.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sort_skip_duplicates.py` | primary solution | Time: O(n*2^n); Space: O(n) excl. output |
| `solution_iterative_cascading.py` | alternative duplicate-aware subsets reference | Time: O(n * 2^n); Space: O(n * 2^n) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
