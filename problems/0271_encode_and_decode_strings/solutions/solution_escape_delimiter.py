"""
271. Encode and Decode Strings - counted escaped delimiter codec

Variant role:
    alternative robust codec reference

Core idea:
    Use a count prefix for the number of strings, then join escaped payloads with a delimiter.

Key invariant:
    During decode, an unescaped delimiter separates strings; escaped delimiter and escape characters belong to the payload.

Mechanics:
    Escape backslash and '#'. Prefix the encoded stream with the number of strings so an empty list is distinguishable from [''].

Common pitfalls:
    A pure delimiter codec cannot represent arbitrary strings unless the delimiter itself is escaped.

Complexity:
    Time: O(total characters); Space: O(total characters)

When to choose this variant:
    Use this to compare delimiter escaping with the simpler length-prefix reference.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        def escape(text: str) -> str:
            out = []
            for ch in text:
                if ch in {"\\", "#"}:
                    out.append("\\")
                out.append(ch)
            return "".join(out)

        return str(len(strs)) + "#" + "#".join(escape(s) for s in strs)

    def decode(self, s: str) -> List[str]:
        sep = s.index("#")
        count = int(s[:sep])
        if count == 0:
            return []

        body = s[sep + 1:]
        result: list[str] = []
        current: list[str] = []
        escaped = False

        for ch in body:
            if escaped:
                current.append(ch)
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == "#" and len(result) < count - 1:
                result.append("".join(current))
                current = []
            else:
                current.append(ch)

        result.append("".join(current))
        return result
