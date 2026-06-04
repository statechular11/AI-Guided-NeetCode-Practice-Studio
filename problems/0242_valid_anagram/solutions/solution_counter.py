"""
242. Valid Anagram - Counter Reference

Return whether two strings are anagrams.

Variant role:
    Clean Pythonic baseline.

Core idea:
    Two strings are anagrams when every character appears the same number of
    times in both strings. `Counter` directly represents that frequency map.

Why equality of counters works:
    A `Counter` maps each character to its frequency. If the two maps are equal,
    every character has the same count on both sides. If any character is
    missing or has a different count, the maps differ and the strings are not
    anagrams.

Example:
    For:

        s = "anagram"
        t = "nagaram"

    both produce the same character counts, so return True.

Complexity:
    Time:
        O(n + m)

    Space:
        O(k), where k is the number of distinct characters.

When to choose this variant:
    Use it when Python standard-library clarity is welcome. For the lowercase
    English constraint, the fixed-count array is the more explicit interview
    implementation.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
