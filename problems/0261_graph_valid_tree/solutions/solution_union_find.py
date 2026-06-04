"""
261. Graph Valid Tree - N 1 Edges Plus Union Find Cycle Check

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    A tree has n-1 edges and no cycle.

    This specific variant uses: n-1 edges plus union-find cycle check.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 5, "edges": [[0, 1], [0, 2], [0, 3], [1, 4]]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(E alpha n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    261. Graph Valid Tree - union find reference Core idea: An undirected graph is a tree iff it has exactly n-1 edges and is connected. With n-1 edges, detecting no cycle via union-find is enough. Complexity: O(E alpha(n)) time, O(n) space.
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        parent=list(range(n)); rank=[0]*n
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        for a,b in edges:
            ra,rb=find(a),find(b)
            if ra==rb: return False
            if rank[ra]<rank[rb]: ra,rb=rb,ra
            parent[rb]=ra
            if rank[ra]==rank[rb]: rank[ra]+=1
        return True
