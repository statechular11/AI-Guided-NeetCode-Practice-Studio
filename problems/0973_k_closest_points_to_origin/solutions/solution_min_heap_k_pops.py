"""
973. K Closest Points to Origin - heapify all distances, then pop k

Variant role:
    Direct heap simulation. This is the most literal priority-queue version:
    put every point into a min heap by distance, then pop the closest k points.

Core idea:
    We repeatedly need:

        "give me the closest remaining point"

    A min heap gives that point at the root. Unlike 1046, no negation is needed
    because Python's min heap already returns the smallest squared distance.

Mechanics:
    1. Convert each point into `(squared_distance, x, y)`.
    2. Heapify the whole list once in O(n).
    3. Pop k times; each pop returns the next closest point.

Example:
    points = [[1, 3], [-2, 2], [2, -1]], k = 2

    heap items by distance:
        (10, 1, 3)
        (8, -2, 2)
        (5, 2, -1)

    pop -> [2, -1]
    pop -> [-2, 2]

    Return those two points. Their output order is accepted either way.

Why it works:
    Heap order guarantees each pop removes the smallest remaining distance.
    After k pops, exactly the k closest points have been removed.

Common pitfalls:
    - This stores all n points, so it is not as memory-efficient as the size-k
      max heap when k is small.
    - Ties are not a concern for correctness here because the prompt guarantees
      a unique answer set except for output order.
    - Do not use Euclidean square roots; squared distance preserves ordering.

Complexity:
    Time: O(n + k log n). Heapify is O(n), then each pop costs O(log n).
    Space: O(n).

When to choose this variant:
    Use it when you want a simple heap answer and k may not be tiny. If k is
    much smaller than n, the size-k max heap uses less memory. If the interviewer
    asks for optimal average time, discuss quickselect.
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(heap)

        closest = []
        for _ in range(k):
            _dist, x, y = heapq.heappop(heap)
            closest.append([x, y])
        return closest
