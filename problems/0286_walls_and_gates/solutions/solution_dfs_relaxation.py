"""
286. Walls and Gates - DFS relaxation from each gate

Variant role:
    educational baseline

Core idea:
    From every gate, recursively relax rooms when the new distance is shorter than the current value.

Key invariant:
    rooms[r][c] is always the shortest gate distance discovered so far for that room.

Mechanics:
    Start DFS at each gate with distance 0. Stop at walls, boundaries, and cells already holding a smaller distance.

Common pitfalls:
    This can revisit rooms many times. Multi-source BFS is the optimized way to visit each room at its shortest distance first.

Complexity:
    Time: O(gmn) worst case; Space: O(mn)

When to choose this variant:
    Use this as a readable relaxation baseline before learning why multi-source BFS is better.
"""

from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])

        def dfs(r: int, c: int, dist: int) -> None:
            if r < 0 or r == rows or c < 0 or c == cols:
                return
            if rooms[r][c] < dist:
                return
            rooms[r][c] = dist
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, dist + 1)

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    dfs(r, c, 0)
