# Notes - 23. Merge k Sorted Lists

## Core Idea

There are two main optimized viewpoints:

- Heap: the next output is always the smallest current head among the k lists.
  Keep those current heads in a min-heap.
- Divide and conquer: merge lists in balanced rounds using the Merge Two Sorted
  Lists primitive.

Baselines are useful for contrast:

- Collect and sort all values is simple but ignores the fact that each input
  list is already sorted.
- Sequential pairwise merging is correct but can repeatedly reprocess early
  nodes; balancing the merges gives the optimized divide-and-conquer solution.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_collect_sort_baseline.py` | brute-force value baseline | Time: O(N log N); Space: O(N) |
| `solution_sequential_merge.py` | pairwise merge baseline, not balanced | Time: O(N*k); Space: O(1) extra |
| `solution_min_heap.py` | primary solution | Time: O(N log k); Space: O(k) |
| `solution_divide_and_conquer.py` | alternative optimized solution | Time: O(N log k); Space: O(1) extra |

## Pitfalls To Watch

- In Python heaps, include a unique tie-breaker like `(node.val, counter, node)`
  so equal values do not compare `ListNode` objects.
- Push only current list heads into the heap, not every node, to keep heap space
  at O(k).
- After popping a heap node, push `node.next` because it becomes that list's new
  current head.
- When reusing original nodes, set the final `tail.next = None` in heap-style
  relinking to avoid stale links.
- Sequential pairwise merging is not the same as divide and conquer; balanced
  rounds are what give O(N log k).
- Handle `lists = []` and lists containing `None`.
- Use a dummy node when merging two linked lists to avoid head special cases.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
