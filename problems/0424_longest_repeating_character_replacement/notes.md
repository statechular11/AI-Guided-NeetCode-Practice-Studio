# Notes - 424. Longest Repeating Character Replacement

## Core Idea

Window validity is `window_len - max_frequency <= k`. The stale max-frequency optimization is safe and common.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | educational baseline | Time: O(n^2); Space: O(1) |
| `solution_sliding_window_exact_max.py` | learning-friendly optimized solution | Time: O(26n); Space: O(1) |
| `solution_sliding_window.py` | primary optimized solution | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- State the window invariant before coding.
- Be clear about when the left boundary moves.
- The key validity formula is `window_len - max_frequency <= k`.
- In the exact-max version, `max_frequency` is the true maximum inside the
  current window.
- In the stale-max version, `max_count` is nondecreasing; it may overestimate
  the current window after shrinking, but it cannot create a larger valid answer.
- For character-count windows, distinguish missing characters from overrepresented characters.
- For fixed-size windows, remove exactly the element that leaves the window.

## Reference Enrichment Log

2026-06-01:

- Added `solution_brute_force.py` to derive the replacement formula from first
  principles by enumerating start positions and tracking the majority count.
- Added `solution_sliding_window_exact_max.py` as the easiest optimized version
  to reason about: shrink while the true current max frequency makes the window
  invalid.
- Expanded `solution_sliding_window.py` into the primary stale-`max_count`
  reference, including the safety argument, operational invariant, and
  `AABABBA` walkthrough.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
