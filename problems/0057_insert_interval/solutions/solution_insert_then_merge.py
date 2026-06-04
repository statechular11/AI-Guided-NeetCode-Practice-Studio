"""
57. Insert Interval - append then reuse merge intervals

Variant role:
    simple baseline reference

Core idea:
    Insert the new interval into the list, sort everything, then run the regular merge-intervals algorithm.

Key invariant:
    After sorting by start, the output only needs to compare the next interval with the last merged interval.

Mechanics:
    Append a copy of newInterval, sort by start, then either extend the previous interval or start a new one.

Common pitfalls:
    This is intentionally simpler but does extra sorting. The three-phase linear solution uses the fact that input is already sorted.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this as a correctness baseline or when deriving the linear insert-specific method.
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals.sort(key=lambda interval: interval[0])

        merged: list[list[int]] = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
