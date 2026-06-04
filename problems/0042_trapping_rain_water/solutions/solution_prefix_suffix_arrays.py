"""
42. Trapping Rain Water - prefix/suffix arrays reference

Variant role:
    This is the learning-friendly dynamic programming view. It explicitly
    computes the best wall available on the left and on the right for every
    index, which makes the water formula almost mechanical.

Core idea:
    Water above index i is limited by the smaller of the tallest wall on its
    left and the tallest wall on its right.

        water[i] = min(left_max[i], right_max[i]) - height[i]

Step-by-step:
    1. Build left_max where left_max[i] is max(height[0:i + 1]).
    2. Build right_max where right_max[i] is max(height[i:n]).
    3. For each index, the water level is the lower of those two walls.
    4. Subtract the current bar height to get water trapped at that index.
    5. Sum all positions.

Example:
    height = [0, 1, 0, 2]

    left_max  = [0, 1, 1, 2]
    right_max = [2, 2, 2, 2]

    At index 2:

        height[2] = 0
        min(left_max[2], right_max[2]) = min(1, 2) = 1
        trapped water = 1 - 0 = 1

Why this is useful:
    It separates the problem into two simple facts:

    - water needs a wall on the left
    - water needs a wall on the right

    The optimized two-pointer solution is easier to understand after this
    prefix/suffix version is clear.

When to choose this variant:
    Use this when you want the safest implementation during practice or when
    explaining the water formula first. For the final interview target, prefer
    the O(1)-space two-pointer version if you can explain it clearly.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
