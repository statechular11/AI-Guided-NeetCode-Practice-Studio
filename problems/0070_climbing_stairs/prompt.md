# 70. Climbing Stairs

Problem: https://leetcode.com/problems/climbing-stairs/

## Study Lists

- LeetCode Top Interview 150; order 137; section: 1D DP
- NeetCode 150; order 99; section: 1-D Dynamic Programming

## Problem Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Signature

```python
class Solution:
    def climbStairs(self, n: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
n = 2
```

Output:

```text
2
```

Explanation:

```text
There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2

Input:

```text
n = 3
```

Output:

```text
3
```

Explanation:

```text
There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Constraints

- 1 <= n <= 45
