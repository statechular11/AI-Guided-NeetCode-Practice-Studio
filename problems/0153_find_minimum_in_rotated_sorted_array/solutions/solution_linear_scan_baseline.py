"""
153. Find Minimum in Rotated Sorted Array - linear scan baseline

Variant role:
    educational baseline

Core idea:
    The minimum can always be found by direct scanning; binary search exploits the rotated sorted structure to do better.

Key invariant:
    best is the minimum value among all elements scanned so far.

Mechanics:
    Initialize best to nums[0], scan the rest, and update best whenever a smaller value appears.

Common pitfalls:
    This intentionally ignores the sorted-rotation property and does not meet the intended logarithmic target.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this as a correctness floor before explaining why comparing mid to right locates the rotation side.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        best = nums[0]
        for num in nums[1:]:
            best = min(best, num)
        return best
