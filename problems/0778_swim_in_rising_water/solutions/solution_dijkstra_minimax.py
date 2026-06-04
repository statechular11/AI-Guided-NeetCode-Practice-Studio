"""
778. Swim in Rising Water - Dijkstra Where Path Cost Is Max Elevation Along Path

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is shortest path under a minimax path cost.

    This specific variant uses: Dijkstra where path cost is max elevation along path.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"grid": [[0, 2], [1, 3]]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(n^2 log n); Space: O(n^2)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    778. Swim in Rising Water - minimax Dijkstra reference Core idea: The cost of a path is the maximum elevation seen along it. Use a min-heap by current path cost; when the target is popped, that cost is the minimum possible water level. Complexity: O(n^2 log n) time, O(n^2) space.
"""

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid); seen={(0,0)}; heap=[(grid[0][0],0,0)]
        while heap:
            t,r,c=heapq.heappop(heap)
            if r==n-1 and c==n-1: return t
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen:
                    seen.add((nr,nc)); heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))
