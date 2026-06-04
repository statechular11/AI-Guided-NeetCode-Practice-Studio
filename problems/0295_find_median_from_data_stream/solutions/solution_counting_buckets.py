"""
295. Find Median from Data Stream - counting buckets over bounded values

Variant role:
    Constraint-aware / follow-up variant. The prompt asks how to optimize when
    values are in a small range such as [0, 100]. This implementation uses the
    full LeetCode constraint range [-100000, 100000] so it remains correct for
    all local tests, but the idea becomes especially strong when the range is
    tiny.

Core idea:
    Instead of storing every value individually, store counts:

        counts[offset] = how many times value (offset + MIN_VALUE) appeared

    To find the median, locate the kth smallest value by scanning cumulative
    counts.

State meaning:
    - `counts[i]` is the frequency of value `i + MIN_VALUE`.
    - `size` is the number of values added so far.

Mechanics:
    1. On add, increment the bucket for `num`.
    2. For odd size, return the `(size // 2 + 1)`th smallest value.
    3. For even size, average the `(size // 2)`th and `(size // 2 + 1)`th
       smallest values.

Walkthrough:
    Stream: 1, 2, 2, 10

    counts say:
        1 -> 1 time
        2 -> 2 times
        10 -> 1 time

    size = 4, so median is the average of kth values 2 and 3:

        sorted stream = [1, 2, 2, 10]
                         ^  ^
                         2  3

        median = (2 + 2) / 2 = 2.0

Why it works:
    The sorted order can be recovered from cumulative frequencies. Scanning
    counts answers "what value would appear at this sorted position?" without
    storing a sorted list or using heaps.

Common pitfalls:
    - Forgetting to offset negative values before indexing `counts`.
    - Mixing 0-based indexes with kth order statistics. `_kth_smallest(k)` here
      expects k to be 1-based.
    - Using this for a huge value range without considering memory and scan
      cost. The follow-up is attractive because the value range can be tiny.

Complexity:
    Let R be the value range size.
    addNum: O(1)
    findMedian: O(R)
    space: O(R)

When to choose this variant:
    Use it when values are known to come from a small bounded range, such as the
    prompt follow-up [0, 100]. For general streams, prefer two heaps.
"""


class MedianFinder:
    MIN_VALUE = -100000
    MAX_VALUE = 100000
    RANGE_SIZE = MAX_VALUE - MIN_VALUE + 1

    def __init__(self):
        self.counts = [0] * self.RANGE_SIZE
        self.size = 0

    def addNum(self, num: int) -> None:
        # Offset maps the possibly negative value into a non-negative index.
        self.counts[num - self.MIN_VALUE] += 1
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2:
            return float(self._kth_smallest(self.size // 2 + 1))

        left = self._kth_smallest(self.size // 2)
        right = self._kth_smallest(self.size // 2 + 1)
        return (left + right) / 2

    def _kth_smallest(self, k: int) -> int:
        # `k` is 1-based: k=1 asks for the smallest value currently present.
        seen = 0
        for offset, count in enumerate(self.counts):
            seen += count
            if seen >= k:
                return offset + self.MIN_VALUE
        raise RuntimeError("k is outside the number of inserted values")
