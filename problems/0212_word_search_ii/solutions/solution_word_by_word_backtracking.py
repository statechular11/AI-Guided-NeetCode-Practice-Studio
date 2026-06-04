"""
212. Word Search II - search each word independently

Variant role:
    educational baseline

Core idea:
    Before building a trie, solve the simpler problem repeatedly: run Word Search for each candidate word.

Key invariant:
    Each DFS path uses board cells at most once and matches the current word prefix exactly.

Mechanics:
    For every word, scan all cells as possible starts. Stop after the first successful path for that word.

Common pitfalls:
    This repeats large amounts of work across words with common prefixes; the trie reference shares that prefix work.

Complexity:
    Time: O(W * mn * 4^L); Space: O(L)

When to choose this variant:
    Use this as the baseline that makes the trie backtracking optimization feel necessary.
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        result: list[str] = []
        seen_words = set()

        def exists(word: str) -> bool:
            visited: set[tuple[int, int]] = set()

            def dfs(r: int, c: int, index: int) -> bool:
                if index == len(word):
                    return True
                if r < 0 or r == rows or c < 0 or c == cols:
                    return False
                if (r, c) in visited or board[r][c] != word[index]:
                    return False
                visited.add((r, c))
                found = (
                    dfs(r + 1, c, index + 1)
                    or dfs(r - 1, c, index + 1)
                    or dfs(r, c + 1, index + 1)
                    or dfs(r, c - 1, index + 1)
                )
                visited.remove((r, c))
                return found

            return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

        for word in words:
            if word not in seen_words and exists(word):
                result.append(word)
                seen_words.add(word)
        return result
