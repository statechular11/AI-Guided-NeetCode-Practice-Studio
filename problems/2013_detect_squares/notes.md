# Notes - 2013. Detect Squares

## Core Idea

A query square can be found in two equivalent ways:

- Choose the opposite diagonal point `(x, y)`. It is valid when
  `x != qx`, `y != qy`, and `abs(x - qx) == abs(y - qy)`. The other two
  corners are forced to be `(qx, y)` and `(x, qy)`.
- Choose a same-row point `(x2, qy)`. The side length is `x2 - qx`, and the
  opposite row is either `qy + side` or `qy - side`.

Duplicate point counts multiply the number of square choices. The query point
itself does not have to be present in the data structure.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_point_counter.py` | primary design solution | add O(1), count O(P); Space: O(P) |
| `solution_row_counter.py` | query-row optimized sparse variant | add O(1), count O(R); Space: O(P) |
| `solution_bounded_grid.py` | coordinate-bounded grid variant | add O(1), count O(1001); Space: O(1001^2) |

## Pitfalls To Watch

- Positive area means the diagonal cannot share x or y with the query.
- Side lengths must match; otherwise you are counting rectangles, not squares.
- The query point is external; do not multiply by how many times it was added.
- Duplicate stored points are distinct choices, so multiply the counts of the
  three selected stored corners.
- A `set` loses duplicate multiplicity; use `Counter` or integer counts.
- In row-based solutions, check both `qy + side` and `qy - side`.
- In grid solutions, keep the coordinate orientation consistent, such as
  `grid[y][x]`.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
