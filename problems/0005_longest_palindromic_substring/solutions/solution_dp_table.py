"""
5. Longest Palindromic Substring - palindrome DP table

Variant role:
    alternative DP reference

Core idea:
    Instead of expanding from centers, precompute whether every substring s[i:j+1] is a palindrome and keep the longest true interval.

Key invariant:
    dp[i][j] is true exactly when s[i:j+1] is a palindrome; shorter inner substrings are computed before longer outer substrings.

Mechanics:
    Process substring lengths from 1 to n. A substring is palindromic when its two ends match and the inside is either empty, one character, or already marked palindromic.

Common pitfalls:
    Iterating by start index first can read dp[i+1][j-1] before it exists. Iterate by length so the dependency is ready.

Complexity:
    Time: O(n^2); Space: O(n^2)

When to choose this variant:
    Use this when you want to expose the interval-DP state behind palindrome problems. Expand-around-center is usually cleaner for this exact problem.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_start = 0
        best_len = 0
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right] and (length <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if length > best_len:
                        best_start = left
                        best_len = length

        return s[best_start:best_start + best_len]
