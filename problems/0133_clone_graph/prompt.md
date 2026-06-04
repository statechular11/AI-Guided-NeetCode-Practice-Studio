# 133. Clone Graph

Problem: https://leetcode.com/problems/clone-graph/

## Study Lists

- LeetCode Top Interview 150; order 91; section: Graph General
- NeetCode 150; order 82; section: Graphs

## Problem Description

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {

public int val;

public List<Node> neighbors;

}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

## Signature

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| edges | integer[][] |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
adjList = [[2,4],[1,3],[2,4],[1,3]]
```

Output:

```text
[[2,4],[1,3],[2,4],[1,3]]
```

Explanation:

```text
There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

### Example 2

Input:

```text
adjList = [[]]
```

Output:

```text
[[]]
```

Explanation:

Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

### Example 3

Input:

```text
adjList = []
```

Output:

```text
[]
```

Explanation:

This an empty graph, it does not have any nodes.

## Constraints

- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.
