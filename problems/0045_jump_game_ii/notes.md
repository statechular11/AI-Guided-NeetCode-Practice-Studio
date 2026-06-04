# Notes - 45. Jump Game II

## Core Idea

Each jump expands a reachable range. Increment jumps only when finishing the current range.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_level_greedy.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_quadratic_dp.py` | educational baseline | Time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
