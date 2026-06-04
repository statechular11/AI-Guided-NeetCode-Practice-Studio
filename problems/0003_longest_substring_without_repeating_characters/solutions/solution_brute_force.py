"""
3. Longest Substring Without Repeating Characters - brute force baseline

Variant role:
    Educational baseline. This is not the intended interview solution for the
    full constraint, but it makes the optimization target very clear.

Core idea:
    Try every possible starting index. From that start, extend the substring to
    the right until the first repeated character appears. Every prefix before
    that repeated character is a valid no-duplicate substring, so update the
    best length as the scan grows.

Why this is correct:
    Any substring has a left boundary. By enumerating every left boundary and
    extending until the first duplicate, this method considers the longest valid
    substring beginning at each position. The answer is the maximum of those
    per-start lengths.

Example:
    s = "abcabcbb"

    start = 0: grows "a", "ab", "abc", then stops at the second "a"
    start = 1: grows "b", "bc", "bca", then stops at the second "b"
    start = 2: grows "c", "ca", "cab", then stops at the second "c"

    The best length seen is 3.

Optimization insight:
    This baseline repeats a lot of work. When a duplicate is found, the next
    useful window can reuse information from the current window instead of
    rebuilding a set from scratch. That reuse is exactly what sliding window
    gives us.

Complexity:
    Time: O(n^2) in the worst case, for example a string with all unique
    characters.
    Space: O(min(n, alphabet size)) for the per-start set.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0

        for start in range(len(s)):
            seen: set[str] = set()
            for end in range(start, len(s)):
                if s[end] in seen:
                    break
                seen.add(s[end])
                best = max(best, end - start + 1)

        return best
