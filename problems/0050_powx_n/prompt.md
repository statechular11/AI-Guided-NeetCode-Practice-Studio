# 50. Pow(x, n)

Problem: https://leetcode.com/problems/powx-n/

## Study Lists

- LeetCode Top Interview 150; order 135; section: Math
- NeetCode 150; order 141; section: Math & Geometry

## Problem Description

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

## Signature

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| x | double |
| n | integer |

Return type: `double`

## Examples

### Example 1

Input:

```text
x = 2.00000, n = 10
```

Output:

```text
1024.00000
```

### Example 2

Input:

```text
x = 2.10000, n = 3
```

Output:

```text
9.26100
```

### Example 3

Input:

```text
x = 2.00000, n = -2
```

Output:

```text
0.25000
```

Explanation:

2^-2 = 1/2^2 = 1/4 = 0.25

## Constraints

- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4
