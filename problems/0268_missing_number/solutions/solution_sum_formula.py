"""
268. Missing Number - Sum Formula Reference

Core idea:
    The complete range should contain every number from `0` through `n`.
    If no number were missing, its sum would be:

        0 + 1 + 2 + ... + n = n * (n + 1) // 2

    The input contains every number in that range except one. Therefore:

        missing = expected_sum - actual_sum

Key invariant:
    Because the numbers are unique and exactly one value from `[0, n]` is
    absent, every present value contributes once to `actual_sum`, and the only
    contribution missing from the expected total is the answer.

Step-by-step mechanics:
    1. Let `n = len(nums)`. The range is `[0, n]`, not `[0, n - 1]`.
    2. Compute the arithmetic-series sum `n * (n + 1) // 2`.
    3. Subtract `sum(nums)`.
    4. Return the difference.

Example:
    For `nums = [3, 0, 1]`, `n = 3`, so the expected range is
    `[0, 1, 2, 3]`.

        expected_sum = 3 * 4 // 2 = 6
        actual_sum = 3 + 0 + 1 = 4
        missing = 6 - 4 = 2

Why this works:
    This is a conservation argument. The expected range and the input differ
    by exactly one value. Subtracting the input sum from the full-range sum
    cancels all shared values and leaves only the missing one.

Common pitfalls:
    - Using `n * (n - 1) // 2`, which sums `0..n-1` and misses the possible
      answer `n`.
    - Forgetting integer division. In Python, use `//`, not `/`.
    - In fixed-width languages, thinking about overflow. Python integers are
      unbounded, but other languages may prefer XOR to avoid overflow concerns.

Complexity:
    Time:
        O(n), because `sum(nums)` reads each input value once.

    Space:
        O(1), ignoring the input array.

When to choose this variant:
    This is the shortest interview answer when overflow is not a concern. In
    the NeetCode Bit Manipulation section, also know the XOR variant because it
    reaches the same O(n)/O(1) target through cancellation rather than algebra.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
