# Notes - 763. Partition Labels

## Core Idea

The current partition must extend to the farthest last occurrence of every character seen so far.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_last_occurrence.py` | primary greedy solution | Time: O(n); Space: O(1) |
| `solution_interval_merge.py` | alternative greedy-interval reference | Time: O(n); Space: O(1) for lowercase alphabet |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
