"""
200. Number of Islands - BFS flood fill

Variant role:
    alternative graph traversal reference

Core idea:
    Every unvisited land cell starts one island; BFS marks all land connected to it.

Key invariant:
    Once BFS starts from a land cell, every land cell in that connected component is converted to visited water.

Mechanics:
    Scan the grid. When a '1' is found, increment count, push it into a queue, and turn connected land cells into '0'.

Common pitfalls:
    Mark cells when enqueuing, not when dequeuing, to avoid duplicate queue entries.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this when iterative traversal is preferred over recursive DFS.
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                islands += 1
                grid[r][c] = "0"
                queue = deque([(r, c)])
                while queue:
                    row, col = queue.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))

        return islands
