"""
57. Insert Interval - Before/Merge/After Scan

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The clean structure is before-overlap, overlapping merge, after-overlap.

    This specific variant uses: before/merge/after scan.

Key invariant:
    After sorting or sweeping, processed intervals/events are summarized so the algorithm only needs to compare against the active frontier.

Mechanics:
    1. Sort by the field that makes the next decision local.
    2. Maintain the active merged/overlapping/available frontier.
    3. Resolve expired or non-overlapping intervals before adding the current one.
    4. Record the answer from the summarized frontier.

Walkthrough:
    On the local case `example_1`, the input is `{"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]}` and the expected result is `[[1, 5], [6, 9]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by the field that makes the next decision local. Be clear about inclusive versus exclusive endpoints. For meeting rooms, an end time equal to a start time does not overlap. For offline query problems, preserve original query order in the answer.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    57. Insert Interval - three phases reference Core idea: Existing intervals are already sorted and non-overlapping. Process: 1. Add intervals ending before the new interval starts. 2. Merge all intervals overlapping the new interval. 3. Add the remaining intervals. Complexity: Time: O(n) Space: O(n)
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        i = 0
        start, end = newInterval

        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        result.extend(intervals[i:])
        return result
