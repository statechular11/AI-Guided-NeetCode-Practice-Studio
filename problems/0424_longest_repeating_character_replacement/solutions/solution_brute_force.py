"""
424. Longest Repeating Character Replacement - brute force baseline

Variant role:
    Educational baseline. This version is too slow for the full constraint, but
    it exposes the central identity used by every optimized solution.

Core idea:
    Enumerate each possible left boundary. As the right boundary expands, keep
    character frequencies and the largest frequency in the current substring.

    For a window of length `window_len`, if the most frequent character appears
    `max_freq` times, then:

        replacements_needed = window_len - max_freq

    Those are exactly the characters we must replace to make the whole window
    equal to the majority character.

Why we can stop early for a fixed left boundary:
    As `right` expands by one character, `window_len - max_freq` never
    decreases. Adding a character either increases both `window_len` and
    `max_freq` by 1, leaving the value unchanged, or increases only
    `window_len`, making the value larger. So once a window needs more than `k`
    replacements, longer windows with the same left boundary cannot become
    valid again.

Example:
    s = "AABABBA", k = 1

    For left = 0:
        "A"      -> len 1, max A count 1, replacements 0
        "AA"     -> len 2, max A count 2, replacements 0
        "AAB"    -> len 3, max A count 2, replacements 1
        "AABA"   -> len 4, max A count 3, replacements 1, best = 4
        "AABAB"  -> len 5, max A count 3, replacements 2, stop this start

Complexity:
    Time: O(n^2), because every start may scan many right endpoints.
    Space: O(1), because the alphabet is fixed to 26 uppercase English letters.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0

        for left in range(len(s)):
            counts: dict[str, int] = defaultdict(int)
            max_freq = 0

            for right in range(left, len(s)):
                counts[s[right]] += 1
                max_freq = max(max_freq, counts[s[right]])
                window_len = right - left + 1

                if window_len - max_freq > k:
                    break

                best = max(best, window_len)

        return best
