"""
215. Kth Largest Element in an Array - max heap pop k times

Variant role:
    Direct priority-queue simulation. This version mirrors the phrase "kth
    largest" literally: repeatedly remove the current largest value k times.

Core idea:
    Python `heapq` is a min heap, so store negative values to simulate a max
    heap:

        value 6 -> heap item -6
        value 5 -> heap item -5

    The smallest heap item, -6, represents the largest original value, 6.

Mechanics:
    1. Negate every number and heapify once.
    2. Pop from the heap k times.
    3. The kth popped value, after negating back, is the answer.

Example:
    nums = [3, 2, 1, 5, 6, 4], k = 2

    max-heap pops values in this order:

        6, then 5

    The 2nd popped value is 5.

Why it works:
    A max heap returns remaining values from largest to smaller. Counting k
    pops counts duplicate values as separate elements, exactly as the prompt
    requires.

Common pitfalls:
    - Forgetting to negate values back after `heappop`.
    - Using this when k is tiny and n is huge; the size-k min heap stores less.
    - Confusing kth largest with kth distinct largest.

Complexity:
    Time: O(n + k log n). Heapify is O(n), then k pops cost O(log n) each.
    Space: O(n).

When to choose this variant:
    Use it as a clear heap stepping stone. For the primary heap answer, the
    size-k min heap is usually better because it stores only k values.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        kth_largest = 0
        for _ in range(k):
            kth_largest = -heapq.heappop(heap)
        return kth_largest
