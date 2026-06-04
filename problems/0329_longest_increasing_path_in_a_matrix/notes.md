# Notes - 329. Longest Increasing Path in a Matrix

## Core Idea

Memoize each cell; increasing edges prevent cycles.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dfs_memo.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_topological_layers.py` | alternative DAG reference | Time: O(mn); Space: O(mn) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
