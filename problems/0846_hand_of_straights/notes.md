# Notes - 846. Hand of Straights

## Core Idea

The smallest remaining card has no predecessor available, so it must start a group.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_counter_start_runs.py` | primary greedy solution | Time: O(n log n + n*g); Space: O(n) |
| `solution_open_groups_heap.py` | alternative greedy grouping reference | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
