"""
238. Product of Array Except Self - left/right arrays reference

Variant role:
    Learning-friendly reference. This is often the easiest no-division version
    to discover during an interview because it names both pieces of the answer
    directly.

Problem restatement:
    For every index i, return the product of all numbers except nums[i].
    The solution must run in O(n) time and cannot use division.

Core idea:
    The answer for index i can be split into two independent products:

        product of everything left of i
        *
        product of everything right of i

    This variant computes those two pieces in separate arrays:

        left[i]  = nums[0] * nums[1] * ... * nums[i - 1]
        right[i] = nums[i + 1] * nums[i + 2] * ... * nums[n - 1]

    Then:

        answer[i] = left[i] * right[i]

Step-by-step walkthrough:
    1. Fill left from left to right.
       left[0] is 1 because there is nothing to the left of index 0.

    2. Fill right from right to left.
       right[n - 1] is 1 because there is nothing to the right of the last
       index.

    3. Multiply left[i] and right[i] for each index.

Example:
    nums = [1, 2, 3, 4]

    left:
        [1, 1, 2, 6]

    right:
        [24, 12, 4, 1]

    answer:
        [1 * 24, 1 * 12, 2 * 4, 6 * 1]
        = [24, 12, 8, 6]

Why zeros work naturally:
    No division is used, so there is no special zero branch. Any zero simply
    participates in the left or right product where it belongs.

Interview note:
    This version is excellent for explaining the invariant. After it is clear,
    optimize away the two helper arrays by storing left products directly in
    the output array and multiplying suffix products in a backward pass.

Complexity:
    Time: O(n)
    Space: O(n) extra for left and right arrays, excluding the returned answer.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return [left[i] * right[i] for i in range(n)]
