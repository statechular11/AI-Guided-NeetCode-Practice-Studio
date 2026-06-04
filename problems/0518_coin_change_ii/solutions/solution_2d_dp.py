"""
518. Coin Change II - coin-index and amount DP table

Variant role:
    first-principles combinations-DP reference

Core idea:
    Count combinations by deciding how many coin types are allowed, so order does not create duplicates.

Key invariant:
    dp[i][a] is the number of ways to form amount a using only the first i coin types.

Mechanics:
    For each coin, either skip it or use it once and stay in the same row because coins are unlimited.

Common pitfalls:
    Looping amounts outside coin types can count permutations instead of combinations.

Complexity:
    Time: O(n * amount); Space: O(n * amount)

When to choose this variant:
    Use this to understand the 1-D combinations DP update.
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i, coin in enumerate(coins, start=1):
            for total in range(1, amount + 1):
                dp[i][total] = dp[i - 1][total]
                if total >= coin:
                    dp[i][total] += dp[i][total - coin]
        return dp[-1][amount]
