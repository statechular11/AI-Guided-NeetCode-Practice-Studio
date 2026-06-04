"""
300. Longest Increasing Subsequence - Lis Ending At Each Index

Variant role:
    baseline DP. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Quadratic DP is easiest to reason about; patience sorting is the optimized pattern.

    This specific variant uses: LIS ending at each index.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [10, 9, 2, 5, 3, 7, 101, 18]}` and the expected result is `4`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: baseline DP. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    300. Longest Increasing Subsequence - quadratic DP reference Core idea: dp[i] is the LIS length ending exactly at i. Look back at every j < i with nums[j] < nums[i] and extend the best such subsequence. Complexity: Time: O(n^2) Space: O(n)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
