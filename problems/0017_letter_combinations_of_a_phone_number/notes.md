# Notes - 17. Letter Combinations of a Phone Number

## Core Idea

This is direct choice-tree backtracking: one digit position, one letter choice.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_backtracking.py` | primary solution | Time: O(4^n*n); Space: O(n) excl. output |
| `solution_iterative_cascade.py` | alternative BFS-style construction | Time: O(4^n * n); Space: O(4^n * n) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
