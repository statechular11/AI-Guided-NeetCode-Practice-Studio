"""
703. Kth Largest Element in a Stream - sorted-list baseline

Variant role:
    Baseline solution. It is simpler than the heap solution and useful for
    understanding the rank being requested before optimizing for streaming
    updates.

Core idea:
    Keep every seen value in sorted increasing order.

    If all values are sorted increasing, the kth largest value is at:

        index = len(values) - k

    Example:

        values = [2, 4, 5, 8]
        k = 3
        len(values) - k = 1
        values[1] = 4

    The value 4 is the 3rd largest because the descending order is
    [8, 5, 4, 2].

Mechanics:
    Python's `bisect.insort` finds the sorted insertion point and inserts the
    new value while preserving sorted order.

    This is readable, but insertion into the middle of a Python list shifts
    elements to the right, so each `add` can cost O(n). That is why the heap
    version is the real interview target for a long stream.

Duplicates:
    Duplicates remain as separate entries. This matters because the kth largest
    is not the kth distinct largest.

Trace:
    k = 3, values = [2, 4, 5, 8]

    add(3):
        insert 3 -> [2, 3, 4, 5, 8]
        index = 5 - 3 = 2
        return values[2] = 4

    add(10):
        insert 10 -> [2, 3, 4, 5, 8, 10]
        index = 6 - 3 = 3
        return values[3] = 5

Common pitfalls:
    - Returning `values[k - 1]`, which would be kth smallest in increasing
      order, not kth largest.
    - Removing duplicates. Sorted-order rank counts duplicate values.
    - Thinking `bisect` makes insertion O(log n). The search is O(log n), but
      list insertion is O(n) because elements may shift.

Complexity:
    Constructor: O(n log n) for sorting.
    add: O(n) due to list insertion shifts.
    Space: O(n).

When to choose this variant:
    Use it as a first-principles baseline or when input sizes are tiny. Upgrade
    to the size-k min heap when the stream is long.
"""

from bisect import insort
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.values = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.values, val)
        return self.values[len(self.values) - self.k]
