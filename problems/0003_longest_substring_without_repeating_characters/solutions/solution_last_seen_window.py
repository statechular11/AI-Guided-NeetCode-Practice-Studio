"""
3. Longest Substring Without Repeating Characters - last-seen index reference

Variant role:
    Primary optimized interview solution. This is the cleanest version once the
    sliding-window invariant is comfortable.

Core idea:
    Store the most recent index for each character. When `s[right]` has appeared
    inside the current window, jump `left` directly to one position after that
    previous occurrence. This skips the repeated one-by-one removals used by the
    set-window version.

Invariant:
    After processing index `right`, the substring `s[left:right + 1]` contains
    no duplicate characters, and `left` never moves backward.

The important boundary check:
    A character can have appeared earlier but still be irrelevant if that earlier
    occurrence is outside the current window. Therefore, only update `left` when
    `last_seen[ch] >= left`.

    Equivalently:

        left = max(left, last_seen[ch] + 1)

    after checking that `ch` has been seen before.

Step-by-step trace:
    s = "abba"

    right = 0, ch = "a":
        last_seen has no "a"; window = "a"; left = 0; best = 1
    right = 1, ch = "b":
        last_seen has no "b"; window = "ab"; left = 0; best = 2
    right = 2, ch = "b":
        previous "b" is at 1, inside the window, so left jumps to 2;
        window = "b"; best remains 2
    right = 3, ch = "a":
        previous "a" is at 0, outside the current window `[2, 3]`, so left
        stays 2; window = "ba"; best remains 2

Why `left` must not move backward:
    In "abba", if the final "a" moved `left` back to 1, the window would become
    "bba", which contains duplicate "b". The max/check preserves the current
    valid window boundary.

Complexity:
    Time: O(n), one pass through the string.
    Space: O(min(n, alphabet size)).

Interview note:
    Phrase `left` as "the first index of the current valid window" and
    `last_seen[ch]` as "where the current character last appeared." The whole
    solution is the decision of whether that previous appearance is inside or
    outside the current window.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best
