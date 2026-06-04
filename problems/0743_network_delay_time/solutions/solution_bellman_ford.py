"""
743. Network Delay Time - Bellman-Ford edge relaxation

Variant role:
    alternative shortest-path baseline

Core idea:
    Repeatedly relax every directed edge until shortest paths using up to V-1 edges are known.

Key invariant:
    After i passes, dist[v] is the shortest path to v using at most i edges.

Mechanics:
    Initialize dist[k] = 0 and all others infinity; relax all edges n-1 times; answer is the max finite distance.

Common pitfalls:
    This is slower than Dijkstra for non-negative edges but works as a general edge-relaxation baseline.

Complexity:
    Time: O(VE); Space: O(V)

When to choose this variant:
    Use this to understand shortest-path relaxation before the heap-optimized Dijkstra variant.
"""

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        for _ in range(n - 1):
            changed = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:
                break

        answer = max(dist[1:])
        return -1 if answer == float("inf") else int(answer)
