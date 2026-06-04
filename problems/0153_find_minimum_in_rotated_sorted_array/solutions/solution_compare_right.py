"""
153. Find Minimum in Rotated Sorted Array - Binary Search Against Right Edge

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Compare mid with the right edge to decide whether the rotation point is right of mid or at/before mid.

    This specific variant uses: binary search against right edge.

Key invariant:
    The search interval always contains every still-possible answer. Each midpoint decision removes a side that cannot contain the target answer.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [3, 4, 5, 1, 2]}` and the expected result is `1`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define whether your binary search interval is closed or half-open. For answer-space search, prove the predicate is monotonic. For boundary problems, test empty arrays and values outside the range. For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

Complexity:
    Time: O(log n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    153. Find Minimum in Rotated Sorted Array - compare right reference Core idea: Compare nums[mid] with nums[right]. If nums[mid] is greater, the minimum is to the right of mid. Otherwise, mid may be the minimum, so keep it by moving right to mid. Complexity: Time: O(log n) Space: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
