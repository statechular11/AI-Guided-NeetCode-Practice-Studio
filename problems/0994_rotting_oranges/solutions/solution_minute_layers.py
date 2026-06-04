"""
994. Rotting Oranges - BFS minute layers

Variant role:
    alternative multi-source BFS reference

Core idea:
    All rotten oranges spread simultaneously, so each BFS layer represents one minute.

Key invariant:
    At the start of each minute, the queue contains exactly the oranges that are currently rotten and can infect neighbors this minute.

Mechanics:
    Seed the queue with every rotten orange, count fresh oranges, process one queue layer per minute, and stop once no fresh oranges remain.

Common pitfalls:
    Only increment minutes after processing a layer that actually rots at least one future layer while fresh oranges remain.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this to make the time-step simulation explicit.
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
