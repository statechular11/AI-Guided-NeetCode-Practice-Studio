"""
66. Plus One - In-Place Carry From Right Reference

Core idea:
    The array stores digits from most significant to least significant, so the
    `+ 1` operation starts at the rightmost digit.

    There are only two cases at each position:

        digit < 9:
            increment it and return immediately; no carry remains.

        digit == 9:
            it becomes 0 and the carry continues left.

    If every digit is `9`, then every original digit becomes `0` and a new
    leading `1` is needed.

Key invariant:
    While scanning from right to left, every digit to the right of `i` has
    already been finalized. If those finalized digits were trailing 9s, they
    are now 0, and the carry is still 1. As soon as we find a digit below 9,
    adding the carry finishes the whole number.

Step-by-step examples:
    `[1, 2, 3]`:

        last digit 3 < 9 -> increment to 4 -> [1, 2, 4]

    `[1, 2, 9]`:

        9 becomes 0, carry continues
        2 < 9 -> increment to 3 -> [1, 3, 0]

    `[9, 9, 9]`:

        each 9 becomes 0
        carry still remains after the scan
        return [1, 0, 0, 0]

Why this works:
    Decimal addition by one only affects the suffix of trailing 9s and the
    first non-9 digit before that suffix. Digits further left are unchanged.
    That is why the algorithm can return immediately after incrementing the
    first digit below 9.

Common pitfalls:
    - Forgetting the all-9s case, e.g. `[9] -> [1, 0]`.
    - Continuing the scan after incrementing a non-9 digit even though no carry
      remains.
    - Building an integer from the digits. The prompt describes a large integer
      as an array; manual digit carry is the intended pattern.
    - Overthinking leading zeros. The input has no leading zeros, and the only
      new leading digit we ever add is `1`.

Complexity:
    Time:
        O(n) in the worst case when all digits are 9; often less because the
        scan stops at the first non-9 digit.

    Space:
        O(1) extra if mutating the input list is acceptable, ignoring the
        unavoidable output growth in the all-9s case.

When to choose this variant:
    This is the primary interview answer: simple, in-place, and tailored to the
    fact that the addend is exactly one.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
