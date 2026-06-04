# 190. Reverse Bits

Problem: https://leetcode.com/problems/reverse-bits/

## Study Lists

- LeetCode Top Interview 150; order 126; section: Bit Manipulation
- NeetCode 150; order 147; section: Bit Manipulation

## Problem Description

Reverse bits of a given 32 bits signed integer.

## Signature

```python
class Solution:
    def reverseBits(self, n: int) -> int:
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
n = 43261596
```

Output:

```text
964176192
```

Explanation:

```text
Integer
Binary
43261596
00000010100101000001111010011100
964176192
00111001011110000010100101000000
```

### Example 2

Input:

```text
n = 2147483644
```

Output:

```text
1073741822
```

Explanation:

```text
Integer
Binary
2147483644
01111111111111111111111111111100
1073741822
00111111111111111111111111111110
```

## Constraints

- 0 <= n <= 2^31 - 2
- n is even.

## Follow-up

If this function is called many times, how would you optimize it?
