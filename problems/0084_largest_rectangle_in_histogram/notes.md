# Notes - 84. Largest Rectangle in Histogram

## Core Idea

A shorter bar finalizes rectangles for taller previous bars. The monotonic stack stores bars whose right boundary is not known yet.

Another way to phrase the problem: choose each bar as the limiting shortest bar
of a rectangle, then ask how far that bar can extend left and right before a
strictly shorter bar blocks it.

The optimized solutions all revolve around nearest-smaller boundaries:

- the one-pass stack discovers the right boundary at pop time,
- the start-index stack carries the left boundary directly,
- the two-pass boundary method computes both sides explicitly.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force_expand.py` | learning baseline | Time: O(n^2); Space: O(1) |
| `solution_monotonic_stack.py` | primary optimized solution | Time: O(n); Space: O(n) |
| `solution_start_index_stack.py` | interview-friendly stack variant | Time: O(n); Space: O(n) |
| `solution_nearest_smaller_boundaries.py` | boundary-explicit optimized solution | Time: O(n); Space: O(n) |
| `solution_segment_tree_divide_conquer.py` | advanced alternative | Time: O(n log n); Space: O(n) |

## Variant Notes

- `solution_brute_force_expand.py`: expands each bar left and right; good for intuition, too slow for constraints.
- `solution_monotonic_stack.py`: compact one-pass target. Use a sentinel and compute width after popping.
- `solution_start_index_stack.py`: stores `(start_index, height)` so the left boundary is carried explicitly.
- `solution_nearest_smaller_boundaries.py`: two monotonic passes make previous/next smaller boundaries visible.
- `solution_segment_tree_divide_conquer.py`: range-minimum divide and conquer; useful for learning, but not the preferred interview answer.

## Pitfalls To Watch

- Be precise about width after popping: `right_index - left_boundary - 1`.
- Equal heights should form one wider rectangle. Boundary-precompute variants usually pop `>=` to find a strictly smaller boundary.
- The current shorter bar finalizes taller previous bars; it is not necessarily part of those rectangles.
- A trailing sentinel height `0` or a final stack-drain step is needed so bars that never see a shorter bar still get processed.
- Zero-height bars split the histogram into independent regions.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
