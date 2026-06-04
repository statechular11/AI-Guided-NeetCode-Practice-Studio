# 567. Permutation in String

Problem: https://leetcode.com/problems/permutation-in-string/

## Study Lists

- NeetCode 150; order 18; section: Sliding Window

## Problem Description

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

## Signature

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s1 | string |
| s2 | string |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
s1 = "ab", s2 = "eidbaooo"
```

Output:

```text
true
```

Explanation:

s2 contains one permutation of s1 ("ba").

### Example 2

Input:

```text
s1 = "ab", s2 = "eidboaoo"
```

Output:

```text
false
```

## Constraints

- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
