# Notes - 115. Distinct Subsequences

## Core Idea

Backward target updates prevent one source character from being reused multiple times.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_1d_dp.py` | primary solution | Time: O(m*n); Space: O(n) |
| `solution_2d_dp.py` | first-principles DP reference | Time: O(mn); Space: O(mn) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
