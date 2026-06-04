"""
253. Meeting Rooms II - Start/End Event Sweep

Variant role:
    sweep-line variant. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    A min heap tracks when rooms become free. A sweep line tracks concurrent active meetings.

    This specific variant uses: start/end event sweep.

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
    Use this variant when its role matches the interview goal: sweep-line variant. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    253. Meeting Rooms II - sweep line reference Variant role: Event-count alternative. Starts add one active meeting, ends remove one. The maximum active count is the room count. Complexity: Time: O(n log n) Space: O(n)
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events: list[tuple[int, int]] = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort(key=lambda x: (x[0], x[1]))

        active = best = 0
        for _time, delta in events:
            active += delta
            best = max(best, active)
        return best
