# 10. Regular Expression Matching

Problem: https://leetcode.com/problems/regular-expression-matching/

## Study Lists

- NeetCode 150; order 121; section: 2-D Dynamic Programming

## Problem Description

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

## Signature

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |
| p | string |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
s = "aa", p = "a"
```

Output:

```text
false
```

Explanation:

"a" does not match the entire string "aa".

### Example 2

Input:

```text
s = "aa", p = "a*"
```

Output:

```text
true
```

Explanation:

'*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

### Example 3

Input:

```text
s = "ab", p = ".*"
```

Output:

```text
true
```

Explanation:

".*" means "zero or more (*) of any character (.)".

## Constraints

- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
