"""
74. Search a 2D Matrix - Virtual Flattened Array

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Map virtual index to row/column with division and modulo. This avoids a separate row-selection binary search.

    This specific variant uses: virtual flattened array.

Key invariant:
    The search interval always contains every still-possible answer. Each midpoint decision removes a side that cannot contain the target answer.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 3}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define whether your binary search interval is closed or half-open. For answer-space search, prove the predicate is monotonic. For boundary problems, test empty arrays and values outside the range. For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

Complexity:
    Time: O(log(m*n)); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    74. Search a 2D Matrix - flattened binary search reference Core idea: The matrix rows form one globally sorted sequence. Binary search over virtual indices from 0 to rows * cols - 1 and map each index back to: row = index // cols col = index % cols Complexity: Time: O(log(m*n)) Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
