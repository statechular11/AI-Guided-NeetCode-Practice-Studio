"""
72. Edit Distance - space-compressed edit distance DP

Variant role:
    optimized-space DP reference

Core idea:
    Each DP row only depends on the previous row and the current row's left neighbor.

Key invariant:
    prev[j] is the edit distance from word1[:i-1] to word2[:j] before the row update; cur[j] becomes the distance from word1[:i] to word2[:j].

Mechanics:
    Carry replacement from prev[j-1], deletion from prev[j], and insertion from cur[j-1].

Common pitfalls:
    Update order matters. Keep the previous row separate or preserve the old diagonal value before overwriting.

Complexity:
    Time: O(mn); Space: O(n)

When to choose this variant:
    Use this when you already understand the 2-D table and want the interview-ready O(n) space refinement.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))

        for i in range(1, m + 1):
            cur = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(
                        prev[j],      # delete word1[i - 1]
                        cur[j - 1],   # insert word2[j - 1]
                        prev[j - 1],  # replace
                    )
            prev = cur

        return prev[n]
