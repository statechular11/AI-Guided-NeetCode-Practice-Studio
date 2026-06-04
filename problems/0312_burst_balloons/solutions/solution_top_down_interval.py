"""
312. Burst Balloons - top-down interval DP

Variant role:
    recursive interval-DP reference

Core idea:
    Choose the last balloon burst inside an open interval; its two neighbors are then fixed.

Key invariant:
    dp(left, right) is the best coins obtainable by bursting only balloons strictly between left and right.

Mechanics:
    Pad nums with 1 at both ends. Try every mid between left and right as the last burst, combining left and right subintervals.

Common pitfalls:
    Choosing the first balloon is hard because neighbors change; choosing the last balloon makes boundaries stable.

Complexity:
    Time: O(n^3); Space: O(n^2)

When to choose this variant:
    Use this when the bottom-up interval order is hard to see; memoization lets the recurrence lead.
"""

from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            best = 0
            for mid in range(left + 1, right):
                coins = balloons[left] * balloons[mid] * balloons[right]
                best = max(best, dp(left, mid) + coins + dp(mid, right))
            return best

        return dp(0, len(balloons) - 1)
