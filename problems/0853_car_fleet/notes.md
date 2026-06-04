# Notes - 853. Car Fleet

## Core Idea

Process cars from closest to target backward. A car with an arrival time less than or equal to the fleet ahead merges into it.

The crucial simplification is to stop simulating positions over time. Once cars
are sorted by starting position from closest to target to farthest, each farther
car only needs its arrival time compared with the fleet directly ahead.

If the farther car arrives earlier than or at the same time as the fleet ahead,
it catches that fleet before or exactly at target. If it arrives later, it can
never catch the fleet ahead and must start a new fleet.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_arrival_stack.py` | primary solution | Time: O(n log n); Space: O(n) |
| `solution_explicit_time_stack.py` | stack-shaped variant | Time: O(n log n); Space: O(n) |
| `solution_exact_time_comparison.py` | precision-aware alternative | Time: O(n log n); Space: O(n) |

## Variant Notes

- `solution_arrival_stack.py`: compact interview target. Track only the latest arrival time among fleets ahead.
- `solution_explicit_time_stack.py`: same idea, but the stack explicitly stores fleet arrival times. This maps more directly to the Stack tag.
- `solution_exact_time_comparison.py`: avoids floating-point arrival times by comparing fractions with cross multiplication.

## Pitfalls To Watch

- Sort by position, not by speed or arrival time alone. Road order determines which cars can catch which fleets.
- Process from closest to target to farthest. Reversing that mental direction is the most common source of wrong merges.
- Use a strict `>` check for new fleets. Equal arrival time means the car catches the fleet exactly at target and should merge.
- The stack, if used, stores fleet arrival times rather than raw cars.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
