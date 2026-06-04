"""
213. House Robber II - Reduce Circle To Two Non Circular Robber Runs

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Break the circle by excluding either first or last house.

    This specific variant uses: reduce circle to two non-circular robber runs.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [2, 3, 2]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    213. House Robber II - two linear ranges reference Core idea: The first and last houses are adjacent because the street is circular, so they cannot both be robbed. Solve two ordinary House Robber ranges: exclude the last house, and exclude the first house. Take the max. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(values: List[int]) -> int:
            two_back = one_back = 0
            for amount in values:
                two_back, one_back = one_back, max(one_back, two_back + amount)
            return one_back

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))
