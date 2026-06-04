"""
190. Reverse Bits - Shift And Append Bits

Variant role:
    primary bit solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Reverse a fixed 32-bit stream, not just the visible bits of the integer. Leading zeros must be processed because they become trailing zeros after reversal. Useful ways to see the same invariant: Shift-accumulate: repeat 32 times, `result = (result << 1) | (n & 1)`, then `n >>= 1`. Direct positions: bit `i` in the input moves to bit `31 - i` in the output. Mask swaps: swap 16-bit halves, then bytes, nibbles, pairs, and individual bits. Many-calls follow-up: cache reversed bytes and combine four byte lookups per call.

    This specific variant uses: shift and append bits.

Key invariant:
    Each bit operation changes or inspects a specific binary fact while preserving the other bits needed by later steps.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 43261596}` and the expected result is `964176192`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Always run exactly 32 iterations or explicitly handle all 32 positions; stopping when `n == 0` drops leading zeros that matter. Return the 32-bit unsigned value. Do not convert answers above `2^31 - 1` into negative Python integers. When using mask swaps in Python, mask intermediate or final values with `0xFFFFFFFF` because Python integers are unbounded. For the repeated-call follow-up, byte caching is easier to explain than trying to memoize every possible 32-bit input.

Complexity:
    Time: O(32); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary bit solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    190. Reverse Bits - Shift-Accumulate Reference Return the 32-bit unsigned integer produced by reversing all 32 bits of `n`. Core bit-stream idea: The input should be treated as a fixed-width 32-bit stream, not as a normal Python integer whose visible representation can stop once the value becomes zero. Reversal means: original bit 0 -> result bit 31 original bit 1 -> result bit 30 ... original bit 31 -> result bit 0 The shift-accumulate method reads the original number from right to left and builds the reversed number from left to right. On each iteration: result = (result << 1) | (n & 1) n >>= 1 `result << 1` makes room for the next incoming bit. `n & 1` extracts the current least-significant bit from the original number. Why exactly 32 iterations matter: Leading zeros in the original number become trailing zeros after reversal. If the loop stops when `n == 0`, those leading zeros ar...
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
