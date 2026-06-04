"""
17. Letter Combinations of a Phone Number - iterative combination cascade

Variant role:
    alternative BFS-style construction

Core idea:
    Build partial strings one digit at a time, replacing the current frontier with all one-letter extensions.

Key invariant:
    After processing k digits, combos contains exactly every letter string that those first k digits can form.

Mechanics:
    Start with one empty prefix. For each digit, append each mapped letter to each existing prefix. Drop the empty prefix for empty input.

Common pitfalls:
    Do not return [''] for empty input. The empty prefix is only a construction seed.

Complexity:
    Time: O(4^n * n); Space: O(4^n * n)

When to choose this variant:
    Use this when you want to avoid recursion and show the same search tree as a level-by-level expansion.
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combos = [""]
        for digit in digits:
            combos = [prefix + ch for prefix in combos for ch in letters[digit]]
        return combos
