# Notes - 128. Longest Consecutive Sequence

## Core Idea

The O(n) trick is to count a sequence only from its first value:

```text
num is a start if num - 1 is not in the set
```

Then walk forward while `num + length` exists.

Important clarification: the algorithm builds `values = set(nums)` before it
starts counting. That means the set already contains every number from the
input, regardless of input order. If `1` appears before `2`, `3`, and `4` in the
input, counting from start `1` still finds `2`, `3`, and `4` by set membership.
The sequence length is computed from the complete set, not from the portion of
the input seen so far.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sorting.py` | Easy baseline after sorting unique values. | Time: O(n log n); Space: O(n) |
| `solution_hash_set_starts.py` | Primary optimized start-only scan. | Time: O(n); Space: O(n) |
| `solution_union_find.py` | Educational component-based variant that unions adjacent values. | Time: O(n * alpha(n)); Space: O(n) |

## Union-Find Variant

This problem can also be modeled as connected components:

```text
connect x and x + 1 when both values exist
```

Each connected component is one consecutive sequence, and the answer is the
largest component size.

This is not usually the shortest interview solution; the hash-set start scan is
cleaner. The union-find variant is useful when practicing DSU or when you want
to see how "adjacent values form groups" can become a graph/component problem.

## Pitfalls To Watch

- Duplicates should not reset or inflate a streak; use a set.
- Do not start counting from every number, or the worst case becomes O(n^2).
- Iterate over unique values, not the original `nums`, so duplicate sequence starts
  do not repeat the same forward scan.
- Empty input should return 0.

## Personal Learning Notes

2026-05-29:

- Needed to read `solutions/solution_hash_set_starts.py` before the main idea
  clicked. The key invariant to remember is: count a sequence only from `num`
  when `num - 1` is absent from the set.
- Transferable pattern: use a set for O(1) membership, then identify the unique
  start of each structure so total work is not repeated.

## Reference Enrichment Log

2026-06-01:

- Expanded `solution_hash_set_starts.py` with a step-by-step walkthrough and an
  explicit explanation that `values` is fully built before the sequence-start
  scan begins. This is the key reason the algorithm does not need to readjust a
  length when later numeric values appear later in input order.

2026-05-29:

- Existing references already covered the sorting baseline and primary O(n)
  hash-set solution.
- Added `solution_union_find.py` because Union-Find is a listed tag for this
  problem and represents a genuinely different component-based model.
- Did not add brute force because it does not add much learning value beyond
  showing why repeated sequence expansion can become O(n^2).

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
