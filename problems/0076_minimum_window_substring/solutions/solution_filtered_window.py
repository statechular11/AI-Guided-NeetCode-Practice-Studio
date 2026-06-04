"""
76. Minimum Window Substring - filtered relevant-character window

Variant role:
    Optimized variant for strings with many irrelevant characters. It uses the
    same formed/required invariant as the primary solution, but slides over only
    characters that appear in `t`.

Core idea:
    Characters not present in `t` never affect whether a window covers `t`.
    Pre-filter `s` into `(index, character)` pairs for characters in `need`.
    Then run the normal cover-and-shrink window over that shorter filtered list.

Why original indexes are still needed:
    The answer must be a substring of the original `s`, including irrelevant
    characters between relevant endpoints. So when filtered positions `left`
    and `right` form a valid coverage, the actual window is:

        s[filtered[left].index : filtered[right].index + 1]

Example:
    s = "ADOBECODEBANC", t = "ABC"

    Relevant stream:
        (0,A), (3,B), (5,C), (9,B), (10,A), (12,C)

    The filtered window `(9,B), (10,A), (12,C)` maps back to original substring
    `s[9:13] == "BANC"`.

Complexity:
    Time: O(len(s) + len(t)).
    Space: O(k + r), where k is distinct characters in `t` and r is the number
    of relevant characters in `s`.
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        filtered = [(idx, ch) for idx, ch in enumerate(s) if ch in need]
        window: dict[str, int] = defaultdict(int)
        required = len(need)
        formed = 0
        left = 0
        best_start = 0
        best_len = float("inf")

        for right, (right_idx, ch) in enumerate(filtered):
            window[ch] += 1
            if window[ch] == need[ch]:
                formed += 1

            while formed == required:
                left_idx, left_ch = filtered[left]
                window_len = right_idx - left_idx + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left_idx

                window[left_ch] -= 1
                if window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start : best_start + best_len]
