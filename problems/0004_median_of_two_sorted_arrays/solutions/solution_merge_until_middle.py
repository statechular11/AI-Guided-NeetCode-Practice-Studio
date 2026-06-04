"""
4. Median of Two Sorted Arrays - Merge To Middle

Variant role:
    learning baseline. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The optimized solution searches the partition in the smaller array. The left side must contain half the values and be <= the right side.

    This specific variant uses: merge to middle.

Key invariant:
    The search interval always contains every still-possible answer. Each midpoint decision removes a side that cannot contain the target answer.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums1": [1, 3], "nums2": [2]}` and the expected result is `2.0`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define whether your binary search interval is closed or half-open. For answer-space search, prove the predicate is monotonic. For boundary problems, test empty arrays and values outside the range. For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

Complexity:
    Time: O(m+n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: learning baseline. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    4. Median of Two Sorted Arrays - merge until middle reference Variant role: Learning baseline. Merge just enough values to know the middle element(s). Complexity: Time: O(m + n) Space: O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        need = total // 2
        i = j = 0
        prev = curr = 0

        for _ in range(need + 1):
            prev = curr
            if j >= len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2:
            return float(curr)
        return (prev + curr) / 2
