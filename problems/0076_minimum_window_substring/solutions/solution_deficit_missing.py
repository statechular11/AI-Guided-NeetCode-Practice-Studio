"""
76. Minimum Window Substring - deficit counts with missing total

Variant role:
    Alternative optimized formulation. It tracks how many total required
    characters are still missing, rather than how many distinct character types
    are currently satisfied.

Core idea:
    Start with `need = Counter(t)` and `missing = len(t)`.

    When a right character enters:
        - If `need[ch] > 0`, that character was genuinely still needed, so
          decrement `missing`.
        - Decrement `need[ch]` either way.

    Interpretation after decrement:
        need[ch] > 0  -> the window still lacks some copies of ch
        need[ch] == 0 -> the window has exactly enough copies of ch
        need[ch] < 0  -> the window has extra copies of ch

    When `missing == 0`, the window covers `t`. Then remove unnecessary left
    characters while the window still covers `t`. A left character is
    unnecessary exactly when `need[left_ch] < 0`, meaning it is extra.

Why this works:
    `missing` counts total required characters, including duplicates. So for
    `t = "AABC"`, matching one `A` only reduces missing by one; the second `A`
    still matters. Negative `need` values represent surplus characters that can
    be discarded without breaking coverage.

Example:
    s = "ADOBECODEBANC", t = "ABC"

    The first time `missing` reaches 0 is at "ADOBEC". Later, after expanding
    and discarding surplus characters, the tightest valid window becomes
    "BANC".

Complexity:
    Time: O(len(s) + len(t)), because each index enters once and leaves once.
    Space: O(k), where k is the number of distinct characters in `t`.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

        if best_len == float("inf"):
            return ""
        return s[best_start : best_start + best_len]
