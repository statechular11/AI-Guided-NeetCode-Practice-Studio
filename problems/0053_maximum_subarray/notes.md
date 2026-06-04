# Notes - 53. Maximum Subarray

## Core Idea

Kadane's invariant: `current` is the best subarray sum ending at the current index.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_kadane.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_divide_and_conquer.py` | alternative algorithmic reference | Time: O(n log n); Space: O(log n) |

## Pitfalls To Watch

- State the greedy choice and why earlier/later choices cannot improve it.
- Watch boundary cases where equality is allowed.
- For reachability problems, track the farthest possible boundary.
- For string balance problems, a range of possibilities can be more useful than one exact state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
