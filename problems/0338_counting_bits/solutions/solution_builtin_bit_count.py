"""
338. Counting Bits - Python bit_count API Contrast

Return an array where index `i` stores the number of 1 bits in `i`.

Core idea:
    Python integers provide:

        i.bit_count()

    which returns the number of set bits in the binary representation of `i`.

Example:
    For:

        i = 5 = 101

    Python returns:

        5.bit_count() == 2

Why this is included:
    This is useful Python API knowledge and a compact production-style solution.
    It also helps clarify what the problem is asking us to implement manually.

Why this is not the intended interview answer:
    The prompt explicitly asks whether you can solve the problem without a
    built-in popcount function. So this should be treated as a contrast, not as
    the answer to present for the follow-up.

Complexity:
    Time:
        O(n log n) bit-work for arbitrary-size Python integers, though fast in
        practice for the given constraints.

    Space:
        O(n) for the required output array.

When to choose this variant:
    Mention it as Python knowledge. Switch to one of the DP references when the
    interviewer asks for the no-built-in linear solution.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if hasattr(int, "bit_count"):
            return [i.bit_count() for i in range(n + 1)]
        return [bin(i).count("1") for i in range(n + 1)]
