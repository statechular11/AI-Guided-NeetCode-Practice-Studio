"""
703. Kth Largest Element in a Stream - heapify then trim

Variant role:
    Alternative heap construction. The `add` method is the same size-k min-heap
    idea as the primary solution, but the constructor demonstrates the
    `heapq.heapify` API and why repeatedly popping the smallest values leaves
    the k largest values behind.

Core idea:
    Start with every initial number in one min heap:

        heapq.heapify(nums_copy)

    Then remove the smallest value until only k values remain. If the heap has
    k values left, those values must be the k largest initial values. The root
    is the smallest among them, so it is the kth largest.

Why trimming works:
    A min heap exposes the current smallest value at `heap[0]`. Any time the
    heap size is greater than k, the smallest value cannot be part of the top k,
    because at least k other values remain after it is removed. So `heappop`
    discards exactly the values outside the top-k set.

Heap shape note:
    After `heapify`, the list is in heap order, not sorted order. Only
    `heap[0]` has a global guarantee. Do not read `heap[1]`, `heap[2]`, or
    `heap[k - 1]` as ranks.

Trace:
    k = 3, nums = [4, 5, 8, 2]

    heapify gives a min heap whose root is 2.
    Since size 4 > k, pop root 2.
    Remaining values are {4, 5, 8}; root 4 is the 3rd largest.

    add(10):
        heap is full and 10 > root 4
        replace 4 with 10
        remaining values are {5, 8, 10}
        root 5 is the 3rd largest.

Common pitfalls:
    - Mutating the caller's `nums` list directly; copy it before heapifying.
    - Assuming `heapify` sorts the list. It only establishes heap invariants.
    - Keeping more than k values after construction; then `heap[0]` would be the
      smallest overall, not kth largest.

Complexity:
    Constructor: O(n) to heapify, then O((n - k) log n) in the worst case to
    trim extra values. Transient space is O(n) for the copied initial list, and
    final heap size is O(k).
    add: O(log k) when the heap changes, O(1) when a full heap ignores a small
    value.

When to choose this variant:
    Use it when you want to practice `heapify` and heap trimming. In an
    interview, the primary stream-style constructor is often simpler to narrate:
    process every value with the same `add` logic.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
