"""
84. Largest Rectangle in Histogram - brute-force expansion baseline.

Variant role:
    Learning baseline for understanding the rectangle definition.

Core idea:
    Treat each bar as the limiting shortest bar of a rectangle. Expand left and
    right while neighboring bars are at least that height, then compute:

        area = height * width

Example:
    heights = [2, 1, 5, 6, 2, 3]

    For bar height 5 at index 2:

    - it cannot extend left because height 1 is shorter
    - it can extend right across height 6
    - it stops before height 2
    - area = 5 * 2 = 10

When to choose this variant:
    Use this to build intuition or debug small cases. It is not acceptable for
    the full constraints because n can be 10^5.

Complexity:
    Time: O(n^2)
    Space: O(1)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        for i, height in enumerate(heights):
            left = right = i
            while left - 1 >= 0 and heights[left - 1] >= height:
                left -= 1
            while right + 1 < len(heights) and heights[right + 1] >= height:
                right += 1
            best = max(best, height * (right - left + 1))
        return best
