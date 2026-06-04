"""
152. Maximum Product Subarray - left-right product scans

Variant role:
    alternative product-sign reference

Core idea:
    Zeros split the array, and within each zero-free segment the best product is found by dropping a bad prefix or suffix when negatives are odd.

Key invariant:
    The running product since the last zero captures every prefix product in the current scan direction.

Mechanics:
    Scan left-to-right and right-to-left, resetting product after zeros, and keep the maximum product seen.

Common pitfalls:
    One scan is not enough when the best subarray must drop a prefix negative; the reverse scan handles the symmetric case.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this as a compact alternative to tracking current max and min products.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)

        product = 1
        for num in nums:
            product *= num
            best = max(best, product)
            if product == 0:
                product = 1

        product = 1
        for num in reversed(nums):
            product *= num
            best = max(best, product)
            if product == 0:
                product = 1

        return best
