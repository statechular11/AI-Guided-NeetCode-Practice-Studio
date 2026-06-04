"""
1046. Last Stone Weight - repeated sorting baseline

Variant role:
    Naive baseline. This version is intentionally simple: each round sorts the
    current stones so the two heaviest are easy to remove.

Core idea:
    If the list is sorted increasing, the two heaviest stones are at the end:

        stones[-1] = heaviest
        stones[-2] = second heaviest

    After smashing them, append the difference if one stone survives. Then sort
    again before the next round.

Mechanics:
    1. Sort the current list.
    2. Pop the largest two values.
    3. If they differ, append their difference.
    4. Repeat until zero or one stone remains.

Trace:
    stones = [2, 7, 4, 1, 8, 1]

    sort -> [1, 1, 2, 4, 7, 8]
    pop 8 and 7, append 1 -> [1, 1, 2, 4, 1]

    sort -> [1, 1, 1, 2, 4]
    pop 4 and 2, append 2 -> [1, 1, 1, 2]

    sort -> [1, 1, 1, 2]
    pop 2 and 1, append 1 -> [1, 1, 1]

    sort -> [1, 1, 1]
    pop 1 and 1 -> [1]

    return 1

Why this is useful:
    It makes the simulation rule obvious before optimizing. The weakness is
    that sorting the whole list every round repeats too much work.

Common pitfalls:
    - Sorting once at the beginning and never restoring order after appending a
      leftover.
    - Appending `0` when equal stones collide.
    - Accidentally subtracting in the wrong order. The heaviest stone is the one
      popped first from the end.

Complexity:
    Time: O(n^2 log n) in the simple analysis, because there can be O(n) rounds
    and each round may sort O(n) stones.
    Space: O(n) for the working list.

When to choose this variant:
    Use it as a correctness baseline or when constraints are tiny. For the
    interview answer, upgrade to the heap variant.
"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(stones)
        while len(stones) > 1:
            stones.sort()
            heaviest = stones.pop()
            second = stones.pop()
            if heaviest != second:
                stones.append(heaviest - second)
        return stones[0] if stones else 0
