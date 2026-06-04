"""
567. Permutation in String - sorted-window brute force baseline

Variant role:
    Educational baseline. This is not the intended solution for the full input
    size, but it makes the problem definition concrete.

Core idea:
    A permutation has the same characters as `s1`, just in a different order.
    So every candidate substring of length `len(s1)` can be sorted and compared
    with `sorted(s1)`.

Why fixed length matters:
    We only need to inspect substrings whose length equals `len(s1)`. Shorter
    substrings cannot contain all characters, and longer substrings contain too
    many characters to be a permutation of `s1`.

Example:
    s1 = "ab", s2 = "eidbaooo"

    sorted(s1) = ["a", "b"]
    Windows of length 2:
        "ei" -> ["e", "i"]
        "id" -> ["d", "i"]
        "db" -> ["b", "d"]
        "ba" -> ["a", "b"]  match

Optimization insight:
    Sorting each window repeats work. The optimized versions keep character
    counts and update only the character that enters and leaves the window.

Complexity:
    Let n = len(s1), m = len(s2).
    Time: O((m - n + 1) * n log n)
    Space: O(n)
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        target = sorted(s1)
        for left in range(len(s2) - n + 1):
            if sorted(s2[left : left + n]) == target:
                return True

        return False
