# Notes - 0. Template

## Core Idea

Primary section: **Template**

Tags: TBD

Identify the problem invariant before writing code.

Start by making the invariant explicit in one sentence. Then code the smallest version that maintains that invariant on every iteration or recursive call.

## Reference Solution

- `solution_reference.py`: reference reference implementation.

Complexity: TBD

## Pitfalls To Watch

- Write down edge cases before coding, especially empty inputs, duplicates, and boundary sizes.

## Edge Cases

- Minimum input size.
- Repeated values or repeated characters.
- Already-sorted, reverse-sorted, or already-valid inputs when relevant.
- Cases where the answer is empty, zero, or impossible.
- For in-place problems, verify both the returned value and the mutated prefix/object state.

## Interview Explanation Checklist

- State the data structure or invariant first.
- Explain why the loop/recursion makes progress.
- Explain why the chosen update cannot discard a valid answer.
- Give time and space complexity without relying on LeetCode runtime numbers.

## Review Log

Add review observations here after Codex reviews your `solution.py`.
