# Notes - 309. Best Time to Buy and Sell Stock with Cooldown

## Core Idea

Cooldown is captured by separating just-sold from resting/not-holding state.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_three_states.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_top_down_memo.py` | recursive DP reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem.
- Initialize empty-prefix and first-row/first-column cases deliberately.
- For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed.
- For interval DP, consider choosing the last action rather than the first action.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
