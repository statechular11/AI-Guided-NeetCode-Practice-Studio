"""
309. Best Time to Buy and Sell Stock with Cooldown - top-down DP over day and holding state

Variant role:
    recursive DP reference

Core idea:
    At each day, the decision depends on whether you currently hold a stock and whether selling creates a cooldown skip.

Key invariant:
    dfs(day, holding) returns the best profit from this day onward given the current holding state.

Mechanics:
    If holding, either sell and jump two days or keep holding. If not holding, either buy or skip one day.

Common pitfalls:
    The cooldown is applied after selling, not after buying.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this to derive the iterative three-state solution from explicit decisions.
"""

from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(day: int, holding: bool) -> int:
            if day >= len(prices):
                return 0
            if holding:
                sell = prices[day] + dfs(day + 2, False)
                hold = dfs(day + 1, True)
                return max(sell, hold)
            buy = -prices[day] + dfs(day + 1, True)
            skip = dfs(day + 1, False)
            return max(buy, skip)

        return dfs(0, False)
