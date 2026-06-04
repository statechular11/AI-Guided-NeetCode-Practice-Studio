# 207. Course Schedule

Problem: https://leetcode.com/problems/course-schedule/

## Study Lists

- LeetCode Top Interview 150; order 93; section: Graph General
- NeetCode 150; order 87; section: Graphs

## Problem Description

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

## Signature

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| numCourses | integer |
| prerequisites | integer[][] |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
numCourses = 2, prerequisites = [[1,0]]
```

Output:

```text
true
```

Explanation:

```text
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2

Input:

```text
numCourses = 2, prerequisites = [[1,0],[0,1]]
```

Output:

```text
false
```

Explanation:

```text
There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
