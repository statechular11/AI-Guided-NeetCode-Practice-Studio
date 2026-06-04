"""
268. Missing Number - Sort + Binary Search Reference

Core idea:
    After sorting, the complete prefix before the missing value lines up with
    its indices:

        nums[i] == i

    Once the missing value is passed, every remaining value is shifted one
    position to the right:

        nums[i] > i

    That monotonic split lets us binary-search for the first index where
    `nums[i] != i`.

Key invariant:
    In sorted order, all values are unique and lie in `[0, n]`.

    - If `nums[mid] == mid`, then every value up through `mid` is present, so
      the missing number must be to the right.
    - If `nums[mid] != mid`, then `mid` itself is missing or the missing value
      is even earlier, so search left.

Step-by-step mechanics:
    1. Sort the array so value/index alignment has meaning.
    2. Binary-search the first mismatch between value and index.
    3. Return the left boundary after the search.

Example:
    For `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`, sorting gives:

        [0, 1, 2, 3, 4, 5, 6, 7, 9]

    Indices `0..7` match their values. At index `8`, the value is `9`, so the
    first mismatch is `8`, which is the missing number.

Why this works:
    Before the missing number, every smaller value exists and occupies its own
    index after sorting. After the missing number, the array is missing one
    smaller value, so each later value appears one index later than it would in
    a complete array. That creates a monotonic predicate:

        nums[i] == i    -> missing value is to the right
        nums[i] != i    -> missing value is at `i` or to the left

Common pitfalls:
    - Returning `nums[left]` instead of `left`. The missing value is the first
      mismatched index.
    - Forgetting the all-matched case. If sorted nums is `[0, 1, ..., n - 1]`,
      the missing value is `n`, and the search ends with `left == n`.
    - Sorting in place when the caller expects `nums` preserved. LeetCode does
      not care here, but `sorted(nums)` keeps this reference side-effect free.
    - Choosing this for the follow-up. It is useful for the Binary Search tag,
      but the O(n) XOR and sum variants are better for the stated follow-up.

Complexity:
    Time:
        O(n log n), dominated by sorting. The binary search is O(log n).

    Space:
        O(n) for `sorted(nums)` in this side-effect-free version. An in-place
        sort would use O(1) or O(log n) auxiliary space depending on language
        and sort implementation, but it would mutate the input.

When to choose this variant:
    Use this when practicing the sorted-index invariant or the Binary Search
    tag. In an interview focused on the follow-up, prefer XOR or sum formula.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        left = 0
        right = len(ordered)

        while left < right:
            mid = (left + right) // 2
            if ordered[mid] == mid:
                left = mid + 1
            else:
                right = mid

        return left
