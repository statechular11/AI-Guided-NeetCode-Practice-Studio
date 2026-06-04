"""
567. Permutation in String - fixed-window counts reference

Variant role:
    Primary learning-friendly solution. This version keeps the fixed-window
    invariant explicit and is usually the easiest correct solution to explain.

Core idea:
    A permutation of `s1` must have:

    1. length exactly `len(s1)`, and
    2. the same character frequencies as `s1`.

    Therefore, slide a fixed-size window of length `len(s1)` over `s2` and
    compare its 26 lowercase-letter counts with the target counts.

Window mechanics:
    Initialize the first window `s2[:len(s1)]`. Then for each next position:

    - add the new right character,
    - remove the character that is now just outside the window on the left,
    - compare the two count arrays.

Example:
    s1 = "adc", s2 = "dcda"

    Fixed window length is 3:
        "dcd" has counts d:2, c:1, a:0 -> not a match
        slide by adding "a" and removing the first "d"
        "cda" has counts a:1, c:1, d:1 -> match

Complexity:
    Time: O(26 * len(s2)), which is O(len(s2)) because 26 is constant.
    Space: O(1), for 26 lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26
        base = ord("a")

        for ch in s1:
            need[ord(ch) - base] += 1
        for ch in s2[:n]:
            window[ord(ch) - base] += 1

        if window == need:
            return True

        for right in range(n, len(s2)):
            window[ord(s2[right]) - base] += 1
            window[ord(s2[right - n]) - base] -= 1
            if window == need:
                return True

        return False
