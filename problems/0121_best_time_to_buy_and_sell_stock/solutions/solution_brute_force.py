"""
121. Best Time to Buy and Sell Stock - Brute Force Baseline

Return the maximum profit from one buy followed by one later sell.

Variant role:
    Educational baseline. This version is too slow for the full constraints,
    but it makes the pair structure of the problem explicit.

Core idea:
    Try every valid transaction:

        buy day < sell day

    For each pair, compute:

        prices[sell] - prices[buy]

    Keep the largest non-negative profit.

Why this is useful:
    The optimized running-min solution comes directly from this baseline.
    Brute force repeatedly asks:

        For this sell day, which earlier buy day is best?

    Since the best earlier buy day is the cheapest earlier price, we can replace
    the inner loop with one running minimum.

Step-by-step example:
    prices = [7, 1, 5]

        buy at 7, sell at 1 -> -6
        buy at 7, sell at 5 -> -2
        buy at 1, sell at 5 -> 4

    The best profit is 4.

Pitfalls:
    - Start `sell` at `buy + 1`; buying and selling on the same day is not a
      valid profitable transaction.
    - Keep `best` initialized to 0 so descending prices return 0.
    - Do not use this as the final interview answer when n can be 100000.

Complexity:
    Time:
        O(n^2)

    Space:
        O(1)

When to choose this variant:
    Use it only to derive the optimized solution or to sanity-check examples.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                best = max(best, prices[sell] - prices[buy])

        return best
