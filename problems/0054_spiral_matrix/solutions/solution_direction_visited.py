"""
54. Spiral Matrix - Direction Walk With Visited Reference

Core idea:
    Simulate the path one cell at a time. Keep a direction index cycling through
    right, down, left, and up:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    At each step:

        1. append the current cell,
        2. mark it visited,
        3. look at the next cell in the current direction,
        4. turn right if the next cell is out of bounds or already visited.

Key invariant:
    `row, col` is always an unvisited valid cell when it is appended. After
    appending it, the algorithm chooses the next valid unvisited neighbor in
    spiral direction order.

Why this works:
    The spiral path is just a deterministic walk that turns whenever it would
    leave the matrix or enter a cell already emitted. A `visited` matrix makes
    the stopping condition local, so we do not have to manage four shrinking
    boundaries.

Step-by-step mechanics:
    For a 3x3 matrix, the path begins:

        (0,0) -> (0,1) -> (0,2)

    The next rightward cell would be `(0,3)`, which is out of bounds, so turn
    down:

        (1,2) -> (2,2)

    Then turn left, then up, and so on. When moving up reaches a visited top row,
    turn right into the inner rectangle.

Common pitfalls:
    - Turning after moving out of bounds instead of before choosing the next
      valid cell.
    - Forgetting to mark the current cell before checking the next move.
    - Using `while row, col` style conditions; the clean stopping rule is
      exactly `m * n` appended cells.
    - Not handling single-row or single-column matrices; the visited check does
      handle them naturally.

Complexity:
    Time:
        O(m * n), one append per cell.

    Space:
        O(m * n), for the visited matrix, excluding output.

When to choose this variant:
    Use this when you want the easiest simulation to reason about or when
    practicing directional grid walks. In interviews, the boundary-shrink
    solution is usually preferred because it uses O(1) extra space.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = []
        row = col = direction = 0
        for _ in range(rows * cols):
            result.append(matrix[row][col])
            visited[row][col] = True

            dr, dc = directions[direction]
            next_row = row + dr
            next_col = col + dc
            if (
                next_row < 0
                or next_row == rows
                or next_col < 0
                or next_col == cols
                or visited[next_row][next_col]
            ):
                direction = (direction + 1) % 4
                dr, dc = directions[direction]

            row += dr
            col += dc

        return result
