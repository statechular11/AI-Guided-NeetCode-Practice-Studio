"""
74. Search a 2D Matrix - row search then column search

Variant role:
    alternative binary-search reference

Core idea:
    First find the only row that could contain target, then binary-search inside that row.

Key invariant:
    Rows are ordered by their first and last values, and each selected row is internally sorted.

Mechanics:
    Binary-search row ranges using first/last values. If target fits one row's range, run standard binary search there.

Common pitfalls:
    Do not flatten index arithmetic and row-range arithmetic at the same time unless you are careful with division and modulo.

Complexity:
    Time: O(log m + log n); Space: O(1)

When to choose this variant:
    Use this when the virtual flattened array trick obscures the two sorted dimensions.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        candidate = -1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                candidate = row
                break
            if target < matrix[row][0]:
                bottom = row - 1
            else:
                top = row + 1

        if candidate == -1:
            return False

        row_values = matrix[candidate]
        left, right = 0, len(row_values) - 1
        while left <= right:
            mid = (left + right) // 2
            if row_values[mid] == target:
                return True
            if row_values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
