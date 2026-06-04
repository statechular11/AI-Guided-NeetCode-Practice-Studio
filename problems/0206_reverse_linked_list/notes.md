# Notes - 206. Reverse Linked List

## Core Idea

Always save next before changing cur.next; otherwise the rest of the list is lost.

The main linked-list skill here is not the algorithmic complexity; it is pointer
ownership. Before rewiring a node, decide which pointer still gives you access
to the unreversed suffix.

For the iterative solution:

- `prev` is the reversed prefix,
- `cur` is the first node not yet reversed,
- `nxt` temporarily preserves the original `cur.next`.

For the recursive solution, the call stack preserves the path back to each node
while the suffix is reversed.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_iterative_pointers.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_recursive.py` | recursive learning variant | Time: O(n); Space: O(n) |
| `solution_explicit_stack.py` | auxiliary-stack learning bridge | Time: O(n); Space: O(n) |

## Variant Notes

- `solution_iterative_pointers.py`: best interview target. It rewires in place with `prev`, `cur`, and `nxt`.
- `solution_recursive.py`: follows the prompt follow-up. Reverse the suffix first, then append the current head to the suffix tail.
- `solution_explicit_stack.py`: uses an explicit stack to make reversed order visible. It is useful for learning, but uses O(n) extra space.

## Pitfalls To Watch

- Save `next` before rewiring a pointer that you still need to traverse.
- Return the new head, not the old head.
- In recursive reversal, set `head.next = None` so the old head becomes the new tail.
- In auxiliary-stack reversal, clear the final tail's `.next` pointer to avoid leaving an old link or creating a cycle.
- Values are irrelevant; reverse node links, not just the stored values.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
