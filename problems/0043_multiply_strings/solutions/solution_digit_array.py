"""
43. Multiply Strings - Fixed Digit Array Reference

Core idea:
    Simulate grade-school multiplication without converting either input string
    into an integer. The product can have at most `m + n` digits:

        len("999" * "999") <= 3 + 3 = 6

    so allocate a result array of length `m + n` and let every pair of digits
    deposit its contribution into that array.

Key index identity:
    If `num1[i]` and `num2[j]` are multiplied, their single-digit product
    contributes to these two result slots:

        ones/current position: i + j + 1
        carry position:        i + j

    Why `i + j + 1`? In a length `m + n` result array, the rightmost slot is
    the ones place. Two rightmost input digits have indexes `m - 1` and
    `n - 1`, and their product lands at:

        (m - 1) + (n - 1) + 1 = m + n - 1

    which is exactly the rightmost result index.

Mechanics:
    For each pair:

        product = digit1 * digit2 + result[i + j + 1]
        result[i + j + 1] = product % 10
        result[i + j] += product // 10

    The `+ result[i + j + 1]` matters because previous digit pairs may already
    have contributed to the same place. After normalizing that place with
    `% 10`, the carry is added one slot to the left.

Mini trace:
    For `"12" * "34"`, the pair `2 * 4` lands at index 3, the ones place.
    The pair `1 * 4` and `2 * 3` both contribute to index 2, the tens place.
    This is exactly the same column structure as paper multiplication.

Common pitfalls:
    - Using `i + j` as the product's low slot; it should be `i + j + 1`.
    - Forgetting to include the current value already stored in
      `result[i + j + 1]`.
    - Returning leading zeroes after joining the result array.
    - Special-casing zero too late and accidentally returning an empty string.

Complexity:
    Time:
        O(m * n), one multiplication per digit pair.

    Space:
        O(m + n), for the result digit array.

When to choose this variant:
    This is the primary interview solution. The index formula is a little
    fussy, but once memorized it gives a compact, direct implementation.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + result[i + j + 1]
                result[i + j + 1] = product % 10
                result[i + j] += product // 10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        return "".join(str(digit) for digit in result[start:])
