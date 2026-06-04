# Notes - 312. Burst Balloons

## Core Idea

Choosing the last balloon in an interval makes neighboring values fixed.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_interval_dp.py` | primary solution | Time: O(n^3); Space: O(n^2) |
| `solution_top_down_interval.py` | recursive interval-DP reference | Time: O(n^3); Space: O(n^2) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
