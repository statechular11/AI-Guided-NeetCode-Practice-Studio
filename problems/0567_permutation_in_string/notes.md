# Notes - 567. Permutation in String

## Core Idea

Use a fixed-size window. The order inside the window does not matter; only counts matter.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force_sorted.py` | educational baseline | Time: O((m-n+1) * n log n); Space: O(n) |
| `solution_fixed_window_counts.py` | primary learning-friendly solution | Time: O(26m); Space: O(1) |
| `solution_matches_count.py` | constant-factor optimized solution | Time: O(m); Space: O(1) |
| `solution_deficit_window.py` | alternative optimized formulation | Time: O(m); Space: O(1) |

## Pitfalls To Watch

- State the window invariant before coding.
- Be clear about when the left boundary moves.
- Permutations require the same length and the same character counts.
- In fixed-window solutions, add the incoming character and remove exactly the
  character at `right - len(s1)`.
- In deficit-window solutions, a negative count means the current window overuses
  that character; shrink until the overuse is gone.
- For the deficit-window style, `window_len == len(s1)` proves a match only
  after all counts are known to be nonnegative.
- For character-count windows, distinguish missing characters from overrepresented characters.
- For fixed-size windows, remove exactly the element that leaves the window.

## Reference Enrichment Log

2026-06-01:

- Added `solution_brute_force_sorted.py` as a baseline that sorts every
  length-`len(s1)` window.
- Expanded `solution_fixed_window_counts.py` with the fixed-window invariant,
  add/remove mechanics, and an `adc` / `dcda` trace.
- Added `solution_matches_count.py` to show the optimized count-array comparison
  using a 26-slot match counter.
- Added `solution_deficit_window.py` to explain the alternative "remaining
  needed counts" formulation, including why nonnegative counts plus exact window
  length implies a permutation.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
