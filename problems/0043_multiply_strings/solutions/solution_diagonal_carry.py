"""
43. Multiply Strings - Diagonal Carry Accumulation Reference

Core idea:
    Instead of writing every pair product directly into a fixed `m + n` array,
    process the multiplication column by column from right to left.

    Reverse-position indexes make this easier to reason about:

        a = 0 means the ones digit of num1
        b = 0 means the ones digit of num2

    For output column `k`, collect every pair where:

        a + b == k

    because those pairs all contribute to the same decimal place.

Key invariant:
    Before processing column `k`, `carry` is everything that overflowed from
    lower columns. The column total is:

        carry + sum(rev1[a] * rev2[b] for all a + b == k)

    The current output digit is `total % 10`, and the carry for the next column
    is `total // 10`.

Boundary formula:
    If `m = len(num1)` and `n = len(num2)`, then for a fixed column `k`:

        a ranges from max(0, k - (n - 1)) through min(m - 1, k)
        b is k - a

    This keeps both reverse indexes inside their valid digit arrays.

Mini trace:
    For `"123" * "45"`, reversed positions are:

        num1: 3(a=0), 2(a=1), 1(a=2)
        num2: 5(b=0), 4(b=1)

    Column k=0: 3*5
    Column k=1: 2*5 + 3*4
    Column k=2: 1*5 + 2*4
    Column k=3: 1*4

    Each column emits one digit and carries the rest left.

Common pitfalls:
    - Mixing normal string indexes with reversed digit positions.
    - Getting the `a` bounds off by one, especially near the first and last
      columns.
    - Forgetting to add the previous `carry` before taking `divmod`.
    - Appending result digits right-to-left but forgetting to reverse at the end.

Complexity:
    Time:
        O(m * n), because every digit pair appears in exactly one diagonal.

    Space:
        O(m + n), for the output digits and reversed digit arrays.

When to choose this variant:
    Use this as a teaching/reference variant when you want to understand the
    column boundaries deeply. In interviews, the fixed-array `i + j + 1` version
    is usually shorter, but this version makes the carry flow very explicit.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        rev1 = [ord(ch) - ord("0") for ch in reversed(num1)]
        rev2 = [ord(ch) - ord("0") for ch in reversed(num2)]
        m = len(rev1)
        n = len(rev2)

        digits = []
        carry = 0
        for column in range(m + n - 1):
            total = carry
            start = max(0, column - (n - 1))
            end = min(m - 1, column)
            for a in range(start, end + 1):
                b = column - a
                total += rev1[a] * rev2[b]

            carry, digit = divmod(total, 10)
            digits.append(str(digit))

        while carry:
            carry, digit = divmod(carry, 10)
            digits.append(str(digit))

        return "".join(reversed(digits))
