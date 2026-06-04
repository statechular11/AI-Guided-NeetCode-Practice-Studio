# Notes - 62. Unique Paths

## Core Idea

The transition is paths from above plus paths from left.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_1d_dp.py` | primary solution | Time: O(m*n); Space: O(n) |
| `solution_combinatorics.py` | math optimized reference | Time: O(min(m, n)); Space: O(1) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
