"""
91. Decode Ways - Prefix Decode Count With One/Two Digit Transitions

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    At each position, add ways from valid single-digit and valid two-digit decodes.

    This specific variant uses: prefix decode count with one/two digit transitions.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "12"}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    91. Decode Ways - rolling DP reference Core idea: dp[i] is the number of ways to decode the prefix s[:i]. A valid one-digit decode contributes dp[i-1]. A valid two-digit decode from 10 to 26 contributes dp[i-2]. Zero handling: '0' cannot stand alone, so it only works as part of 10 or 20. Complexity: Time: O(n) Space: O(1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current += one_back
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += two_back
            two_back, one_back = one_back, current
        return one_back
