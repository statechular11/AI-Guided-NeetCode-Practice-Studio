# Notes - 238. Product of Array Except Self

## Core Idea

Primary section: **Arrays & Hashing**

Tags: Array, Prefix Sum

This problem is about splitting the answer at each index into two independent pieces:

```text
product of everything left of i * product of everything right of i
```

The important move is to avoid thinking in terms of "total product divided by nums[i]". Division is explicitly disallowed, and division also creates awkward zero handling. Prefix and suffix products handle zeros without special cases.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_left_right_arrays.py` | Learning-friendly no-division version. Builds separate `left` and `right` product arrays, then multiplies them. | Time: O(n); Space: O(n) extra |
| `solution_prefix_suffix.py` | Primary optimized interview version. Stores left products in the output array, then multiplies right products during a backward scan. | Time: O(n); Space: O(1) extra, excluding output |

## Preferred Interview Path

Start with the left/right-array explanation if you need to make the idea obvious:

```text
answer[i] = left_product_before_i * right_product_after_i
```

Then compress the space:

1. Store each left product directly into `answer[i]`.
2. Walk from right to left with one running `suffix`.
3. Multiply `answer[i]` by `suffix`.
4. Update `suffix *= nums[i]` after using it.

That last ordering is the key invariant. If you update `suffix` before multiplying into `answer[i]`, you accidentally include `nums[i]` in its own answer.

## Example Walkthrough

For `nums = [1, 2, 3, 4]`:

Forward pass stores left products:

```text
answer = [1, 1, 2, 6]
```

Backward pass multiplies right products:

```text
i = 3, suffix = 1,  answer[3] = 6
i = 2, suffix = 4,  answer[2] = 8
i = 1, suffix = 12, answer[1] = 12
i = 0, suffix = 24, answer[0] = 24
```

Final answer:

```text
[24, 12, 8, 6]
```

## Pitfalls To Watch

- Do not use total product plus division; it violates the problem requirement.
- Update `prefix` and `suffix` only after using them for the current index.
- Single-zero and two-zero cases should work without branches.
- Remember that the output array does not count as extra space for the follow-up.
- State clearly whether your prefix/suffix includes or excludes the current index.

## Edge Cases

- Two elements, e.g. `[5, -2] -> [-2, 5]`.
- Exactly one zero, e.g. `[2, 0, 4] -> [0, 8, 0]`.
- Two or more zeros, e.g. `[0, 4, 0] -> [0, 0, 0]`.
- Negative values where sign changes, e.g. `[-1, -2, -3, -4]`.

## Reference Enrichment Log

2026-05-29:

- Existing references cover the meaningful compliant approaches for this problem:
  - `solution_left_right_arrays.py`: explicit left/right product arrays, best for learning the decomposition.
  - `solution_prefix_suffix.py`: optimized two-pass output-array solution, best for interviews and the O(1) extra-space follow-up.
- Other commonly discussed directions were intentionally not promoted into `solutions/`:
  - Brute force is useful as a mental baseline but violates the required O(n) time target.
  - Total product plus division can be made to handle zeros, but division is explicitly disallowed by the problem.
- A good interview explanation should therefore focus on "left of i" times "right of i", then show how to compress the explicit arrays into one output array plus a running suffix.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
