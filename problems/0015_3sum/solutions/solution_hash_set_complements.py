"""
15. 3Sum - hash set complements reference

Variant role:
    Educational alternative. This is useful if the user already understands
    Two Sum through a hash set and wants to see how that idea can be extended
    to 3Sum. It is not usually the cleanest interview version because duplicate
    handling is less direct than the sorted two-pointer solution.

Core idea:
    Fix one value nums[i]. For the remaining suffix, run a Two Sum style scan:
    keep a set of values already seen for this fixed i, and for each nums[j],
    ask whether the complement needed to reach zero has appeared.

        needed = -(nums[i] + nums[j])

    If needed is in seen, then needed + nums[j] + nums[i] == 0.

Why sort anyway:
    Sorting is still useful even though this variant uses a hash set. It lets us
    put each discovered triplet into a canonical sorted order and skip duplicate
    fixed values. A result set then removes repeated triplets.

Step-by-step:
    1. Sort nums.
    2. For each fixed index i, skip duplicate fixed values.
    3. Create an empty `seen` set for the suffix after i.
    4. For each j > i:
       - compute the value needed to complete the triplet
       - if needed was seen earlier in this suffix, record the sorted triplet
       - add nums[j] to seen
    5. Return the unique triplets stored in the result set.

Example:
    nums = [-1, 0, 1, 2, -1, -4]
    sorted nums = [-4, -1, -1, 0, 1, 2]

    Fix nums[i] = -1. Scanning the suffix:
        j at 0:
            needed = 1, seen = {}
            add 0

        j at 1:
            needed = 0, seen = {0}
            found [-1, 0, 1]

        j at 2:
            needed = -1, seen = {0, 1}
            add 2

    Another fixed -1 can discover [-1, -1, 2], and the result set keeps
    triplets unique.

Tradeoff:
    The primary two-pointer solution has O(1) extra workspace excluding output.
    This hash-set version uses O(n) transient space per fixed value plus a set
    of result tuples. It is still O(n^2) time and is a good bridge from Two Sum,
    but it is less elegant for duplicate handling.

Complexity:
    Time: O(n^2)
    Space: O(n + k), where k is the number of unique output triplets stored in
    the result set.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets: set[tuple[int, int, int]] = set()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen: set[int] = set()
            for j in range(i + 1, len(nums)):
                needed = -(nums[i] + nums[j])
                if needed in seen:
                    triplets.add((nums[i], needed, nums[j]))
                seen.add(nums[j])

        return [list(triplet) for triplet in sorted(triplets)]
