"""
84. Largest Rectangle in Histogram - precompute nearest smaller boundaries.

Variant role:
    Boundary-explicit O(n) solution.

Core idea:
    For each bar, find:

    - `left_less[i]`: nearest index to the left with height < heights[i]
    - `right_less[i]`: nearest index to the right with height < heights[i]

    Then bar `i` can be the limiting height over the open interval:

        (left_less[i], right_less[i])

    Its best rectangle area is:

        heights[i] * (right_less[i] - left_less[i] - 1)

Why pop `>=`:
    Equal-height bars should merge into one wider rectangle. Popping heights
    greater than or equal to the current height ensures the boundary is truly
    smaller, not merely equal.

Example:
    heights = [2, 2, 2]

    Every bar has left boundary -1 and right boundary 3, so the best area is:

        2 * (3 - (-1) - 1) = 6

When to choose this variant:
    Choose this when you want the "nearest smaller on both sides" idea to be
    very explicit. It is slightly longer than the one-pass stack but often
    easier to reason about.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_less = [-1] * n
        right_less = [n] * n

        stack: list[int] = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            if stack:
                left_less[i] = stack[-1]
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_less[i] = stack[-1]
            stack.append(i)

        best = 0
        for i, height in enumerate(heights):
            width = right_less[i] - left_less[i] - 1
            best = max(best, height * width)

        return best
