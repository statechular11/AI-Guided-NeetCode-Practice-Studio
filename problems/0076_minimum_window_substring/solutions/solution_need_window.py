"""
76. Minimum Window Substring - formed/required cover-and-shrink window

Variant role:
    Primary interview solution. This version keeps separate maps for required
    counts and current window counts, then uses a `formed` counter to know when
    all required character types are satisfied.

Core idea:
    Expand the right side until the window covers every required character from
    `t`, including multiplicities. Once the window is valid, shrink from the
    left while it remains valid, recording every valid candidate before removing
    its left character.

Definitions:
    `need[ch]`:
        How many copies of `ch` must appear in a valid window.
    `window[ch]`:
        How many copies of `ch` are currently inside `s[left:right + 1]`.
    `required`:
        Number of distinct character types in `t`.
    `formed`:
        Number of distinct character types `ch` where
        `window[ch] >= need[ch]`.

Invariant:
    `formed == required` means the current window covers all characters in `t`.
    It does not mean the window is minimal. Minimality is achieved by the inner
    shrink loop.

Step-by-step trace:
    s = "ADOBECODEBANC", t = "ABC"

    1. Expand until the first valid window "ADOBEC"; now formed == 3.
    2. Record it, then remove from the left.
    3. Removing "A" breaks validity, so expansion resumes.
    4. Later the window reaches "...BANC"; shrinking removes irrelevant and
       surplus characters until "BANC" is recorded as the best valid window.

Pitfalls:
    - Count duplicates in `t`; one copy is not enough for `t = "aa"`.
    - Record the current valid window before removing the left character.
    - When shrinking, decrement `formed` only when a needed character drops
      below its required count.

Complexity:
    Time: O(len(s) + len(t)), because each pointer moves forward at most once.
    Space: O(k), where k is the number of distinct characters in `t`.
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)
        window: dict[str, int] = defaultdict(int)
        required = len(need)
        formed = 0
        left = 0
        best = (float("inf"), 0, 0)

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right + 1)

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2]]
