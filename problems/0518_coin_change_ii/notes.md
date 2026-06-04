# Notes - 518. Coin Change II

## Core Idea

Coin outer loop avoids counting different orders of the same combination.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_combinations_dp.py` | primary solution | Time: O(amount*coins); Space: O(amount) |
| `solution_2d_dp.py` | first-principles combinations-DP reference | Time: O(n * amount); Space: O(n * amount) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
