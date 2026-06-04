"""
217. Contains Duplicate - Sorting Reference

Return whether any value appears at least twice.

Variant role:
    Space-conscious comparison point.

Core idea:
    If equal values exist, they become adjacent after sorting. Scan neighboring
    pairs and return True when two adjacent values match.

Why sorting reveals duplicates:
    Sorting groups equal values into one contiguous block. A duplicate exists if
    and only if at least one neighboring pair in the sorted order is equal.

Example:
    For:

        [1, 2, 3, 1]

    sorting gives:

        [1, 1, 2, 3]

    The adjacent 1s reveal the duplicate.

Tradeoff:
    Sorting can use less explicit auxiliary data, but it costs O(n log n) time.
    This implementation uses `sorted(nums)` to avoid mutating the input, so it
    allocates a sorted copy.

Complexity:
    Time:
        O(n log n)

    Space:
        O(n) in Python when using `sorted(nums)`; in-place sorting would mutate.

When to choose this variant:
    Use it as a comparison point when discussing the time/space tradeoff. The
    hash-set version is the usual primary answer because it is O(n) time.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ordered = sorted(nums)
        return any(ordered[i] == ordered[i - 1] for i in range(1, len(ordered)))
