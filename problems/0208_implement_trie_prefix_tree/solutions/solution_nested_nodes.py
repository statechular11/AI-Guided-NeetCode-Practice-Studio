"""
208. Implement Trie (Prefix Tree) - Character Edges With Terminal Word Marker

Variant role:
    primary design solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Exact search needs terminal marker; prefix search only needs the path to exist.

    This specific variant uses: character edges with terminal word marker.

Key invariant:
    Each trie node represents the prefix formed by the path from the root, while terminal markers distinguish complete words from prefixes.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{}` and the expected result is `[null, null, true, false, true, null, true]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    O(L) operations; Space: O(total chars)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary design solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    208. Implement Trie - nested dictionary nodes reference Core idea: Each node maps characters to children and stores whether a word ends there. Insert walks/creates child nodes; search and startsWith walk existing edges. Complexity: O(L) per operation, where L is word/prefix length.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True
    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.is_word)
    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
    def _walk(self, text: str):
        node = self.root
        for ch in text:
            if ch not in node.children: return None
            node = node.children[ch]
        return node
