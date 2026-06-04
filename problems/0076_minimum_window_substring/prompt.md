# 76. Minimum Window Substring

Problem: https://leetcode.com/problems/minimum-window-substring/

## Study Lists

- LeetCode Top Interview 150; order 33; section: Sliding Window
- NeetCode 150; order 19; section: Sliding Window

## Problem Description

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

## Signature

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| t | string |

Return type: `string`

## Examples

### Example 1

Input:

```text
s = "ADOBECODEBANC", t = "ABC"
```

Output:

```text
"BANC"
```

Explanation:

The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

### Example 2

Input:

```text
s = "a", t = "a"
```

Output:

```text
"a"
```

Explanation:

The entire string s is the minimum window.

### Example 3

Input:

```text
s = "a", t = "aa"
```

Output:

```text
""
```

Explanation:

```text
Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

## Follow-up

Could you find an algorithm that runs in O(m + n) time?
