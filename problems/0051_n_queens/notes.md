# Notes - 51. N-Queens

## Core Idea

The reusable encoding is columns plus row-col and row+col diagonals.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sets_backtracking.py` | primary solution | Time: O(n!); Space: O(n) excl. output |
| `solution_bitmask_backtracking.py` | optimized state-representation reference | Time: O(n!); Space: O(n) excl. output |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
