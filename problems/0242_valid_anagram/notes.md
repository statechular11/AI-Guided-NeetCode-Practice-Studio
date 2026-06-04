# Notes - 242. Valid Anagram

## Core Idea

An anagram preserves character multiplicities. Compare frequency maps, or maintain a net balance array.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_counter.py` | Pythonic frequency-map baseline. | Time: O(n + m); Space: O(k) |
| `solution_fixed_counts.py` | Primary lowercase-English optimized version. | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- Check length first.
- Same set of letters is not enough; counts must match.
- The fixed-array solution assumes lowercase English letters, matching the standard LeetCode constraints.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
