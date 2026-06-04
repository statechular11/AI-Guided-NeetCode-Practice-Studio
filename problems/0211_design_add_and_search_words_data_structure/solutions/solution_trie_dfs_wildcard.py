"""
211. Design Add and Search Words Data Structure - Trie Search That Branches On Dot Wildcard

Variant role:
    primary design solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The dot wildcard turns trie search into DFS over all child branches.

    This specific variant uses: trie search that branches on dot wildcard.

Key invariant:
    Each trie node represents the prefix formed by the path from the root, while terminal markers distinguish complete words from prefixes.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{}` and the expected result is `[null, null, null, null, false, true, true, true]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    add O(L); search wildcard-dependent

When to choose this variant:
    Use this variant when its role matches the interview goal: primary design solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    211. Design Add and Search Words - trie wildcard DFS reference Core idea: Store words in a trie. Search walks characters normally, but '.' branches to every child at that trie node. DFS succeeds only if the full pattern ends on a terminal word node. Complexity: O(L) for addWord; search is O(branches) worst-case with wildcards.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word): return node.is_word
            ch = word[i]
            if ch == '.': return any(dfs(child, i+1) for child in node.children.values())
            return ch in node.children and dfs(node.children[ch], i+1)
        return dfs(self.root, 0)
