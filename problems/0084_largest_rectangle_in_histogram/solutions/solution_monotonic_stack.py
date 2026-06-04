"""
84. Largest Rectangle in Histogram - one-pass monotonic index stack.

Variant role:
    Primary optimized interview solution.

Core idea:
    Every maximal rectangle has a limiting bar: the shortest bar inside that
    rectangle. If we know how far a bar can extend left and right before a
    shorter bar appears, we can compute the largest rectangle using that bar as
    the limiting height.

    The stack keeps indices of bars whose right boundary is not known yet. Its
    heights are monotonically non-decreasing. When a shorter current bar
    appears, it becomes the first shorter bar to the right for any taller bars
    on top of the stack, so those bars can be finalized.

For a popped bar:
    - height is `heights[popped_index]`
    - right boundary is `i - 1`
    - left boundary is `stack[-1] + 1` after popping
    - width is `i - stack[-1] - 1`

Sentinels:
    - stack starts with index -1, which acts as the boundary before the array
    - a virtual trailing height 0 forces all remaining bars to be finalized

Small trace:
    heights = [2, 1, 5, 6, 2, 3]

    When we reach the second 2 at index 4, it is shorter than 6 and 5:

    - pop 6 at index 3: width 1, area 6
    - pop 5 at index 2: width 2, area 10

    Area 10 is the best rectangle: height 5 across bars [5, 6].

When to choose this variant:
    Choose this in interviews once you recognize the nearest-smaller-boundary
    pattern. It is the most compact O(n) solution.

Complexity:
    Time: O(n), because each index is pushed once and popped at most once
    Space: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = [-1]
        best = 0

        for i, height in enumerate(heights + [0]):
            while stack[-1] != -1 and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                width = i - stack[-1] - 1
                best = max(best, h * width)
            stack.append(i)

        return best
