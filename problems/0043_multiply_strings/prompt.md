# 43. Multiply Strings

Problem: https://leetcode.com/problems/multiply-strings/

## Study Lists

- NeetCode 150; order 142; section: Math & Geometry

## Problem Description

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Signature

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| num1 | string |
| num2 | string |

Return type: `string`

## Examples

### Example 1

Input:

```text
num1 = "2", num2 = "3"
```

Output:

```text
"6"
```

### Example 2

Input:

```text
num1 = "123", num2 = "456"
```

Output:

```text
"56088"
```

## Constraints

- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.
