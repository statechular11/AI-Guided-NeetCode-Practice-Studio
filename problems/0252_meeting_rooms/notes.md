# Notes - 252. Meeting Rooms

## Core Idea

Sort by start time. Only adjacent meetings can reveal a conflict after sorting.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sort_and_check.py` | primary solution | Time: O(n log n); Space: O(1) extra |
| `solution_sweep_line.py` | alternative interval reference | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- Sort by the field that makes the next decision local.
- Be clear about inclusive versus exclusive endpoints.
- For meeting rooms, an end time equal to a start time does not overlap.
- For offline query problems, preserve original query order in the answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
