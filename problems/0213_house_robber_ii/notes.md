# Notes - 213. House Robber II

## Core Idea

Break the circle by excluding either first or last house.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_two_linear_ranges.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_dp_array_ranges.py` | first-principles circular-DP reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
