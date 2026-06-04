"""
15. 3Sum - sort and two pointers reference

Variant role:
    Primary interview solution. This is the version to aim for once the sorted
    two-pointer invariant is understood.

Core idea:
    Sort the array. Fix one value, then solve a two-sum problem on the suffix
    using left/right pointers. Skip duplicates for the fixed value and for each
    accepted pair.

Why sorting helps:
    After sorting, moving the left pointer right always makes the pair sum
    larger or equal, and moving the right pointer left always makes the pair sum
    smaller or equal. That gives us a deterministic way to search for the two
    remaining values after fixing nums[i].

Step-by-step:
    1. Sort nums.
    2. Fix nums[i] as the first value of the triplet.
    3. Skip duplicate fixed values so the same triplet family is not repeated.
    4. Use two pointers on the suffix i + 1 ... n - 1.
    5. If the triplet sum is too small, move left right.
    6. If the triplet sum is too large, move right left.
    7. If the sum is zero, record the triplet and skip duplicate second/third
       values before continuing.

Example:
    [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
    Fix -1, then find pairs [ -1, 2 ] and [ 0, 1 ] in the suffix.

Duplicate invariant:
    The result must not contain duplicate triplets. There are three places where
    duplicates matter:

        fixed value: skip nums[i] if it equals nums[i - 1]
        left value: after accepting a triplet, skip repeated nums[left]
        right value: after accepting a triplet, skip repeated nums[right]

When to choose this variant:
    Use this in interviews. It satisfies the O(n^2) target, uses only constant
    extra workspace apart from the output, and naturally explains duplicate
    handling through sorted order.

Complexity:
    Time: O(n^2)
    Space: O(1) extra, excluding output.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: list[list[int]] = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
