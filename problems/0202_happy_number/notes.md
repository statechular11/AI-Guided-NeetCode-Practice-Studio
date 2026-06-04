# Notes - 202. Happy Number

## Core Idea

The digit-square process is deterministic: each number maps to exactly one next
number. So the sequence either reaches `1` or eventually repeats a previous
state and cycles.

Useful ways to detect the same outcome:

- Seen set: store every generated value; a repeat means an unhappy cycle.
- Floyd cycle detection: treat `next(n)` like a linked-list pointer and use
  slow/fast pointers for O(1) extra space.
- Known cycle shortcut: in base 10, unhappy numbers eventually hit the cycle
  containing `4`.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_cycle_set.py` | primary hash-set solution | Bounded time; O(seen states) space |
| `solution_floyd_cycle.py` | two-pointers O(1)-space variant | Bounded time; O(1) space |
| `solution_known_cycle.py` | math shortcut | Bounded time; O(1) space |

## Pitfalls To Watch

- Do not assume the sequence strictly decreases; it is bounded, then cyclic.
- In the digit-square helper, remember zeros contribute `0`, and `while n`
  works because constraints require positive `n`.
- A repeated value before reaching `1` means the process will never reach `1`.
- Floyd's version must advance `fast` twice per loop.
- The `4` shortcut is base-10-specific; it is a neat math fact, not the most
  general cycle-detection pattern.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
