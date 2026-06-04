"""
329. Longest Increasing Path in a Matrix - Memoized Dfs Over Increasing Neighbors

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Memoize each cell; increasing edges prevent cycles.

    This specific variant uses: memoized DFS over increasing neighbors.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}` and the expected result is `4`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    329. Longest Increasing Path in a Matrix - DFS memo reference Core idea: Let dfs(r,c) be the longest increasing path starting from cell (r,c). Try neighbors with larger values and memoize the result. The increasing condition makes the dependency graph acyclic. Complexity: O(m*n) time and space.
"""

from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        @lru_cache(None)
        def dfs(r: int, c: int) -> int:
            best = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
