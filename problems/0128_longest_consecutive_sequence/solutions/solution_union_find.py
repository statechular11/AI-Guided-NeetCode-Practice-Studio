"""
128. Longest Consecutive Sequence - union-find reference

Variant role:
    Educational graph/component variant. The hash-set start scan is still the
    cleanest interview solution, but union-find is a meaningful alternative
    because the problem can be modeled as connected components of adjacent
    integer values.

Core idea:
    Treat each distinct number as a node. If both `x` and `x + 1` exist, connect
    those two nodes. After all adjacent values are unioned, every connected
    component represents one consecutive sequence.

    The answer is the size of the largest connected component.

Why use distinct values:
    Duplicates should not inflate the sequence length. For example:

        nums = [1, 2, 2, 3]

    The longest consecutive sequence is still [1, 2, 3] with length 3, not 4.
    Therefore, build union-find nodes from `set(nums)`.

Step-by-step walkthrough:
    1. Convert nums to a set of unique values.
    2. Initialize every value as its own parent with component size 1.
    3. For each value x, if x + 1 exists, union x and x + 1.
    4. Track component sizes at roots.
    5. Return the largest component size seen.

Example:
    nums = [100, 4, 200, 1, 3, 2]

    Unique values:
        {1, 2, 3, 4, 100, 200}

    Union adjacent pairs:
        union(1, 2)
        union(2, 3)
        union(3, 4)

    The component containing 1,2,3,4 has size 4, so the answer is 4.

When to choose this variant:
    Use the hash-set start solution for most interviews because it is shorter
    and more direct. Use this variant to practice union-find or when a problem
    naturally asks about connected groups formed by adjacency relationships.

Complexity:
    Time: O(n * alpha(n)), effectively O(n), where alpha is the inverse
    Ackermann function from union-find path compression.
    Space: O(n), for parent and component-size maps.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        if not values:
            return 0

        parent = {value: value for value in values}
        size = {value: 1 for value in values}
        best = 1

        def find(value: int) -> int:
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        def union(a: int, b: int) -> int:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return size[root_a]

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return size[root_a]

        for value in values:
            if value + 1 in values:
                best = max(best, union(value, value + 1))

        return best
