# Notes - 253. Meeting Rooms II

## Core Idea

A min heap tracks when rooms become free. A sweep line tracks concurrent active meetings.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_min_heap_end_times.py` | primary heap solution | Time: O(n log n); Space: O(n) |
| `solution_sweep_line.py` | sweep-line variant | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- Sort by the field that makes the next decision local.
- Be clear about inclusive versus exclusive endpoints.
- For meeting rooms, an end time equal to a start time does not overlap.
- For offline query problems, preserve original query order in the answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
