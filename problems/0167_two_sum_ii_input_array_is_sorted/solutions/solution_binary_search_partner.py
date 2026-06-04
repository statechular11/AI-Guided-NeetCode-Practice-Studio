"""
167. Two Sum II - Input Array Is Sorted - binary search partner for each index

Variant role:
    alternative sorted-array reference

Core idea:
    For each first number, binary-search the sorted suffix for the exact complement.

Key invariant:
    The complement search range excludes the current index and remains sorted.

Mechanics:
    Loop i from left to right, search numbers[i+1:] for target - numbers[i], and return 1-based indices.

Common pitfalls:
    The output is 1-indexed. Also search only after i so the same element is not reused.

Complexity:
    Time: O(n log n); Space: O(1)

When to choose this variant:
    Use this to practice binary search on sorted input; two pointers is the optimized O(n) solution.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, value in enumerate(numbers):
            need = target - value
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == need:
                    return [i + 1, mid + 1]
                if numbers[mid] < need:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
