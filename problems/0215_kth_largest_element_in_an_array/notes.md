# Notes - 215. Kth Largest Element in an Array

## Core Idea

The kth largest element counts duplicate occurrences, not distinct values.

```text
nums = [5, 5, 4], k = 2
answer = 5
```

A size-k min heap keeps only the k largest candidates. The root is the weakest
value among those k candidates, so after scanning the whole array the root is
the kth largest.

There are four useful strategy levels:

1. Sort descending and return index `k - 1`.
2. Build a max heap and pop k times.
3. Keep a size-k min heap for the primary heap solution.
4. Use quickselect with target ascending index `len(nums) - k`.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sorting.py` | simple baseline | Time: O(n log n); Space: O(n) |
| `solution_max_heap_k_pops.py` | direct priority-queue simulation | Time: O(n + k log n); Space: O(n) |
| `solution_min_heap_size_k.py` | primary heap solution | Time: O(n log k); Space: O(k) |
| `solution_quickselect.py` | optimized average-time selection | Average time: O(n); worst-case time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Do not remove duplicates. This is kth largest in sorted order, not kth
  distinct largest.
- For the size-k min heap, `heap[0]` is the kth-largest candidate, not the
  global maximum.
- In quickselect, kth largest maps to ascending index `len(nums) - k`, not
  `k - 1`.
- In the max-heap pop-k variant, Python needs negated values because `heapq` is
  a min heap.
- Replacing the root in a size-k heap should happen only when the new value is
  greater than `heap[0]`.

## Reference Enrichment Log

2026-06-02:

- Expanded sorting and size-k heap references with duplicate semantics,
  invariants, examples, and pitfalls.
- Added `solution_max_heap_k_pops.py` as the direct heap simulation variant.
- Added `solution_quickselect.py` as the optimized average-time order-statistic
  variant.
- Expanded tests for duplicates, negative values, `k = 1`, `k = n`, and
  all-equal arrays.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
