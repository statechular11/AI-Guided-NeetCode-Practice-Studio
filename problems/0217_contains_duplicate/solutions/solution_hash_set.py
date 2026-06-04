"""
217. Contains Duplicate - Hash Set Reference

Return whether any value appears at least twice.

Variant role:
    Primary interview solution.

Core idea:
    Track values seen so far. When a value appears that is already in the set, a
    duplicate has been found immediately.

Invariant:
    Before processing `nums[i]`, `seen` contains exactly the distinct values
    from `nums[0:i]`.

Example:
    For:

        nums = [1, 2, 3, 1]

    after the first three values:

        seen = {1, 2, 3}

    The final 1 is already present, so return True.

Why early return is valid:
    The problem only asks whether any duplicate exists. Once one repeated value
    is found, later values cannot change the answer.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Use this in interviews. It is the clean linear-time solution and states the
    membership invariant directly.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
