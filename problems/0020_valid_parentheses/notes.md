# Notes - 20. Valid Parentheses

## Core Idea

Use a stack because bracket matching is last-in, first-out. At the end, no unmatched openings may remain.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_stack.py` | primary solution | Time: O(n); Space: O(n) |
| `solution_expected_closers.py` | equivalent stack state representation | Time: O(n); Space: O(n) |
| `solution_repeated_reduction.py` | learning baseline | Time: O(n^2); Space: O(n) |

## Variant Notes

The primary stack solution stores unmatched opening brackets:

```text
stack = openings that still need to be closed
```

When a closing bracket appears, it must match the most recent unmatched opening.
That is the core last-in, first-out invariant.

The expected-closers variant stores future obligations instead:

```text
stack = closing brackets expected in the future
```

This is often easier to reason about because when a closing bracket appears, it
must equal the top of the stack directly.

The repeated-reduction baseline removes adjacent valid pairs like `()`, `[]`,
and `{}` until the string stops changing. It is useful for intuition because
valid nested structures reduce from the inside out, but it is not the interview
target because it can be O(n^2).

## Pitfalls To Watch

- Be explicit about what the stack stores: openings or expected closers.
- A closing bracket with an empty stack is immediately invalid.
- At the end, the stack must be empty; otherwise there are unmatched openings.
- `([)]` is invalid because nesting order matters, even though counts match.
- Counts alone are insufficient for multiple bracket types and nesting order.

## Reference Enrichment Log

2026-05-29:

- Expanded the primary opening-bracket stack reference with failure examples and
  the stack invariant.
- Added `solution_expected_closers.py` as an equivalent but often easier state
  representation: push the closing bracket you expect to see later.
- Added `solution_repeated_reduction.py` as an O(n^2) learning baseline that
  shows valid strings can be reduced from innermost adjacent pairs.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
