"""
70. Climbing Stairs - Rolling Fibonacci Transition

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The transition is Fibonacci: ways to reach current step come from previous one or two steps.

    This specific variant uses: rolling Fibonacci transition.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 2}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    70. Climbing Stairs - Fibonacci DP reference Core idea: To reach step i, the last move came from i-1 or i-2. Therefore ways[i] = ways[i-1] + ways[i-2]. Keep only the previous two values. Complexity: Time: O(n) Space: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(2, n + 1):
            one, two = two, one + two
        return two
