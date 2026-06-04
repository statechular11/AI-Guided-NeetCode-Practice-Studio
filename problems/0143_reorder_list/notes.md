# Notes - 143. Reorder List

## Core Idea

This is the classic split, reverse, and merge linked-list composition.

The target order alternates between the front and back of the original list:

`L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`

The in-place trick is to reverse the second half so the original tail side can
be consumed from left to right during weaving.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_split_reverse_merge.py` | primary in-place solution | Time: O(n); Space: O(1) |
| `solution_stack.py` | baseline learning solution | Time: O(n); Space: O(n) |

## Variant Notes

- `solution_split_reverse_merge.py`: best interview target. Find the middle, split the list, reverse the second half, then weave the first half and reversed second half. This composes three core linked-list skills and satisfies O(1) extra space.
- `solution_stack.py`: easier baseline. Push all nodes so tail nodes are available by popping. This makes the desired order intuitive, but uses O(n) extra memory and still needs a final tail cleanup to avoid stale links.

## Pitfalls To Watch

- Use dummy nodes when deleting or inserting near the head.
- Save `next` before rewiring a pointer that you still need to traverse.
- Distinguish node identity from node value, especially for cycle and random-pointer problems.
- Split the list before weaving; otherwise old links can create cycles.
- During weaving, save `first_next` and `second_next` before changing either `.next`.
- Clear the final tail's `.next` pointer after stack-based or manual rewiring variants.
- For design problems, separate lookup state from order-maintenance state.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
