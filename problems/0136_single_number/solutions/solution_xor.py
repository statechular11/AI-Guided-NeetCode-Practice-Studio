"""
136. Single Number - XOR Cancellation Reference

Return the only value that appears once when every other value appears exactly
twice.

Variant role:
    Primary bit-manipulation solution.

Core idea:
    XOR is a cancellation operator for equal pairs:

        x ^ x == 0
        x ^ 0 == x

    Since every duplicated number appears exactly twice, XORing all values
    cancels every pair and leaves only the single value.

Why order does not matter:
    XOR is associative and commutative, so the values can be grouped mentally as
    duplicate pairs plus the unique value:

        unique ^ (a ^ a) ^ (b ^ b)

    which becomes:

        unique ^ 0 ^ 0

Step-by-step:
    1. Start with `result = 0`.
    2. XOR each number into `result`.
    3. Duplicate values cancel out whenever both copies have appeared.
    4. Return the remaining value.

Mental trace:
    `[4,1,2,1,2]` becomes:

        4 ^ (1 ^ 1) ^ (2 ^ 2)

    which is:

        4 ^ 0 ^ 0 == 4

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Lead with this answer. It is the only included variant that meets both the
    linear-time and constant-extra-space requirements.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
