"""
242. Valid Anagram - Fixed Character Counts Reference

Return whether two lowercase English strings are anagrams.

Variant role:
    Primary interview solution for lowercase English letters.

Core idea:
    Count the net character balance between the two strings. Increment for
    characters in `s`, decrement for characters in `t`, and require every count
    to return to zero.

Why net balance works:
    An anagram uses exactly the same multiset of characters. Adding one for the
    first string and subtracting one for the second leaves zero in every bucket
    if and only if all character frequencies match.

Walkthrough:
    For:

        s = "rat"
        t = "car"

    after processing both strings, the balance for r, t, c, and a cannot all be
    zero, so the strings are not anagrams.

Why check length first:
    Different lengths cannot be anagrams, and the early return avoids doing
    unnecessary counting.

Complexity:
    Time:
        O(n)

    Space:
        O(1), because there are 26 lowercase English letters.

When to choose this variant:
    Use this in interviews when the alphabet is fixed. It avoids hash-map
    overhead and makes the frequency invariant explicit.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        base = ord("a")
        for left, right in zip(s, t):
            counts[ord(left) - base] += 1
            counts[ord(right) - base] -= 1
        return all(count == 0 for count in counts)
