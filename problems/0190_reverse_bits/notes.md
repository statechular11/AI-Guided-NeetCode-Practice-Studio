# Notes - 190. Reverse Bits

## Core Idea

Reverse a fixed 32-bit stream, not just the visible bits of the integer. Leading zeros must be processed because they become trailing zeros after reversal.

Useful ways to see the same invariant:

- Shift-accumulate: repeat 32 times, `result = (result << 1) | (n & 1)`, then `n >>= 1`.
- Direct positions: bit `i` in the input moves to bit `31 - i` in the output.
- Mask swaps: swap 16-bit halves, then bytes, nibbles, pairs, and individual bits.
- Many-calls follow-up: cache reversed bytes and combine four byte lookups per call.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_shift_accumulate.py` | primary bit solution | Time: O(32); Space: O(1) |
| `solution_direct_positions.py` | positional invariant variant | Time: O(32); Space: O(1) |
| `solution_mask_swaps.py` | constant-operation optimized bit trick | Time: O(1); Space: O(1) |
| `solution_byte_cache.py` | many-calls follow-up optimization | Time: O(1) per call; Space: O(256) |

## Pitfalls To Watch

- Always run exactly 32 iterations or explicitly handle all 32 positions; stopping when `n == 0` drops leading zeros that matter.
- Return the 32-bit unsigned value. Do not convert answers above `2^31 - 1` into negative Python integers.
- When using mask swaps in Python, mask intermediate or final values with `0xFFFFFFFF` because Python integers are unbounded.
- For the repeated-call follow-up, byte caching is easier to explain than trying to memoize every possible 32-bit input.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
