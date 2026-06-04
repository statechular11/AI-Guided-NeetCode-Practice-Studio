# Notes - 50. Pow(x, n)

## Core Idea

Binary exponentiation is the reusable pattern: repeatedly square the base and
consume the exponent one binary bit at a time.

Useful ways to express the same idea:

- Iterative bit scan: when `n & 1`, multiply the answer by the current base;
  then square the base and shift `n` right.
- Recursive divide and conquer: compute `x^(n // 2)` once, square it, and
  multiply by one extra `x` when `n` is odd.

For negative exponents, convert once at the top:

```python
x = 1 / x
n = -n
```

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_binary_exponentiation.py` | primary iterative solution | Time: O(log |n|); Space: O(1) |
| `solution_recursive_fast_power.py` | recursion variant | Time: O(log |n|); Space: O(log |n|) |

## Pitfalls To Watch

- Do not multiply `|n|` times; `n` can be very large.
- Handle `n == 0` as `1.0`.
- Normalize negative exponents before the main loop or recursive helper.
- In recursion, store the half result instead of calling the helper twice.
- Avoid using Python's `pow` or `**`; the point is implementing fast power.
- The prompt guarantees either `x != 0` or `n > 0`, so reciprocal conversion
  will not divide by zero for valid inputs.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
