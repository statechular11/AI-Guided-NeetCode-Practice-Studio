# Notes - 1851. Minimum Interval to Include Each Query

## Core Idea

This is an offline query problem: sort queries, add intervals as they become eligible, and heap by interval size.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sort_queries_heap.py` | primary solution | Time: O((n+q) log n); Space: O(n+q) |
| `solution_brute_force.py` | educational baseline | Time: O(qn); Space: O(1) excl. output |

## Pitfalls To Watch

- Sort by the field that makes the next decision local.
- Be clear about inclusive versus exclusive endpoints.
- For meeting rooms, an end time equal to a start time does not overlap.
- For offline query problems, preserve original query order in the answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
