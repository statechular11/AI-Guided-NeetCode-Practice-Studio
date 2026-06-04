"""
49. Group Anagrams - Sorted Key Reference

Group strings that are anagrams of each other.

Variant role:
    Easiest interview solution to implement correctly.

Core idea:
    Anagrams become identical after sorting their characters. Use the sorted
    string as the dictionary key and collect all words with the same key.

Why the key works:
    Sorting removes the original character order and leaves only the multiset of
    characters. Two words with the same sorted key contain exactly the same
    letters with the same frequencies.

Example:
    The strings:

        "eat", "tea", "ate"

    all map to:

        "aet"

    so they end up in one group.

Tradeoff:
    Sorting each word is simple, but costs O(k log k) per word of length k. A
    frequency tuple key can reduce that to O(k) for fixed lowercase English.

Complexity:
    Time:
        O(n * k log k)

    Space:
        O(n * k)

When to choose this variant:
    Use this when implementation clarity matters most. It is often accepted and
    easy to explain.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return list(groups.values())
