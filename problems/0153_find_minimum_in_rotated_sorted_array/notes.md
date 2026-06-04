# Notes - 153. Find Minimum in Rotated Sorted Array

## Core Idea

Compare mid with the right edge to decide whether the rotation point is right of mid or at/before mid.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_compare_right.py` | primary solution | Time: O(log n); Space: O(1) |
| `solution_linear_scan_baseline.py` | educational baseline | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
