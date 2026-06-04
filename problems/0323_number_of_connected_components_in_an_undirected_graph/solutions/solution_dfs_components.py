"""
323. Number of Connected Components in an Undirected Graph - DFS component counting

Variant role:
    alternative graph traversal reference

Core idea:
    Every unvisited node starts a new connected component; DFS marks the whole component.

Key invariant:
    After DFS from a start node finishes, every node reachable from that start is marked seen.

Mechanics:
    Build an undirected adjacency list, scan all nodes, and launch DFS only from unseen nodes.

Common pitfalls:
    Include isolated nodes even if they never appear in edges.

Complexity:
    Time: O(V + E); Space: O(V + E)

When to choose this variant:
    Use this as the traversal counterpart to union-find.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen: set[int] = set()

        def dfs(node: int) -> None:
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)

        components = 0
        for node in range(n):
            if node not in seen:
                components += 1
                dfs(node)
        return components
