"""
424. Longest Repeating Character Replacement - exact max-frequency window

Variant role:
    Learning-friendly optimized solution. It keeps the validity check exact by
    recomputing the current window's maximum character frequency when needed.

Core idea:
    Maintain a sliding window and character counts for that window. A window is
    valid when:

        window_len - max(counts.values()) <= k

    If the window becomes invalid, move `left` rightward until the formula is
    valid again. Because the alphabet is only uppercase English letters,
    recomputing `max(counts.values())` costs at most 26 checks, which is still
    constant time.

Invariant:
    After the shrink loop, `s[left:right + 1]` can be converted into one
    repeated character using at most `k` replacements.

Step-by-step trace:
    s = "AABABBA", k = 1

    Window "AABA":
        counts A=3, B=1, length=4
        replacements = 4 - 3 = 1, valid, best = 4

    Extend to "AABAB":
        counts A=3, B=2, length=5
        replacements = 5 - 3 = 2, invalid
        shrink from the left until valid again.

Why this variant is useful:
    It is often the easiest version to explain first because the value in the
    validity formula is always the true current maximum frequency. After this is
    clear, the primary reference shows how to avoid recomputing that maximum.

Complexity:
    Time: O(26 * n), which is O(n) for the fixed uppercase alphabet.
    Space: O(1), for at most 26 counts.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict[str, int] = defaultdict(int)
        left = 0
        best = 0

        for right, ch in enumerate(s):
            counts[ch] += 1

            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
