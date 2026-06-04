"""
56. Merge Intervals - Sort By Start Then Merge

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    After sorting, compare each interval only to the last merged interval.

    This specific variant uses: sort by start then merge.

Key invariant:
    After sorting or sweeping, processed intervals/events are summarized so the algorithm only needs to compare against the active frontier.

Mechanics:
    1. Sort by the field that makes the next decision local.
    2. Maintain the active merged/overlapping/available frontier.
    3. Resolve expired or non-overlapping intervals before adding the current one.
    4. Record the answer from the summarized frontier.

Walkthrough:
    On the local case `example_1`, the input is `{"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}` and the expected result is `[[1, 6], [8, 10], [15, 18]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by the field that makes the next decision local. Be clear about inclusive versus exclusive endpoints. For meeting rooms, an end time equal to a start time does not overlap. For offline query problems, preserve original query order in the answer.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    56. Merge Intervals - sort and merge reference Core idea: Sort intervals by start. The only interval that can overlap the current one is the last merged interval. If they overlap, extend the end; otherwise, start a new merged interval. Complexity: Time: O(n log n) Space: O(n) for the merged output.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged: list[list[int]] = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
