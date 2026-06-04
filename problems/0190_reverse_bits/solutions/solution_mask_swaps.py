"""
190. Reverse Bits - Mask-Swap Reference

Return the 32-bit unsigned integer produced by reversing all 32 bits of `n`.

Core idea:
    Reverse the bit stream by divide-and-conquer. A 32-bit reversal can be
    decomposed into a fixed sequence of swaps:

        1. swap the two 16-bit halves,
        2. inside each 16-bit half, swap its two 8-bit bytes,
        3. inside each byte, swap its two 4-bit nibbles,
        4. inside each nibble, swap its two 2-bit pairs,
        5. inside each pair, swap the two individual bits.

    After those five passes, every bit has moved from original position `i`
    to reversed position `31 - i`.

Why this works:
    Think of the bit positions as a 32-character string:

        abcdefgh ijklmnop qrstuvwx yzABCDEF

    The first pass swaps the left and right 16-bit blocks:

        qrstuvwx yzABCDEF abcdefgh ijklmnop

    That puts each bit in the correct half of the answer, but its order inside
    the half is still not reversed. The next pass swaps 8-bit blocks, then
    4-bit blocks, then 2-bit blocks, then 1-bit blocks. Each pass fixes one
    smaller level of order, like reversing a list by first swapping large
    chunks and then recursively fixing the inside of each chunk.

The general mask-swap pattern:
    For a group size `k`, select the groups that need to move right, select
    the groups that need to move left, shift them by `k`, then combine:

        ((n & HIGH_GROUP_MASK) >> k) | ((n & LOW_GROUP_MASK) << k)

    The two masks are complementary at that group size. They keep neighboring
    chunks separate so the shifts do not smear bits across boundaries.

Step-by-step masks:
    1. 16-bit halves:

           ((n >> 16) | (n << 16)) & 0xFFFFFFFF

       This does not need two masks because there are only two halves. The
       final `& 0xFFFFFFFF` discards any bits shifted beyond the 32-bit window.

    2. 8-bit bytes:

           0xFF00FF00 = 11111111 00000000 11111111 00000000
           0x00FF00FF = 00000000 11111111 00000000 11111111

       The first mask selects the high byte in each 16-bit block and shifts it
       right by 8. The second mask selects the low byte in each 16-bit block
       and shifts it left by 8.

    3. 4-bit nibbles:

           0xF0F0F0F0 selects high nibbles: 1111 0000 ...
           0x0F0F0F0F selects low nibbles:  0000 1111 ...

       Each byte changes from `[high_nibble][low_nibble]` to
       `[low_nibble][high_nibble]`.

    4. 2-bit pairs:

           0xCCCCCCCC = binary pattern 1100 repeated
           0x33333333 = binary pattern 0011 repeated

       Each nibble changes from `[high_pair][low_pair]` to
       `[low_pair][high_pair]`.

    5. Single bits:

           0xAAAAAAAA = binary pattern 1010 repeated
           0x55555555 = binary pattern 0101 repeated

       Each adjacent pair changes from `[left_bit][right_bit]` to
       `[right_bit][left_bit]`.

Concrete mini-trace:
    Focus on one byte after the larger block swaps have put it in the right
    byte position:

        1101 0010

    Nibble swap:

        0010 1101

    Pair swap:

        1000 0111

    Single-bit swap:

        0100 1011

    `01001011` is exactly the reverse of `11010010`.

Why Python needs masking:
    Python integers are arbitrary precision, so `n << 16` can temporarily
    create bits wider than the intended 32-bit unsigned value. Applying
    `& 0xFFFFFFFF` after the half swap, and again before returning, keeps the
    calculation within the 32-bit problem contract.

Common pitfalls:
    - Forgetting that the answer is the unsigned 32-bit bit pattern.
    - Using the right masks but shifting in the wrong direction.
    - Omitting the final 32-bit mask in Python.
    - Treating this as the first solution to explain in an interview; the
      32-step shift-accumulate version is usually easier to derive aloud.

Complexity:
    Time:
        O(1), using a fixed number of bitwise operations.

    Space:
        O(1).

When to choose this variant:
    Choose this as the optimized bit-trick reference, or when the interviewer
    wants a constant-operation solution beyond the straightforward 32-step loop.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        n &= 0xFFFFFFFF
        n = ((n >> 16) | (n << 16)) & 0xFFFFFFFF
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        return n & 0xFFFFFFFF
