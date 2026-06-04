# 647. Palindromic Substrings

Problem: https://leetcode.com/problems/palindromic-substrings/

## Study Lists

- NeetCode 150; order 104; section: 1-D Dynamic Programming

## Problem Description

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Signature

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |

Return type: `integer`

## Examples

### Example 1

Input:

```text
s = "abc"
```

Output:

```text
3
```

Explanation:

Three palindromic strings: "a", "b", "c".

### Example 2

Input:

```text
s = "aaa"
```

Output:

```text
6
```

Explanation:

Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

## Constraints

- 1 <= s.length <= 1000
- s consists of lowercase English letters.
