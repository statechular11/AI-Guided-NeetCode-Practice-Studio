"""
787. Cheapest Flights Within K Stops - K+1 Rounds Of Edge Relaxation

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Copy distances each round to enforce the edge-count limit.

    This specific variant uses: k+1 rounds of edge relaxation.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 4, "flights": [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], "src": 0, "dst": 3, "k": 1}` and the expected result is `700`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(kE); Space: O(V)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    787. Cheapest Flights Within K Stops - limited Bellman-Ford reference Core idea: With at most k stops, we may use at most k+1 edges. Relax all flights k+1 times, always reading from the previous iteration's distances so a single iteration cannot use multiple new edges. Complexity: O(k*E) time, O(V) space.
"""

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF=float('inf'); dist=[INF]*n; dist[src]=0
        for _ in range(k+1):
            nxt=dist[:]
            for u,v,w in flights:
                if dist[u] != INF and dist[u]+w < nxt[v]: nxt[v]=dist[u]+w
            dist=nxt
        return -1 if dist[dst]==INF else dist[dst]
