# 7. Reverse Integer

Problem: https://leetcode.com/problems/reverse-integer/

## Study Lists

- NeetCode 150; order 150; section: Bit Manipulation

## Problem Description

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Signature

```python
class Solution:
    def reverse(self, x: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| x | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
x = 123
```

Output:

```text
321
```

### Example 2

Input:

```text
x = -123
```

Output:

```text
-321
```

### Example 3

Input:

```text
x = 120
```

Output:

```text
21
```

## Constraints

- -2^31 <= x <= 2^31 - 1
