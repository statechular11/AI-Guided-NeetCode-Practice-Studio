"""
416. Partition Equal Subset Sum - integer bitset subset-sum DP

Variant role:
    optimized Python state-compression reference

Core idea:
    Represent reachable subset sums as set bits in one integer; shifting left by num adds num to every reachable sum.

Key invariant:
    After processing values, bit s is 1 exactly when sum s is reachable.

Mechanics:
    Start with bit 0 set. For each num, OR the bitset with bitset << num, then test target's bit.

Common pitfalls:
    Only works after confirming total sum is even; otherwise target is not an integer.

Complexity:
    Time: O(n * target / word_size) conceptually; Space: O(target) bits

When to choose this variant:
    Use this to see DP state compression and a Pythonic high-performance subset-sum trick.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        bits = 1
        for num in nums:
            bits |= bits << num
        return ((bits >> target) & 1) == 1
