# Notes - 2. Add Two Numbers

## Core Idea

The reverse digit order means a single forward traversal plus carry is enough.
At every step, add the current digit from each list plus the incoming carry,
write `total % 10`, and carry `total // 10` into the next digit.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_digit_carry.py` | primary linked-list solution | Time: O(max(n,m)); Space: O(max(n,m)) |
| `solution_recursive_carry.py` | recursive control-flow variant | Time: O(max(n,m)); Space: O(max(n,m)) recursion stack |
| `solution_reuse_nodes.py` | mutation tradeoff / allocation-minimizing variant | Time: O(max(n,m)); Space: O(1) auxiliary |

## Pitfalls To Watch

- Continue while `l1` or `l2` or `carry`; the final carry may create one extra
  node.
- `divmod(total, 10)` is a tidy way to compute `(carry, digit)` when assigned as
  `carry, digit = divmod(total, 10)`.
- Lists can have different lengths; treat missing digits as 0.
- Avoid converting the whole linked list to an integer as the main interview
  answer. The intended invariant is digit-by-digit carry propagation.
- The input-reusing reference mutates nodes. Prefer the dummy-node version when
  preserving inputs or keeping the explanation simple matters.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
