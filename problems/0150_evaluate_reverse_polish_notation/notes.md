# Notes - 150. Evaluate Reverse Polish Notation

## Core Idea

Pop operands in right-to-left order: second pop is the left operand. Division truncates toward zero.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_operand_stack.py` | primary solution | Time: O(n); Space: O(n) |
| `solution_operand_stack_integer_division.py` | Python division-rule variant | Time: O(n); Space: O(n) |
| `solution_recursive_from_right.py` | educational parser/tree variant | Time: O(n); Space: O(n) |

## Variant Notes

The primary operand-stack solution is the interview target:

```text
number   -> push it
operator -> pop right, pop left, apply left operator right, push result
```

The operand order is the main correctness invariant. For `["4", "13", "5",
"/", "+"]`, the `/` operator pops `5` first and `13` second, so the operation
is:

```text
13 / 5
```

not:

```text
5 / 13
```

The integer-division variant uses the same stack idea but makes LeetCode's
truncation-toward-zero rule explicit with integer arithmetic. This avoids the
common Python pitfall:

```text
7 // -3 == -3       # floor division, wrong for this problem
7 / -3  -> -2       # truncate toward zero, expected behavior
```

The recursive right-to-left variant treats RPN as a postfix expression tree:
the final token is the root, and recursive calls consume the right operand
before the left operand. It is useful for understanding expression structure,
but the iterative stack version is the practical interview answer.

## Pitfalls To Watch

- State what the stack stores: values, indices, partial results, or design state.
- For arithmetic stacks, preserve operand order.
- The first popped value is the right operand; the second popped value is the
  left operand.
- Do not use Python `//` for division with negative operands; it floors instead
  of truncating toward zero.
- Negative numbers like `"-11"` are operands, not operators.
- The input is guaranteed valid, so the final stack should contain exactly one
  value.

## Reference Enrichment Log

2026-05-29:

- Expanded `solution_operand_stack.py` with operand-order examples and the
  truncation-toward-zero division rule.
- Added `solution_operand_stack_integer_division.py` to show a Python-safe
  integer helper for division.
- Added `solution_recursive_from_right.py` as an educational parser/tree view of
  postfix notation.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
