# Notes - 141. Linked List Cycle

## Core Idea

Floyd pointers detect a cycle by eventual pointer equality, not by node values.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_floyd.py` | primary O(1)-space solution | Time: O(n); Space: O(1) |
| `solution_hash_set.py` | baseline clarity solution | Time: O(n); Space: O(n) |

## Variant Notes

- `solution_floyd.py`: best interview target. Slow moves one step, fast moves two, and if a cycle exists then fast eventually laps slow inside the cycle. Compare node identity with `is`, not values.
- `solution_hash_set.py`: easiest baseline to reason about. Store visited node objects and return true if the same node object appears again. This is helpful for understanding the problem definition, but it uses O(n) extra space and does not satisfy the follow-up.

## Pitfalls To Watch

- Use dummy nodes when deleting or inserting near the head.
- Save `next` before rewiring a pointer that you still need to traverse.
- Distinguish node identity from node value, especially for cycle and random-pointer problems.
- For cycle detection, use object identity (`is` or storing node objects), not repeated values.
- Check `fast and fast.next` before advancing `fast.next.next` in Floyd's algorithm.
- For design problems, separate lookup state from order-maintenance state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
