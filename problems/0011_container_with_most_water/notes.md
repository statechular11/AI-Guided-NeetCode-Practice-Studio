# Notes - 11. Container With Most Water

## Core Idea

The shorter wall limits area; move that pointer because reducing width without increasing the limit cannot help.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | learning baseline | Time: O(n^2); Space: O(1) |
| `solution_two_pointers.py` | primary optimized solution | Time: O(n); Space: O(1) |
| `solution_two_pointers_skip_dominated.py` | dominance-pruning variant | Time: O(n); Space: O(1) |

## Variant Notes

The brute-force baseline tries every pair and is useful only for understanding
the area formula:

```text
area = (right - left) * min(height[left], height[right])
```

The primary interview solution starts with the widest container and always moves
the shorter wall. If the left wall is shorter, every future container that keeps
that same left wall has smaller width and no larger limiting height, so that
left index can be discarded. The same argument applies symmetrically when the
right wall is shorter.

The skip-dominated variant uses the same proof but jumps over consecutive walls
that are no taller than the old limiting height. It is not necessary for an
interview implementation, but it is a good way to internalize the dominance
reasoning behind the two-pointer move.

## Pitfalls To Watch

- State what each pointer means before coding.
- Move pointers only after using the current state.
- The shorter wall limits the current area.
- Moving the taller wall while keeping the shorter wall cannot help.
- Do not sort the heights; the index distance is part of the area.

## Reference Enrichment Log

2026-05-29:

- Expanded the brute-force and primary two-pointer reference docstrings with
  examples and the dominance proof.
- Added `solution_two_pointers_skip_dominated.py` as an educational variant that
  skips heights that cannot improve the answer.
- Did not add more variants because the meaningful solution space is small:
  brute force establishes the objective, and the two-pointer dominance argument
  is the optimized solution.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
