"""
329. Longest Increasing Path in a Matrix - topological peeling by outdegree

Variant role:
    alternative DAG reference

Core idea:
    Increasing moves form a DAG. Peel local maxima layer by layer; the number of layers is the longest increasing path length.

Key invariant:
    outdegree[r][c] counts larger neighbors not yet peeled from the DAG.

Mechanics:
    Start with cells that have no larger neighbor. When a cell is peeled, reduce outdegree of smaller neighbors that could move into it.

Common pitfalls:
    Edges point from smaller to larger values. Peeling starts at sinks, not sources.

Complexity:
    Time: O(mn); Space: O(mn)

When to choose this variant:
    Use this to see the graph/topological perspective beyond DFS memoization.
"""

from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        outdegree = [[0] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        outdegree[r][c] += 1
                if outdegree[r][c] == 0:
                    queue.append((r, c))

        layers = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        outdegree[nr][nc] -= 1
                        if outdegree[nr][nc] == 0:
                            queue.append((nr, nc))
            layers += 1
        return layers
