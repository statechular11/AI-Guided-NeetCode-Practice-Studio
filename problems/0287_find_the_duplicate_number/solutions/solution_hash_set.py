"""
287. Find the Duplicate Number - Hash Set Baseline Reference

Find the repeated value by remembering values already seen.

Variant role:
    Baseline set-based solution.

Core idea:
    Scan left to right and remember every value already seen. The first value
    that appears in the set is the duplicate.

Step-by-step:
    1. Create an empty `seen` set.
    2. For each number, check whether it is already in `seen`.
    3. If yes, return it.
    4. Otherwise add it and continue.

Mental trace:
    For:

        [3,1,3,4,2]

    see 3, then 1, then 3 again. Since 3 is already present, return 3.

Constraint tradeoff:
    This is simple and linear, but it uses O(n) extra memory. The problem's
    stricter follow-up asks for constant extra space, which is why Floyd's
    cycle-entry solution is preferred.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Start here if you need a quick correct baseline. Then improve to Floyd or
    binary search because the problem asks for constant extra space.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        raise ValueError("input is guaranteed to contain a duplicate")
