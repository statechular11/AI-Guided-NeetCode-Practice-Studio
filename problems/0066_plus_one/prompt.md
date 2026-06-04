# 66. Plus One

Problem: https://leetcode.com/problems/plus-one/

## Study Lists

- LeetCode Top Interview 150; order 132; section: Math
- NeetCode 150; order 140; section: Math & Geometry

## Problem Description

You are given a large integer represented as an integer array digits, where each digits[i] is the i^th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Signature

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| digits | integer[] |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
digits = [1,2,3]
```

Output:

```text
[1,2,4]
```

Explanation:

```text
The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

### Example 2

Input:

```text
digits = [4,3,2,1]
```

Output:

```text
[4,3,2,2]
```

Explanation:

```text
The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

### Example 3

Input:

```text
digits = [9]
```

Output:

```text
[1,0]
```

Explanation:

```text
The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## Constraints

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.
