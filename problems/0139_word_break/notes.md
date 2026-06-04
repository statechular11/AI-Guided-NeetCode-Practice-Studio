# Notes - 139. Word Break

## Core Idea

dp[i] answers whether the prefix ending at i is segmentable.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_prefix_dp.py` | primary solution | Time: O(n^2); Space: O(n) |
| `solution_top_down_memo.py` | recursive DP reference | Time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
