"""
76. Minimum Window Substring - brute force coverage baseline

Variant role:
    Educational baseline. This is too slow for the full constraint, but it
    makes the validity condition and the minimum-window objective explicit.

Core idea:
    Try every left boundary. Expand the right boundary until the substring
    covers all required characters from `t`, including duplicates. The first
    valid right boundary for a fixed left is the smallest valid window starting
    at that left, so record it and move to the next left.

Validity:
    A window covers `t` when, for every character `ch` in `t`:

        window_count[ch] >= need_count[ch]

    This is why duplicates in `t` matter. If `t = "aa"`, a window containing
    one `"a"` is not valid.

Example:
    s = "ADOBECODEBANC", t = "ABC"

    Starting at index 0, the first valid window is "ADOBEC".
    Later starts eventually find the shorter valid window "BANC".

Optimization insight:
    Rebuilding a window for every left boundary repeats work. Sliding window
    keeps one moving window: expand right until valid, then move left while
    preserving validity.

Complexity:
    Let m = len(s), n = len(t), and k = distinct characters in t.
    Time: O(m^2 + n), with O(1) per expansion using a missing counter.
    Space: O(k).
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        best_start = 0
        best_len = float("inf")

        for left in range(len(s)):
            window: dict[str, int] = defaultdict(int)
            missing = len(t)

            for right in range(left, len(s)):
                ch = s[right]
                window[ch] += 1
                if ch in need and window[ch] <= need[ch]:
                    missing -= 1

                if missing == 0:
                    window_len = right - left + 1
                    if window_len < best_len:
                        best_len = window_len
                        best_start = left
                    break

        if best_len == float("inf"):
            return ""
        return s[best_start : best_start + best_len]
