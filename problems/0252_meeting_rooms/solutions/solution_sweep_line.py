"""
252. Meeting Rooms - sweep-line overlap detection

Variant role:
    alternative interval reference

Core idea:
    A person can attend all meetings exactly when the active meeting count never exceeds one.

Key invariant:
    active counts how many meetings are open at the current sweep point.

Mechanics:
    Sort start events after end events at the same timestamp, because a meeting ending at t frees the room for one starting at t.

Common pitfalls:
    For non-overlap, end-before-start tie ordering matters; otherwise back-to-back meetings look like a conflict.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this to connect meeting-room checks to the general sweep-line pattern.
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        events: list[tuple[int, int]] = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort(key=lambda event: (event[0], event[1]))

        active = 0
        for _, delta in events:
            active += delta
            if active > 1:
                return False
        return True
