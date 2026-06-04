"""
271. Encode and Decode Strings - length-prefix codec reference

Variant role:
    Primary robust codec solution.

Problem:
    Encode a list of arbitrary strings into one string, then decode it back to
    the exact original list.

Core idea:
    Prefix each string with its length and a separator:

        <length>#<string>

    During decode, read digits until `#`, parse the length, then consume exactly
    that many characters as the next string.

Why this is robust:
    The payload string may contain `#`, digits, spaces, or be empty. That is
    fine because the decoder trusts the length, not a delimiter search inside
    the payload.

Example:
    ["Hello", "World"] becomes:

        "5#Hello5#World"

    Decode reads length 5, takes "Hello", then reads length 5, takes "World".

    ["", "#"] becomes:

        "0#1##"

    The empty string has length 0, and the literal "#" has length 1.

Complexity:
    Time: O(total characters)
    Space: O(total characters)
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result: list[str] = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length

        return result
