# Notes - 338. Counting Bits

## Core Idea

Build a learning ladder from the prompt's follow-up:

- Baseline: count each number independently with a bit loop or Kernighan's `value &= value - 1`; this is the easy O(n log n)-style direction.
- DP by lowest bit: `bits[i] = bits[i >> 1] + (i & 1)`. Shift off the low bit, then add it back.
- DP by clearing lowest set bit: `bits[i] = bits[i & (i - 1)] + 1`. Clear exactly one 1-bit, then add one.
- DP by offset/highest power of two: `bits[i] = 1 + bits[i - offset]`, where `offset` is the largest power of two not greater than `i`.
- Python API contrast: `i.bit_count()` is useful in real Python, but it violates the no-built-in follow-up.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dp_lowest_bit.py` | primary DP bit solution | Time: O(n); Space: O(n) |
| `solution_dp_clear_lowest_bit.py` | bit-trick variant | Time: O(n); Space: O(n) |
| `solution_dp_offset.py` | offset recurrence variant | Time: O(n); Space: O(n) |
| `solution_per_number_kernighan.py` | O(n log n) educational baseline | Time: O(n log n); Space: O(n) |
| `solution_builtin_bit_count.py` | Python API contrast | Time: O(n log n) bit-work; Space: O(n) |

## Pitfalls To Watch

- Include index 0 in the output; `bits[0]` is the base case.
- The output array itself costs O(n) space. The good DP solutions use O(1) auxiliary state beyond that output.
- In the low-bit recurrence, `i >> 1` is always smaller than `i`, so the needed answer is already computed.
- In the offset recurrence, update `offset` exactly when `i` reaches the next power of two.
- Built-in popcount helpers are fine API knowledge, but they do not satisfy this prompt's follow-up.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
