# Notes - 1143. Longest Common Subsequence

## Core Idea

Subsequence DP compares prefixes and either matches characters or drops one side.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dp_table.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_1d_dp.py` | optimized-space DP reference | Time: O(mn); Space: O(n) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
