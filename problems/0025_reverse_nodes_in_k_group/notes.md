# Notes - 25. Reverse Nodes in k-Group

## Core Idea

Always check that a full group exists before rewiring; incomplete suffix stays
unchanged.

The core pointer shape is:

```text
group_prev -> group_start -> ... -> kth -> group_next
```

After reversing a full group:

- `kth` becomes the new group head.
- `group_start` becomes the group tail.
- the group tail must reconnect to `group_next`.
- `group_prev` moves to that tail for the next iteration.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_iterative_group_reversal.py` | primary O(1)-space interview solution | Time: O(n); Space: O(1) |
| `solution_detach_reverse.py` | boundary-explicit O(1)-space variant | Time: O(n); Space: O(1) |
| `solution_recursive_half_open.py` | recursive formulation | Time: O(n); Space: O(n/k) |
| `solution_stack_relink.py` | educational O(k)-space variant | Time: O(n); Space: O(k) |

## Pitfalls To Watch

- Use dummy nodes when deleting or inserting near the head.
- Save `next` before rewiring a pointer that you still need to traverse.
- Confirm that k nodes exist before reversing; do not touch an incomplete suffix.
- Save `group_next` before reversing or detaching the group.
- Remember that the old group head becomes the new group tail after reversal.
- Move `group_prev` to the old group head/new tail, not to the new head.
- In half-open reversal, `[start, stop)` includes `start` but does not include
  `stop`.
- For `k = 1`, every group has one node and the list should remain unchanged.
- Distinguish node identity from node value, especially for cycle and random-pointer problems.
- For design problems, separate lookup state from order-maintenance state.

## Reference Enrichment Log

2026-06-01:

- Expanded `solution_iterative_group_reversal.py` with a module-level guide for
  the primary O(1)-space half-open reversal pattern, including pointer
  invariants, a `[1,2,3,4,5], k=2` trace, and boundary pitfalls.
- Added `solution_detach_reverse.py`, which temporarily cuts each complete group
  before reversing it and reconnecting saved boundaries.
- Added `solution_recursive_half_open.py`, which shows the recursive structure
  and clarifies why recursion is not O(1) extra space.
- Added `solution_stack_relink.py` as an educational O(k)-space bridge toward
  in-place pointer rewiring.
- Added local cases for `k=1`, full-list reversal, exact multiple groups,
  incomplete suffix preservation, and a two-node pair.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
