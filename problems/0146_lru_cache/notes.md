# Notes - 146. LRU Cache

## Core Idea

LRU Cache needs both O(1) key lookup and O(1) recency maintenance.

The primary design combines:

- a dictionary mapping `key -> node`, for lookup
- a doubly linked list storing usage order, for O(1) move-to-front and
  least-recent eviction

The linked-list invariant is usually:

```text
head <-> most recent ... least recent <-> tail
```

Then `get` and `put` both refresh the key's recency by moving its node near the
head. Eviction removes the node next to the tail.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_linear_order_baseline.py` | teaching baseline, not O(1) | O(capacity) get/put; Space: O(capacity) |
| `solution_hash_map_doubly_linked_list.py` | primary design solution | O(1) get/put; Space: O(capacity) |
| `solution_ordered_dict.py` | Pythonic built-in ordered map solution | O(1) get/put; Space: O(capacity) |

## Pitfalls To Watch

- `get` must refresh recency, not only return the value.
- `put` on an existing key must update the value and refresh recency.
- Evict the least recent key, not the oldest inserted key.
- Keep the dictionary and linked list consistent: every cached key should have
  exactly one linked-list node.
- Remove a node before reinserting it at the most-recent position.
- Delete the evicted key from the dictionary after unlinking the least-recent
  node.
- Dummy head/tail nodes remove empty-list and one-node special cases.
- A Python list of ordered keys is correct but not O(1); `list.remove` and
  front eviction are linear.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
