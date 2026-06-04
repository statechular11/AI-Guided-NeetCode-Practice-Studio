"""
55. Jump Game - backward goalpost greedy

Variant role:
    alternative optimized greedy reference

Core idea:
    Work backward: if index i can reach the current goal, then reaching i is enough to reach the end.

Key invariant:
    goal is the leftmost index currently known to be able to reach the final position.

Mechanics:
    Start goal at n-1. Scan right to left; whenever i + nums[i] >= goal, move goal to i.

Common pitfalls:
    This answers reachability, not minimum jumps. Do not count moves in this variant.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this when the forward farthest-reach version feels slippery; the goalpost version has a very crisp invariant.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
