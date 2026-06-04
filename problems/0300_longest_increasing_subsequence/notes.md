# Notes - 300. Longest Increasing Subsequence

## Core Idea

Quadratic DP is easiest to reason about; patience sorting is the optimized pattern.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_patience.py` | optimized primary solution | Time: O(n log n); Space: O(n) |
| `solution_quadratic_dp.py` | baseline DP | Time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
