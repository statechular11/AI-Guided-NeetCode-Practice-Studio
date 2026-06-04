"""
213. House Robber II - two linear DP tables

Variant role:
    first-principles circular-DP reference

Core idea:
    The first and last houses conflict, so solve two linear robber problems: exclude first or exclude last.

Key invariant:
    Within each chosen linear range, dp[i] is the best value from the first i houses in that range.

Mechanics:
    Run standard House Robber DP on nums[:-1] and nums[1:], then take the larger answer.

Common pitfalls:
    Handle n == 1 before slicing, because excluding first or last would leave an empty range.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this before compressing each linear range to two rolling variables.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(values: List[int]) -> int:
            dp = [0] * (len(values) + 1)
            for i, amount in enumerate(values, start=1):
                dp[i] = max(dp[i - 1], dp[i - 2] + amount)
            return dp[-1]

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
