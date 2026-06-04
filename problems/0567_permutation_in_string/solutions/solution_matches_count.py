"""
567. Permutation in String - fixed window with match counter

Variant role:
    Constant-factor optimized fixed-window solution. It avoids comparing all 26
    counts after every slide by tracking how many character slots currently
    match between `need` and `window`.

Core idea:
    A length-`len(s1)` window is a permutation exactly when all 26 character
    counts match `s1`.

    Instead of checking:

        window == need

    after every slide, keep:

        matches = number of indices i where window[i] == need[i]

    A permutation exists when `matches == 26`.

Mechanics:
    When one character enters, only that character's count can change. Before
    changing it, subtract one match if that slot used to match. After changing
    it, add one match if it matches now. Do the same for the outgoing character.

Example:
    s1 = "ab", s2 = "eidbaooo"

    The fixed window length is 2. When the window reaches "ba", the `a` and `b`
    slots match the target counts, and every other lowercase slot matches at 0,
    so `matches == 26`.

Complexity:
    Time: O(m + 26), one pass through `s2` after initialization.
    Space: O(1), for 26 lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        base = ord("a")
        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - base] += 1
        for ch in s2[:n]:
            window[ord(ch) - base] += 1

        matches = sum(1 for i in range(26) if need[i] == window[i])
        if matches == 26:
            return True

        for right in range(n, len(s2)):
            in_idx = ord(s2[right]) - base
            if window[in_idx] == need[in_idx]:
                matches -= 1
            window[in_idx] += 1
            if window[in_idx] == need[in_idx]:
                matches += 1

            out_idx = ord(s2[right - n]) - base
            if window[out_idx] == need[out_idx]:
                matches -= 1
            window[out_idx] -= 1
            if window[out_idx] == need[out_idx]:
                matches += 1

            if matches == 26:
                return True

        return False
