"""
136. Single Number - Hash Set Baseline Reference

Return the only value that appears once when every other value appears exactly
twice.

Variant role:
    Baseline hash-set solution.

Core idea:
    Track unpaired values. When a value appears for the first time, add it to
    the set. When it appears again, remove it. Every duplicate pair is added
    once and removed once, so only the single value remains.

Step-by-step:
    1. Create an empty `unpaired` set.
    2. For each number:
       - remove it if it is already unpaired,
       - otherwise add it as currently unpaired.
    3. Return the only value left in the set.

Mental trace:
    `[2,2,1]`:

        add 2
        remove 2
        add 1

    The remaining set is:

        {1}

Constraint tradeoff:
    This is easy to derive, but it uses O(n) space. The XOR solution compresses
    the same "pair cancellation" idea into one integer accumulator.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Useful as a first correct idea. Then improve to XOR because the prompt asks
    for constant extra space.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unpaired = set()
        for num in nums:
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)

        return next(iter(unpaired))
