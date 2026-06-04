# Notes - 973. K Closest Points to Origin

## Core Idea

Squared distance preserves ordering and avoids floating point:

```text
distance([x, y]) = sqrt(x^2 + y^2)

Since sqrt is monotonic, compare x^2 + y^2 instead.
```

The answer can be returned in any order, so the problem is really asking for
"which k points" rather than "the k points sorted by distance."

That creates a useful strategy ladder:

1. Sort all points by squared distance and take the first k.
2. Heapify all points and pop k closest points.
3. Keep a size-k max heap when k is small compared with n.
4. Use quickselect when the interviewer wants optimized average time.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sort_distance.py` | simple primary solution | Time: O(n log n); Space: O(n) |
| `solution_min_heap_k_pops.py` | direct priority-queue simulation | Time: O(n + k log n); Space: O(n) |
| `solution_max_heap_size_k.py` | heap optimization | Time: O(n log k); Space: O(k) |
| `solution_quickselect.py` | optimized average-time selection | Average time: O(n); worst-case time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Use squared Euclidean distance `x*x + y*y`; do not sort by `x + y`, Manhattan
  distance, or `sqrt`.
- Output order is flexible, but the returned set must contain exactly k closest
  points.
- A min heap over all points pops closest points directly; no negation needed.
- A size-k heap needs max-heap behavior to expose the farthest kept candidate,
  so Python implementations usually store negative distances.
- Quickselect returns an unordered prefix of k closest points. Do not expect the
  prefix itself to be sorted.

## Reference Enrichment Log

2026-06-02:

- Expanded the sort and size-k heap reference headers with squared-distance
  reasoning, invariants, and common pitfalls.
- Added `solution_min_heap_k_pops.py` to match the direct heapify-then-pop
  priority-queue pattern.
- Added `solution_quickselect.py` for the optimized average-time selection
  strategy.
- Expanded tests beyond the examples to cover negative coordinates, `k == n`,
  the origin, and larger top-k selection.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
