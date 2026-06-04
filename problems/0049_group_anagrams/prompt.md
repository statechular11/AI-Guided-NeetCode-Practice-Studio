# 49. Group Anagrams

Problem: https://leetcode.com/problems/group-anagrams/

## Study Lists

- LeetCode Top Interview 150; order 43; section: Hashmap
- NeetCode 150; order 4; section: Arrays & Hashing

## Problem Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## Signature

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| strs | string[] |

Return type: `list<list<string>>`

## Examples

### Example 1

Input:

```text
strs = ["eat","tea","tan","ate","nat","bat"]
```

Output:

```text
[["bat"],["nat","tan"],["ate","eat","tea"]]
```

Explanation:

```text
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

### Example 2

Input:

```text
strs = [""]
```

Output:

```text
[[""]]
```

### Example 3

Input:

```text
strs = ["a"]
```

Output:

```text
[["a"]]
```

## Constraints

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
