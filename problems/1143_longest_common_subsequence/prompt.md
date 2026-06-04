# 1143. Longest Common Subsequence

Problem: https://leetcode.com/problems/longest-common-subsequence/

## Study Lists

- NeetCode 150; order 112; section: 2-D Dynamic Programming

## Problem Description

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

## Signature

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| text1 | string |
| text2 | string |

Return type: `integer`

## Examples

### Example 1

Input:

```text
text1 = "abcde", text2 = "ace"
```

Output:

```text
3
```

Explanation:

The longest common subsequence is "ace" and its length is 3.

### Example 2

Input:

```text
text1 = "abc", text2 = "abc"
```

Output:

```text
3
```

Explanation:

The longest common subsequence is "abc" and its length is 3.

### Example 3

Input:

```text
text1 = "abc", text2 = "def"
```

Output:

```text
0
```

Explanation:

There is no such common subsequence, so the result is 0.

## Constraints

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
