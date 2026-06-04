# Notes - 33. Search in Rotated Sorted Array

## Core Idea

At every step, one side of the midpoint is sorted. Use that side to decide which half can contain target.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_rotated_binary_search.py` | primary solution | Time: O(log n); Space: O(1) |
| `solution_find_pivot_then_binary.py` | two-step binary-search reference | Time: O(log n); Space: O(1) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
