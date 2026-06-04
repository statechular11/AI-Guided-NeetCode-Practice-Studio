# Notes - 155. Min Stack

## Core Idea

Store minimum history alongside value history. Duplicated minimums should survive one pop at a time.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_pair_stack.py` | readable design solution | Time: O(1) per op; Space: O(n) |
| `solution_parallel_min_stack.py` | primary design solution | Time: O(1) per op; Space: O(n) |
| `solution_sparse_min_stack_counts.py` | space-conscious duplicate-aware variant | Time: O(1) per op; Space: O(n) |

## Variant Notes

The pair-stack solution stores one tuple per pushed value:

```text
(value, minimum_after_this_push)
```

This is often the easiest implementation to write correctly because `top()` and
`getMin()` both read from the same top entry.

The parallel-min-stack solution separates concerns:

```text
values   = pushed values
minimums = running minimum after each push
```

Both stacks stay the same length, so `pop()` simply pops both. This avoids
special cases and is a strong interview default.

The sparse min-stack-with-counts variant stores only minima and duplicate counts:

```text
mins = [(minimum_value, active_count_for_that_minimum)]
```

This uses fewer auxiliary entries when most pushes do not change the minimum.
The count is important: duplicate minima must survive one pop at a time.

## Pitfalls To Watch

- State exactly what each stack stores.
- `getMin()` must be O(1); scanning the value stack is not acceptable.
- Duplicate minima matter. If two equal minima are pushed, popping one must not
  lose the other.
- For the parallel-min-stack version, push a min snapshot for every value so
  both stacks stay aligned.
- For the sparse-count version, decrement the count when popping a duplicate
  minimum and remove the min entry only when the count reaches zero.

## Reference Enrichment Log

2026-05-30:

- Expanded `solution_pair_stack.py` and `solution_parallel_min_stack.py` with
  explicit invariants, examples, and duplicate-min reasoning.
- Added `solution_sparse_min_stack_counts.py` as a meaningfully different
  duplicate-aware min-history representation.
- Did not add more exotic encoded-min tricks because they are less readable and
  do not improve the asymptotic complexity for interview purposes.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
