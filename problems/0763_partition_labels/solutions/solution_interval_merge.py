"""
763. Partition Labels - character intervals then merge

Variant role:
    alternative greedy-interval reference

Core idea:
    Each character demands an interval from its first to last occurrence; partitions are merged character intervals.

Key invariant:
    The current partition end is the farthest last occurrence of any character seen in the partition.

Mechanics:
    Compute first/last indices, sort intervals by start, merge overlaps, and output merged lengths.

Common pitfalls:
    A partition cannot close before every character inside it has reached its final occurrence.

Complexity:
    Time: O(n); Space: O(1) for lowercase alphabet

When to choose this variant:
    Use this if interval merging makes the greedy boundary easier to visualize.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first: dict[str, int] = {}
        last: dict[str, int] = {}
        for i, ch in enumerate(s):
            first.setdefault(ch, i)
            last[ch] = i

        intervals = sorted((first[ch], last[ch]) for ch in first)
        result: list[int] = []
        start, end = intervals[0]
        for left, right in intervals[1:]:
            if left <= end:
                end = max(end, right)
            else:
                result.append(end - start + 1)
                start, end = left, right
        result.append(end - start + 1)
        return result
