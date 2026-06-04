"""
312. Burst Balloons - Choose Last Balloon Inside Interval

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Choosing the last balloon in an interval makes neighboring values fixed.

    This specific variant uses: choose last balloon inside interval.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [3, 1, 5, 8]}` and the expected result is `167`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(n^3); Space: O(n^2)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    312. Burst Balloons - interval DP reference Core idea: Instead of choosing the first balloon to burst, choose the last balloon left inside an interval. If k is last in (left, right), the gained coins are nums[left] * nums[k] * nums[right] plus the best results of the two inner intervals. Complexity: O(n^3) time, O(n^2) space.
"""

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], dp[left][k] + arr[left] * arr[k] * arr[right] + dp[k][right])
        return dp[0][n - 1]
