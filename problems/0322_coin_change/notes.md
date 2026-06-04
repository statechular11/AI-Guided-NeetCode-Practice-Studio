# Notes - 322. Coin Change

## Core Idea

Use an impossible sentinel larger than any valid coin count.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bottom_up.py` | primary solution | Time: O(amount*coins); Space: O(amount) |
| `solution_top_down_memo.py` | recursive DP reference | Time: O(amount * len(coins)); Space: O(amount) |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
