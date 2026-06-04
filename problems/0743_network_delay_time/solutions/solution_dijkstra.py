"""
743. Network Delay Time - Shortest Paths With Min Heap Dijkstra

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The delay is the longest shortest-path distance from the source.

    This specific variant uses: shortest paths with min-heap Dijkstra.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]], "n": 4, "k": 2}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O((V+E)logV); Space: O(V+E)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    743. Network Delay Time - Dijkstra reference Core idea: Edge weights are non-negative, so Dijkstra from source k gives the shortest signal arrival time to every node. The answer is the maximum distance, or -1 if any node is unreachable. Complexity: O((V+E) log V) time, O(V+E) space.
"""

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times: graph[u].append((v,w))
        dist={}; heap=[(0,k)]
        while heap:
            d,u=heapq.heappop(heap)
            if u in dist: continue
            dist[u]=d
            for v,w in graph[u]:
                if v not in dist: heapq.heappush(heap,(d+w,v))
        return max(dist.values()) if len(dist)==n else -1
