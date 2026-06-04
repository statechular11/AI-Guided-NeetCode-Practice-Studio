"""
371. Sum of Two Integers - Fixed-Width Full-Adder Scan

Core idea:
    This variant simulates the hardware full-adder directly, one bit position
    at a time. For each bit column, it reads:

        bit from a
        bit from b
        incoming carry

    It writes the result bit and computes the carry that flows into the next
    bit position.

Key invariant:
    Before processing bit position `i`, `carry` is the carry-out from position
    `i - 1`, and `result` already contains the correct answer bits for all
    positions below `i`.

Full-adder identities:
    For one bit position:

        result_bit = bit_a ^ bit_b ^ carry

    A carry goes to the next column when at least two of the three input bits
    are `1`. That can be written without addition as:

        next_carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

    The first term covers both input bits being `1`. The second term covers
    exactly one input bit being `1` while the incoming carry is also `1`.

Step-by-step mechanics:
    1. Mask `a` and `b` to 32 bits so Python behaves like a fixed-width
       two's-complement integer.
    2. For each bit position `0..31`:
       - extract `bit_a` and `bit_b`,
       - compute the output bit with XOR,
       - OR that output bit into `result`,
       - compute the next carry.
    3. Ignore any carry beyond bit 31, matching 32-bit overflow behavior.
    4. Convert the final unsigned 32-bit pattern back into a Python signed
       integer.

Example:
    Add `2 + 3`:

        a = 0010
        b = 0011

        bit 0: 0, 1, carry 0 -> output 1, next carry 0
        bit 1: 1, 1, carry 0 -> output 0, next carry 1
        bit 2: 0, 0, carry 1 -> output 1, next carry 0

    The low bits of the result are `101`, which is `5`.

Why this works:
    This is the same logic as the XOR + carry loop, just viewed at a lower
    level. The loop version lets all bit columns update in parallel each pass;
    this version walks the columns serially and carries state forward.

Common pitfalls:
    - Forgetting that the carry is a single bit in this variant.
    - Using arithmetic `+` to count the three input bits; the problem forbids
      addition, so use boolean/bitwise carry identities instead.
    - Failing to convert the 32-bit unsigned result back to a Python negative
      integer when the sign bit is set.
    - Choosing this as the main interview solution when the XOR + carry loop is
      shorter. This version is best for understanding why the bit identities
      are valid.

Complexity:
    Time:
        O(32), one fixed pass over the 32 bit positions.

    Space:
        O(1).

When to choose this variant:
    Use this as an explanatory reference if the XOR/carry loop feels magical.
    For an actual interview implementation, prefer `solution_bitwise_add.py`.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= mask
        b &= mask
        result = 0
        carry = 0

        for bit in range(32):
            bit_a = (a >> bit) & 1
            bit_b = (b >> bit) & 1

            result_bit = bit_a ^ bit_b ^ carry
            result |= result_bit << bit

            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

        return result if result <= max_int else ~(result ^ mask)
