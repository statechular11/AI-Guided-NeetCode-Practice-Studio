"""
11. Container With Most Water - two pointers reference

Core idea:
    Start with the widest container. The shorter wall limits the area, so move
    the pointer at the shorter wall inward to search for a taller limiting wall.

Why moving the taller wall is unnecessary:
    Keeping the shorter wall while reducing width can never improve area, since
    the limiting height would not increase.

Step-by-step:
    1. Put one pointer at the left edge and one pointer at the right edge.
    2. Compute the area from the current pair.
    3. If the left wall is shorter, move left inward.
    4. Otherwise, move right inward.
    5. Keep the best area seen.

Dominance argument:
    Suppose height[left] <= height[right]. The current area is limited by
    height[left]. If we keep left fixed and move right inward, the width becomes
    smaller and the limiting height is still at most height[left]. Therefore no
    pair with this same left index and a smaller right index can beat the
    current pair. It is safe to discard left.

Example:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    Start with indexes 0 and 8:

        width = 8
        min height = 1
        area = 8

    The left wall is shorter, so move left. Eventually indexes 1 and 8 give:

        width = 7
        min height = 7
        area = 49

    That is the maximum.

When to choose this variant:
    This is the standard interview solution. It is short, O(n), and the key is
    being able to explain why moving the shorter wall is the only useful move.

Complexity:
    Time: O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
