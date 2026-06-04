"""
338. Counting Bits - Per-Number Kernighan Baseline

Return an array where index `i` stores the number of 1 bits in `i`.

Core idea:
    Count each number independently using Brian Kernighan's bit trick:

        value &= value - 1

    This operation clears the lowest set bit of `value`. Repeating it until the
    number becomes zero counts how many 1 bits were present.

Example:
    For:

        value = 13 = 1101

    The loop clears one set bit at a time:

        1101 -> 1100
        1100 -> 1000
        1000 -> 0000

    The loop ran three times, so 13 has three set bits.

Why this is not the final follow-up solution:
    This approach recomputes each number's count from scratch. It is useful as
    the obvious baseline, but the prompt asks for a linear one-pass improvement.

    The DP references improve this by reusing previous answers:

        bits[i >> 1] + (i & 1)
        bits[i & (i - 1)] + 1
        1 + bits[i - offset]

Complexity:
    Time:
        O(total set bits), often described as O(n log n) for this prompt.

    Space:
        O(n) for the required output array, with O(1) auxiliary state.

When to choose this variant:
    Choose this as the educational baseline before presenting the linear DP
    recurrence.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(value: int) -> int:
            count = 0
            while value:
                value &= value - 1
                count += 1
            return count

        return [count_ones(i) for i in range(n + 1)]
