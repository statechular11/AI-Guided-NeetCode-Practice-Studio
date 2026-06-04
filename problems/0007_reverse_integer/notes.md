# Notes - 7. Reverse Integer

## Core Idea

This is digit manipulation rather than bit manipulation. The intended fixed-width
integer solution builds the reversed value one decimal digit at a time and
checks overflow before pushing the next digit.

Useful ways to see the same transformation:

- Guarded digit pop/push: pop `x % 10`, push with `result * 10 + digit`, and
  reject before the push would exceed the signed 32-bit range.
- String slicing baseline: reverse the decimal characters, then range-check.
  This is easy in Python but does not exercise the no-64-bit-storage constraint.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_digit_pop_push.py` | primary math solution | Time: O(digits); Space: O(1) |
| `solution_string_slice.py` | Python baseline contrast | Time: O(digits); Space: O(digits) |

## Pitfalls To Watch

- The signed 32-bit range is asymmetric: `[-2147483648, 2147483647]`.
- Positive reversed values can end in at most boundary digit `7`, while
  negative reversed values can reach absolute boundary digit `8`.
- Check overflow before `result = result * 10 + digit` if honoring the prompt's
  fixed-width-storage assumption.
- Work with `abs(x)` and reapply the sign; Python modulo on negative numbers is
  not the digit-pop behavior most people expect from languages like C++/Java.
- Trailing zeros need no special case: `120` naturally becomes `21`.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
