"""
208. Implement Trie (Prefix Tree) - nested dictionaries with terminal sentinel

Variant role:
    compact design reference

Core idea:
    A trie node can be represented as a dictionary from characters to child dictionaries, with a sentinel key for word endings.

Key invariant:
    Walking a string through nested dictionaries reaches exactly the node for that prefix when it exists.

Mechanics:
    insert creates missing child dictionaries. search requires the terminal sentinel. startsWith only requires the path.

Common pitfalls:
    A prefix path is not necessarily a complete word; keep a terminal marker separate from child edges.

Complexity:
    O(L) per operation; Space: O(total characters)

When to choose this variant:
    Use this for a compact Pythonic trie implementation without a custom node class.
"""

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end] = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self.end in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, text: str):
        node = self.root
        for ch in text:
            if ch not in node:
                return None
            node = node[ch]
        return node
