# Notes - 79. Word Search

## Core Idea

Mark visited cells temporarily and restore them when backtracking.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dfs_marking.py` | primary solution | Time: O(m*n*4^L); Space: O(L) |
| `solution_dfs_visited_set.py` | alternative backtracking reference | Time: O(mn * 4^L); Space: O(L) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
