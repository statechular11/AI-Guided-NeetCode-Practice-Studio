"""
56. Merge Intervals - sweep-line active interval count

Variant role:
    alternative interval reference

Core idea:
    Treat every start/end as an event. A merged interval begins when active count rises from 0 and ends when it falls back to 0.

Key invariant:
    active is the number of original intervals covering the current sweep position.

Mechanics:
    Sort starts before ends at the same coordinate so touching intervals like [1,4] and [4,5] merge into [1,5].

Common pitfalls:
    Ordering events at the same point matters. If ends came before starts, touching intervals would split incorrectly.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this to connect interval merging with sweep-line thinking; sort-and-merge is shorter for this exact task.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events: list[tuple[int, int]] = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort(key=lambda event: (event[0], -event[1]))

        merged: list[list[int]] = []
        active = 0
        current_start = None
        for point, delta in events:
            if active == 0:
                current_start = point
            active += delta
            if active == 0:
                merged.append([current_start, point])
        return merged
