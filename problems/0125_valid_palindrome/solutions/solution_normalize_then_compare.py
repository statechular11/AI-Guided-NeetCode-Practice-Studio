"""
125. Valid Palindrome - Normalize Then Compare Reference

Return whether a string is a palindrome after ignoring non-alphanumeric
characters and case.

Variant role:
    Simple baseline. Build a lowercase alphanumeric-only string, then compare it
    to its reverse.

Core idea:
    Normalize the input into the exact sequence that matters:

        lowercase alphanumeric characters only

    Then the problem becomes an ordinary palindrome check on that cleaned
    sequence.

Example:
    For:

        "A man, a plan, a canal: Panama"

    normalization produces:

        "amanaplanacanalpanama"

    which reads the same forward and backward.

Tradeoff:
    This version is easy to reason about, but it allocates O(n) extra space for
    the cleaned sequence. The two-pointer version avoids that allocation.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Use it as a clarity baseline. Switch to two pointers when the interviewer
    cares about O(1) extra space.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]
