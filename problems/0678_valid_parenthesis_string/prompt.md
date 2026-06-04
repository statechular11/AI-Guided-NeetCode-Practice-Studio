# 678. Valid Parenthesis String

Problem: https://leetcode.com/problems/valid-parenthesis-string/

## Study Lists

- NeetCode 150; order 129; section: Greedy

## Problem Description

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

## Signature

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| s | string |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
s = "()"
```

Output:

```text
true
```

### Example 2

Input:

```text
s = "(*)"
```

Output:

```text
true
```

### Example 3

Input:

```text
s = "(*))"
```

Output:

```text
true
```

## Constraints

- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.
