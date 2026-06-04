"""
323. Number of Connected Components in an Undirected Graph - Decrease Component Count On Successful Union

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Union-find tracks component merges without building traversal adjacency.

    This specific variant uses: decrease component count on successful union.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 5, "edges": [[0, 1], [1, 2], [3, 4]]}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(E alpha n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    323. Number of Connected Components - union find reference Core idea: Start with n components. Each successful union between two different roots merges two components and decreases the count by one. Complexity: O(E alpha(n)) time, O(n) space.
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n)); rank=[0]*n; count=n
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        for a,b in edges:
            ra,rb=find(a),find(b)
            if ra==rb: continue
            if rank[ra]<rank[rb]: ra,rb=rb,ra
            parent[rb]=ra
            if rank[ra]==rank[rb]: rank[ra]+=1
            count-=1
        return count
