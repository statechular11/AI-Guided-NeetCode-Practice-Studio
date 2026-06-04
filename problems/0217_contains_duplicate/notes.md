# Notes - 217. Contains Duplicate

## Core Idea

This is the smallest useful hash-set pattern: maintain `seen`, and fail as soon as the current value is already present.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sorting.py` | Sorting-based comparison point. | Time: O(n log n); Space: O(n) in Python |
| `solution_hash_set.py` | Primary seen-set solution. | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Do not count frequencies when a boolean early return is enough.
- Add the value after checking it.
- Sorting is acceptable to explain, but the hash set is the usual final answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
