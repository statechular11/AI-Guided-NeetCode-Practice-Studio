# 424. Longest Repeating Character Replacement

Problem: https://leetcode.com/problems/longest-repeating-character-replacement/

## Study Lists

- NeetCode 150; order 17; section: Sliding Window

## Problem Description

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Signature

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| k | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
s = "ABAB", k = 2
```

Output:

```text
4
```

Explanation:

Replace the two 'A's with two 'B's or vice versa.

### Example 2

Input:

```text
s = "AABABBA", k = 1
```

Output:

```text
4
```

Explanation:

```text
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

## Constraints

- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
