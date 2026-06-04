"""
647. Palindromic Substrings - palindrome DP table

Variant role:
    alternative DP reference

Core idea:
    Count substrings whose endpoints match and whose interior is already known to be palindromic.

Key invariant:
    dp[left][right] is true exactly when s[left:right+1] is a palindrome.

Mechanics:
    Iterate substring lengths from short to long so dp[left+1][right-1] is ready before use.

Common pitfalls:
    Length 1 and length 2 substrings need special handling because their interiors are empty or one character.

Complexity:
    Time: O(n^2); Space: O(n^2)

When to choose this variant:
    Use this to practice interval DP; center expansion is the leaner solution for this problem.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] == s[right] and (length <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    count += 1
        return count
