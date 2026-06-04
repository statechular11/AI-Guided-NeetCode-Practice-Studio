"""
212. Word Search II - Board Dfs Constrained By Trie Prefixes

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Trie prefixes stop impossible DFS paths early; clear found words to avoid duplicates.

    This specific variant uses: board DFS constrained by trie prefixes.

Key invariant:
    Each trie node represents the prefix formed by the path from the root, while terminal markers distinguish complete words from prefixes.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"board": [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], "words": ["oath", "pea", "eat", "rain"]}` and the expected result is `["eat", "oath"]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: pruned DFS; Space: O(total word chars)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    212. Word Search II - trie plus board DFS reference Core idea: Build a trie of target words, then DFS from each board cell while following trie edges. When a trie node stores a word, emit it and clear it to avoid duplicates. Prune exhausted trie branches for efficiency. Complexity: O(m*n*4^L) worst-case, heavily pruned by trie prefixes.
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                node = node.children.setdefault(ch, TrieNode())
            node.word = word
        rows, cols = len(board), len(board[0]); result=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node.children: return
            nxt=node.children[ch]
            if nxt.word:
                result.append(nxt.word); nxt.word=None
            board[r][c]='#'
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != '#': dfs(nr,nc,nxt)
            board[r][c]=ch
            if not nxt.children and nxt.word is None: node.children.pop(ch)
        for r in range(rows):
            for c in range(cols): dfs(r,c,root)
        return result
