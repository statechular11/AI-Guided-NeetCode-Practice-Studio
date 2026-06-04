# Notes - 704. Binary Search

## Core Idea

Keep the interval convention explicit. This reference uses a closed interval and loops while `left <= right`.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_iterative_binary_search.py` | primary solution | Time: O(log n); Space: O(1) |
| `solution_recursive_binary_search.py` | alternative binary-search reference | Time: O(log n); Space: O(log n) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
