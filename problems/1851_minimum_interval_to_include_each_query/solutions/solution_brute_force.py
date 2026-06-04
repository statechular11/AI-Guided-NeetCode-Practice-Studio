"""
1851. Minimum Interval to Include Each Query - scan all intervals per query

Variant role:
    educational baseline

Core idea:
    For each query, directly inspect every interval and keep the smallest interval length that contains it.

Key invariant:
    best is the shortest containing interval found so far for the current query.

Mechanics:
    For each query q, test start <= q <= end and minimize end - start + 1.

Common pitfalls:
    This is too slow for large input but makes the optimized heap solution's filtering goal clear.

Complexity:
    Time: O(qn); Space: O(1) excl. output

When to choose this variant:
    Use this to understand the query contract before sorting queries and maintaining candidate intervals in a heap.
"""

from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answer: list[int] = []
        for query in queries:
            best = float("inf")
            for start, end in intervals:
                if start <= query <= end:
                    best = min(best, end - start + 1)
            answer.append(-1 if best == float("inf") else int(best))
        return answer
