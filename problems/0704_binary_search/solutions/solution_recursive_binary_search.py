"""
704. Binary Search - recursive closed-interval binary search

Variant role:
    alternative binary-search reference

Core idea:
    The recursive call keeps only the half of the search interval that can still contain target.

Key invariant:
    If target exists, it is inside nums[left:right+1] for the current call.

Mechanics:
    Compare target to nums[mid], then recurse left or right until the interval is empty.

Common pitfalls:
    Use left > right as the not-found base case for a closed interval.

Complexity:
    Time: O(log n); Space: O(log n)

When to choose this variant:
    Use this to practice the binary-search invariant before preferring the iterative O(1)-space version.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return find(mid + 1, right)
            return find(left, mid - 1)

        return find(0, len(nums) - 1)
