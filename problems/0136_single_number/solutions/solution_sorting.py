"""
136. Single Number - Sorting Reference

Return the only value that appears once when every other value appears exactly
twice.

Variant role:
    Sorting and adjacent-pair scan.

Core idea:
    Sorting groups duplicate values next to each other. After sorting, scan in
    pairs; the first position whose neighbor is different is the single value.
    If all earlier pairs match, the last value is the single one.

Step-by-step:
    1. Sort the numbers.
    2. Check indices `0, 2, 4, ...` as pair starts.
    3. If `ordered[i] != ordered[i + 1]`, return `ordered[i]`.
    4. Otherwise skip the matching pair.
    5. If no mismatch appears, return the final value.

Mental trace:
    `[4,1,2,1,2]` sorts to:

        [1,1,2,2,4]

    Pairs `1,1` and `2,2` match, so the last value `4` is the answer.

Constraint tradeoff:
    Sorting makes the structure obvious, but it costs O(n log n) time. The XOR
    solution preserves linear time and constant space.

Complexity:
    Time:
        O(n log n)

    Space:
        O(n) in this non-mutating Python version

When to choose this variant:
    Good for understanding why adjacent pairs matter after sorting, but it
    misses the required linear-time target. Move from this to XOR.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        for i in range(0, len(ordered) - 1, 2):
            if ordered[i] != ordered[i + 1]:
                return ordered[i]
        return ordered[-1]
