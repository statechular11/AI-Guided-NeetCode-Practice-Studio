"""
417. Pacific Atlantic Water Flow - reverse DFS from both oceans

Variant role:
    alternative graph traversal reference

Core idea:
    Instead of asking where each cell can flow, start at each ocean and move uphill to cells that can flow back down to it.

Key invariant:
    A cell in visited can reach that ocean by following non-increasing heights in the original direction.

Mechanics:
    DFS from Pacific borders and Atlantic borders separately, allowing moves to neighbors with height >= current height, then intersect visited sets.

Common pitfalls:
    The reverse move is uphill or level, not downhill.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this as the recursive counterpart to reverse-ocean BFS.
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def explore(starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
            seen: set[tuple[int, int]] = set()

            def dfs(r: int, c: int) -> None:
                seen.add((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                        if heights[nr][nc] >= heights[r][c]:
                            dfs(nr, nc)

            for start in starts:
                if start not in seen:
                    dfs(*start)
            return seen

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        both = explore(pacific) & explore(atlantic)
        return [[r, c] for r, c in both]
