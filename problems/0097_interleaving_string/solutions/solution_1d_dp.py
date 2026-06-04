"""
97. Interleaving String - space-compressed interleaving DP

Variant role:
    optimized-space DP reference

Core idea:
    The 2-D state only needs the previous row and the current row, so keep one row of booleans.

Key invariant:
    dp[j] answers whether s3[:i+j] can be formed by s1[:i] and s2[:j] after processing row i.

Mechanics:
    Update from top (old dp[j]) when taking s1[i-1], and from left (new dp[j-1]) when taking s2[j-1].

Common pitfalls:
    The dp[j] value before assignment is the previous row; dp[j-1] after assignment is the current row.

Complexity:
    Time: O(mn); Space: O(n)

When to choose this variant:
    Use this after the full table is comfortable and you want the memory-optimized version.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        n = len(s2)
        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2

        return dp[n]
