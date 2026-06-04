"""
703. Kth Largest Element in a Stream - size-k min heap

Variant role:
    Primary interview solution. This is the pattern to remember for "track the
    kth largest/smallest while values arrive over time."

Core idea:
    Keep only the k largest values seen so far in a Python min heap.

    The min heap does not store every value. It stores the current top-k
    candidates:

        heap = [the k largest stream values, in heap order]

    Because Python's `heapq` is a min-heap, `heap[0]` is the smallest value
    among those k candidates. The smallest among the k largest values is exactly
    the kth largest overall.

Heap mental model:
    `heap[0]` is the priority root/top, not a queue head or stack top. It is the
    smallest value in the heap because `heapq` implements a min heap.

    - `heapq.heappush(heap, x)` inserts a value and repairs heap order.
    - `heapq.heappop(heap)` removes and returns the root/top priority value.
    - `heapq.heapreplace(heap, x)` removes the root, then inserts x.
    - raw `append`/`pop` are list operations; they do not maintain heap order.

Invariant:
    After construction and after every `add`, `self.heap` contains at most k
    values, and when at least k total stream values have been seen, it contains
    exactly the k largest values seen so far.

Mechanics:
    1. If the heap has fewer than k values, push the new value. We still need
       more candidates before a full top-k set exists.
    2. If the heap already has k values, compare the new value with `heap[0]`.
       - If `val <= heap[0]`, it cannot enter the top k; ignore it.
       - If `val > heap[0]`, it belongs in the top k. Replace the current kth
         largest candidate with `val`.
    3. Return `heap[0]`.

Trace:
    k = 3, nums = [4, 5, 8, 2]

    Build by calling add:
        add(4) -> heap [4]
        add(5) -> heap [4, 5]
        add(8) -> heap [4, 5, 8]
        add(2) -> 2 <= heap[0] = 4, ignore

    Now heap holds the three largest values {4, 5, 8}. The root 4 is the 3rd
    largest.

    add(10):
        10 > 4, replace 4 with 10
        heap holds {5, 8, 10}
        return heap[0] = 5

Common pitfalls:
    - Keeping all values in the heap and assuming `heap[k - 1]` is kth largest.
      Heap order only guarantees the root, not sorted order by index.
    - Using a max heap. A max heap exposes the largest value, but this problem
      needs the boundary between the top k and the rest.
    - Forgetting duplicates count. The kth largest is sorted-order rank, not kth
      distinct value.
    - Calling raw `self.heap.append(val)` after heapifying; use `heappush`.

Complexity:
    Constructor: O(n log k), because each initial value is processed like a
    stream value.
    add: O(log k) when the heap changes, O(1) when a full heap ignores a small
    value.
    Space: O(k).

When to choose this variant:
    Use this as the default interview answer. It is efficient, streaming-safe,
    and directly explains why a min heap is the right priority queue direction.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
