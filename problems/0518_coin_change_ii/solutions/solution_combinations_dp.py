"""
518. Coin Change II - Coin Outer Loop Counts Order Insensitive Combinations

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Coin outer loop avoids counting different orders of the same combination.

    This specific variant uses: coin outer loop counts order-insensitive combinations.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"amount": 5, "coins": [1, 2, 5]}` and the expected result is `4`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(amount*coins); Space: O(amount)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    518. Coin Change II - combinations DP reference Core idea: dp[a] counts combinations to make amount a. Iterate coins outside and amounts increasing inside so each combination is counted once regardless of order. Complexity: O(amount * coins) time, O(amount) space.
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
