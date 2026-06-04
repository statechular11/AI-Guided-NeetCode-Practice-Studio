# Notes - 416. Partition Equal Subset Sum

## Core Idea

Reduce to subset sum target = total // 2; odd total is immediately impossible.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_subset_sum_set.py` | primary solution | Time: O(n*target); Space: O(target) |
| `solution_bitset_dp.py` | optimized Python state-compression reference | Time: O(n * target / word_size) conceptually; Space: O(target) bits |

## Pitfalls To Watch

- Define the DP state in words before coding the recurrence.
- Check base cases, especially empty prefixes, zeros, and one-element arrays.
- When optimizing space, update rolling variables in an order that preserves old values.
- For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
