"""
287. Find the Duplicate Number - Binary Search on Value Counts Reference

Find the repeated value without modifying the array and using O(1) extra space.

Variant role:
    Alternative no-mutation, constant-space solution.

Core idea:
    Binary search the answer value, not an array index. For any `mid`, count how
    many numbers are `<= mid`.

    If that count is greater than `mid`, then too many values fall into the
    range `[1, mid]`, so the duplicate must be in that lower half. Otherwise it
    is in `[mid + 1, n]`.

Why the count test works:
    In a perfect range `1..n` with no duplicate, at most `mid` values can be
    `<= mid`. If more than `mid` input values land there, the pigeonhole
    principle says some lower-half value is duplicated.

Step-by-step:
    1. Search over the value range `[1, len(nums) - 1]`.
    2. Count values less than or equal to the current midpoint.
    3. If the count overflows the available slots, keep the left half.
    4. Otherwise keep the right half.
    5. When the range collapses, the remaining value is the duplicate.

Mental trace:
    For:

        [1,3,4,2,2]

    `mid = 2` gives three values `<= 2`, but only two distinct values fit in
    `[1,2]`, so the duplicate is at most 2.

Pitfall:
    This is not binary search over sorted positions. The array is not sorted;
    only the possible answer range is being searched.

Complexity:
    Time:
        O(n log n)

    Space:
        O(1)

When to choose this variant:
    Useful when Floyd's linked-list interpretation is hard to derive but the
    interviewer still wants no mutation and constant space.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left
