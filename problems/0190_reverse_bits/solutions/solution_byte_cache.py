"""
190. Reverse Bits - Cache Reversed Bytes And Compose Four Lookups

Variant role:
    many-calls follow-up optimization. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Reverse a fixed 32-bit stream, not just the visible bits of the integer. Leading zeros must be processed because they become trailing zeros after reversal. Useful ways to see the same invariant: Shift-accumulate: repeat 32 times, `result = (result << 1) | (n & 1)`, then `n >>= 1`. Direct positions: bit `i` in the input moves to bit `31 - i` in the output. Mask swaps: swap 16-bit halves, then bytes, nibbles, pairs, and individual bits. Many-calls follow-up: cache reversed bytes and combine four byte lookups per call.

    This specific variant uses: cache reversed bytes and compose four lookups.

Key invariant:
    Each bit operation changes or inspects a specific binary fact while preserving the other bits needed by later steps.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 43261596}` and the expected result is `964176192`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Always run exactly 32 iterations or explicitly handle all 32 positions; stopping when `n == 0` drops leading zeros that matter. Return the 32-bit unsigned value. Do not convert answers above `2^31 - 1` into negative Python integers. When using mask swaps in Python, mask intermediate or final values with `0xFFFFFFFF` because Python integers are unbounded. For the repeated-call follow-up, byte caching is easier to explain than trying to memoize every possible 32-bit input.

Complexity:
    Time: O(1) per call; Space: O(256)

When to choose this variant:
    Use this variant when its role matches the interview goal: many-calls follow-up optimization. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    190. Reverse Bits - Byte-Cache Reference Return the 32-bit unsigned integer produced by reversing all 32 bits of `n`. Follow-up idea: If `reverseBits` is called many times, repeated work can be cached. A 32-bit integer has four bytes, and there are only 256 possible byte values. Precomputing the reversed form of each byte lets every call use four table lookups instead of processing 32 individual bits. How the table is built: `_BYTE_REVERSE[value]` stores the 8-bit reversal of `value`. Example: value = 0b00000101 The reversed byte is: 0b10100000 The table has exactly 256 entries, one for every possible byte. How a 32-bit value is reconstructed: The low byte of the input becomes the high byte of the output, but with its eight bits reversed: table[n & 0xFF] << 24 The next input byte becomes the next output byte: table[(n >> 8) & 0xFF] << 16 The same idea continues for all four bytes. Why...
"""

class Solution:
    _BYTE_REVERSE = tuple(
        int(f"{value:08b}"[::-1], 2) for value in range(256)
    )

    def reverseBits(self, n: int) -> int:
        table = self._BYTE_REVERSE
        return (
            (table[n & 0xFF] << 24)
            | (table[(n >> 8) & 0xFF] << 16)
            | (table[(n >> 16) & 0xFF] << 8)
            | table[(n >> 24) & 0xFF]
        )
