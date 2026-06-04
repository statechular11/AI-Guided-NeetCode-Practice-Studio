# Notes - 5. Longest Palindromic Substring

## Core Idea

A palindrome is determined by its center; expand around both odd and even centers.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_expand_centers.py` | primary solution | Time: O(n^2); Space: O(1) |
| `solution_dp_table.py` | alternative DP reference | Time: O(n^2); Space: O(n^2) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
