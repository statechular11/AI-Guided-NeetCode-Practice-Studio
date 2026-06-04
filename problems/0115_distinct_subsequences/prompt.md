# 115. Distinct Subsequences

Problem: https://leetcode.com/problems/distinct-subsequences/

## Study Lists

- NeetCode 150; order 118; section: 2-D Dynamic Programming

## Problem Description

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

## Signature

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| t | string |

Return type: `integer`

## Examples

### Example 1

Input:

```text
s = "rabbbit", t = "rabbit"
```

Output:

```text
3
```

Explanation:

```text
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

### Example 2

Input:

```text
s = "babgbag", t = "bag"
```

Output:

```text
5
```

Explanation:

```text
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

## Constraints

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.
