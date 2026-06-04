"""
295. Find Median from Data Stream - two heaps

Variant role:
    Primary streaming median solution. This is the interview target because
    each insertion is logarithmic and median lookup is constant time.

Core idea:
    Split numbers into two halves:

    - `low`: max heap for the smaller half, implemented with negative values
    - `high`: min heap for the larger half

    Keep sizes balanced so the median is either the top of one heap or the
    average of both tops.

Two invariants:
    1. Size invariant:

           len(low) == len(high) or len(low) == len(high) + 1

       This implementation lets `low` hold one extra value when the total count
       is odd.

    2. Order invariant:

           every value in low <= every value in high

       Because `low` stores negative numbers, the largest value in the lower
       half is `-low[0]`. The smallest value in the upper half is `high[0]`.

Mechanics of addNum:
    The compact insertion sequence may look odd at first:

        heappush(low, -num)
        heappush(high, -heappop(low))

    Read it as:

        "put the new value into the lower half, then move the largest lower-half
        value into the upper half."

    That transfer repairs the order invariant. If `high` becomes larger than
    `low`, move its smallest value back to `low` to repair the size invariant.

Walkthrough:
    Stream: 1, 2, 3, 4

    Add 1:
        low  = [1]      # stored as [-1]
        high = []
        median = 1

    Add 2:
        low  = [1]
        high = [2]
        median = (1 + 2) / 2 = 1.5

    Add 3:
        low  = [2, 1]
        high = [3]
        median = 2

    Add 4:
        low  = [2, 1]
        high = [3, 4]
        median = (2 + 3) / 2 = 2.5

Why it works:
    The median depends only on the boundary between the lower half and upper
    half. The heaps maintain exactly those boundary values at their roots:

        lower boundary: -low[0]
        upper boundary: high[0]

    There is no need to keep either half fully sorted.

Common pitfalls:
    - Forgetting that `low` is a max heap simulated by negative values.
    - Returning `low[0]` instead of `-low[0]`.
    - Rebalancing sizes but not preserving the order invariant.
    - Letting `high` have more elements than `low` while `findMedian` assumes
      `low` owns the odd-count median.

Complexity:
    addNum: O(log n)
    findMedian: O(1)
    space: O(n)

When to choose this variant:
    Use it for the general data-stream problem where numbers are unbounded or
    only bounded by a large range.
"""

import heapq


class MedianFinder:
    def __init__(self):
        # `low` stores the lower half as negative values: root is max lower.
        self.low: list[int] = []
        # `high` stores the upper half normally: root is min upper.
        self.high: list[int] = []

    def addNum(self, num: int) -> None:
        # First place the new number in the lower half.
        heapq.heappush(self.low, -num)
        # Move the largest lower-half value to the upper half. This preserves
        # the order invariant: every low value <= every high value.
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Keep `low` the same size as `high`, or one element larger. That makes
        # the odd-count median live at -low[0].
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
