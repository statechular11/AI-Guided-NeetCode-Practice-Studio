"""
198. House Robber - full DP table

Variant role:
    first-principles DP baseline

Core idea:
    For each house, choose between skipping it or robbing it plus the best value two houses back.

Key invariant:
    dp[i] is the best amount obtainable from the first i houses.

Mechanics:
    dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]). The rolling-state version stores only the previous two cells.

Common pitfalls:
    Index dp by count of houses rather than house index to keep base cases clean.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this before compressing the state to two variables.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i, amount in enumerate(nums, start=1):
            dp[i] = max(dp[i - 1], dp[i - 2] + amount)
        return dp[-1]
