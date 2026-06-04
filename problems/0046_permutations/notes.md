# Notes - 46. Permutations

## Core Idea

Either track used indices or swap values into fixed positions; both are core permutation patterns.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_used_flags.py` | primary clear solution | Time: O(n!*n); Space: O(n) |
| `solution_in_place_swaps.py` | alternative backtracking pattern | Time: O(n!*n); Space: O(n) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
