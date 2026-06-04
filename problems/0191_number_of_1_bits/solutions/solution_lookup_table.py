"""
191. Number of 1 Bits - Byte Lookup Table Reference

Return the number of set bits in the 32-bit unsigned representation of `n`.

Variant role:
    Repeated-call optimization with byte lookup.

Core idea:
    Precompute the number of set bits for every 8-bit value. A 32-bit input can
    then be split into four bytes and answered with four table lookups.

How the table is used:
    The lowest byte is:

        n & 0xFF

    After looking up its count, shift by 8 bits so the next byte becomes the
    low byte:

        n >>= 8

    Repeat for four total bytes.

Mental trace:
    `0b1011` has low byte:

        00001011

    The table stores 3 for that byte, and the higher three bytes contribute 0.

Follow-up value:
    If the function is called many times, the fixed table avoids repeated
    per-bit work inside each call.

Complexity:
    Time:
        O(4), which is O(1) for 32-bit inputs.

    Space:
        O(256) shared lookup table.

When to choose this variant:
    Use this for the follow-up where the function is called many times. It
    trades a tiny fixed table for very predictable per-call work.
"""

def _count_byte(value: int) -> int:
    count = 0
    while value:
        value &= value - 1
        count += 1
    return count


BYTE_COUNTS = tuple(_count_byte(i) for i in range(256))


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(4):
            count += BYTE_COUNTS[n & 0xFF]
            n >>= 8
        return count
