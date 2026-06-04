"""
338. Counting Bits - Highest Power Offset Dp

Variant role:
    offset recurrence variant. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Build a learning ladder from the prompt's follow-up: Baseline: count each number independently with a bit loop or Kernighan's `value &= value - 1`; this is the easy O(n log n)-style direction. DP by lowest bit: `bits[i] = bits[i >> 1] + (i & 1)`. Shift off the low bit, then add it back. DP by clearing lowest set bit: `bits[i] = bits[i & (i - 1)] + 1`. Clear exactly one 1-bit, then add one. DP by offset/highest power of two: `bits[i] = 1 + bits[i - offset]`, where `offset` is the largest power of two not greater than `i`. Python API contrast: `i.bit_count()` is useful in real Python, but it violates the no-built-in follow-up.

    This specific variant uses: highest power offset DP.

Key invariant:
    Each bit operation changes or inspects a specific binary fact while preserving the other bits needed by later steps.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 2}` and the expected result is `[0, 1, 1]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Include index 0 in the output; `bits[0]` is the base case. The output array itself costs O(n) space. The good DP solutions use O(1) auxiliary state beyond that output. In the low-bit recurrence, `i >> 1` is always smaller than `i`, so the needed answer is already computed. In the offset recurrence, update `offset` exactly when `i` reaches the next power of two. Built-in popcount helpers are fine API knowledge, but they do not satisfy this prompt's follow-up.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: offset recurrence variant. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    338. Counting Bits - Offset DP Reference Return an array where index `i` stores the number of 1 bits in `i`. Core offset idea: Between two powers of two, every number shares the same leading 1. If `offset` is the largest power of two not greater than `i`, then: i = offset + remainder The leading `offset` contributes one set bit, and the remaining bits are the same as `remainder`: bits[i] = 1 + bits[i - offset] Example block: For values from 4 through 7: 4 = 100 -> 1 + bits[0] 5 = 101 -> 1 + bits[1] 6 = 110 -> 1 + bits[2] 7 = 111 -> 1 + bits[3] The block after a power of two repeats the previous counts with one extra leading bit. Updating `offset`: `offset` should change exactly when `i` reaches the next power of two: if offset * 2 == i: offset = i Complexity: Time: O(n), one recurrence per number. Space: O(n) for the required output array, with O(1) auxiliary state. When to choose thi...
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            bits[i] = 1 + bits[i - offset]

        return bits
