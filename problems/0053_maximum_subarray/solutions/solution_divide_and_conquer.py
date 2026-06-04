"""
53. Maximum Subarray - divide and conquer crossing sum

Variant role:
    alternative algorithmic reference

Core idea:
    The best subarray is either entirely left, entirely right, or crosses the midpoint.

Key invariant:
    solve(left, right) returns the best subarray sum inside nums[left:right+1].

Mechanics:
    Recurse on both halves, compute the best suffix ending at mid and best prefix starting at mid+1, and take the maximum of the three candidates.

Common pitfalls:
    The crossing sum must include elements from both sides. Initialize side sums to -infinity so all-negative arrays work.

Complexity:
    Time: O(n log n); Space: O(log n)

When to choose this variant:
    Use this when discussing recurrence thinking. Kadane is the preferred optimized interview solution.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            best_left = solve(left, mid)
            best_right = solve(mid + 1, right)

            total = 0
            best_suffix = float("-inf")
            for i in range(mid, left - 1, -1):
                total += nums[i]
                best_suffix = max(best_suffix, total)

            total = 0
            best_prefix = float("-inf")
            for i in range(mid + 1, right + 1):
                total += nums[i]
                best_prefix = max(best_prefix, total)

            return max(best_left, best_right, best_suffix + best_prefix)

        return solve(0, len(nums) - 1)
