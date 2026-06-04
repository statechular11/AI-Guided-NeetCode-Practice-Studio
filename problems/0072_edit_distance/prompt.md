# 72. Edit Distance

Problem: https://leetcode.com/problems/edit-distance/

## Study Lists

- LeetCode Top Interview 150; order 147; section: Multidimensional DP
- NeetCode 150; order 119; section: 2-D Dynamic Programming

## Problem Description

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

## Signature

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| word1 | string |
| word2 | string |

Return type: `integer`

## Examples

### Example 1

Input:

```text
word1 = "horse", word2 = "ros"
```

Output:

```text
3
```

Explanation:

```text
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

### Example 2

Input:

```text
word1 = "intention", word2 = "execution"
```

Output:

```text
5
```

Explanation:

```text
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints

- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.
