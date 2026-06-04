# Notes - 131. Palindrome Partitioning

## Core Idea

Backtracking chooses the next palindrome prefix; DP precompute removes repeated palindrome checks.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_backtracking.py` | primary clear solution | Time: O(n*2^n); Space: O(n) |
| `solution_dp_precompute.py` | optimized substring-check variant | Time: O(n^2 + output*n); Space: O(n^2) |

## Pitfalls To Watch

- State the recursion state clearly: index, start position, path, and remaining target.
- Copy the current path before adding it to results.
- Restore every mutation during backtracking, including used flags, board cells, swaps, and sets.
- For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
