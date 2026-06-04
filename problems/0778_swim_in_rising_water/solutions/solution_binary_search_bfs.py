"""
778. Swim in Rising Water - binary search water level with BFS feasibility

Variant role:
    alternative answer-search reference

Core idea:
    A water level t is feasible if cells with elevation <= t connect start to target; feasibility is monotonic in t.

Key invariant:
    If can_swim(t) is true, every higher water level is also true.

Mechanics:
    Binary-search t between max(start, target) and max elevation, using BFS to test reachability under that threshold.

Common pitfalls:
    The lower bound must at least include start and target elevations.

Complexity:
    Time: O(n^2 log n); Space: O(n^2)

When to choose this variant:
    Use this to practice binary search on a monotonic graph predicate; Dijkstra solves it in one priority-queue pass.
"""

from collections import deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def can_swim(level: int) -> bool:
            if grid[0][0] > level:
                return False
            queue = deque([(0, 0)])
            seen = {(0, 0)}
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                        if grid[nr][nc] <= level:
                            seen.add((nr, nc))
                            queue.append((nr, nc))
            return False

        left = max(grid[0][0], grid[-1][-1])
        right = max(max(row) for row in grid)
        while left < right:
            mid = (left + right) // 2
            if can_swim(mid):
                right = mid
            else:
                left = mid + 1
        return left
