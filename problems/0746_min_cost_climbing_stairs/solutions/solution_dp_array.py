"""
746. Min Cost Climbing Stairs - full DP table

Variant role:
    first-principles DP baseline

Core idea:
    The cheapest way to stand on step i comes from either i-1 or i-2 plus that previous step's cost.

Key invariant:
    dp[i] is the minimum cost to reach position i, where position n is the top beyond the last step.

Mechanics:
    Set dp[0] = dp[1] = 0 and fill dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]).

Common pitfalls:
    The top is not a paid step; you pay the cost of the step you leave from.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this before compressing to two rolling costs.
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
