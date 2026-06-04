"""
11. Container With Most Water - Brute Force Reference

Return the maximum water area formed by two vertical lines.

Variant role:
    Baseline objective-function reference.

Core idea:
    Try every pair of lines and compute:

        width * min(height[left], height[right])

    The shorter wall limits the water height, and the index distance gives the
    width.

Why keep this reference:
    This version is not interview-ready for the real constraints, but it is the
    cleanest way to verify the objective function:

        area = distance_between_lines * shorter_wall

    It also makes clear why an optimized solution must avoid checking all pairs.

Example:
    For:

        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    the pair at indexes 1 and 8 gives:

        width = 8 - 1 = 7
        limiting height = min(8, 7) = 7
        area = 49

Complexity:
    Time:
        O(n^2)

    Space:
        O(1)

When to choose this variant:
    Use this only as the first mental model. Then explain that O(n^2) is too
    slow for n up to 10^5, which motivates the two-pointer dominance argument.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                best = max(best, (right - left) * min(height[left], height[right]))
        return best
