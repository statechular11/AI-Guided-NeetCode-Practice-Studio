# Notes - 295. Find Median from Data Stream

## Core Idea

The median is the boundary between the lower half and upper half of the sorted
stream.

Two heaps keep that boundary available without sorting the whole stream after
every insertion:

```text
low  = max heap for lower half   # Python stores negatives
high = min heap for upper half

size invariant:
len(low) == len(high) or len(low) == len(high) + 1

order invariant:
every value in low <= every value in high
```

Then:

```text
odd count:  median = max(low)
even count: median = (max(low) + min(high)) / 2
```

For Python heaps:

```text
max(low) = -low[0]
min(high) = high[0]
```

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_two_heaps.py` | primary streaming median solution | add O(log n), find O(1); Space O(n) |
| `solution_sorted_list.py` | educational baseline | add O(n), find O(1); Space O(n) |
| `solution_counting_buckets.py` | constraint-aware follow-up variant | add O(1), find O(R), Space O(R), where R is value range size |

## Pitfalls To Watch

- Know whether Python's `heapq` is min-heap only and negate values for max-heap behavior.
- In the two-heap solution, `low[0]` is negative. The lower-half max is
  `-low[0]`.
- Preserve both invariants: size balance and lower-half values <= upper-half
  values.
- Decide which heap owns the extra item for odd counts. The references keep the
  extra item in `low`.
- For sorted-list baseline, `bisect.insort` has O(log n) search but O(n)
  insertion because list elements shift.
- For counting buckets, remember to offset negative values before indexing and
  use 1-based kth order statistics when scanning cumulative counts.
- For design problems, define what each operation must update.

## Reference Enrichment Log

2026-06-02:

- Expanded `solution_two_heaps.py` with a deeper invariant explanation,
  step-by-step mechanics, a stream walkthrough, and inline comments for the key
  heap transfers.
- Added `solution_sorted_list.py` as a simple baseline for understanding direct
  median indexes.
- Added `solution_counting_buckets.py` as a bounded-value follow-up variant that
  demonstrates frequency scanning and offset handling for negative numbers.
- Expanded tests beyond the sample to cover increasing/decreasing streams,
  duplicates, negatives, even/odd medians, and value boundaries.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
