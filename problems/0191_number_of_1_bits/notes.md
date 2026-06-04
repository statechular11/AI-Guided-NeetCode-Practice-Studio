# Notes - 191. Number of 1 Bits

## Core Idea

`n & (n - 1)` clears the lowest set bit, so the loop runs once per 1-bit.

The learning ladder is:

- shift and count: inspect every bit in a fixed-width word,
- clear-lowest-set-bit: loop once per `1` bit,
- built-in API: know `int.bit_count()` for real Python work,
- lookup table: answer repeated calls with four byte-count lookups,
- parallel bit count: combine bit fields with masks as a divide-and-conquer
  popcount pattern.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_shift_count.py` | simple baseline | Time: O(32); Space: O(1) |
| `solution_clear_lowest_set_bit.py` | primary bit trick | Time: O(set bits); Space: O(1) |
| `solution_builtin_bit_count.py` | Python API variant | Time: O(1) for bounded input; Space: O(1) |
| `solution_lookup_table.py` | repeated-call optimization | Time: O(1); Space: O(256) |
| `solution_parallel_bit_count.py` | divide-and-conquer bit-count variant | Time: O(1); Space: O(1) |

## Pitfalls To Watch

- Write down the bit identity before coding.
- `n & (n - 1)` clears the lowest set bit; `n & 1` only inspects the lowest bit.
- If using a fixed-width loop, iterate the expected bit width or stop once `n`
  becomes zero for positive inputs.
- For repeated calls, a small lookup table can be a practical optimization.
- Be careful with Python's unbounded signed integers when the problem assumes 32-bit behavior.
- For count/modulo problems, decide whether each bit is independent.
- For string/digit variants, keep carry and overflow rules explicit.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
