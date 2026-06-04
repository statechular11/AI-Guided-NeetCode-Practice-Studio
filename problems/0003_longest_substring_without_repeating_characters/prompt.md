# 3. Longest Substring Without Repeating Characters

Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Study Lists

- LeetCode Top Interview 150; order 31; section: Sliding Window
- NeetCode 150; order 16; section: Sliding Window

## Problem Description

Given a string s, find the length of the longest substring without duplicate characters.

## Signature

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
s = "abcabcbb"
```

Output:

```text
3
```

Explanation:

The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

### Example 2

Input:

```text
s = "bbbbb"
```

Output:

```text
1
```

Explanation:

The answer is "b", with the length of 1.

### Example 3

Input:

```text
s = "pwwkew"
```

Output:

```text
3
```

Explanation:

```text
The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
