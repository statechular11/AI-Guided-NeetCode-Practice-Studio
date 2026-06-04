"""
211. Design Add and Search Words Data Structure - length buckets with wildcard scan

Variant role:
    educational non-trie baseline

Core idea:
    Group inserted words by length, then search only candidates whose length matches the pattern.

Key invariant:
    A pattern with dots can only match words of the same length.

Mechanics:
    For search, compare every same-length word character by character, treating '.' as a wildcard.

Common pitfalls:
    This is simple but can be slow when many words share a length. The trie prunes by fixed-prefix characters.

Complexity:
    addWord: O(1) amortized; search: O(kL) for same-length words; Space: O(total characters)

When to choose this variant:
    Use this to understand the design tradeoff that motivates the trie wildcard DFS.
"""

from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.words_by_length: dict[int, list[str]] = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.words_by_length[len(word)].append(word)

    def search(self, word: str) -> bool:
        for candidate in self.words_by_length.get(len(word), []):
            if all(p == "." or p == c for p, c in zip(word, candidate)):
                return True
        return False
