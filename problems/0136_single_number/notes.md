# Notes - 136. Single Number

## Core Idea

XOR is the compressed state: duplicate pairs cancel to zero, leaving the unique value.

The learning ladder is:

- hash set: keep currently unpaired values, but use `O(n)` space,
- sorting: group duplicates together, but pay `O(n log n)` time,
- XOR: use `x ^ x == 0` and `x ^ 0 == x` to satisfy both constraints.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_xor.py` | primary bit solution | Time: O(n); Space: O(1) |
| `solution_hash_set.py` | baseline solution | Time: O(n); Space: O(n) |
| `solution_sorting.py` | sorting tradeoff | Time: O(n log n); Space: O(n) |

## Pitfalls To Watch

- Write down the bit identity before coding.
- XOR is commutative and associative, so input order does not matter.
- Hash-set and sorting solutions are correct baselines, but they miss at least
  one required constraint.
- Be careful with Python's unbounded signed integers when the problem assumes 32-bit behavior.
- For count/modulo problems, decide whether each bit is independent.
- For string/digit variants, keep carry and overflow rules explicit.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
