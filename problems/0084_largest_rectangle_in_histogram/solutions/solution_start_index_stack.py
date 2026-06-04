"""
84. Largest Rectangle in Histogram - stack of `(start_index, height)` pairs.

Variant role:
    Interview-friendly monotonic stack with an explicit left boundary.

Core idea:
    Scan from left to right with a stack of increasing heights. Each stack item
    stores the earliest index where that height could start after merging over
    taller bars.

    When the current height is smaller than the stack top, the taller bar can no
    longer extend to the right. Its rectangle ends just before the current
    index, so:

        area = popped_height * (current_index - popped_start)

    The current shorter bar inherits the popped bar's start index because it can
    extend through the region previously occupied by taller bars.

Small trace:
    heights = [2, 1, 5, 6, 2, 3]

    At index 4, height 2:

    - pop (3, 6): area = 6 * (4 - 3) = 6
    - pop (2, 5): area = 5 * (4 - 2) = 10
    - push current height 2 with inherited start index 2

    That inherited start index captures that height 2 can span from index 2
    through the current position.

When to choose this variant:
    Choose this if carrying the left boundary directly feels easier than using
    a sentinel index and computing `i - stack[-1] - 1`.

Complexity:
    Time: O(n), because each bar is pushed once and popped at most once
    Space: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[tuple[int, int]] = []
        best = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                prev_start, prev_height = stack.pop()
                best = max(best, prev_height * (i - prev_start))
                start = prev_start

            stack.append((start, height))

        n = len(heights)
        for start, height in stack:
            best = max(best, height * (n - start))

        return best
