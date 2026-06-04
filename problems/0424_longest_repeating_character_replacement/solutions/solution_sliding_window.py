"""
424. Longest Repeating Character Replacement - stale max-frequency window

Variant role:
    Primary interview solution. It uses the same validity identity as the exact
    variant, but keeps a nondecreasing `max_count` instead of recomputing the
    true maximum count after every shrink.

Core idea:
    A window can be turned into a single repeated character if every
    non-majority character is replaced. Therefore:

        replacements_needed = window_len - max_frequency_in_window

    The exact window is valid when `replacements_needed <= k`.

Stale `max_count` optimization:
    `max_count` stores the largest frequency any character has reached while
    scanning. When `left` moves, the true current maximum frequency might drop,
    but `max_count` is intentionally not reduced.

Why stale `max_count` is safe:
    A stale value can make the current window look slightly more valid than it
    really is, but it cannot invent a larger answer.

    When `max_count` increases, it is exact for the current window, so any new
    longer window admitted by that increase is genuinely valid. When
    `max_count` is stale, it does not create a new higher frequency; it only
    keeps the allowed window length tied to a frequency that was exact earlier.
    That can delay shrinking, but it cannot justify a best length beyond one
    already made possible when the maximum frequency was current.

Operational invariant:
    The algorithm keeps the window from growing beyond what the best historical
    `max_count` can support:

        window_len - max_count <= k

    Whenever that inequality fails, move `left` until the window length is back
    within the allowed size.

Step-by-step trace:
    s = "AABABBA", k = 1

    right = 0..3 gives window "AABA":
        counts A=3, B=1, max_count=3
        window_len - max_count = 4 - 3 = 1, best = 4

    right = 4 gives window "AABAB":
        counts A=3, B=2, max_count=3
        5 - 3 = 2, so shrink left once

    Later `max_count` may remain 3 even if the current true max is lower. That
    does not hurt the final answer because best length 4 was already justified
    by the earlier valid window "AABA".

Complexity:
    Time: O(n), one pass with each character added once and removed at most once.
    Space: O(1), for 26 uppercase letters.

Interview note:
    If the stale-max proof feels hard to explain, start with the exact-max
    variant first. Then say the optimized version avoids recomputing the maximum
    because a stale maximum only delays shrinking and does not create a false
    larger best.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict[str, int] = defaultdict(int)
        left = 0
        max_count = 0
        best = 0

        for right, ch in enumerate(s):
            counts[ch] += 1
            max_count = max(max_count, counts[ch])

            while right - left + 1 - max_count > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
