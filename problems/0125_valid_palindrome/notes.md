# Notes - 125. Valid Palindrome

## Core Idea

Skip punctuation from both ends before comparing lowercase characters. A string with no alphanumeric characters is valid.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_normalize_then_compare.py` | easy baseline | Time: O(n); Space: O(n) |
| `solution_two_pointers.py` | primary optimized solution | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- State what each pointer means before coding.
- Move pointers only after using the current state.
- Treat digits as valid alphanumeric characters; `"0P"` is not a palindrome.
- Skip punctuation before comparing, then compare lowercase forms.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
