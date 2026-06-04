# Notes - 167. Two Sum II - Input Array Is Sorted

## Core Idea

Use sorted order to decide which pointer to move: small sum moves left up; large sum moves right down.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_two_pointers.py` | primary solution | Time: O(n); Space: O(1) |
| `solution_binary_search_partner.py` | alternative sorted-array reference | Time: O(n log n); Space: O(1) |

## Pitfalls To Watch

- State what each pointer means before coding.
- Move pointers only after using the current state.
- Return 1-indexed positions, not 0-indexed positions.
- Use sorted order to decide pointer movement; do not fall back to a hash map if
  the goal is O(1) extra space.
- The prompt guarantees exactly one solution, so falling through the loop is
  outside valid test inputs. A defensive `return []` is optional.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
