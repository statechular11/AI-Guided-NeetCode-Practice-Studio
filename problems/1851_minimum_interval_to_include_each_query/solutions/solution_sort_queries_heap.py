"""
1851. Minimum Interval to Include Each Query - Offline Sorted Queries With Min Heap

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is an offline query problem: sort queries, add intervals as they become eligible, and heap by interval size.

    This specific variant uses: offline sorted queries with min heap.

Key invariant:
    After sorting or sweeping, processed intervals/events are summarized so the algorithm only needs to compare against the active frontier.

Mechanics:
    1. Sort by the field that makes the next decision local.
    2. Maintain the active merged/overlapping/available frontier.
    3. Resolve expired or non-overlapping intervals before adding the current one.
    4. Record the answer from the summarized frontier.

Walkthrough:
    On the local case `example_1`, the input is `{"intervals": [[1, 4], [2, 4], [3, 6], [4, 4]], "queries": [2, 3, 4, 5]}` and the expected result is `[3, 3, 1, 4]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by the field that makes the next decision local. Be clear about inclusive versus exclusive endpoints. For meeting rooms, an end time equal to a start time does not overlap. For offline query problems, preserve original query order in the answer.

Complexity:
    Time: O((n+q) log n); Space: O(n+q)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    1851. Minimum Interval to Include Each Query - sorted queries plus heap reference Core idea: Process queries in increasing order. Add every interval whose start is <= the query to a min heap keyed by interval size. Remove intervals whose end is < query. The heap top is the smallest interval covering the query. Why sort queries: It lets each interval enter the heap once as the query value moves forward. Complexity: Time: O((n + q) log n) Space: O(n + q)
"""

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        indexed_queries = sorted((query, i) for i, query in enumerate(queries))
        result = [-1] * len(queries)
        heap: list[tuple[int, int]] = []
        i = 0

        for query, original_index in indexed_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                result[original_index] = heap[0][0]

        return result
