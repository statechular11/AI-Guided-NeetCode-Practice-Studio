# Notes - 73. Set Matrix Zeroes

## Core Idea

The key is to separate discovery of original zeros from the rewrite pass.
Never zero rows/columns immediately while scanning, because newly written zeros
would cascade into extra rows/columns.

Main approaches:

- Row/column sets: record which row indexes and column indexes originally had a
  zero, then rewrite cells whose row or column was recorded. This is simplest
  and uses O(m+n) extra space.
- First row/column markers: reuse `matrix[r][0]` and `matrix[0][c]` as marker
  arrays to reach O(1) extra space. The first row/column need special handling
  because they are both data and marker storage.
- Single-flag marker variant: use `matrix[0][0]` for first-column state and one
  boolean for first-row state.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_row_col_sets.py` | clean O(m+n)-space baseline | Time: O(m*n); Space: O(m+n) |
| `solution_first_row_col_markers.py` | primary O(1)-space solution | Time: O(m*n); Space: O(1) |
| `solution_single_flag_markers.py` | compact canonical O(1)-space variant | Time: O(m*n); Space: O(1) |

## Pitfalls To Watch

- Do not mutate whole rows/columns during the discovery pass; that creates
  cascading zeros.
- The method must mutate `matrix` in place and should not return a new matrix.
- In the O(1) marker solution, `matrix[0][0]` overlaps first-row and
  first-column state, so one side needs a separate flag.
- Rewrite the inner matrix before zeroing the first row/column, or marker
  information can be destroyed too early.
- Single-row and single-column matrices stress the first-row/first-column logic.
- Values can be any 32-bit integer, so sentinel values are not a safe general
  solution.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
