"""
347. Top K Frequent Elements - bucket sort reference

Variant role:
    Primary optimized solution and the key technique this problem is designed to
    teach.

Core idea:
    A value can appear only 1 through n times. Create buckets where bucket[f]
    stores all values that appear exactly f times. Then scan buckets from high
    frequency to low frequency until k values have been collected.

Walkthrough:
    nums = [1,1,1,2,2,3], k = 2

    counts:
        1 -> 3
        2 -> 2
        3 -> 1

    buckets:
        bucket[3] = [1]
        bucket[2] = [2]
        bucket[1] = [3]

    Scan from bucket[6] down. Collect 1, then 2.

Why order does not matter:
    The problem accepts the top k elements in any order, and the local comparator
    treats this result as unordered.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        result: list[int] = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
