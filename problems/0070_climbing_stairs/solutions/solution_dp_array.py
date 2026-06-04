"""
70. Climbing Stairs - full DP table

Variant role:
    first-principles DP baseline

Core idea:
    The number of ways to reach step i is the sum of the ways to reach the two previous steps.

Key invariant:
    dp[i] stores the complete number of ways to land exactly on step i.

Mechanics:
    Seed dp[0] = dp[1] = 1, then fill forward with dp[i] = dp[i-1] + dp[i-2].

Common pitfalls:
    Define whether dp[0] means one way to stand at the bottom. That convention makes the recurrence clean.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this before compressing to the rolling Fibonacci variables.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for step in range(2, n + 1):
            dp[step] = dp[step - 1] + dp[step - 2]
        return dp[n]
