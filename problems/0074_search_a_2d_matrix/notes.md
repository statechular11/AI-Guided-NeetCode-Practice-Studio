# Notes - 74. Search a 2D Matrix

## Core Idea

Map virtual index to row/column with division and modulo. This avoids a separate row-selection binary search.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_flattened_binary_search.py` | primary solution | Time: O(log(m*n)); Space: O(1) |
| `solution_two_phase_binary_search.py` | alternative binary-search reference | Time: O(log m + log n); Space: O(1) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
