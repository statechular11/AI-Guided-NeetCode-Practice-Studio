"""
84. Largest Rectangle in Histogram - segment tree divide and conquer.

Variant role:
    Advanced algorithmic alternative, not the usual interview target.

Core idea:
    In any interval `[left, right]`, the largest rectangle is one of:

    1. the rectangle spanning the entire interval using the minimum-height bar
    2. the best rectangle entirely left of that minimum bar
    3. the best rectangle entirely right of that minimum bar

    So if we can quickly find the index of the minimum-height bar in any range,
    we can solve the problem by repeatedly splitting intervals around their
    minimum bar.

Why a segment tree:
    A naive divide-and-conquer implementation scans for the minimum in each
    interval and can degrade to O(n^2), especially for sorted heights. A segment
    tree answers range-minimum-index queries in O(log n), making the whole
    interval-splitting process O(n log n).

Implementation note:
    This version uses an explicit interval stack instead of recursion to avoid
    Python recursion-depth issues on large inputs.

Small trace:
    heights = [2, 1, 5, 6, 2, 3]

    The minimum in the full range is height 1 at index 1:

    - spanning area = 1 * 6 = 6
    - solve left interval [0, 0]
    - solve right interval [2, 5]

    The best right-side interval eventually finds height 5 over width 2, area
    10.

When to choose this variant:
    Use this for learning range-query driven divide and conquer. In interviews,
    prefer the O(n) monotonic stack unless the interviewer explicitly asks for
    alternative approaches.

Complexity:
    Time: O(n log n)
    Space: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        size = 1
        while size < n:
            size *= 2

        tree = [-1] * (2 * size)
        for i in range(n):
            tree[size + i] = i

        def better(left_index: int, right_index: int) -> int:
            if left_index == -1:
                return right_index
            if right_index == -1:
                return left_index
            if heights[left_index] <= heights[right_index]:
                return left_index
            return right_index

        for node in range(size - 1, 0, -1):
            tree[node] = better(tree[2 * node], tree[2 * node + 1])

        def min_index(left: int, right: int) -> int:
            left += size
            right += size
            best_index = -1

            while left <= right:
                if left % 2 == 1:
                    best_index = better(best_index, tree[left])
                    left += 1
                if right % 2 == 0:
                    best_index = better(best_index, tree[right])
                    right -= 1
                left //= 2
                right //= 2

            return best_index

        best = 0
        intervals = [(0, n - 1)]

        while intervals:
            left, right = intervals.pop()
            if left > right:
                continue

            pivot = min_index(left, right)
            best = max(best, heights[pivot] * (right - left + 1))

            if left <= pivot - 1:
                intervals.append((left, pivot - 1))
            if pivot + 1 <= right:
                intervals.append((pivot + 1, right))

        return best
