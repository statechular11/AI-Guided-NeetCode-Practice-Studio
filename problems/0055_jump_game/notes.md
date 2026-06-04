# Notes - 55. Jump Game

## Core Idea

The greedy state is the farthest reachable index. If the scan passes it, no future jump can help.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_farthest_reach.py` | primary greedy solution | Time: O(n); Space: O(1) |
| `solution_backward_goal.py` | alternative optimized greedy reference | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
