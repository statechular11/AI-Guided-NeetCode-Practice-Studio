# Notes - 57. Insert Interval

## Core Idea

The clean structure is before-overlap, overlapping merge, after-overlap.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_three_phases.py` | primary solution | Time: O(n); Space: O(n) |
| `solution_insert_then_merge.py` | simple baseline reference | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- Sort by the field that makes the next decision local.
- Be clear about inclusive versus exclusive endpoints.
- For meeting rooms, an end time equal to a start time does not overlap.
- For offline query problems, preserve original query order in the answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
