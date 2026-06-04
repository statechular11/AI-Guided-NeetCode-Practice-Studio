# Notes - 621. Task Scheduler

## Core Idea

The formula comes from the most frequent task's gaps.

If the most frequent task appears `max_freq` times, its first `max_freq - 1`
copies create blocks of size `n + 1`:

```text
A _ _ | A _ _ | A        n = 2
```

If multiple task labels tie for the maximum frequency, they occupy the tail
together:

```text
A B C _ | A B C _ | A B C
```

Optimized frame formula:

```text
frame = (max_freq - 1) * (n + 1) + max_count
answer = max(len(tasks), frame)
```

The `max(len(tasks), frame)` part matters because enough filler tasks can remove
all idle time, making the answer just the number of tasks.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_formula.py` | primary optimized solution | Time: O(T + A); Space: O(A), O(1) for uppercase letters |
| `solution_idle_slots.py` | alternative formula derivation | Time: O(T + A log A); Space: O(A) |
| `solution_heap_simulation.py` | process-oriented variant | Time: O(answer log A); Space: O(A) |
| `solution_cooldown_queue.py` | fine-grained timing simulation | Time: O(answer log A); Space: O(A) |

## Pitfalls To Watch

- Formula: include `max_count`, the number of labels tied at maximum frequency.
- Formula: return `max(len(tasks), frame)`, not just the frame length.
- Idle-slot derivation: a filler task can fill at most `max_freq - 1` gaps.
- Heap cycle simulation: do not push a used task back until the cycle ends.
- Cooldown queue simulation: a task run at time `t` is ready again at
  `t + n + 1`.
- Python `heapq` is a min heap, so heap simulations store negative counts to
  pop the task with the largest remaining count.

## Reference Enrichment Log

2026-06-02:

- Expanded `solution_formula.py` to explain the max-frequency frame, the
  `max_count` tail, and why the answer is capped below by `len(tasks)`.
- Added `solution_idle_slots.py` to derive the same greedy result by counting
  forced idle slots and filling them with other tasks.
- Expanded `solution_heap_simulation.py` with cycle mechanics and the
  "do not push back until the cycle ends" invariant.
- Added `solution_cooldown_queue.py` for one-interval-at-a-time heap plus
  cooldown queue simulation, including the `t + n + 1` timing rule.
- Expanded tests for zero cooldown, all-unique tasks, multiple max-frequency
  labels, no-idle filler-heavy cases, and idle-heavy dominant-task cases.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
