# 338. Counting Bits

Problem: https://leetcode.com/problems/counting-bits/

## Study Lists

- NeetCode 150; order 146; section: Bit Manipulation

## Problem Description

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## Signature

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
n = 2
```

Output:

```text
[0,1,1]
```

Explanation:

```text
0 --> 0
1 --> 1
2 --> 10
```

### Example 2

Input:

```text
n = 5
```

Output:

```text
[0,1,1,2,1,2]
```

Explanation:

```text
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

## Constraints

- 0 <= n <= 10^5

## Follow-up

- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
- Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
