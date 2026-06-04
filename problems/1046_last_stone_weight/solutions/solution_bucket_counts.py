"""
1046. Last Stone Weight - bucket counts by weight

Variant role:
    Constraint-aware counting variant. The prompt bounds stone weights, so we
    can store frequencies by weight instead of storing each stone in a heap.

Core idea:
    `counts[w]` means "how many stones of weight w remain."

    To follow the game rule, repeatedly remove the heaviest available weight
    twice. If the two removed weights differ, add one stone of weight
    `heaviest - second`.

Why this works:
    The game only cares about stone weights, not stone identities or original
    positions. A frequency table preserves all information needed for the
    simulation:

        individual stones: [2, 7, 4, 1, 8, 1]
        counts: weight 1 -> 2, 2 -> 1, 4 -> 1, 7 -> 1, 8 -> 1

Mechanics:
    1. Count every stone weight.
    2. Track how many stones remain.
    3. Pop the heaviest available weight by scanning downward from the current
       maximum non-empty bucket.
    4. Smash two popped weights and insert the difference if non-zero.
    5. When at most one stone remains, return it or 0.

Trace:
    stones = [2, 7, 4, 1, 8, 1]

    pop 8 and 7 -> add 1
    pop 4 and 2 -> add 2
    pop 2 and 1 -> add 1
    pop 1 and 1 -> add nothing
    remaining weight is 1.

Common pitfalls:
    - Forgetting that a newly created difference may be larger than the current
      downward scan pointer, so the pointer must be updated after insertion.
    - Mishandling equal stones. Equal stones cancel and do not create a zero
      weight stone.
    - Using this pattern when weights are unbounded or huge; then a sparse heap
      is better than a large bucket array.

Complexity:
    Let W be the maximum stone weight.
    Time: O(n * W) in this straightforward scanner, which is fine for small W.
    Space: O(W).

When to choose this variant:
    Use it when the value range is small and bounded. For a general interview
    answer, prefer the max-heap simulation.
"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        counts = [0] * (max_weight + 1)
        for stone in stones:
            counts[stone] += 1

        current = max_weight
        remaining = len(stones)

        def pop_heaviest() -> int:
            nonlocal current, remaining
            while current > 0 and counts[current] == 0:
                current -= 1
            weight = current
            counts[weight] -= 1
            remaining -= 1
            return weight

        while remaining > 1:
            heaviest = pop_heaviest()
            second = pop_heaviest()
            if heaviest != second:
                leftover = heaviest - second
                counts[leftover] += 1
                remaining += 1
                current = max(current, leftover)

        return pop_heaviest() if remaining else 0
