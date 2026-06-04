"""
7. Reverse Integer - Guarded Digit Pop/Push Reference

Core idea:
    Reverse the integer the same way you would reverse a stack of decimal
    digits:

        digit = x % 10
        result = result * 10 + digit
        x //= 10

    The important part is checking whether `result * 10 + digit` would overflow
    before performing the push. That matches the prompt's assumption that the
    environment cannot store 64-bit integers.

Key invariant:
    After each loop iteration, `result` contains the reversed suffix of the
    original absolute value, and `x` contains the not-yet-processed prefix.

    Example for `x = 123`:

        result = 0,   x = 123
        result = 3,   x = 12
        result = 32,  x = 1
        result = 321, x = 0

Handling sign:
    Work on `abs(x)` and remember whether the final result should be negative.
    The signed 32-bit range is asymmetric:

        INT_MIN = -2147483648
        INT_MAX =  2147483647

    That means a negative answer is allowed to have absolute value
    `2147483648`, while a positive answer can only reach `2147483647`.

Overflow guard:
    Let `limit` be the largest allowed absolute value:

        2147483647 for positive results
        2147483648 for negative results

    Before pushing a digit, reject when:

        result > limit // 10

    because multiplying by 10 would already exceed the limit.

    Also reject when:

        result == limit // 10 and digit > limit % 10

    because the next digit would cross the boundary. For positive results, the
    final allowed last digit is `7`; for negative results, it is `8`.

Concrete boundary examples:
    `1534236469` reverses toward `9646324351`, which exceeds INT_MAX, so return
    `0`.

    `-8463847412` is outside the input constraints, but it illustrates the
    output boundary: reversing its digits would produce `-2147483648`, which is
    valid because INT_MIN has absolute value one larger than INT_MAX.

Common pitfalls:
    - Checking overflow only after constructing the whole result. That is fine
      in Python, but it ignores the prompt's fixed-width-storage assumption.
    - Forgetting the negative bound allows last digit `8`, not only `7`.
    - Applying `% 10` directly to a negative Python integer. Python's modulo
      behavior differs from some languages, so this reference works with
      `abs(x)` and reapplies the sign at the end.
    - Treating trailing zeros specially. The digit loop naturally drops them:
      `120 -> 21`.

Complexity:
    Time:
        O(d), where `d` is the number of decimal digits.

    Space:
        O(1).

When to choose this variant:
    This is the primary interview solution. It respects the no-64-bit-storage
    spirit by guarding overflow before each push and keeps the state compact.
"""


class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 - 1
        int_min_abs = 2**31
        sign = -1 if x < 0 else 1
        limit = int_max if sign > 0 else int_min_abs
        x = abs(x)
        result = 0

        while x:
            digit = x % 10
            if result > limit // 10 or (
                result == limit // 10 and digit > limit % 10
            ):
                return 0
            result = result * 10 + digit
            x //= 10

        return sign * result
