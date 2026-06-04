"""
191. Number of 1 Bits - Python bit_count Reference

Return the number of set bits in the 32-bit unsigned representation of `n`.

Variant role:
    Python API / production-practical solution.

Core idea:
    Python integers expose:

        int.bit_count()

    which returns the number of set bits in the integer's binary representation.

Step-by-step:
    1. Call `n.bit_count()`.
    2. Return the result.

Mental trace:
    `11` is binary:

        1011

    so:

        11.bit_count() == 3

Interview caveat:
    This is excellent Python API knowledge, but a bit-manipulation interview may
    expect the manual shift loop or `n & (n - 1)` version.

Complexity:
    Time:
        O(number of machine words used by the integer); O(1) for this bounded
        LeetCode input.

    Space:
        O(1)

When to choose this variant:
    Great to know in real Python. In an interview, also be ready to write the
    manual shift or `n & (n - 1)` version.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        if hasattr(int, "bit_count"):
            return n.bit_count()
        return bin(n & 0xFFFFFFFF).count("1")
