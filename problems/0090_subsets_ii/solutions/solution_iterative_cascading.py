"""
90. Subsets II - iterative cascading with duplicate window

Variant role:
    alternative duplicate-aware subsets reference

Core idea:
    When a value repeats, extend only the subsets created in the previous round, avoiding duplicate subsets.

Key invariant:
    subsets contains all unique subsets for processed numbers; start marks where the last value's new subsets began.

Mechanics:
    Sort nums. For a new value, extend every existing subset. For a duplicate value, extend only the subsets added by the previous copy.

Common pitfalls:
    Without the start boundary, duplicate values produce the same subset through multiple paths.

Complexity:
    Time: O(n * 2^n); Space: O(n * 2^n)

When to choose this variant:
    Use this to see duplicate handling without recursive skip logic.
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets: list[list[int]] = [[]]
        previous_start = 0

        for i, num in enumerate(nums):
            start = previous_start if i > 0 and nums[i] == nums[i - 1] else 0
            previous_start = len(subsets)
            for j in range(start, previous_start):
                subsets.append(subsets[j] + [num])

        return subsets
