"""
191. Number of 1 Bits - Clear-Lowest-Set-Bit Reference

Return the number of set bits in the 32-bit unsigned representation of `n`.

Variant role:
    Primary manual bit trick, also known as Brian Kernighan's algorithm.

Core idea:
    The expression:

        n & (n - 1)

    clears exactly the lowest set bit in `n`. Repeating that operation until
    `n == 0` counts one set bit per loop.

Why the identity works:
    Subtracting 1 flips the lowest set bit to 0 and turns all lower bits into 1.
    AND-ing with the original number preserves the higher bits and clears that
    lowest set bit.

Step-by-step:
    1. Start `count = 0`.
    2. While `n` still has any set bit, clear its lowest set bit.
    3. Increment `count` for the cleared bit.
    4. Return the number of clear operations.

Mental trace:
    For:

        n = 0b1011

    the loop visits:

        1011 -> 1010 -> 1000 -> 0000

    so the answer is 3.

Complexity:
    Time:
        O(k), where k is the number of set bits; at most O(32).

    Space:
        O(1)

When to choose this variant:
    Lead with this after the straightforward shift loop. It shows the key bit
    trick and is faster for sparse numbers.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
