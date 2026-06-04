"""
42. Trapping Rain Water - monotonic stack reference

Variant role:
    This is the representative stack solution. Instead of deciding water at each
    index from left/right maxima, it computes water when a right boundary closes
    a basin.

Core idea:
    Keep indexes of bars in a monotonically decreasing stack. When the current
    bar is taller than the bar at the stack top, the current bar may be a right
    boundary for a basin whose bottom is the popped bar.

Step-by-step:
    1. Scan bars from left to right.
    2. While the current height is greater than the height at the stack top:
       - Pop the stack top. That popped index is the basin bottom.
       - If the stack is empty, there is no left boundary, so no water is added.
       - Otherwise, the new stack top is the left boundary and the current index
         is the right boundary.
       - Water height is:

             min(height[left_boundary], height[right_boundary]) - height[bottom]

       - Width is the number of positions between the two boundaries.
    3. Push the current index.

Example:
    height = [0, 1, 0, 2]

    When we reach height 2 at index 3, index 2 with height 0 is popped as the
    basin bottom. The left boundary is index 1 with height 1, and the right
    boundary is index 3 with height 2:

        bounded height = min(1, 2) - 0 = 1
        width = 3 - 1 - 1 = 1
        water added = 1

Why this works:
    A decreasing stack stores unresolved left boundaries. A basin becomes
    resolvable only when a sufficiently tall right boundary appears. Popping
    exposes the next left boundary and lets us compute the rectangular slice of
    trapped water above the popped bottom.

When to choose this variant:
    Use the two-pointer solution for the shortest interview implementation.
    Use this stack variant when practicing monotonic stack patterns or when you
    want to connect this problem to "next greater boundary" reasoning.

Complexity:
    Time: O(n), because each index is pushed and popped at most once.
    Space: O(n), for the stack.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack: list[int] = []
        water = 0

        for right, right_height in enumerate(height):
            while stack and right_height > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                bounded_height = min(height[left], right_height) - height[bottom]
                width = right - left - 1
                water += bounded_height * width

            stack.append(right)

        return water
