"""
51. N-Queens - bitmask backtracking

Variant role:
    optimized state-representation reference

Core idea:
    Represent occupied columns and diagonals as bits, so each row can compute available queen positions with bit operations.

Key invariant:
    At row r, the masks describe exactly which columns are attacked by queens placed in rows < r.

Mechanics:
    available = all_columns & ~(cols | diag_down | diag_up). Repeatedly take the lowest available bit, place a queen, and shift diagonal masks for the next row.

Common pitfalls:
    The two diagonal masks shift in opposite directions as you move to the next row. Also mask with all_columns to discard bits beyond n.

Complexity:
    Time: O(n!); Space: O(n) excl. output

When to choose this variant:
    Use this for a compact optimized N-Queens implementation and to practice turning set membership into bit masks.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result: list[list[str]] = []
        board = [["."] * n for _ in range(n)]
        all_columns = (1 << n) - 1

        def backtrack(row: int, cols: int, diag_down: int, diag_up: int) -> None:
            if row == n:
                result.append(["".join(line) for line in board])
                return

            available = all_columns & ~(cols | diag_down | diag_up)
            while available:
                bit = available & -available
                available -= bit
                col = bit.bit_length() - 1
                board[row][col] = "Q"
                backtrack(
                    row + 1,
                    cols | bit,
                    (diag_down | bit) << 1,
                    (diag_up | bit) >> 1,
                )
                board[row][col] = "."

        backtrack(0, 0, 0, 0)
        return result
