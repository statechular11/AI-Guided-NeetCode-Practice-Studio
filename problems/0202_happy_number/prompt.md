# 202. Happy Number

Problem: https://leetcode.com/problems/happy-number/

## Study Lists

- LeetCode Top Interview 150; order 45; section: Hashmap
- NeetCode 150; order 139; section: Math & Geometry

## Problem Description

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

## Signature

```python
class Solution:
    def isHappy(self, n: int) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
n = 19
```

Output:

```text
true
```

Explanation:

```text
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

### Example 2

Input:

```text
n = 2
```

Output:

```text
false
```

## Constraints

- 1 <= n <= 2^31 - 1
