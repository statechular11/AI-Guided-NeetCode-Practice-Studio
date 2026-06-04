# 323. Number of Connected Components in an Undirected Graph

Problem: https://neetcode.io/problems/count-connected-components/question
LeetCode: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Study Lists

- NeetCode 150; order 90; section: Graphs

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

## Signature

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |
| edges | integer[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
n = 5, edges = [[0,1],[1,2],[3,4]]
```

Output:

```text
2
```

### Example 2

Input:

```text
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
```

Output:

```text
1
```

## Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= aᵢ <= bᵢ < n
- aᵢ != bᵢ
- There are no repeated edges.
