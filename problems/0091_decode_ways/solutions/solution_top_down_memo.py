"""
91. Decode Ways - top-down memoized decoding

Variant role:
    recursive DP reference

Core idea:
    Let dfs(i) be the number of ways to decode the suffix s[i:]. Try one-digit and valid two-digit letters.

Key invariant:
    dfs(i) fully counts every valid decoding of s[i:], independent of how the prefix was decoded.

Mechanics:
    A leading zero has no decodings. Otherwise take one digit, and also take two digits when the value is between 10 and 26.

Common pitfalls:
    The string '06' is invalid as a two-digit letter because encodings cannot start with zero.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this to derive the rolling DP version from a clear suffix-state definition.
"""

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            ways = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                ways += dfs(i + 2)
            return ways

        return dfs(0)
