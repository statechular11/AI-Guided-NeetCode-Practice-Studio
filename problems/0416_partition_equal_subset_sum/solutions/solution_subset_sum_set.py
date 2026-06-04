"""
416. Partition Equal Subset Sum - Subset Sum Reachable Totals Up To Half Total

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Reduce to subset sum target = total // 2; odd total is immediately impossible.

    This specific variant uses: subset-sum reachable totals up to half total.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [1, 5, 11, 5]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n*target); Space: O(target)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    416. Partition Equal Subset Sum - reachable sums reference Core idea: The array can be split equally only if total is even. Then the question is whether any subset sums to total // 2. Maintain reachable sums and update in descending order via a set of new sums. Complexity: Time: O(n * target) Space: O(target)
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        reachable = {0}
        for num in nums:
            reachable |= {value + num for value in reachable if value + num <= target}
            if target in reachable:
                return True
        return False
