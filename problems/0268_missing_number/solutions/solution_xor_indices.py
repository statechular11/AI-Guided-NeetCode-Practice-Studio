"""
268. Missing Number - XOR Indices Reference

Core idea:
    XOR has three identities that make it perfect for "everything appears
    once except one missing value" problems:

        x ^ x = 0
        x ^ 0 = x
        XOR is commutative and associative

    If we XOR all values in the complete range `[0, n]` and also XOR all values
    that actually appear in `nums`, every present value cancels with itself.
    The only value that never gets canceled is the missing number.

Key invariant:
    After processing index `i`, `result` equals:

        n ^ 0 ^ 1 ^ ... ^ i ^ nums[0] ^ nums[1] ^ ... ^ nums[i]

    Starting `result = n` includes the final range value because the loop only
    naturally visits indices `0..n-1`.

Step-by-step mechanics:
    1. Initialize `result = len(nums)` to include the range endpoint `n`.
    2. For each pair `(i, num)`:
       - XOR `i`, representing one expected value from `0..n-1`.
       - XOR `num`, representing one actual input value.
    3. Every value that appears in both the expected range and the input
       cancels out.
    4. Return the leftover value.

Example:
    For `nums = [3, 0, 1]`, `n = 3`.

        result starts as 3
        i = 0, num = 3: result = 3 ^ 0 ^ 3
        i = 1, num = 0: result = 3 ^ 0 ^ 3 ^ 1 ^ 0
        i = 2, num = 1: result = 3 ^ 0 ^ 3 ^ 1 ^ 0 ^ 2 ^ 1

    Reordering the XOR terms shows the cancellations:

        (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2 = 2

Why this works:
    The input has length `n`, while the full range has `n + 1` values. By
    seeding with `n` and then XOR-ing each index and value, we combine exactly
    the full range and exactly the input. Duplicate terms cancel; the missing
    term has no partner.

Common pitfalls:
    - Forgetting to include `n`. If you start with `0`, the case where `n` is
      missing becomes easy to mishandle.
    - Adding instead of XOR-ing. XOR cancellation depends on bitwise identity,
      not arithmetic subtraction.
    - Thinking order matters. XOR can be grouped freely, which is why the
      interleaved index/value loop is equivalent to XOR-ing two whole sets.

Complexity:
    Time:
        O(n), one pass over `nums`.

    Space:
        O(1).

When to choose this variant:
    This is the primary Bit Manipulation answer. It is still O(n)/O(1), avoids
    fixed-width overflow concerns from the sum formula, and reinforces the
    same cancellation idea used in Single Number.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i
            result ^= num
        return result
