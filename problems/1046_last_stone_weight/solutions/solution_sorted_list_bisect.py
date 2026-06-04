"""
1046. Last Stone Weight - sorted list with binary insertion

Variant role:
    Ordered-list alternative. It avoids sorting the entire list every round by
    keeping the list sorted after each smash.

Core idea:
    Maintain `stones` in increasing order.

    The two heaviest stones are still at the end, so removing them is simple.
    If a leftover stone survives, use `bisect.insort` to put it back in sorted
    position.

Mechanics:
    1. Sort the list once.
    2. Pop the last two values: `heaviest` and `second`.
    3. If they differ, insert `heaviest - second` back into sorted position.
    4. Repeat.

Example:
    stones = [1, 1, 2, 4, 7, 8]

    pop 8 and 7 -> leftover 1
    insort 1 -> [1, 1, 1, 2, 4]

    pop 4 and 2 -> leftover 2
    insort 2 -> [1, 1, 1, 2]

    The list stays sorted without a full re-sort.

Why it works:
    The only value that can disturb sorted order after a round is the leftover
    stone. Inserting that one value back into the correct position restores the
    invariant that the list is sorted.

Complexity detail:
    `bisect` finds the insertion index in O(log n), but Python list insertion
    shifts elements and costs O(n). So this is better organized than repeated
    sorting, but still not as scalable as a heap.

Common pitfalls:
    - Thinking `bisect.insort` makes the whole insertion O(log n); the list
      shift is O(n).
    - Returning the last value without considering the empty-list case.
    - Removing from the front instead of the end of the increasing list.

Complexity:
    Time: O(n^2) from O(n) insertions/shifts over O(n) rounds.
    Space: O(n).

When to choose this variant:
    Use it to connect sorted-array thinking to priority queues. The heap variant
    is the cleaner interview target.
"""

from bisect import insort
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            heaviest = stones.pop()
            second = stones.pop()
            if heaviest != second:
                insort(stones, heaviest - second)
        return stones[0] if stones else 0
