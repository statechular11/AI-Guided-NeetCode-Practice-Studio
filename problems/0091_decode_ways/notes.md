# Notes - 91. Decode Ways

## Core Idea

At each position, add ways from valid single-digit and valid two-digit decodes.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_rolling_dp.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_top_down_memo.py` | recursive DP reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
