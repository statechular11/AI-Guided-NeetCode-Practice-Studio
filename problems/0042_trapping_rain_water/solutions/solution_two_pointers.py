"""
42. Trapping Rain Water - two pointers reference

Variant role:
    This is the primary interview solution. It compresses the prefix/suffix
    arrays into two running maxima and uses O(1) extra space.

Core idea:
    Maintain:

        left_max:  tallest wall seen so far from the left side
        right_max: tallest wall seen so far from the right side

    Whichever running maximum is smaller determines the water on that side,
    because the other side already has a boundary at least that tall.

Walkthrough:
    1. Place left and right pointers at the two ends.
    2. Update left_max and right_max from the current bars.
    3. If left_max <= right_max, then the left side is decided:

           water += left_max - height[left]

       Then move left inward.

    4. Otherwise, the right side is decided:

           water += right_max - height[right]

       Then move right inward.

Example:
    height = [4, 2, 0, 3, 2, 5]

    The right boundary of height 5 is high enough to decide several left-side
    positions. At index 1, left_max is 4 and height[1] is 2, so this index traps:

        4 - 2 = 2

    At index 2, it traps:

        4 - 0 = 4

    The final total is 9.

Why this works:
    This is the prefix/suffix formula without storing arrays. If left_max is
    smaller than right_max, then the unknown future right boundary cannot be the
    limiting factor for the left index; left_max is the limit. The symmetric
    argument holds for the right side.

When to choose this variant:
    Use this as the final interview solution when you can state the running-max
    invariant confidently. It is O(n) time and O(1) extra space.

Complexity:
    Time: O(n)
    Space: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water
