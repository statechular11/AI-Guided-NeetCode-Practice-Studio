# Notes - 1. Two Sum

## Core Idea

Use the target to turn a pair-search problem into a lookup problem:

```text
needed = target - current_value
```

If `needed` has already appeared, the answer is the earlier index plus the current index.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | Learning baseline that checks every pair. | Time: O(n^2); Space: O(1) |
| `solution_hash_map.py` | Primary one-pass interview solution. | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Return indices, not values.
- Look up the complement before storing the current index so one element is not reused.
- Duplicates are valid when they occur at different indices, e.g. `[3, 3]`.
- The output order is not important for the local comparator, but returning earlier index first is conventional.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
