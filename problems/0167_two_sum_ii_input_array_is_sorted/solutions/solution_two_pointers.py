"""
167. Two Sum II - Two Pointers Reference

Return 1-based indices of two numbers in a sorted array that sum to target.

Variant role:
    Primary interview solution.

Core idea:
    The array is sorted. If the smallest plus largest value is too small, move
    the left pointer right to increase the sum. If it is too large, move the
    right pointer left to decrease the sum.

Why the pointer move is safe:
    When `numbers[left] + numbers[right] < target`, keeping `left` cannot work
    with any smaller right-side value, because moving `right` left only
    decreases the sum. So `left` must move right.

    Symmetrically, when the sum is too large, keeping `right` cannot work with
    any larger left-side value, so `right` must move left.

Example:
    For:

        numbers = [2, 3, 4]
        target = 6

    `2 + 4 = 6`, so return the 1-based indices:

        [1, 3]

Pitfall:
    The returned indices are 1-based, not 0-based.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews. It is the whole reason the sorted input matters.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        return []
