"""
567. Permutation in String - deficit sliding window

Variant role:
    Alternative optimized solution. This formulation is compact once the
    invariant clicks, and it is close to a common hand-coded interview approach.

Core idea:
    Start with `need[c] = count of c required by s1`.
    As the right boundary consumes characters from `s2`, decrement `need`.

    Interpretation while scanning:
        need[c] > 0  -> the current window still lacks some c's
        need[c] == 0 -> the current window has exactly enough c's
        need[c] < 0  -> the current window has too many c's

    Whenever adding `s2[right]` makes its count negative, move `left` forward
    and return characters to `need` until that overused character is no longer
    negative.

Why length proves a match:
    After the shrink loop, no count is negative: the current window does not
    overuse any character relative to `s1`. If its length is exactly len(s1),
    then it also cannot be missing any required character, because the total
    number of consumed characters is already len(s1). Therefore all counts are
    zero, and the window is a permutation.

Example:
    s1 = "ab", s2 = "eidbaooo"

    need starts as a:1, b:1.
    Reading "e" makes e negative, so left moves past "e".
    Reading "i" makes i negative, so left moves past "i".
    Reading "d" makes d negative, so left moves past "d".
    Reading "b" is allowed; window = "b", still missing "a".
    Reading "a" is allowed; window = "ba", length 2, match.

Complexity:
    Time: O(m), because each character enters and leaves the window at most once.
    Space: O(1), for 26 lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        base = ord("a")
        need = [0] * 26
        for ch in s1:
            need[ord(ch) - base] += 1

        left = 0
        for right, ch in enumerate(s2):
            idx = ord(ch) - base
            need[idx] -= 1

            while need[idx] < 0:
                need[ord(s2[left]) - base] += 1
                left += 1

            if right - left + 1 == n:
                return True

        return False
