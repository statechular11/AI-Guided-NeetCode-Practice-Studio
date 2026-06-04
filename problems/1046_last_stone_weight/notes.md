# Notes - 1046. Last Stone Weight

## Core Idea

Use negative values in Python's min heap to simulate max-heap behavior.

The problem repeatedly asks for the two heaviest stones. A priority queue is the
natural fit because it exposes the current heaviest item without re-sorting the
entire collection after every smash.

Python `heapq` is a min heap:

```text
heap[0] = smallest stored value
```

To retrieve the heaviest stone first, store each stone as a negative value:

```text
stone weight 8 -> heap value -8
stone weight 7 -> heap value -7

heapq pops -8 before -7, so we recover 8 before 7.
```

Equal stones disappear. Unequal stones produce exactly one leftover stone with
weight `heaviest - second_heaviest`.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_max_heap.py` | primary heap simulation | Time: O(n log n); Space: O(n) |
| `solution_sort_each_round.py` | naive simulation baseline | Time: O(n^2 log n); Space: O(n) |
| `solution_sorted_list_bisect.py` | ordered-list incremental variant | Time: O(n^2); Space: O(n) |
| `solution_bucket_counts.py` | bounded-weight counting variant | Time: O(nW), where W is max stone weight; Space: O(W) |

## Pitfalls To Watch

- Know whether Python's `heapq` is min-heap only and negate values for max-heap behavior.
- `heap[0]` is the root/top priority value, not a sorted index. Use `heappop`
  twice to get the two heaviest stones.
- When using negated heap values, be careful with signs. A popped heap value
  like `-8` represents stone weight `8`.
- Do not push a leftover when two stones are equal; both are destroyed.
- Sorting once is not enough if using a list baseline; a leftover stone can
  disturb order and must be reinserted or the list must be sorted again.
- `bisect.insort` has O(log n) search but O(n) insertion because the list shifts.
- Bucket counting works because weights are bounded. Prefer heap when the value
  range is large or unbounded.

## Reference Enrichment Log

2026-06-02:

- Expanded `solution_max_heap.py` into a full teaching reference for Python's
  negative-value max-heap simulation, including sign handling and a step trace.
- Added `solution_sort_each_round.py` as the naive simulation baseline.
- Added `solution_sorted_list_bisect.py` to show how maintaining sorted order
  avoids full re-sorts but still pays O(n) list insertion cost.
- Added `solution_bucket_counts.py` as a bounded-weight frequency-table variant.
- Expanded tests for equal cancellation, repeated duplicates, max-weight
  boundaries, and leftover stones that must be reinserted.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
