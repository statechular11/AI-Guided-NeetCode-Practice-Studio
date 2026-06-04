"""
435. Non-overlapping Intervals - Keep Earliest Ending Intervals

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Equivalent to keeping the maximum number of non-overlapping intervals; earliest end time is the safe greedy choice.

    This specific variant uses: keep earliest-ending intervals.

Key invariant:
    After sorting or sweeping, processed intervals/events are summarized so the algorithm only needs to compare against the active frontier.

Mechanics:
    1. Sort by the field that makes the next decision local.
    2. Maintain the active merged/overlapping/available frontier.
    3. Resolve expired or non-overlapping intervals before adding the current one.
    4. Record the answer from the summarized frontier.

Walkthrough:
    On the local case `example_1`, the input is `{"intervals": [[1, 2], [2, 3], [3, 4], [1, 3]]}` and the expected result is `1`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by the field that makes the next decision local. Be clear about inclusive versus exclusive endpoints. For meeting rooms, an end time equal to a start time does not overlap. For offline query problems, preserve original query order in the answer.

Complexity:
    Time: O(n log n); Space: O(1) extra

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    435. Non-overlapping Intervals - greedy by end time reference Core idea: To keep as many intervals as possible, sort by end time and always keep the interval that ends earliest. Every overlap with the current kept interval must remove the later-ending candidate. Return: removals = total intervals - kept intervals Complexity: Time: O(n log n) Space: O(1) extra after sorting.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        kept = 0
        current_end = float("-inf")

        for start, end in intervals:
            if start >= current_end:
                kept += 1
                current_end = end

        return len(intervals) - kept
