# Notes - 981. Time Based Key-Value Store

## Core Idea

Per key, timestamps are sorted by construction. Use binary search to find the rightmost timestamp not greater than the query.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_binary_search_per_key.py` | primary design solution | set O(1), get O(log n); Space O(n) |
| `solution_manual_binary_search.py` | alternative design reference | set: O(1); get: O(log n); Space: O(total set calls) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
