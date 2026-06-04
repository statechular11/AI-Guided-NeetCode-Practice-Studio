# Notes - 76. Minimum Window Substring

## Core Idea

Expand until all needs are covered, then shrink until removing the left character would break validity.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | educational baseline | Time: O(m^2 + n); Space: O(k) |
| `solution_need_window.py` | primary interview solution | Time: O(m + n); Space: O(k) |
| `solution_deficit_missing.py` | alternative optimized formulation | Time: O(m + n); Space: O(k) |
| `solution_filtered_window.py` | optimization for many irrelevant characters | Time: O(m + n); Space: O(k + r) |

## Pitfalls To Watch

- State the window invariant before coding.
- Be clear about when the left boundary moves.
- A valid window must cover multiplicities from `t`, not just distinct
  characters.
- In the formed/required version, `formed == required` means all required
  character types are covered; it does not mean the window is minimal yet.
- Record a valid window before removing its left character during the shrink
  loop.
- Decrement `formed` only when a needed character drops below its required count.
- In the deficit/missing version, `missing == 0` means all required copies have
  been found; negative counts are surplus that can be shrunk away.
- For character-count windows, distinguish missing characters from overrepresented characters.
- For fixed-size windows, remove exactly the element that leaves the window.

## Reference Enrichment Log

2026-06-01:

- Added `solution_brute_force.py` to derive coverage with multiplicity by
  enumerating left boundaries and expanding until valid.
- Expanded `solution_need_window.py` with the formed/required invariant,
  shrink-loop mechanics, duplicate-count pitfalls, and an `ADOBECODEBANC` trace.
- Added `solution_deficit_missing.py` as an alternative optimized formulation
  that tracks total missing required characters and surplus via negative counts.
- Added `solution_filtered_window.py` to show how filtering out characters not
  in `t` keeps the same invariant while reducing work on irrelevant positions.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
