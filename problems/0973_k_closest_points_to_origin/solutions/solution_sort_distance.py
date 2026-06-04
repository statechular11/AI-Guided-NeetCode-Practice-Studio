"""
973. K Closest Points to Origin - sort by squared distance

Variant role:
    Simple baseline / primary readability solution. It is often the first
    correct answer to explain before choosing a heap or quickselect variant.

Core idea:
    A point [x, y] is closer to the origin when:

        sqrt(x^2 + y^2)

    is smaller. Because square root is monotonic, comparing distances is exactly
    the same as comparing squared distances:

        x^2 + y^2

    That avoids floating point work and keeps the key calculation simple.

Mechanics:
    1. Sort every point by squared distance.
    2. Return the first k points.

Example:
    points = [[1, 3], [-2, 2], [2, -1]], k = 2

    squared distances:
        [1, 3]  -> 10
        [-2, 2] -> 8
        [2, -1] -> 5

    sorted by distance -> [[2, -1], [-2, 2], [1, 3]]
    return the first two.

Why it works:
    Sorting imposes the complete distance order. Since the answer is the first k
    points in that order and output order does not matter, slicing the sorted
    list is sufficient.

Common pitfalls:
    - Calling `sqrt`; it is unnecessary and can introduce floating point noise.
    - Sorting by `x + y` or Manhattan distance instead of `x*x + y*y`.
    - Forgetting that the answer can be returned in any order.

Complexity:
    Time: O(n log n)
    Space: O(n) for sorting output/copy.

When to choose this variant:
    Use it when clarity matters most or when n is small enough that full sorting
    is acceptable. For large n with small k, use a size-k heap; for the optimal
    average-time strategy, use quickselect.
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]
