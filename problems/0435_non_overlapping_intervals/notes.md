# Notes - 435. Non-overlapping Intervals

## Core Idea

Equivalent to keeping the maximum number of non-overlapping intervals; earliest end time is the safe greedy choice.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_greedy_end_time.py` | primary greedy solution | Time: O(n log n); Space: O(1) extra |
| `solution_quadratic_dp.py` | educational baseline | Time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Sort by the field that makes the next decision local.
- Be clear about inclusive versus exclusive endpoints.
- For meeting rooms, an end time equal to a start time does not overlap.
- For offline query problems, preserve original query order in the answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
