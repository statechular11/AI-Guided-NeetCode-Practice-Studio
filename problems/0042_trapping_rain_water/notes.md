# Notes - 42. Trapping Rain Water

## Core Idea

Water at each index is bounded by the shorter of the best wall to the left and right. The two-pointer version compresses the prefix/suffix arrays.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_prefix_suffix_arrays.py` | learning-friendly DP view | Time: O(n); Space: O(n) |
| `solution_two_pointers.py` | primary optimized solution | Time: O(n); Space: O(1) |
| `solution_monotonic_stack.py` | representative stack solution | Time: O(n); Space: O(n) |

## Variant Notes

The prefix/suffix array solution is the clearest way to see the core formula:

```text
water[i] = min(max wall to the left, max wall to the right) - height[i]
```

The two-pointer solution compresses those two arrays into `left_max` and
`right_max`. When `left_max <= right_max`, the left side is decided because the
right side already has a boundary at least that high. The symmetric rule applies
when `right_max < left_max`.

The monotonic stack solution uses a different mental model: it waits until a
right boundary appears, then pops basin bottoms from a decreasing stack and
computes water between the new left boundary and the current right boundary.
This is useful for connecting the problem to next-greater-boundary patterns.

## Pitfalls To Watch

- State what each pointer means before coding.
- Move pointers only after using the current state.
- Do not confuse this with Container With Most Water; here the water is summed
  across many basins, not one pair of walls.
- In the prefix/suffix view, every index needs both a left wall and a right wall.
- In the two-pointer view, compare the running maxima, not just the final answer.
- In the stack view, the popped bar is the basin bottom; the new stack top is
  the left boundary.

## Reference Enrichment Log

2026-05-29:

- Expanded the prefix/suffix and two-pointer reference docstrings with examples,
  invariants, and when-to-use guidance.
- Added `solution_monotonic_stack.py` because monotonic stack is a meaningful
  different approach and one of the official tags for this problem.
- Did not add brute force because the prefix/suffix version already provides a
  clear learning baseline while remaining efficient.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
