# 242. Valid Anagram

Problem: https://leetcode.com/problems/valid-anagram/

## Study Lists

- LeetCode Top Interview 150; order 42; section: Hashmap
- NeetCode 150; order 2; section: Arrays & Hashing

## Problem Description

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## Signature

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| t | string |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
s = "anagram", t = "nagaram"
```

Output:

```text
true
```

### Example 2

Input:

```text
s = "rat", t = "car"
```

Output:

```text
false
```

## Constraints

- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

## Follow-up

What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
