"""
190. Reverse Bits - Direct Position Mapping Reference

Return the 32-bit unsigned integer produced by reversing all 32 bits of `n`.

Core idea:
    In a 32-bit reversal, every source position has exactly one destination:

        source bit i -> destination bit 31 - i

    This version implements that mapping literally. For each `i`, extract the
    bit at position `i`:

        bit = (n >> i) & 1

    Then place it at the mirrored position:

        bit << (31 - i)

    OR-ing all placed bits together builds the final reversed integer.

Why this is useful:
    This version is slightly more verbose than shift-accumulate, but the
    invariant is extremely direct. If an interviewer asks where each bit moves,
    this implementation answers that question line by line.

Example:
    If bit 0 of `n` is 1:

        bit = (n >> 0) & 1 = 1

    It contributes:

        1 << 31

    If bit 31 of `n` is 1, it contributes:

        1 << 0

Unsigned return value:
    The answer should remain the unsigned 32-bit value. Python can represent
    values such as `2147483648` directly, so no signed conversion is needed.

Complexity:
    Time:
        O(32), which is O(1) for this fixed-width problem.

    Space:
        O(1).

When to choose this variant:
    Choose this when the clearest explanation is "bit `i` moves to bit
    `31 - i`."
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result |= bit << (31 - i)
        return result
