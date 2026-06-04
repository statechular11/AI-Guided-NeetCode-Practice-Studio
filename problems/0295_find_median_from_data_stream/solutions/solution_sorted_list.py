"""
295. Find Median from Data Stream - sorted list baseline

Variant role:
    Educational baseline. Keep the full stream sorted after each insertion so
    median lookup is direct.

Core idea:
    If all values are stored in sorted order, the median is just the middle
    index, or the average of the two middle indexes:

        odd length:  values[n // 2]
        even length: (values[n // 2 - 1] + values[n // 2]) / 2

Mechanics:
    1. Use `bisect.insort` to insert each new number into sorted position.
    2. Read the middle value(s) when `findMedian` is called.

Walkthrough:
    Add 5:
        values = [5]
        median = 5

    Add 1:
        values = [1, 5]
        median = (1 + 5) / 2 = 3.0

    Add 3:
        values = [1, 3, 5]
        median = 3

Why it works:
    Maintaining sorted order materializes the exact order statistic after every
    insertion. The tradeoff is insertion cost: Python lists must shift elements
    to make room.

Common pitfalls:
    - Thinking `bisect.insort` is fully O(log n). The search is O(log n), but
      the list insertion shift is O(n).
    - Using the wrong even-length indexes. For length n, the middle pair is
      `n // 2 - 1` and `n // 2`.
    - Treating this as the optimized stream answer. It is simple, not scalable.

Complexity:
    addNum: O(n)
    findMedian: O(1)
    space: O(n)

When to choose this variant:
    Use it to build intuition or when the stream is small. Upgrade to two heaps
    for the main interview solution.
"""

from bisect import insort


class MedianFinder:
    def __init__(self):
        self.values: list[int] = []

    def addNum(self, num: int) -> None:
        # Keep the whole stream sorted so median indexes are direct.
        insort(self.values, num)

    def findMedian(self) -> float:
        size = len(self.values)
        mid = size // 2
        if size % 2:
            return float(self.values[mid])
        return (self.values[mid - 1] + self.values[mid]) / 2
