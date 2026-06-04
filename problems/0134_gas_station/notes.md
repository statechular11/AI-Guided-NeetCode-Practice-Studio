# Notes - 134. Gas Station

## Core Idea

A negative tank invalidates every start in the current segment, so reset after it.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_reset_start.py` | primary greedy solution | Time: O(n); Space: O(1) |
| `solution_prefix_min_start.py` | alternative greedy proof reference | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
