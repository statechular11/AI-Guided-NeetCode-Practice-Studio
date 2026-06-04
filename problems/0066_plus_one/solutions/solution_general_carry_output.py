"""
66. Plus One - General Carry Output Array Reference

Core idea:
    Simulate addition from right to left with an explicit carry and build a new
    result array. This is slightly more general than the in-place shortcut:

        carry, digit = divmod(digits[i] + carry, 10)

    For Plus One, the initial carry is `1`, but the same pattern also prepares
    you for problems like Add Binary or Add to Array-Form of Integer.

Key invariant:
    After processing position `i`, `result_reversed` contains the finalized
    output digits for the suffix `digits[i:]`, stored from least significant to
    most significant. `carry` is the value that must be added into the next
    more significant position.

Step-by-step example:
    For `[1, 2, 9]`:

        carry = 1

        9 + 1 = 10 -> append 0, carry 1
        2 + 1 = 3  -> append 3, carry 0
        1 + 0 = 1  -> append 1, carry 0

        result_reversed = [0, 3, 1]
        reverse it -> [1, 3, 0]

All-9s example:
    For `[9, 9]`:

        9 + 1 = 10 -> append 0, carry 1
        9 + 1 = 10 -> append 0, carry 1
        carry remains -> append 1
        reverse -> [1, 0, 0]

Why this works:
    This is ordinary column addition. Each output digit is the current column
    sum modulo 10, and the carry is the current column sum divided by 10.

Common pitfalls:
    - Forgetting to append the final carry.
    - Returning the reversed working list without reversing it back.
    - Using this when the in-place shortcut would be simpler; it is excellent
      for learning carry mechanics, but not the shortest Plus One solution.

Complexity:
    Time:
        O(n), one pass over the digits plus reversing the result.

    Space:
        O(n), because this variant builds a separate output list.

When to choose this variant:
    Use this when you want the most transferable carry template. For the
    smallest Plus One implementation, prefer the in-place carry-from-right
    reference.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result_reversed = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            carry, digit = divmod(digits[i] + carry, 10)
            result_reversed.append(digit)

        if carry:
            result_reversed.append(carry)

        return result_reversed[::-1]
