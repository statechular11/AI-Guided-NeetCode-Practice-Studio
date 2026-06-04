"""
1143. Longest Common Subsequence - space-compressed LCS DP

Variant role:
    optimized-space DP reference

Core idea:
    Each LCS row depends only on the previous row, current row left value, and previous diagonal.

Key invariant:
    dp[j] is the LCS length for text1 prefix processed so far and text2[:j].

Mechanics:
    For each char in text1, carry prev_diag while updating dp[j] from left to right.

Common pitfalls:
    Save old dp[j] before overwriting it; that old value becomes the next diagonal.

Complexity:
    Time: O(mn); Space: O(n)

When to choose this variant:
    Use this after the 2-D table is comfortable and you want the interview-ready space optimization.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for ch1 in text1:
            prev_diag = 0
            for j, ch2 in enumerate(text2, start=1):
                old = dp[j]
                if ch1 == ch2:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = old
        return dp[-1]
