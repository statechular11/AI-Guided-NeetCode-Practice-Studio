"""
215. Kth Largest Element in an Array - sorting baseline

Variant role:
    Simple baseline. This is the easiest way to verify the target value before
    moving to heap or quickselect optimizations.

Core idea:
    If nums is sorted descending, then:

        index 0     -> largest
        index 1     -> 2nd largest
        index k - 1 -> kth largest

    Duplicates count as separate positions. For example, in
    [5, 5, 4], the 2nd largest element is 5, not 4.

Mechanics:
    1. Sort a copy of nums in descending order.
    2. Return `sorted_nums[k - 1]`.

Why it works:
    Sorting materializes the complete order statistic. The kth largest element
    is exactly the value at descending position k - 1.

Common pitfalls:
    - Treating kth largest as kth distinct largest.
    - Using index k instead of k - 1.
    - Mutating `nums` with in-place sort when the caller might expect it intact.

Complexity:
    Time: O(n log n)
    Space: O(n) for sorted copy.

When to choose this variant:
    Use it as a correctness baseline or when the prompt allows sorting. The
    prompt explicitly asks whether you can solve it without sorting, so discuss
    heap or quickselect next.
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]
