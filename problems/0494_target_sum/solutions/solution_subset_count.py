"""
494. Target Sum - Transform Signs To Subset Sum Count

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Convert P-N=target into a subset-sum counting problem.

    This specific variant uses: transform signs to subset-sum count.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [1, 1, 1, 1, 1], "target": 3}` and the expected result is `5`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(n*S); Space: O(S)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    494. Target Sum - subset count transform reference Core idea: Assigning + and - partitions nums into positive sum P and negative sum N. P - N = target and P + N = total, so P = (total + target) / 2. Count subsets with that sum. Complexity: O(n*target_sum) time, O(target_sum) space.
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0
        subset = (total + target) // 2
        dp = [0] * (subset + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[subset]
