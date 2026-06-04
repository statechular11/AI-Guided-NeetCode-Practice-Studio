"""
4. Median of Two Sorted Arrays - Binary Partition Smaller Array

Variant role:
    primary optimized solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The optimized solution searches the partition in the smaller array. The left side must contain half the values and be <= the right side.

    This specific variant uses: binary partition smaller array.

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
    Time: O(log(min(m,n))); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary optimized solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    4. Median of Two Sorted Arrays - binary partition reference Core idea: Partition both arrays so the left partition contains half the total values and every left value is <= every right value. Binary search the partition in the smaller array. Partition condition: max(left parts) <= min(right parts) When valid: - odd total: median is max(left parts) - even total: median is average of max(left parts) and min(right parts) Complexity: Time: O(log(min(m, n))) Space: O(1)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left = float("-inf") if i == 0 else nums1[i - 1]
            nums1_right = float("inf") if i == m else nums1[i]
            nums2_left = float("-inf") if j == 0 else nums2[j - 1]
            nums2_right = float("inf") if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2:
                    return float(max(nums1_left, nums2_left))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            if nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("Input arrays are not sorted as required.")
