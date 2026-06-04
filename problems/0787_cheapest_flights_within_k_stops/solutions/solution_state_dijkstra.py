"""
787. Cheapest Flights Within K Stops - Dijkstra over node and edge-count state

Variant role:
    alternative constrained-shortest-path reference

Core idea:
    The cheapest route depends on both city and how many flights have been used, so the heap state must include edge count.

Key invariant:
    best[node][edges] is the cheapest known cost to reach node using exactly edges flights.

Mechanics:
    Pop cheapest states first; from a state, push outgoing flights only if edges used is still at most k+1.

Common pitfalls:
    Tracking only best cost per city is wrong because a slightly more expensive route with fewer stops may still be needed.

Complexity:
    Time: O(EK log(VK)); Space: O(VK)

When to choose this variant:
    Use this to contrast with Bellman-Ford limited relaxations and to practice augmented graph state.
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        max_edges = k + 1
        best = [[float("inf")] * (max_edges + 1) for _ in range(n)]
        best[src][0] = 0
        heap = [(0, src, 0)]

        while heap:
            cost, city, edges = heapq.heappop(heap)
            if city == dst:
                return cost
            if edges == max_edges or cost > best[city][edges]:
                continue
            for nxt, price in graph[city]:
                new_cost = cost + price
                new_edges = edges + 1
                if new_cost < best[nxt][new_edges]:
                    best[nxt][new_edges] = new_cost
                    heapq.heappush(heap, (new_cost, nxt, new_edges))

        return -1
