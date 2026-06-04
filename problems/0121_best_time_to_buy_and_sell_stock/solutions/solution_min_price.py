"""
121. Best Time to Buy and Sell Stock - Running Minimum Reference

Return the maximum profit from one buy followed by one later sell.

Variant role:
    Primary optimized interview solution. This is the version to aim for after
    deriving the brute-force pair search.

Core idea:
    Every valid transaction is a pair:

        buy day < sell day
        profit = prices[sell] - prices[buy]

    If today is the sell day, the best possible buy day is simply the cheapest
    price seen before today. We do not need to remember every earlier price;
    only the minimum earlier price can produce the largest profit for today's
    sell price.

First-principles derivation:
    Brute force asks this for every sell day:

        Which earlier buy day gives the best profit?

    For a fixed sell price, maximizing:

        sell_price - buy_price

    means minimizing `buy_price`. So as we scan left to right, we maintain the
    cheapest buy price seen so far.

Sliding-window interpretation:
    Think of `min_price` as the left boundary of a flexible window: it is the
    best buy candidate available before the current sell day. The current index
    is the right boundary, the sell day.

    If today's price is lower than all previous prices, today becomes the new
    best buy candidate for future sell days. It cannot create profit today,
    because buying and selling on the same day is not a useful transaction.

Key invariant:
    Before processing `prices[i]` as a sell price:

        min_price = min(prices[0], prices[1], ..., prices[i - 1])
        best = best profit from all valid pairs ending before i

    Then today's candidate profit is:

        prices[i] - min_price

    After checking that profit, update:

        min_price = min(min_price, prices[i])

    so future days can buy at today's price if it is cheaper.

Step-by-step example:
    prices = [7, 1, 5, 3, 6, 4]

        start:
            min_price = 7
            best = 0

        sell at 1:
            candidate = 1 - 7 = -6 -> best stays 0
            update min_price to 1

        sell at 5:
            candidate = 5 - 1 = 4 -> best becomes 4
            min_price stays 1

        sell at 3:
            candidate = 3 - 1 = 2 -> best stays 4
            min_price stays 1

        sell at 6:
            candidate = 6 - 1 = 5 -> best becomes 5
            min_price stays 1

        sell at 4:
            candidate = 4 - 1 = 3 -> best stays 5

    Return 5.

Why descending prices return 0:
    prices = [7, 6, 4, 3, 1]

    Every candidate profit is negative, so `best` never improves beyond 0.
    Returning 0 means "do not make a losing transaction."

Pitfalls:
    - The buy day must be before the sell day.
    - Do not compute the global minimum and global maximum independently; the
      maximum might appear before the minimum.
    - Update best profit before replacing the buy candidate with today's price
      if your invariant says `min_price` is strictly before the sell day.
    - Returning a negative profit is wrong; the answer is 0 when no profitable
      transaction exists.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews. It is the simplest optimal solution and introduces
    the sliding-window habit of carrying just enough state from the left side to
    answer the question at the right side.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0

        for price in prices[1:]:
            best = max(best, price - min_price)
            min_price = min(min_price, price)

        return best
