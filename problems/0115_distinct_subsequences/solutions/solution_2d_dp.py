"""
115. Distinct Subsequences - full prefix DP table

Variant role:
    first-principles DP reference

Core idea:
    Count how many ways prefixes of s can form prefixes of t.

Key invariant:
    dp[i][j] is the number of ways s[:i] can form t[:j] as a subsequence.

Mechanics:
    If s[i-1] matches t[j-1], either use it or skip it. If not, only skip it.

Common pitfalls:
    dp[i][0] is 1 for every i because the empty target can always be formed by deleting all characters.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this before compressing to the 1-D DP update that scans target backward.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]
