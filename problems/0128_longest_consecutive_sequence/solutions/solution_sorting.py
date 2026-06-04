"""
128. Longest Consecutive Sequence - Sorting Reference

Return the length of the longest run of consecutive integer values.

Variant role:
    Learning baseline that is easy to reason about.

Core idea:
    Sort unique values, then scan adjacent numbers. Consecutive values extend
    the current streak; gaps reset it.

Why use `set` before sorting:
    Duplicate values should not break or extend a consecutive sequence. Sorting
    `set(nums)` removes duplicates so the scan only needs to handle true gaps.

Example:
    For:

        [100, 4, 200, 1, 3, 2]

    the unique sorted values are:

        [1, 2, 3, 4, 100, 200]

    The longest streak is:

        1, 2, 3, 4

    with length 4.

Tradeoff:
    Sorting is clear, but it costs O(n log n). The hash-set-starts solution
    reaches O(n) by expanding each sequence only from its smallest value.

Complexity:
    Time:
        O(n log n)

    Space:
        O(n)

When to choose this variant:
    Use it as a baseline when deriving the problem. Then move to the set-start
    invariant for the optimal interview answer.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ordered = sorted(set(nums))
        best = current = 1
        for i in range(1, len(ordered)):
            if ordered[i] == ordered[i - 1] + 1:
                current += 1
            else:
                current = 1
            best = max(best, current)
        return best
