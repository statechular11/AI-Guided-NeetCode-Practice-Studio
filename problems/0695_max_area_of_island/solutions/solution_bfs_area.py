"""
695. Max Area of Island - BFS island area flood fill

Variant role:
    alternative graph traversal reference

Core idea:
    Each island's area is the number of land cells reached by one flood fill.

Key invariant:
    The queue contains land cells belonging to the current island that have been marked visited but not fully expanded.

Mechanics:
    When a 1 is found, turn it to 0, BFS its component, count cells, and update the best area.

Common pitfalls:
    Mark when enqueuing to avoid counting a cell more than once.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this as the iterative counterpart to recursive DFS area counting.
"""

from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                grid[r][c] = 0
                area = 0
                queue = deque([(r, c)])
                while queue:
                    row, col = queue.popleft()
                    area += 1
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            queue.append((nr, nc))
                best = max(best, area)
        return best
