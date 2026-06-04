# 131. Palindrome Partitioning

Problem: https://leetcode.com/problems/palindrome-partitioning/

## Study Lists

- NeetCode 150; order 74; section: Backtracking

## Problem Description

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

## Signature

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |

Return type: `list<list<string>>`

## Examples

### Example 1

Input:

```text
s = "aab"
```

Output:

```text
[["a","a","b"],["aa","b"]]
```

### Example 2

Input:

```text
s = "a"
```

Output:

```text
[["a"]]
```

## Constraints

- 1 <= s.length <= 16
- s contains only lowercase English letters.
