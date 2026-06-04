# Notes - 66. Plus One

## Core Idea

Adding one starts at the least-significant digit, which is the right edge of the
array. Only the suffix of trailing 9s needs to turn into 0s; the first non-9
digit to the left can be incremented and then the operation is done.

Useful ways to implement the same carry idea:

- In-place shortcut: scan from right to left, increment the first digit below
  9, and return immediately.
- General carry template: keep an explicit `carry`, compute each output digit
  with `divmod`, and build a new result array.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_carry_from_right.py` | primary in-place solution | Time: O(n); Space: O(1) extra |
| `solution_general_carry_output.py` | transferable carry-template variant | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Handle the all-9s case: `[9, 9] -> [1, 0, 0]`.
- Stop immediately after incrementing a non-9 digit in the in-place solution.
- If building a new result from right to left, remember to reverse it or append
  to the front.
- Do not convert the digit array into an integer; the point is manual decimal
  carry over a potentially large integer representation.
- The input has no leading zeros, and the only valid new leading digit is `1`.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
