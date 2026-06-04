# Notes - 739. Daily Temperatures

## Core Idea

The stack holds days not yet resolved by a warmer future day. Today's warmer temperature resolves as many previous cooler days as possible.

The main interview pattern is a monotonic stack of unresolved indices. The key
sentence to be able to say out loud is: "When today is warmer than the day on
top of the stack, today is the first warmer day for that stacked index."

This problem also has a useful constraint-aware alternative: temperatures are
bounded from 30 to 100, so a reverse scan can remember the nearest future index
for each exact temperature and look only across the warmer temperature range.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_monotonic_stack.py` | primary solution | Time: O(n); Space: O(n) |
| `solution_next_temperature_table.py` | constraint-aware alternative | Time: O(n); Space: O(1) |
| `solution_brute_force.py` | baseline for understanding | Time: O(n^2); Space: O(1) |

## Variant Notes

- `solution_monotonic_stack.py`: the best default interview solution. Store indices, not temperatures, because the answer needs a distance.
- `solution_next_temperature_table.py`: works because the temperature range is tiny and fixed. It is a good reminder to read constraints for bounded-domain tricks.
- `solution_brute_force.py`: useful for checking intuition, but too slow for the full constraint limit.

## Pitfalls To Watch

- Store indices on the stack. Storing only temperatures loses the distance needed for the output.
- Use `<`, not `<=`, when popping for "warmer" days. Equal temperatures do not resolve the wait.
- For the left-to-right stack version, the stack is unresolved and non-increasing by temperature.
- Leave the default answer as `0` when no warmer future day exists.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
