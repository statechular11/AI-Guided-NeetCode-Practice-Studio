"""
494. Target Sum - memoized sign assignment DFS

Variant role:
    recursive DP reference

Core idea:
    At each index choose +nums[i] or -nums[i], memoizing by index and current sum.

Key invariant:
    dfs(i, total) counts assignments for nums[i:] that lead from current total to target.

Mechanics:
    Branch into adding and subtracting the current number; at the end, count one way only if total equals target.

Common pitfalls:
    Zeros double the number of assignments because +0 and -0 are distinct choices in this problem.

Complexity:
    Time: O(n * sum(nums)); Space: O(n * sum(nums))

When to choose this variant:
    Use this before transforming the problem into subset-sum counting.
"""

from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(index: int, total: int) -> int:
            if index == len(nums):
                return 1 if total == target else 0
            return dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])

        return dfs(0, 0)
