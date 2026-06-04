"""
3. Longest Substring Without Repeating Characters - set window reference

Variant role:
    Learning-friendly sliding-window solution. Use this when you want the
    invariant to be visually obvious: the set stores exactly the characters
    currently inside the window.

Core idea:
    Keep a window `s[left:right + 1]` with no duplicate characters. Before
    adding `s[right]`, if that character already appears in the window, move
    `left` rightward and remove characters from the set until the duplicate copy
    is gone. Then adding `s[right]` restores the no-duplicate invariant.

Invariant:
    After each iteration, `seen == set(s[left:right + 1])`, and every character
    in that window is unique.

Why the while-loop is necessary:
    The old copy of `s[right]` may not be exactly at `left`.

    For `s = "abba"`, when `right` reaches the second "b", the window is "ab".
    Removing only one character would remove "a", leaving the old "b" still in
    the set. The loop must continue until the old "b" leaves the window.

Step-by-step trace:
    s = "pwwkew"

    right = 0, "p": seen = {"p"},       window = "p",   best = 1
    right = 1, "w": seen = {"p", "w"},  window = "pw",  best = 2
    right = 2, "w": duplicate "w"; remove "p", then old "w";
                    add new "w",       window = "w",   best = 2
    right = 3, "k": seen = {"w", "k"},  window = "wk",  best = 2
    right = 4, "e": seen = {"w","k","e"}, window = "wke", best = 3
    right = 5, "w": duplicate "w"; remove old "w";
                    add new "w",       window = "kew", best = 3

Complexity:
    Time: O(n), because each character is added once by `right` and removed at
    most once by `left`.
    Space: O(min(n, alphabet size)).

Interview note:
    This version is usually easier to derive than the last-seen-index jump. If
    asked to optimize the mechanics, explain that the next variant jumps `left`
    directly after the old duplicate instead of removing one character at a
    time.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        left = 0
        best = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            best = max(best, right - left + 1)

        return best
