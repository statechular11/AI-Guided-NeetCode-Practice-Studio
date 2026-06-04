"""
97. Interleaving String - Prefix Dp Over Consumed Characters From S1 And S2

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    State is how many characters have been consumed from each source string.

    This specific variant uses: prefix DP over consumed characters from s1 and s2.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s1": "aabcc", "s2": "dbbca", "s3": "aadbbcbcac"}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    97. Interleaving String - 2D DP reference Core idea: dp[i][j] means s3[:i+j] can be formed by interleaving s1[:i] and s2[:j]. The next character can come from s1 or s2 if it matches the corresponding character in s3. Complexity: O(m*n) time and space.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        return dp[m][n]
