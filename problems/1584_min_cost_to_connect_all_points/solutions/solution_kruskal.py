"""
1584. Min Cost to Connect All Points - Kruskal minimum spanning tree

Variant role:
    alternative MST reference

Core idea:
    Create every Manhattan-distance edge and greedily add the smallest edges that connect different components.

Key invariant:
    The chosen edges are always a subset of some minimum spanning tree by Kruskal's cut property.

Mechanics:
    Sort all pair edges by weight, use DSU to skip edges inside the same component, and stop after n-1 edges.

Common pitfalls:
    This stores all O(n^2) edges, whereas Prim can avoid materializing the full edge list.

Complexity:
    Time: O(n^2 log n); Space: O(n^2)

When to choose this variant:
    Use this to contrast the two classic MST algorithms: Kruskal with DSU and Prim with a growing frontier.
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges: list[tuple[int, int, int]] = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))
        edges.sort()

        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1
            return True

        cost = 0
        used = 0
        for weight, a, b in edges:
            if union(a, b):
                cost += weight
                used += 1
                if used == n - 1:
                    break
        return cost
