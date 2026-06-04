"""
1584. Min Cost to Connect All Points - O(N^2) Prim Over Implicit Complete Graph

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is an MST on a complete graph; compute distances lazily in Prim.

    This specific variant uses: O(n^2) Prim over implicit complete graph.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}` and the expected result is `20`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    1584. Min Cost to Connect All Points - Prim MST reference Core idea: Complete graph edge weights are Manhattan distances. Prim's algorithm grows a minimum spanning tree by repeatedly adding the cheapest point outside the tree. This O(n^2) version updates best distance to the tree directly. Complexity: O(n^2) time, O(n) space.
"""

from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points); in_tree=[False]*n; min_dist=[float('inf')]*n; min_dist[0]=0; total=0
        for _ in range(n):
            u=-1
            for i in range(n):
                if not in_tree[i] and (u==-1 or min_dist[i]<min_dist[u]): u=i
            in_tree[u]=True; total+=min_dist[u]
            x1,y1=points[u]
            for v,(x2,y2) in enumerate(points):
                if not in_tree[v]: min_dist[v]=min(min_dist[v], abs(x1-x2)+abs(y1-y2))
        return total
