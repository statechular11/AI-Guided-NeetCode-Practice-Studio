"""
11. Container With Most Water - skip dominated heights reference

Variant role:
    This is the same O(n) two-pointer idea, written to make the dominance
    pruning more explicit.

Core idea:
    After evaluating a pair, the shorter side is the bottleneck. Any future pair
    using that same side with a smaller width and a height no taller than the
    old bottleneck cannot improve the answer. So instead of moving the pointer
    only once, skip over all heights that are less than or equal to the old
    limiting height.

Step-by-step:
    1. Start with the widest possible pair: left = 0, right = n - 1.
    2. Compute the current area and remember the better answer.
    3. Let limit = min(height[left], height[right]).
    4. Move left inward while height[left] <= limit.
    5. Move right inward while height[right] <= limit.
    6. Repeat until the pointers cross.

Why the skips are safe:
    If height[left] <= limit after moving inward, then using that left wall with
    the current or any smaller width cannot beat an area already evaluated with
    the same or taller limiting height and a wider container.

Example:
    For height = [1, 8, 6, 2, 5, 4, 8, 3, 7], the first pair has limit 1.
    Height 1 at index 0 cannot be part of a better future container, so left
    jumps to index 1. Later, low interior heights are skipped for the same
    reason.

When to choose this variant:
    The simpler one-step two-pointer solution is usually easier to code in an
    interview. This version is useful for learning because it exposes the
    "dominated candidate" reasoning behind the pointer movement.

Complexity:
    Time: O(n), because each pointer only moves inward.
    Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            limit = min(height[left], height[right])
            best = max(best, (right - left) * limit)

            while left < right and height[left] <= limit:
                left += 1
            while left < right and height[right] <= limit:
                right -= 1

        return best
