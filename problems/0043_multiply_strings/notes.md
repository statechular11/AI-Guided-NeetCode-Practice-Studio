# Notes - 43. Multiply Strings

## Core Idea

Simulate grade-school multiplication without converting either input string to
an integer. There are two useful ways to keep the indexes straight:

- Fixed result array: `num1[i] * num2[j]` writes its low digit to
  `result[i + j + 1]` and its carry to `result[i + j]`.
- Diagonal accumulation: work from the ones column leftward; reversed digit
  positions `a` and `b` belong to output column `k` when `a + b == k`.

The fixed-array formula is the shortest interview implementation, while the
diagonal view is a good way to debug boundary mistakes.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_digit_array.py` | primary solution | Time: O(m*n); Space: O(m+n) |
| `solution_diagonal_carry.py` | boundary-focused column variant | Time: O(m*n); Space: O(m+n) |

## Pitfalls To Watch

- Return `"0"` immediately if either input is `"0"`.
- The maximum product length is `m + n`, not `m + n - 1`.
- In the fixed-array solution, the low slot for `num1[i] * num2[j]` is
  `i + j + 1`; the carry slot is `i + j`.
- In the diagonal solution, use reversed digit positions so the boundary rule
  becomes `a + b == column`.
- Strip leading zeroes when using a full result array.
- Do not use `int(num1)`, `int(num2)`, `pow`, or BigInteger-style conversion.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
