"""
253. Meeting Rooms II - Min Heap Of Room End Times

Variant role:
    primary heap solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    A min heap tracks when rooms become free. A sweep line tracks concurrent active meetings.

    This specific variant uses: min heap of room end times.

Key invariant:
    After sorting or sweeping, processed intervals/events are summarized so the algorithm only needs to compare against the active frontier.

Mechanics:
    1. Sort by the field that makes the next decision local.
    2. Maintain the active merged/overlapping/available frontier.
    3. Resolve expired or non-overlapping intervals before adding the current one.
    4. Record the answer from the summarized frontier.

Walkthrough:
    On the local case `example_1`, the input is `{"intervals": [[0, 30], [5, 10], [15, 20]]}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by the field that makes the next decision local. Be clear about inclusive versus exclusive endpoints. For meeting rooms, an end time equal to a start time does not overlap. For offline query problems, preserve original query order in the answer.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary heap solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    253. Meeting Rooms II - min heap of end times reference Core idea: Sort meetings by start time. Keep a min heap of room end times. If the earliest-ending room is free before the next meeting starts, reuse it; otherwise allocate a new room. Complexity: Time: O(n log n) Space: O(n)
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms: list[int] = []

        for start, end in intervals:
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

        return len(rooms)
