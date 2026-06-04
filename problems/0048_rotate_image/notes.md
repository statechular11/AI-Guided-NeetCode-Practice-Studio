# Notes - 48. Rotate Image

## Core Idea

Rotate clockwise in place. Two useful mental models:

- Transpose then reverse each row. This decomposes
  `old (r, c) -> new (c, n - 1 - r)` into two simpler transforms:
  `(r, c) -> (c, r)` and then `(c, r) -> (c, n - 1 - r)`.
- Layer-by-layer four-way swaps. Rotate each square ring by cycling top, left,
  bottom, and right cells.

Transpose+row-reverse is the shortest interview solution; layer swaps are the
best boundary/index drill.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_transpose_reverse.py` | primary in-place solution | Time: O(n^2); Space: O(1) |
| `solution_layer_four_way_swap.py` | layer/index-control variant | Time: O(n^2); Space: O(1) |

## Pitfalls To Watch

- The prompt requires mutating `matrix` in place; do not return a new matrix.
- During transpose, swap only `c > r`; otherwise each pair gets swapped twice.
- Clockwise rotation is transpose + reverse each row. Transpose + reverse row
  order is counterclockwise.
- In Python, `row.reverse()` mutates one row; `matrix.reverse()` reverses the
  order of rows.
- In layer swaps, each layer of width `w` has `w - 1` four-way cycles, not `w`.
- Save one cell before the four-way assignment so you do not overwrite it.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
