"""
127. Word Ladder - bidirectional BFS with wildcard patterns

Variant role:
    optimized graph-search reference

Core idea:
    Search simultaneously from beginWord and endWord, always expanding the smaller frontier.

Key invariant:
    front and back are the current BFS layers from opposite ends; if they touch, the shortest ladder length is known.

Mechanics:
    Precompute wildcard patterns such as h*t. Each expansion jumps through words sharing a pattern.

Common pitfalls:
    Mark words visited when enqueuing them, not after popping, to prevent repeated frontier growth.

Complexity:
    Time: O(n * L^2); Space: O(n * L)

When to choose this variant:
    Use this when normal BFS is clear and you want the common hard-problem optimization.
"""

from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        words.add(beginWord)

        patterns: dict[str, list[str]] = defaultdict(list)
        length = len(beginWord)
        for word in words:
            for i in range(length):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)

        front = {beginWord}
        back = {endWord}
        visited = {beginWord, endWord}
        steps = 1

        while front:
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for word in front:
                for i in range(length):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in patterns[pattern]:
                        if neighbor in back:
                            return steps + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_front.add(neighbor)
            front = next_front
            steps += 1

        return 0
