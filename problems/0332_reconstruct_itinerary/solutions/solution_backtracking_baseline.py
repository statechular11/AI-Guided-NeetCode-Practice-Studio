"""
332. Reconstruct Itinerary - lexicographic backtracking baseline

Variant role:
    educational baseline

Core idea:
    Try tickets in lexical order and stop at the first route that uses every ticket exactly once.

Key invariant:
    path is always a valid prefix built from distinct used tickets.

Mechanics:
    Sort tickets, track used ticket indices, and recursively extend only tickets whose source equals the current airport.

Common pitfalls:
    This is too slow for large inputs; Hierholzer's algorithm is the optimized Eulerian-path solution.

Complexity:
    Time: O(E! * E) worst case; Space: O(E)

When to choose this variant:
    Use this to understand the brute-force search space and why the Eulerian-path insight matters.
"""

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        used = [False] * len(tickets)
        path = ["JFK"]

        def dfs() -> bool:
            if len(path) == len(tickets) + 1:
                return True
            current = path[-1]
            for i, (src, dst) in enumerate(tickets):
                if used[i] or src != current:
                    continue
                used[i] = True
                path.append(dst)
                if dfs():
                    return True
                path.pop()
                used[i] = False
            return False

        dfs()
        return path
