"""
322. Coin Change - top-down minimum coins DP

Variant role:
    recursive DP reference

Core idea:
    The minimum coins for an amount is one plus the minimum over reachable smaller amounts.

Key invariant:
    dfs(remaining) returns the fewest coins needed to make exactly remaining, or infinity if impossible.

Mechanics:
    Try subtracting every coin from remaining, memoize the result, and convert infinity to -1 at the end.

Common pitfalls:
    Return infinity for negative remaining so invalid branches do not look like good answers.

Complexity:
    Time: O(amount * len(coins)); Space: O(amount)

When to choose this variant:
    Use this to understand the recurrence before filling the bottom-up table.
"""

from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(remaining: int) -> int:
            if remaining == 0:
                return 0
            if remaining < 0:
                return float("inf")
            return 1 + min(dfs(remaining - coin) for coin in coins)

        answer = dfs(amount)
        return -1 if answer == float("inf") else int(answer)
