"""
435. Non-overlapping Intervals - maximum non-overlapping subset DP

Variant role:
    educational baseline

Core idea:
    Minimizing removals is equivalent to maximizing how many non-overlapping intervals we keep.

Key invariant:
    dp[i] is the largest keepable chain ending at sorted interval i.

Mechanics:
    Sort by end time, then for every previous interval that ends before current starts, extend its chain.

Common pitfalls:
    This solves the same objective but is slower than the greedy earliest-end-time choice.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this as a DP baseline before proving the greedy solution.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[1])
        n = len(intervals)
        dp = [1] * n
        best = 1
        for i in range(n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
            best = max(best, dp[i])
        return n - best
