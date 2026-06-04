# Notes - 40. Combination Sum II

## Core Idea

Sort first; skip duplicate values only within the same recursion depth.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_skip_duplicates.py` | primary solution | Time: O(2^n*n); Space: O(n) excl. output |
| `solution_counter_counts.py` | alternative duplicate-handling reference | Time: O(product(count_i + 1)); Space: O(u + target/min(candidates)) excl. output |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
