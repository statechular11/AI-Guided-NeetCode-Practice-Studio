"""
191. Number of 1 Bits - Fixed-Width Shift Count Reference

Return the number of set bits in the 32-bit unsigned representation of `n`.

Variant role:
    Straightforward fixed-width bit inspection.

Core idea:
    Look at the least-significant bit with:

        n & 1

    add it to the count, then shift `n` right so the next bit becomes the new
    least-significant bit.

Why exactly 32 iterations:
    The problem is defined over a 32-bit unsigned integer. Repeating exactly 32
    times makes the width explicit and avoids relying on when Python's integer
    representation happens to become zero.

Step-by-step:
    1. Repeat exactly 32 times for the expected unsigned integer width.
    2. Add `1` when the current low bit is set.
    3. Shift right by one bit.
    4. Return the total.

Mental trace:
    `0b1011` exposes low bits:

        1, 1, 0, 1

    contributing three ones.

Complexity:
    Time:
        O(32)

    Space:
        O(1)

When to choose this variant:
    Good first answer because it is easy to explain. Then mention `n & (n - 1)`
    as the optimized sparse-number version.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += n & 1
            n >>= 1
        return count
