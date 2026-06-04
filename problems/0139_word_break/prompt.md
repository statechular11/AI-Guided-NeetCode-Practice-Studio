# 139. Word Break

Problem: https://leetcode.com/problems/word-break/

## Study Lists

- LeetCode Top Interview 150; order 139; section: 1D DP
- NeetCode 150; order 108; section: 1-D Dynamic Programming

## Problem Description

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Signature

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| wordDict | list<string> |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
s = "leetcode", wordDict = ["leet","code"]
```

Output:

```text
true
```

Explanation:

Return true because "leetcode" can be segmented as "leet code".

### Example 2

Input:

```text
s = "applepenapple", wordDict = ["apple","pen"]
```

Output:

```text
true
```

Explanation:

Return true because "applepenapple" can be segmented as "apple pen apple".

## Constraints

- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
