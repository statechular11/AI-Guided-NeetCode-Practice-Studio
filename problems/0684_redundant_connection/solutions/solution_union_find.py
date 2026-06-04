"""
684. Redundant Connection - Return First Edge Whose Endpoints Are Already Connected

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Union-find detects the first edge connecting two already-connected nodes.

    This specific variant uses: return first edge whose endpoints are already connected.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"edges": [[1, 2], [1, 3], [2, 3]]}` and the expected result is `[2, 3]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(E alpha n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    684. Redundant Connection - union find reference Core idea: Edges are added to a tree until one extra edge creates a cycle. The first edge whose endpoints already have the same root is the redundant edge. Complexity: O(E alpha(n)) time, O(n) space.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=list(range(len(edges)+1))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        for a,b in edges:
            ra,rb=find(a),find(b)
            if ra==rb: return [a,b]
            parent[rb]=ra
        return []
