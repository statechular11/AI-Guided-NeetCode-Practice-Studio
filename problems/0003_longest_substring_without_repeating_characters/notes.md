# Notes - 3. Longest Substring Without Repeating Characters

## Core Idea

Maintain a window with no duplicates. The last-seen variant jumps the left boundary instead of shrinking one character at a time.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | educational baseline | Time: O(n^2); Space: O(k) |
| `solution_set_window.py` | learning-friendly sliding window | Time: O(n); Space: O(k) |
| `solution_last_seen_window.py` | primary optimized solution | Time: O(n); Space: O(k) |

## Pitfalls To Watch

- State the window invariant before coding.
- Be clear about when the left boundary moves.
- In the set-window version, use `while ch in seen`, not a single `if`, because
  the old duplicate may be deeper inside the window.
- In the last-seen version, only jump `left` when the previous occurrence is
  inside the current window; otherwise old positions can move `left` backward.
- For character-count windows, distinguish missing characters from overrepresented characters.
- For fixed-size windows, remove exactly the element that leaves the window.

## Reference Enrichment Log

2026-06-01:

- Added `solution_brute_force.py` as an educational baseline that enumerates
  each start index and extends until the first duplicate.
- Expanded `solution_set_window.py` with the exact window/set invariant, a
  `pwwkew` trace, and the reason the duplicate-removal loop must be `while`.
- Expanded `solution_last_seen_window.py` with the `left` boundary invariant,
  an `abba` trace, and the key guard that prevents moving `left` backward.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
