"""
130. Surrounded Regions - union-find border sentinel

Variant role:
    alternative graph connectivity reference

Core idea:
    Every 'O' connected to the border survives. Union all adjacent 'O' cells and connect border 'O' cells to one sentinel node.

Key invariant:
    An 'O' should remain 'O' exactly when it belongs to the same component as the border sentinel.

Mechanics:
    Build DSU over all cells plus one dummy border node, union neighboring O cells, then flip O cells not connected to dummy.

Common pitfalls:
    Only border-connected regions survive. Interior O components must be flipped even if they are large.

Complexity:
    Time: O(mn alpha(mn)); Space: O(mn)

When to choose this variant:
    Use this to practice DSU as an alternative to border flood fill.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dummy = rows * cols
        parent = list(range(dummy + 1))
        rank = [0] * (dummy + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1

        def cell_id(r: int, c: int) -> int:
            return r * cols + c

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O":
                    continue
                if r in {0, rows - 1} or c in {0, cols - 1}:
                    union(cell_id(r, c), dummy)
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if nr < rows and nc < cols and board[nr][nc] == "O":
                        union(cell_id(r, c), cell_id(nr, nc))

        border_root = find(dummy)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and find(cell_id(r, c)) != border_root:
                    board[r][c] = "X"
