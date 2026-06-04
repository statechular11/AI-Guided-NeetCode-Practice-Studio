# Notes - 138. Copy List with Random Pointer

## Core Idea

This is a deep-copy problem, so the key invariant is: every pointer in the
copied list must point to a cloned node or `None`, never back into the original
list.

The safest approach is a hash map from original node identity to cloned node.
Create all cloned nodes first, then wire `next` and `random` by looking up the
clone of each original pointer target.

The optimized linked-list approach interweaves each clone after its original.
That makes an original random target's clone available as `original.random.next`,
then a final pass restores the original list and extracts the copy.

A graph-traversal framing also works: treat `next` and `random` as outgoing
edges, use a memo dictionary, and clone each reachable node once. This is a good
bridge to Clone Graph.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_hash_map.py` | primary clear solution | Time: O(n); Space: O(n) |
| `solution_interweaving.py` | optimized extra-space solution | Time: O(n); Space: O(1) extra |
| `solution_graph_traversal.py` | educational graph-clone framing | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Key hash maps by node identity, not by `val`; duplicate values are allowed.
- Do not assign a clone's `random` to the original random target. Always map the
  original target to its clone first.
- In the interweaving solution, save or read the original next pointer before
  rewiring so you can restore the input chain.
- Handle `None` random pointers without looking them up as real nodes.
- The empty list is valid: return `None` when `head` is `None`.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
