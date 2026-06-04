# Notes - 239. Sliding Window Maximum

## Core Idea

A decreasing deque keeps only indices whose values can still become a future
window maximum. Expire indices from the front when they leave the window, and
remove dominated indices from the back when a newer value is greater than or
equal to them.

The front of the deque is always the maximum candidate for the current complete
window.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | educational baseline | Time: O(nk); Space: O(1) |
| `solution_heap.py` | practical alternative | Time: O(n log n); Space: O(n) |
| `solution_monotonic_deque.py` | primary optimized solution | Time: O(n); Space: O(k) |
| `solution_block_decomposition.py` | alternative optimized formulation | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- State the window invariant before coding.
- Be clear about when the left boundary moves.
- Store indices, not just values, so expired candidates can be removed.
- Remove expired front indices before using the front as the answer.
- Remove dominated candidates from the back: if a newer value is greater than or
  equal to an older value, the older value cannot become a future maximum.
- Output only after the first full window exists: `right >= k - 1`.
- For duplicate values, keeping the newer equal value is safe because it lasts
  longer in future windows.
- In the heap variant, stale entries below the heap top are harmless; only stale
  top entries must be popped before reading the answer.
- In the block-decomposition variant, reset `left_max` at block starts and
  `right_max` at block ends.
- For fixed-size windows, remove exactly the element that leaves the window.

## Reference Enrichment Log

2026-06-01:

- Expanded `solution_monotonic_deque.py` with the candidate invariant,
  domination proof, index-expiration reasoning, detailed trace, operation order,
  common pitfalls, and interview guidance.
- Expanded `solution_heap.py` with the lazy-deletion invariant, Python max-heap
  mechanics, stale-entry reasoning, pitfalls, and complexity nuance.
- Added `solution_brute_force.py` as a baseline that exposes the repeated work
  optimized away by the monotonic deque.
- Added `solution_block_decomposition.py` as an alternative O(n) offline method
  using block prefix/suffix maxima and the identity
  `max(window) = max(right_max[left], left_max[right])`.
- Added extra local cases for full-window, decreasing, duplicate, negative, and
  late-maximum-after-expiration scenarios.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
