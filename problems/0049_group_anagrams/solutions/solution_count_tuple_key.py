"""
49. Group Anagrams - Character-Count Key Reference

Group strings that are anagrams of each other.

Variant role:
    Optimized representative solution for lowercase English strings.

Core idea:
    Instead of sorting each word, count its letters. All anagrams have the same
    26-number count tuple, so that tuple can be used as a dictionary key.

Why the key works:
    For lowercase English letters, a 26-length frequency vector completely
    describes the character multiset. Anagrams share the same vector; non-
    anagrams differ in at least one count.

Walkthrough:
    For:

        "eat" -> one a, one e, one t
        "tea" -> one a, one e, one t

    their count tuples match, so they are grouped together.

Why tuple:
    Lists are mutable and cannot be dictionary keys. A tuple is immutable and
    safely represents the count signature.

Complexity:
    Time:
        O(n * k), where n is the number of strings and k is average length.

    Space:
        O(n * k), counting the grouped output.

When to choose this variant:
    Use this when the alphabet is fixed and you want to avoid sorting every
    word. It is the stronger asymptotic reference for lowercase English input.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
        base = ord("a")
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - base] += 1
            groups[tuple(counts)].append(word)
        return list(groups.values())
