"""
371. Sum of Two Integers - XOR + Carry Reference

Core idea:
    Integer addition can be decomposed into two bit operations:

        a ^ b         gives the carry-free partial sum
        (a & b) << 1  gives the carry bits shifted into the next position

    Repeating those two operations is the same process as grade-school
    addition: write down the current sum bits, move the carries one column to
    the left, and continue until no carry remains.

Key invariant:
    At the start of each loop:

        a = current partial sum without the outstanding carry
        b = outstanding carry that still needs to be added

    The true mathematical sum represented by the pair does not change when we
    replace `(a, b)` with:

        (a ^ b, (a & b) << 1)

    The loop ends when `b == 0`, meaning there are no carry bits left to add.
    At that point, `a` is the final 32-bit result.

Why XOR and AND model addition:
    For a single bit column:

        0 + 0 -> sum bit 0, carry 0
        0 + 1 -> sum bit 1, carry 0
        1 + 0 -> sum bit 1, carry 0
        1 + 1 -> sum bit 0, carry 1

    `a ^ b` exactly matches the sum bit when ignoring carry. `a & b` detects
    the `1 + 1` columns that produce carry. Shifting left moves those carry
    bits into the next column.

Step-by-step example:
    Add `2 + 3`:

        a = 0010
        b = 0011

        partial sum = a ^ b        = 0001
        carry       = (a & b) << 1 = 0100

        a = 0001
        b = 0100

        partial sum = a ^ b        = 0101
        carry       = (a & b) << 1 = 0000

        result = 0101 = 5

Why Python needs a mask:
    In languages with fixed-width signed integers, overflow naturally discards
    bits outside the integer width. Python integers are arbitrary precision, so
    negative values conceptually have infinitely many leading `1` bits. Without
    masking, a negative carry can keep propagating forever.

    The mask:

        0xFFFFFFFF

    limits every intermediate value to 32 bits, matching the usual LeetCode
    two's-complement contract for this problem.

Signed conversion at the end:
    After the loop, `a` is a 32-bit unsigned bit pattern. If it is at most
    `0x7FFFFFFF`, it already represents a non-negative Python integer. If it is
    larger, the high bit is set, so the same 32-bit pattern represents a
    negative two's-complement value.

    This expression converts it back to Python's negative integer:

        ~(a ^ 0xFFFFFFFF)

    Example: `0xFFFFFFFF` becomes `~0`, which is `-1`.

    Algebra proof:
        Python's bitwise NOT obeys:

            ~x == -x - 1

        With `mask = 0xFFFFFFFF = 2^32 - 1`, flipping a masked 32-bit value
        is the same as:

            a ^ mask == mask - a

        Therefore:

            ~(a ^ mask)
            = -((mask - a)) - 1
            = a - mask - 1
            = a - (2^32 - 1) - 1
            = a - 2^32

        That is exactly the signed interpretation of a 32-bit unsigned pattern
        whose sign bit is set.

Common pitfalls:
    - Forgetting to mask inside the loop in Python.
    - Returning the unsigned value directly for negative answers.
    - Using `+` or `-` in helper logic when the problem explicitly forbids
      those operators.
    - Stopping after one XOR/carry pass; carries can cascade across many bits.

Complexity:
    Time:
        O(32), because each iteration moves carries left within a fixed
        32-bit width.

    Space:
        O(1).

When to choose this variant:
    This is the primary interview answer. It is concise once the XOR/carry
    identity is known, and it directly addresses Python's signed-integer
    masking issue.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= mask
        b &= mask
        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        return a if a <= max_int else ~(a ^ mask)
