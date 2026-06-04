"""
7. Reverse Integer - String Slicing Baseline

Core idea:
    Convert the absolute value to a string, reverse the characters, convert
    back to an integer, reapply the sign, and finally check the 32-bit signed
    range.

Why this is useful:
    This is the clearest way to understand the transformation:

        120 -> "120" -> "021" -> 21
        -123 -> "123" -> "321" -> -321

    It also makes trailing-zero behavior obvious because `int("021")` becomes
    `21`.

Why this is not the primary interview solution:
    The prompt says to assume the environment cannot store 64-bit integers.
    A string solution sidesteps the digit-by-digit overflow issue and builds
    the whole reversed value before checking the range. That is acceptable as a
    baseline in Python, but it does not demonstrate the intended fixed-width
    integer reasoning.

Step-by-step mechanics:
    1. Record the sign.
    2. Convert `abs(x)` to a string.
    3. Reverse the string with slicing.
    4. Convert back to an integer.
    5. Reapply the sign.
    6. Return `0` if the result is outside `[-2^31, 2^31 - 1]`.

Common pitfalls:
    - Trying to reverse the string including the `-` sign.
    - Forgetting that `int("000")` and `int("021")` are valid and naturally
      remove leading zeros.
    - Presenting this as the best answer when the interviewer cares about the
      no-64-bit constraint.

Complexity:
    Time:
        O(d), where `d` is the number of decimal digits.

    Space:
        O(d), because the string representation and reversed string are stored.

When to choose this variant:
    Use this as a baseline or quick Python contrast. For the real interview
    answer, prefer the guarded digit pop/push reference.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_value = int(str(abs(x))[::-1]) * sign
        if -(2**31) <= reversed_value <= 2**31 - 1:
            return reversed_value
        return 0
