"""
115. Distinct Subsequences - Subsequence Count Updated Backward Over Target

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Backward target updates prevent one source character from being reused multiple times.

    This specific variant uses: subsequence count updated backward over target.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "rabbbit", "t": "rabbit"}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    115. Distinct Subsequences - 1D DP reference Core idea: dp[j] counts ways to form t[:j] from the processed prefix of s. For each character in s, update j backward so each source character is used at most once in the transition. Complexity: O(len(s)*len(t)) time, O(len(t)) space.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for ch in s:
            for j in range(len(t) - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]
