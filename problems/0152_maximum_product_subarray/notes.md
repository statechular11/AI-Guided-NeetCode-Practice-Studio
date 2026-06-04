# Notes - 152. Maximum Product Subarray

## Core Idea

Track both max and min products because a negative flips signs.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_track_max_min.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_two_pass_scan.py` | alternative product-sign reference | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
