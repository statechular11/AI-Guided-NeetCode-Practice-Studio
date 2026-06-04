"""
684. Redundant Connection - incremental DFS cycle check

Variant role:
    alternative graph baseline

Core idea:
    Before adding an edge, check whether its endpoints are already connected; if so, that edge creates a cycle.

Key invariant:
    The graph contains exactly the previously accepted edges and is acyclic before the next edge is considered.

Mechanics:
    For each edge, DFS from u to see whether v is reachable. If reachable, return the edge; otherwise add it.

Common pitfalls:
    This is slower than union-find because connectivity is recomputed from scratch for many edges.

Complexity:
    Time: O(n^2); Space: O(n)

When to choose this variant:
    Use this to make the cycle condition obvious before introducing DSU.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph: dict[int, list[int]] = defaultdict(list)

        def connected(src: int, dst: int, seen: set[int]) -> bool:
            if src == dst:
                return True
            seen.add(src)
            return any(nei not in seen and connected(nei, dst, seen) for nei in graph[src])

        for u, v in edges:
            if u in graph and v in graph and connected(u, v, set()):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []
