"""
127. Word Ladder - Bfs Over Wildcard Neighbor Buckets

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Because every edit has equal cost, BFS gives the shortest ladder.

    This specific variant uses: BFS over wildcard neighbor buckets.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"beginWord": "hit", "endWord": "cog", "wordList": ["hot", "dot", "dog", "lot", "log", "cog"]}` and the expected result is `5`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(n*L^2); Space: O(n*L)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    127. Word Ladder - BFS with wildcard patterns reference Core idea: Shortest transformation length means BFS. Precompute wildcard patterns such as h*t -> [hot, hit] so each word can jump to one-letter neighbors quickly. Complexity: O(n * L^2) preprocessing/traversal scale, O(n * L) space.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        patterns = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(L):
                patterns[word[:i] + '*' + word[i+1:]].append(word)
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(L):
                for nxt in patterns[word[:i] + '*' + word[i+1:]]:
                    if nxt not in seen:
                        seen.add(nxt); q.append((nxt, dist + 1))
        return 0
