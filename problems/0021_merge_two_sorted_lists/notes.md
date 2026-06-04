# Notes - 21. Merge Two Sorted Lists

## Core Idea

A dummy tail pointer keeps pointer ownership simple and avoids first-node special cases.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_iterative_dummy.py` | primary interview solution | Time: O(n+m); Space: O(1) |
| `solution_recursive.py` | alternative learning solution | Time: O(n+m); Space: O(n+m) |

## Variant Notes

- `solution_iterative_dummy.py`: best interview target. The dummy node removes first-node special cases, and `tail` always marks the end of the merged prefix. The key pointer idea is that `tail.next = list1` attaches the current node object, while `list1 = list1.next` only moves the local variable to the next unmerged node.
- `solution_recursive.py`: clean recurrence. The smaller head is returned as the current merged head, and its `.next` is set to the recursively merged suffix. It is elegant, but uses O(n+m) call-stack space.

## Pitfalls To Watch

- Use dummy nodes when deleting or inserting near the head.
- Save `next` before rewiring a pointer that you still need to traverse.
- Distinguish node identity from node value, especially for cycle and random-pointer problems.
- Distinguish assigning a node field, such as `tail.next = list1`, from rebinding a local variable, such as `list1 = list1.next`.
- For design problems, separate lookup state from order-maintenance state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
