"""
10. Regular Expression Matching - top-down memoized pattern matching

Variant role:
    recursive DP reference

Core idea:
    View matching as a decision at positions (i, j): does s[i:] match p[j:]? Memoization keeps the recursive branching from exploding.

Key invariant:
    match(i, j) answers the full suffix question for s[i:] and p[j:], so every recursive call has the same precise contract.

Mechanics:
    If p[j+1] is '*', either consume zero copies of p[j] or consume one matching character and stay on the same pattern position. Otherwise consume one character from both strings.

Common pitfalls:
    The star applies to the previous pattern character, not to itself. The zero-copy branch must be tried even when the current string character matches.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this when the bottom-up table feels hard to derive. It mirrors the grammar of '.' and '*' directly.
"""

from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_matches = i < len(s) and p[j] in {s[i], "."}

            if j + 1 < len(p) and p[j + 1] == "*":
                return match(i, j + 2) or (first_matches and match(i + 1, j))

            return first_matches and match(i + 1, j + 1)

        return match(0, 0)
