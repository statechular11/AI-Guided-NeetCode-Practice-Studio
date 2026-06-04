"""
139. Word Break - Dp Over Segmentable Prefixes

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    dp[i] answers whether the prefix ending at i is segmentable.

    This specific variant uses: dp over segmentable prefixes.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "leetcode", "wordDict": ["leet", "code"]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    139. Word Break - prefix DP reference Core idea: dp[i] means s[:i] can be segmented into dictionary words. For each end i, try dictionary words or split points j; if dp[j] is true and s[j:i] is a word, then dp[i] is true. Complexity: Time: O(n^2) substring checks in the split-point version Space: O(n)
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for end in range(1, len(s) + 1):
            for start in range(end):
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break
        return dp[-1]
