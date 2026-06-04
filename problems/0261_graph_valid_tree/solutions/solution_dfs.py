"""
261. Graph Valid Tree - DFS connected-and-acyclic check

Variant role:
    alternative graph reference

Core idea:
    An undirected graph is a tree iff it is connected and has no cycle.

Key invariant:
    DFS never revisits an already seen node except through the edge back to its parent.

Mechanics:
    Build adjacency, DFS from node 0 with parent tracking, fail on a visited neighbor that is not the parent, then ensure every node was seen.

Common pitfalls:
    Checking only edge count or only connectivity is incomplete unless combined with the tree identity edges == n - 1.

Complexity:
    Time: O(V + E); Space: O(V + E)

When to choose this variant:
    Use this as a traversal alternative to union-find.
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen: set[int] = set()

        def dfs(node: int, parent: int) -> bool:
            if node in seen:
                return False
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n
