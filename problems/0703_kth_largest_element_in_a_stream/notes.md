# Notes - 703. Kth Largest Element in a Stream

## Core Idea

The heap stores the k largest seen values, so its minimum is the kth largest.

For this problem, "top of the heap" means `heap[0]`, the priority root. In
Python `heapq`, that root is the smallest value because `heapq` is a min-heap.
That is exactly why a size-k min heap works: among the k largest values, the
smallest one is the kth largest overall.

```text
all seen values:
    [values too small for top k] + [k largest values]

size-k min heap stores:
    [k largest values only]

heap[0]:
    smallest among those k values = kth largest overall
```

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_size_k_heap.py` | primary stream solution | Constructor O(n log k); add O(log k) when heap changes; Space O(k) |
| `solution_sorted_list_bisect.py` | baseline rank solution | Constructor O(n log n); add O(n); Space O(n) |
| `solution_heapify_trim.py` | heap API and construction variant | Constructor O(n + (n-k) log n); add O(log k); Space O(n) transient, O(k) final |

## Pitfalls To Watch

- Know whether Python's `heapq` is min-heap only and negate values for max-heap behavior.
- For size-k heaps, keep exactly the candidates you need.
- `heap[0]` is the root/top priority item. Other indexes are not sorted ranks.
- Use `heappush`, `heappop`, `heapreplace`, or `heappushpop`; raw list `append`
  or `pop` does not maintain heap order.
- Do not use a max heap for the optimized stream solution. A max heap exposes
  the largest value, but this problem needs the boundary value between the top k
  and everything else.
- Duplicates count as separate ranks; kth largest does not mean kth distinct
  largest.
- If the initial list has fewer than k values, the first `add` call can be the
  one that completes the first k values.
- For streaming medians, rebalance heaps after every insertion.
- For design problems, define what each operation must update.

## Reference Enrichment Log

2026-06-01:

- Expanded `solution_size_k_heap.py` with a full teaching header for the
  size-k min-heap invariant, `heapq` root/top terminology, replacement logic,
  duplicates, and common heap API traps.
- Added `solution_sorted_list_bisect.py` as a first-principles baseline: keep
  all values sorted and return `values[len(values) - k]`.
- Added `solution_heapify_trim.py` to illustrate `heapq.heapify`, repeated
  `heappop` trimming, and why heap order is not sorted order.
- Added design cases for duplicates, negative values, empty initial stream,
  initially fewer than k values, and full-heap additions that are too small to
  affect the kth largest.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
