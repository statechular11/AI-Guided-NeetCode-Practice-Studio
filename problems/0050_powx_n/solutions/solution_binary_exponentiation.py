"""
50. Pow(x, n) - Iterative Binary Exponentiation Reference

Core idea:
    Compute `x^n` by reading the exponent in binary. Every integer exponent can
    be written as a sum of powers of two:

        n = b0 * 2^0 + b1 * 2^1 + b2 * 2^2 + ...

    where each `bi` is either 0 or 1. That means:

        x^n = product of x^(2^i) for every bit i where bi == 1

    We can generate those powers by repeatedly squaring the base:

        x, x^2, x^4, x^8, ...

    and multiply the answer only when the corresponding exponent bit is set.

Key invariant:
    At the start of each loop:

        result * (base ^ n) == original_x ^ original_abs_n

    where `base` is the current power of `x`, and `n` is the remaining exponent
    bits still to consume. If the low bit of `n` is 1, we move one copy of
    `base` into `result`. Then we square `base` and shift `n` right to examine
    the next bit.

Step-by-step example:
    Compute `2^10`. Since `10` is binary `1010`:

        result = 1, base = 2,  n = 10  even -> skip multiply
        result = 1, base = 4,  n = 5   odd  -> result *= 4
        result = 4, base = 16, n = 2   even -> skip multiply
        result = 4, base = 256,n = 1   odd  -> result *= 256

        result = 1024

    This used the identity:

        2^10 = 2^(8 + 2) = 2^8 * 2^2 = 256 * 4

Negative exponents:
    Use:

        x^(-n) = 1 / x^n

    So for `n < 0`, invert the base and make the exponent positive:

        x = 1 / x
        n = -n

    This is safe under the prompt constraint that either `x` is nonzero or
    `n > 0`; we never need to compute `1 / 0` for a valid input.

Why this is O(log |n|):
    Each loop discards one binary bit with `n >>= 1`. A 32-bit exponent has at
    most 32 relevant bits, so this is dramatically faster than multiplying
    `|n|` times.

Common pitfalls:
    - Using the linear loop `for _ in range(abs(n))`, which can time out for
      large exponents.
    - Forgetting `n == 0`; the loop naturally returns `1.0`.
    - Handling negative `n` after the loop instead of converting first.
    - Multiplying by `base` on every loop instead of only when `n & 1`.
    - Using Python's built-in `pow` or `**`, which defeats the purpose of the
      implementation exercise.

Floating-point note:
    Results are judged with tolerance. The algorithm follows the same
    multiplication order as fast power, so tiny floating-point rounding
    differences are expected and acceptable.

Complexity:
    Time:
        O(log |n|), one iteration per exponent bit.

    Space:
        O(1).

When to choose this variant:
    This is the primary interview answer: iterative, compact, and avoids
    recursion stack concerns.
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        base = x
        while n:
            if n & 1:
                result *= base
            base *= base
            n >>= 1
        return result
