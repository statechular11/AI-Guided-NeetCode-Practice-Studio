"""
10. Regular Expression Matching - Prefix Dp With Star Zero Or More Transitions

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    `*` either deletes the previous token or consumes one matching character while staying on the same pattern index.

    This specific variant uses: prefix DP with star zero-or-more transitions.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "aa", "p": "a"}` and the expected result is `false`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    10. Regular Expression Matching - DP reference Core idea: dp[i][j] means s[:i] matches p[:j]. A normal character or '.' consumes one character from both strings. A '*' can represent zero copies of the previous token, or one more copy if the previous token matches s[i-1]. Complexity: O(len(s)*len(p)) time and space.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
