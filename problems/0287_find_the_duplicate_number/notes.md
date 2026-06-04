# Notes - 287. Find the Duplicate Number

## Core Idea

Floyd works by viewing values as next pointers: index/value transitions form a
functional graph, and the duplicate value is the cycle entry.

Binary-search-on-answer is a useful alternative. It searches the value range
`[1, n]`, not sorted array positions, and uses counts plus the pigeonhole
principle to decide which half must contain the duplicate.

There are also educational baseline/tradeoff approaches: a hash set is the
simplest correct baseline but costs `O(n)` space, and bit counting reconstructs
the duplicate from the difference between input bit counts and the ideal
`1..n` bit counts.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_floyd_cycle.py` | optimized primary solution | Time: O(n); Space: O(1) |
| `solution_binary_search_count.py` | alternative no-mutation solution | Time: O(n log n); Space: O(1) |
| `solution_hash_set.py` | baseline solution | Time: O(n); Space: O(n) |
| `solution_bit_count.py` | bit-manipulation variant | Time: O(n log n); Space: O(1) |

## Pitfalls To Watch

- In Floyd's approach, the first slow/fast meeting point is not necessarily the
  duplicate. Reset a finder pointer and locate the cycle entry.
- Treat values as next pointers, not the array as sorted. The transition is
  `i -> nums[i]`.
- In binary-search-on-answer, `count <= mid` means the duplicate is in the upper
  value range; `count > mid` means the lower range is overloaded.
- Do not sort or negative-mark `nums` as the final answer if the interviewer is
  enforcing the "do not modify the array" constraint.
- Hash-set solutions are a good baseline, but they do not satisfy the constant
  extra-space constraint.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
