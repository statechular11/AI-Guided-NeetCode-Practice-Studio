"""
322. Coin Change - Minimum Coins For Every Amount Prefix

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Use an impossible sentinel larger than any valid coin count.

    This specific variant uses: minimum coins for every amount prefix.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"coins": [1, 2, 5], "amount": 11}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(amount*coins); Space: O(amount)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    322. Coin Change - bottom-up DP reference Core idea: dp[a] is the fewest coins needed to make amount a. For each amount, try each coin and use dp[a - coin] + 1 when the coin fits. Complexity: Time: O(amount * number_of_coins) Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1
        dp = [0] + [impossible] * amount
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        return -1 if dp[amount] == impossible else dp[amount]
