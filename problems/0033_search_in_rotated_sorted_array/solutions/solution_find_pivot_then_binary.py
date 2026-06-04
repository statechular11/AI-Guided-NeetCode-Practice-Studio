"""
33. Search in Rotated Sorted Array - find rotation pivot then binary search

Variant role:
    two-step binary-search reference

Core idea:
    Separate the problem into finding the smallest element's index, then binary-searching the sorted half that could contain target.

Key invariant:
    The pivot search keeps the minimum inside [left, right]; the second search runs on an actually sorted interval.

Mechanics:
    Find pivot by comparing nums[mid] to nums[right]. Then decide whether target belongs to [pivot, n-1] or [0, pivot-1].

Common pitfalls:
    After finding the pivot, do not binary-search across the rotation break. Choose one sorted half first.

Complexity:
    Time: O(log n); Space: O(1)

When to choose this variant:
    Use this when the one-pass rotated binary search feels too branchy; the two phases are easier to narrate.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        if nums[pivot] <= target <= nums[-1]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
