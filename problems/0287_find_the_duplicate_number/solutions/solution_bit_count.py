"""
287. Find the Duplicate Number - Bit-Count Reconstruction Reference

Find the repeated value without modifying the array and using O(1) extra space.

Variant role:
    Bit-manipulation reference.

Core idea:
    Compare bit counts in the input against bit counts in the ideal range
    `1..n`. The duplicate contributes extra occurrences of its set bits, so any
    bit position with a larger input count belongs to the duplicate.

Step-by-step:
    1. Let `n = len(nums) - 1`, so valid values are `1..n`.
    2. For each bit position needed to represent `n`, count how many input
       numbers have that bit set.
    3. Count how many values from `1` through `n` have that bit set.
    4. If the input count is larger, set that bit in the answer.

Mental trace:
    For:

        [1,3,4,2,2]

    the duplicate is:

        2 = 10 in binary

    The 2's bit appears one extra time in the input compared with the ideal
    range `1..4`, so the reconstructed answer becomes 2.

Counting nuance:
    Prefer:

        sum(1 for num in nums if num & mask)

    when explaining the invariant. Summing `mask & num` also works only because
    both sides of the comparison are scaled by the same mask.

Complexity:
    Time:
        O(n log n), where `log n` is the number of value bits.

    Space:
        O(1)

When to choose this variant:
    Useful for connecting this problem to the Bit Manipulation tag. It satisfies
    no mutation and constant auxiliary space, but Floyd is simpler and linear.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        for bit in range(n.bit_length()):
            mask = 1 << bit
            nums_count = sum(1 for num in nums if num & mask)
            range_count = sum(1 for value in range(1, n + 1) if value & mask)
            if nums_count > range_count:
                duplicate |= mask

        return duplicate
