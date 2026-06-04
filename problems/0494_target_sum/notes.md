# Notes - 494. Target Sum

## Core Idea

Convert P-N=target into a subset-sum counting problem.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_subset_count.py` | primary solution | Time: O(n*S); Space: O(S) |
| `solution_dfs_memo.py` | recursive DP reference | Time: O(n * sum(nums)); Space: O(n * sum(nums)) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
