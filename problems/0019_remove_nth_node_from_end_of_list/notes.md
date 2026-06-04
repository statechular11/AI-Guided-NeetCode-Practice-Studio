# Notes - 19. Remove Nth Node From End of List

## Core Idea

This is a linked-list deletion problem, so the important node is usually the
predecessor of the node you want to remove. A dummy node before `head` gives
you a predecessor even when the real target is the original head.

For the follow-up one-pass solution, keep `fast` exactly `n + 1` links ahead of
`slow` when both start at `dummy`. When `fast` becomes `None`, `slow` is sitting
right before the nth node from the end, so the deletion is `slow.next =
slow.next.next`.

For the clarity-first two-pass solution, count the length, convert "nth from the
end" into a front index `length - n`, then walk from `dummy` to the predecessor.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_two_pointers.py` | primary one-pass solution | Time: O(n); Space: O(1) |
| `solution_two_pass_length.py` | baseline clarity solution | Time: O(n); Space: O(1) |

## Pitfalls To Watch

- Use a dummy node so deleting the head does not need a special branch.
- In the one-pass version, be precise about the gap invariant. Starting both
  pointers at `dummy` means advancing `fast` `n + 1` times.
- Stop on the predecessor, not the target. Linked-list deletion needs the node
  before the target so you can rewrite its `.next`.
- The constraints guarantee `1 <= n <= sz`, so you do not need defensive
  invalid-`n` handling for LeetCode.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
