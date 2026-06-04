"""
746. Min Cost Climbing Stairs - Rolling Min Cost To Reach Recent Steps

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The top can be reached from either of the last two steps, so return the min of both states.

    This specific variant uses: rolling min cost to reach recent steps.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"cost": [10, 15, 20]}` and the expected result is `15`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    746. Min Cost Climbing Stairs - rolling DP reference Core idea: The cost to reach the top from step i depends on the cheaper of starting from i-1 or i-2. Rolling two values gives the minimum cost to reach each next position. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_back = 0
        one_back = 0
        for c in cost:
            two_back, one_back = one_back, min(one_back, two_back) + c
        return min(one_back, two_back)
