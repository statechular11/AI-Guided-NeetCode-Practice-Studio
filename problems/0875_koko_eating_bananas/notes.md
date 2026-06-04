# Notes - 875. Koko Eating Bananas

## Core Idea

This is binary search on the answer: feasible speeds form a suffix of the search range.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_answer_binary_search.py` | primary solution | Time: O(n log max(piles)); Space: O(1) |
| `solution_linear_scan_baseline.py` | educational answer-search baseline | Time: O(max(piles) * n); Space: O(1) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
