"""
191. Number of 1 Bits - Parallel Bit Count Reference

Return the number of set bits in the 32-bit unsigned representation of `n`.

Variant role:
    Divide-and-conquer / parallel bit count (SWAR).

Core idea:
    Count bits in parallel by grouping neighboring bit fields. First each 2-bit
    group stores its number of ones, then each 4-bit group, then each byte, then
    wider groups. This is the bit-level divide-and-conquer idea behind many
    popcount implementations.

Meaning of the masks:
    `0x55555555` selects alternating single bits.

    `0x33333333` selects alternating 2-bit groups.

    `0x0F0F0F0F` keeps each 4-bit group after neighboring counts have been
    combined.

    These masks prevent neighboring count fields from bleeding into each other
    while the algorithm combines smaller groups into larger ones.

Step-by-step:
    1. Convert adjacent 1-bit fields into 2-bit counts.
    2. Combine 2-bit counts into 4-bit counts.
    3. Combine 4-bit counts into byte counts.
    4. Accumulate byte counts across the 32-bit word.
    5. Mask the low result bits.

Mental trace:
    For small values like:

        0b1011

    the masks first count pairs `10` and `11`, then combine those pair counts
    into the final total 3.

Complexity:
    Time:
        O(1)

    Space:
        O(1)

When to choose this variant:
    Educational for the Divide and Conquer tag and systems-flavored
    conversations. For ordinary interviews, Kernighan's trick is much easier to
    derive and explain.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        n &= 0xFFFFFFFF
        n = n - ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n + (n >> 4)) & 0x0F0F0F0F
        n += n >> 8
        n += n >> 16
        return n & 0x3F
