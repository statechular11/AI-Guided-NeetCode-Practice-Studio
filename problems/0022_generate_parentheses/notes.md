# Notes - 22. Generate Parentheses

## Core Idea

Only add a close parenthesis when it can match a previously opened one.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_open_close_counts.py` | primary solution | Time: O(C_n*n); Space: O(n) excl. output |
| `solution_iterative_stack_states.py` | iterative backtracking reference | Time: O(C_n * n); Space: O(C_n * n) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
