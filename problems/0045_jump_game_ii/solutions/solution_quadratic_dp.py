"""
45. Jump Game II - quadratic dynamic programming baseline

Variant role:
    educational baseline

Core idea:
    Let dp[i] be the fewest jumps needed to reach index i, then relax every reachable forward edge.

Key invariant:
    After processing index i, every position already reachable through i has the best jump count discovered so far.

Mechanics:
    Initialize dp[0] = 0. For each reachable i, try every next index within nums[i] and minimize dp[next].

Common pitfalls:
    This baseline is easy to reason about but too slow for large inputs; the greedy level method compresses the same reachability layers.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this as the first-principles derivation before learning the O(n) greedy window of reachable indices.
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0

        for i, reach in enumerate(nums):
            if dp[i] == float("inf"):
                continue
            for nxt in range(i + 1, min(n, i + reach + 1)):
                dp[nxt] = min(dp[nxt], dp[i] + 1)

        return int(dp[-1])
