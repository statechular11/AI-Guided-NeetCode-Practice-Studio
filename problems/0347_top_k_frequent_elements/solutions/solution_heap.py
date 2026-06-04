"""
347. Top K Frequent Elements - Heap Reference

Return the k values that appear most frequently.

Variant role:
    Practical interview solution when you naturally reach for a priority queue.

Core idea:
    Count each value, then keep the k largest frequencies using a heap. Python's
    `heapq.nlargest` expresses this directly:

        heapq.nlargest(k, counts.keys(), key=counts.get)

    The keys are the unique values, and the priority is each value's frequency.

Example:
    For:

        nums = [1,1,1,2,2,3]
        k = 2

    counts are:

        1 -> 3
        2 -> 2
        3 -> 1

    so the top two values are 1 and 2.

Heapq note:
    `heapq.nlargest` returns the elements themselves, not `(priority, element)`
    pairs. The `key` function supplies the comparison priority.

Tradeoff:
    This is concise and general, but it has a log factor in k. Bucket sort can
    reach O(n) because frequencies are bounded by n.

Complexity:
    Time:
        O(n log k)

    Space:
        O(n)

When to choose this variant:
    Use it when a priority queue feels natural or when you want a compact Python
    solution. Mention bucket sort as the linear-time optimization.
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
