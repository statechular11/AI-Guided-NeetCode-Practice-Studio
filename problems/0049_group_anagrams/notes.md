# Notes - 49. Group Anagrams

## Core Idea

Choose a canonical representation that is identical for anagrams:

- sorted characters, e.g. `"tea" -> "aet"`
- count tuple, e.g. 26 lowercase letter counts

Use that representation as the hash-map key.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_sorted_key.py` | Easiest correct implementation. | Time: O(n*k log k); Space: O(n*k) |
| `solution_count_tuple_key.py` | Optimized lowercase-English key. | Time: O(n*k); Space: O(n*k) |

## Pitfalls To Watch

- The order of groups and order inside groups do not matter for this problem.
- A list cannot be a dictionary key; convert character counts to a tuple.
- Do not compare each pair of strings; grouping by canonical key is the point.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
