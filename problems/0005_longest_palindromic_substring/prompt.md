# 5. Longest Palindromic Substring

Problem: https://leetcode.com/problems/longest-palindromic-substring/

## Study Lists

- LeetCode Top Interview 150; order 145; section: Multidimensional DP
- NeetCode 150; order 103; section: 1-D Dynamic Programming

## Problem Description

Given a string s, return the longest palindromic substring in s.

## Signature

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |

Return type: `string`

## Examples

### Example 1

Input:

```text
s = "babad"
```

Output:

```text
"bab"
```

Explanation:

"aba" is also a valid answer.

### Example 2

Input:

```text
s = "cbbd"
```

Output:

```text
"bb"
```

## Constraints

- 1 <= s.length <= 1000
- s consist of only digits and English letters.
