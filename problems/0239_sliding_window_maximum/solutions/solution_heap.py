"""
239. Sliding Window Maximum - lazy max-heap

Variant role:
    Practical alternative. This is easier to invent if you already know heaps:
    each window asks for a maximum, so keep a priority queue of seen values and
    discard entries that are no longer inside the window.

Core idea:
    Python has a min-heap, so store (-value, index). The smallest tuple in the
    heap then corresponds to the largest value. The index is required because a
    large value may remain in the heap after its window has moved past it.

Complexity:
    Time: O(n log n). Each index is pushed once and popped at most once.
    Space: O(n) worst case because stale entries may accumulate below the top.

Heap top/root mental model:
    A heap is not a head/tail structure like a deque. It is a list-backed binary
    tree whose priority item is always at heap[0].

    For this problem:
        heap[0] is the top/root candidate for the current maximum.
        heapq.heappush(heap, item) inserts and restores heap order.
        heapq.heappop(heap) removes and returns the top/root item.
        heap.append(...) and heap.pop() are raw list operations; they do not
        provide priority-queue behavior.

Lazy deletion invariant:
    The heap may contain stale entries, but before reading the answer for a
    complete window ending at right, repeatedly remove heap[0] while its index is
    outside the window:

        heap[0].index <= right - k

    After that cleanup, heap[0] is both:
        1. the largest value among all heap entries, and
        2. inside the current window.

    Stale entries below the top do not matter yet. They are removed only if they
    rise to the top later.

Walkthrough 1 - stale top must be deleted:
    nums = [9, 1, 2, 3], k = 2

    Store entries as (-value, index).

    right = 0, value = 9
        push (-9, 0)
        no answer yet because the first full window has not formed

    right = 1, value = 1, window [0..1] = [9, 1]
        push (-1, 1)
        heap[0] is (-9, 0), index 0 is inside the window
        answer = 9

    right = 2, value = 2, window [1..2] = [1, 2]
        push (-2, 2)
        heap[0] is still (-9, 0), but index 0 is expired because:

            heap[0][1] <= right - k
            0 <= 2 - 2

        pop (-9, 0)
        the new heap top is (-2, 2), which is inside the window
        answer = 2

    right = 3, value = 3, window [2..3] = [2, 3]
        push (-3, 3)
        heap[0] is (-3, 3), inside the window
        answer = 3

    Lazy deletion is visible at right = 2: the old 9 stayed in the heap after it
    left the window, but it was removed exactly when it tried to become the
    answer.

Walkthrough 2 - stale entries buried below the top are harmless:
    nums = [1, 3, -1, -3, 5], k = 3

    By right = 2, window [0..2] = [1, 3, -1]
        top is value 3 at index 1
        answer = 3

    By right = 3, window [1..3] = [3, -1, -3]
        index 1 is still inside
        top remains value 3
        answer = 3

    By right = 4, window [2..4] = [-1, -3, 5]
        value 5 at index 4 is pushed
        heap[0] becomes value 5 at index 4
        the old value 3 at index 1 is now expired, but it is below 5
        answer = 5

    The expired 3 does not need to be removed immediately because it is not at
    heap[0]. Only heap[0] can be returned as the maximum. If that expired 3 ever
    rises back to heap[0] later, the while-loop will check its index and remove
    it before returning an answer.

Why lazy deletion is correct:
    Before each answer, the algorithm runs:

        while heap[0][1] <= right - k:
            heapq.heappop(heap)

    After this loop, heap[0] is the largest value among heap entries and is also
    inside the current window. Any stale entries that remain buried below heap[0]
    cannot affect the current answer because they are not the heap top. They are
    postponed, not forgotten.

Why not remove every expired element immediately:
    A binary heap supports fast access to the top, not fast deletion from the
    middle. Lazy deletion keeps the code simple: stale entries are harmless until
    they try to become the answer.

Common pitfalls:
    - Forgetting the negative sign when pushing values into Python's min-heap.
    - Returning heap[0] before removing expired top entries.
    - Storing values without indices, which makes expiration ambiguous.
    - Assuming heap space is O(k). With lazy deletion, stale entries can remain
      buried, so worst-case space is O(n).

When to choose this variant:
    Use it as a fallback or as an intermediate derivation. It is usually accepted
    but not as optimal or as pattern-rich as the monotonic deque.
"""

import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap: list[tuple[int, int]] = []
        result: list[int] = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                result.append(-heap[0][0])

        return result
