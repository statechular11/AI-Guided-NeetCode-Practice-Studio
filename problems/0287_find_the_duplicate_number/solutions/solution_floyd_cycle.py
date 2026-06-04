"""
287. Find the Duplicate Number - Floyd Cycle Entry Reference

Find the repeated value without modifying the array and using O(1) extra space.

Variant role:
    Optimized primary solution.

Core idea:
    Treat the array as a linked structure where an index points to
    `nums[index]`. Values are in `[1, n]`, so every pointer lands at a valid
    index after the first step. Because there are `n + 1` array positions but
    only `n` possible values, the repeated value becomes the entry point of a
    cycle.

Why the duplicate is a cycle entry:
    Two different positions point to the same value. In the implicit graph
    `index -> nums[index]`, that repeated target has more than one incoming
    edge, which creates the same shape as a linked list with a cycle. The
    duplicate value is the first value reached when entering the cycle.

Step-by-step:
    1. Start `slow` and `fast` at `nums[0]`.
    2. Move `slow` by one value-pointer and `fast` by two until they meet.
    3. Start a `finder` pointer back at `nums[0]`.
    4. Move `finder` and `slow` one step at a time.
    5. Their meeting value is the duplicate.

Mental trace:
    For:

        [1,3,4,2,2]

    the value pointers eventually enter the cycle:

        2 -> 4 -> 2

    The second phase finds the cycle entry:

        2

Pitfall:
    The first slow/fast meeting point proves a cycle exists but is not
    necessarily the duplicate. The reset-and-walk phase is what finds the cycle
    entry.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Lead with this when asked to satisfy both constraints: do not modify the
    array and use constant extra space.
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
        return finder
