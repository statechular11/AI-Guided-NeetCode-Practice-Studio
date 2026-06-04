"""
139. Word Break - top-down memoized suffix search

Variant role:
    recursive DP reference

Core idea:
    Let dfs(i) mean whether s[i:] can be segmented into dictionary words.

Key invariant:
    dfs(i) is true exactly when at least one dictionary word matches at i and leaves a breakable suffix.

Mechanics:
    Try every word as the next token, memoizing each start index to avoid recomputing suffixes.

Common pitfalls:
    Without memoization, overlapping suffix states make this exponential.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this to derive the bottom-up prefix DP from an intuitive recursive search.
"""

from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = tuple(wordDict)

        @lru_cache(None)
        def dfs(index: int) -> bool:
            if index == len(s):
                return True
            return any(
                s.startswith(word, index) and dfs(index + len(word))
                for word in words
            )

        return dfs(0)
