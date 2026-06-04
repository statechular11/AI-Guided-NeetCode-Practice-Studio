# Notes - 54. Spiral Matrix

## Core Idea

Spiral traversal is a clockwise walk around nested rectangles.

Two useful mental models:

- Boundary shrink: keep `top`, `bottom`, `left`, and `right`; walk the outer
  ring, then shrink inward. This is the primary O(1)-extra-space approach.
- Direction walk: move right/down/left/up and turn when the next cell is out of
  bounds or already visited. This is easier to simulate but uses a visited
  matrix.

For boundary shrink, the bottom-row and left-column traversals need guards so
single remaining rows/columns are not duplicated.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_boundary_shrink.py` | primary solution | Time: O(m*n); Space: O(1) excl. output |
| `solution_direction_visited.py` | directional simulation variant | Time: O(m*n); Space: O(m*n) excl. output |

## Pitfalls To Watch

- For boundary shrink, guard the bottom row with `if top <= bottom`.
- For boundary shrink, guard the left column with `if left <= right`.
- Remember the ranges are inclusive: top row uses `left..right`, right column
  uses `top..bottom`, bottom row uses `right..left`, left column uses
  `bottom..top`.
- Rectangular matrices are allowed; do not assume `m == n`.
- Single-row and single-column matrices are the edge cases most likely to
  reveal duplicate appends.
- In direction simulation, turn before stepping into an invalid or visited cell.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
