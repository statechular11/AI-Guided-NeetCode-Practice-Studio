"""
300. Longest Increasing Subsequence - Patience Tails With Binary Search

Variant role:
    optimized primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Quadratic DP is easiest to reason about; patience sorting is the optimized pattern.

    This specific variant uses: patience tails with binary search.

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
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: optimized primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    300. Longest Increasing Subsequence - patience sorting reference Core idea: tails[length-1] stores the smallest possible tail value of an increasing subsequence of that length. For each num, replace the first tail >= num. Smaller tails leave more room for future growth. This returns the length, not necessarily the actual subsequence. Complexity: Time: O(n log n) Space: O(n)
"""

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)
