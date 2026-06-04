"""
125. Valid Palindrome - Two Pointers Reference

Return whether a string is a palindrome after ignoring non-alphanumeric
characters and case.

Variant role:
    Primary O(1)-extra-space interview solution.

Core idea:
    Compare meaningful characters from both ends. Skip non-alphanumeric
    characters, lowercase before comparing, and move inward after a match.

Pointer invariant:
    Before each comparison, `left` and `right` either point to meaningful
    alphanumeric characters or have crossed. If the meaningful characters differ,
    the normalized string cannot be a palindrome.

Example:
    For:

        "A man, a plan, a canal: Panama"

    the meaningful lowercase sequence is:

        "amanaplanacanalpanama"

    which reads the same forward and backward.

Pitfall:
    Skip punctuation before comparing. Also lowercase both sides before checking
    equality.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews. It avoids allocating the normalized string while
    keeping the same logical comparison.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
