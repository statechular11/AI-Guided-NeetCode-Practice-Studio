"""
152. Maximum Product Subarray - Carry Max/Min Product Ending Here

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Track both max and min products because a negative flips signs.

    This specific variant uses: carry max/min product ending here.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [2, 3, -2, 4]}` and the expected result is `6`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    152. Maximum Product Subarray - track max and min reference Core idea: A negative number can turn the smallest product into the largest product. Track both the maximum and minimum product ending at the current index. Transition: Candidates are num alone, num * previous max, and num * previous min. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = best = nums[0]
        for num in nums[1:]:
            a = num * cur_max
            b = num * cur_min
            cur_max = max(num, a, b)
            cur_min = min(num, a, b)
            best = max(best, cur_max)
        return best
