# Notes - 678. Valid Parenthesis String

## Core Idea

Track a range of possible open counts, not one exact count.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_balance_range.py` | primary greedy solution | Time: O(n); Space: O(1) |
| `solution_stack_indices.py` | alternative greedy-stack reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
