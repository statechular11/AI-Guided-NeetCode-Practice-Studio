# Notes - 347. Top K Frequent Elements

## Core Idea

First count frequencies. Then choose how to retrieve the largest k frequencies:

- heap: direct and concise, O(n log k)
- bucket sort: optimized O(n), because frequency is between 1 and n

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_heap.py` | Practical priority-queue solution. | Time: O(n log k); Space: O(n) |
| `solution_bucket_sort.py` | Primary optimized bucket solution. | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- The answer order does not matter.
- `Counter(nums).most_common(k)` is convenient, but know the heap/bucket ideas for interviews.
- Bucket sort works because frequencies are bounded by `len(nums)`.
- `heapq.heapify` mutates the list in place; remember that when experimenting.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
