# Notes - 268. Missing Number

## Core Idea

The input contains `n` distinct values from the full range `[0, n]`, so there
are `n + 1` possible values and exactly one missing value.

Useful ways to see the same invariant:

- Sum formula: subtract the actual sum from `0 + 1 + ... + n`.
- XOR: combine all expected indices/endpoint and all actual values; matching
  values cancel and leave the missing one.
- Hash set: record all actual values, then scan the full range for the absent
  value.
- Sort + binary search: after sorting, find the first index where
  `nums[i] != i`.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sum_formula.py` | math baseline | Time: O(n); Space: O(1) |
| `solution_xor_indices.py` | primary bit solution | Time: O(n); Space: O(1) |
| `solution_hash_set.py` | baseline membership solution | Time: O(n); Space: O(n) |
| `solution_sort_binary_search.py` | sorting and binary-search variant | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- The full range is `[0, n]`, so the answer can be `n`.
- In the XOR solution, seed with `len(nums)` or otherwise explicitly include
  the endpoint `n`.
- In the sum solution, use `n * (n + 1) // 2`, not the sum through `n - 1`.
- In the sorted variant, return the first mismatched index, not the value at
  that index.
- Hash set and sorting are useful learning variants, but the follow-up asks
  for O(1) extra space and O(n) time, which points to XOR or sum formula.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
