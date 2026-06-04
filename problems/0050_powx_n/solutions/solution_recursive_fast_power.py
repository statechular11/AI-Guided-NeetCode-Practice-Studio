"""
50. Pow(x, n) - Recursive Fast Power Reference

Core idea:
    Use divide and conquer on the exponent:

        x^n = (x^(n // 2))^2              when n is even
        x^n = (x^(n // 2))^2 * x          when n is odd

    Each recursive call halves the exponent, so the recursion depth is
    O(log |n|).

Key invariant:
    `power(base, exp)` returns `base^exp` for a non-negative integer `exp`.
    The recursion solves the smaller exponent `exp // 2`, then rebuilds the
    answer by squaring the half result and multiplying by one extra `base` only
    when `exp` is odd.

Step-by-step example:
    Compute `2^10`:

        power(2, 10)
        half = power(2, 5)

        power(2, 5)
        half = power(2, 2)

        power(2, 2)
        half = power(2, 1)

        power(2, 1)
        half = power(2, 0) = 1
        odd -> 1 * 1 * 2 = 2

        exp 2 even -> 2 * 2 = 4
        exp 5 odd  -> 4 * 4 * 2 = 32
        exp 10 even -> 32 * 32 = 1024

Negative exponents:
    The helper handles only non-negative exponents. At the top level, convert:

        x^(-n) = 1 / x^n

    by inverting `x` and negating `n` before calling the helper.

Why this works:
    Exponentiation has overlapping structure by powers of two. Squaring
    `x^(n // 2)` accounts for most of the exponent. If `n` is odd, one copy of
    `x` remains and must be multiplied in.

Common pitfalls:
    - Recursing with `n - 1`, which becomes O(n) instead of O(log n).
    - Forgetting the base case `exp == 0`, which should return `1.0`.
    - Handling the negative exponent inside every recursive call instead of
      normalizing once at the top.
    - Computing `power(base, exp // 2)` twice; store it in `half` to avoid
      exponential recursion.

Complexity:
    Time:
        O(log |n|), because each call halves the exponent.

    Space:
        O(log |n|), for the recursion stack.

When to choose this variant:
    Use this when practicing the recursion/divide-and-conquer interpretation.
    In interviews, the iterative binary-exponentiation version is usually a bit
    easier to make stack-safe.
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0

            half = power(base, exp // 2)
            result = half * half
            if exp % 2:
                result *= base
            return result

        if n < 0:
            x = 1 / x
            n = -n

        return power(x, n)
