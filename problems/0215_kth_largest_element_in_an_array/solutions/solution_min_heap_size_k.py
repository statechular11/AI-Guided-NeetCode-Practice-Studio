"""
215. Kth Largest Element in an Array - size-k min heap

Variant role:
    Primary heap solution. Keep exactly the k largest values seen so far.

Core idea:
    Keep the k largest values seen so far in a min heap. The heap root is the
    smallest among those k values, which is exactly the kth largest overall once
    all numbers have been processed.

Invariant:
    After processing each number, `heap` contains the k largest values from the
    processed prefix, or all processed values if fewer than k have been seen.

    Because the heap contains only those k best candidates, `heap[0]` is the
    weakest candidate still inside the answer set. At the end, that weakest
    kept candidate is the kth largest overall.

Mechanics:
    1. Push numbers until the heap size reaches k.
    2. For each later number:
       - if it is <= heap[0], it cannot beat any kept candidate, so skip it;
       - if it is > heap[0], replace the weakest kept candidate.
    3. Return heap[0].

Example:
    nums = [3, 2, 1, 5, 6, 4], k = 2

    keep [2, 3] after first two numbers, root 2
    see 1 -> skip
    see 5 -> replace 2, keep [3, 5]
    see 6 -> replace 3, keep [5, 6]
    see 4 -> skip

    root is 5, the 2nd largest.

Common pitfalls:
    - This is a min heap, not a max heap. The root is the smallest of the k
      kept largest values.
    - Do not remove duplicates; kth largest is not kth distinct largest.
    - Only replace the root when the new number is strictly greater than it.
      Equal values are already represented correctly by heap size/count.

Complexity:
    Time: O(n log k)
    Space: O(k)

When to choose this variant:
    Use it for the standard heap interview answer, especially when k is much
    smaller than n or when numbers arrive as a stream.
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: list[int] = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
