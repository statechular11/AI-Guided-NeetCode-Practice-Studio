"""
268. Missing Number - Hash Set Baseline

Core idea:
    Store every input value in a set, then scan the full range `[0, n]` and
    return the first value that is not present.

Key invariant:
    `seen` contains exactly the values that appear in `nums`. Since the prompt
    guarantees all values are unique and drawn from `[0, n]`, there is exactly
    one value in the full range that will fail the membership check.

Step-by-step mechanics:
    1. Build `seen = set(nums)`.
    2. Iterate `candidate` from `0` through `len(nums)`, inclusive.
    3. Return the first `candidate` not in `seen`.
    4. The loop must include `n`, because the missing number can be the upper
       endpoint.

Example:
    For `nums = [0, 1]`, `n = 2`.

        seen = {0, 1}
        candidate = 0 -> present
        candidate = 1 -> present
        candidate = 2 -> missing, return 2

Why this works:
    The set gives O(1)-average membership checks, and the prompt's uniqueness
    guarantee means the first absent value in `[0, n]` is not just an absent
    value; it is the only missing value.

Common pitfalls:
    - Scanning only `range(n)`, which misses the valid answer `n`.
    - Treating this as the follow-up solution. It is simple, but it uses O(n)
      extra space.
    - Sorting unnecessarily when the only operation needed is membership.

Complexity:
    Time:
        O(n), to build the set and scan up to `n + 1` candidates.

    Space:
        O(n), for the set of input values.

When to choose this variant:
    Use this as the baseline explanation when first learning the problem or
    when optimizing from a direct membership-check idea toward O(1) space.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for candidate in range(len(nums) + 1):
            if candidate not in seen:
                return candidate
        raise AssertionError("input contract guarantees one missing number")
