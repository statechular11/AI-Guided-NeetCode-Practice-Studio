# Notes - 371. Sum of Two Integers

## Core Idea

Addition can be represented with bit operations:

- `a ^ b` gives the carry-free sum bits.
- `(a & b) << 1` gives the carry bits shifted into the next column.
- Repeating those two steps until no carry remains produces the final sum.

In Python, mask intermediate values to 32 bits because Python integers are
unbounded and negative numbers otherwise behave like they have infinitely many
leading `1` bits.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bitwise_add.py` | primary bit solution | Time: O(32); Space: O(1) |
| `solution_full_adder_scan.py` | educational hardware-adder variant | Time: O(32); Space: O(1) |

## Pitfalls To Watch

- Mask with `0xFFFFFFFF` inside the carry loop; otherwise negative inputs can
  keep propagating carries forever in Python.
- Convert the final unsigned 32-bit pattern back to a Python signed integer
  when it is greater than `0x7FFFFFFF`.
- Remember that one XOR/carry pass is not enough; carries can cascade.
- Avoid using `+` or `-` in helper logic because the problem forbids those
  operators.
- The full-adder scan is useful for understanding the bit identity, but the
  XOR + carry loop is the cleaner interview implementation.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
