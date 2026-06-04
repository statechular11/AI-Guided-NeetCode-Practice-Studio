# Notes - 4. Median of Two Sorted Arrays

## Core Idea

The optimized solution searches the partition in the smaller array. The left side must contain half the values and be <= the right side.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_merge_until_middle.py` | learning baseline | Time: O(m+n); Space: O(1) |
| `solution_binary_partition.py` | primary optimized solution | Time: O(log(min(m,n))); Space: O(1) |

## Pitfalls To Watch

- Define whether your binary search interval is closed or half-open.
- For answer-space search, prove the predicate is monotonic.
- For boundary problems, test empty arrays and values outside the range.
- For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
