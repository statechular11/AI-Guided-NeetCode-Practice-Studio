# 191. Number of 1 Bits

Problem: https://leetcode.com/problems/number-of-1-bits/

## Study Lists

- LeetCode Top Interview 150; order 127; section: Bit Manipulation
- NeetCode 150; order 145; section: Bit Manipulation

## Problem Description

Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

## Signature

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
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
n = 11
```

Output:

```text
3
```

Explanation:

The input binary string 1011 has a total of three set bits.

### Example 2

Input:

```text
n = 128
```

Output:

```text
1
```

Explanation:

The input binary string 10000000 has a total of one set bit.

### Example 3

Input:

```text
n = 2147483645
```

Output:

```text
30
```

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

## Constraints

- 1 <= n <= 2^31 - 1

## Follow-up

If this function is called many times, how would you optimize it?
