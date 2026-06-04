# Notes - 15. 3Sum

## Core Idea

Sort first, fix one value, then use two pointers for the remaining two values. Duplicate skipping is the main bug source.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sort_two_pointers.py` | primary solution | Time: O(n^2); Space: O(1) extra |
| `solution_hash_set_complements.py` | educational hash-set variant | Time: O(n^2); Space: O(n + k) |

## Variant Notes

The primary solution is sort + two pointers:

```text
fix nums[i], then search the suffix with left/right pointers
```

This is the interview target because sorted order tells us which pointer to
move and duplicate skipping is explicit.

The hash-set complement variant is useful as a bridge from Two Sum:

```text
fix nums[i], scan j > i, and ask whether -(nums[i] + nums[j]) was seen
```

It has the same O(n^2) time complexity but uses extra space and relies on a set
of result tuples for uniqueness. Use it for learning, but prefer two pointers
when explaining the final interview solution.

## Pitfalls To Watch

- State what each pointer means before coding.
- Move pointers only after using the current state.
- Be explicit about duplicate handling when the output must be unique.
- The result can be in any order, but triplets themselves should be unique.
- After accepting a triplet in the two-pointer solution, skip duplicate left and
  right values before continuing.

## Reference Enrichment Log

2026-05-29:

- Existing reference covered the primary sort + two-pointers solution.
- Added `solution_hash_set_complements.py` as a meaningfully different
  educational variant that extends the Two Sum complement-set idea to 3Sum.
- Did not add pure brute force because it is O(n^3) and mostly teaches only why
  the two-pointer/hash-set reductions are needed.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
