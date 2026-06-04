"""
1. Two Sum - hash map reference

Variant role:
    Primary interview solution.

Core idea:
    While scanning left to right, store numbers already seen with their indices.
    For the current number `num`, the only value that can complete the pair is:

        complement = target - num

    If the complement has already appeared, return its index and the current
    index. Otherwise, remember the current number for future positions.

Key invariant:
    Before processing index i, `seen` maps each value in nums[0:i] to one valid
    earlier index where that value appeared.

Example:
    nums = [3, 2, 4], target = 6

    i = 0, num = 3, complement = 3, not seen -> seen[3] = 0
    i = 1, num = 2, complement = 4, not seen -> seen[2] = 1
    i = 2, num = 4, complement = 2, seen[2] = 1 -> return [1, 2]

Why storing after the lookup matters:
    If target is twice the current number, storing before lookup could reuse the
    same index. Looking up first guarantees two different positions.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
