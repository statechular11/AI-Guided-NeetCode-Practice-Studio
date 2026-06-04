"""
72. Edit Distance - Prefix Edit Distance With Insert/Delete/Replace

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The state compares prefixes; mismatches branch into the three edit operations.

    This specific variant uses: prefix edit distance with insert/delete/replace.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"word1": "horse", "word2": "ros"}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    72. Edit Distance - DP table reference Core idea: dp[i][j] is the minimum edits to convert word1[:i] to word2[:j]. If last characters match, inherit dp[i-1][j-1]. Otherwise take one plus insert, delete, or replace. Complexity: O(m*n) time and space.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]
