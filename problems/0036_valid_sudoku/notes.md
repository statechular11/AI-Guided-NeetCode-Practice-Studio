# Notes - 36. Valid Sudoku

## Core Idea

For each non-empty cell, validate the digit in three independent scopes: row, column, and 3x3 box.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_seen_sets.py` | Primary marker-set solution. | Time: O(1); Space: O(1) |
| `solution_bitmask.py` | Compressed-state bitmask variant. | Time: O(1); Space: O(1) |

## Bitmask Variant

Digits `1` through `9` fit in 9 bits. For each row, column, and 3x3 box, keep one integer mask:

```text
digit "1" -> 1 << 0
digit "9" -> 1 << 8
```

If the bit for a digit is already set in the row, column, or box mask, that digit is duplicated in the corresponding scope. Otherwise, set the bit in all three masks and continue.

## Pitfalls To Watch

- Ignore `"."` cells.
- Compute the box as `(row // 3, col // 3)`.
- This validates the current board only; it does not solve Sudoku.
- Complexity is O(1) because the board size is fixed at 9x9, though you can also describe it as scanning 81 cells.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
