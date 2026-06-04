# 20. Valid Parentheses

Problem: https://leetcode.com/problems/valid-parentheses/

## Study Lists

- LeetCode Top Interview 150; order 52; section: Stack
- NeetCode 150; order 21; section: Stack

## Problem Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Signature

```python
class Solution:
    def isValid(self, s: str) -> bool:
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
s = "()[]{}"
```

Output:

```text
true
```

### Example 3

Input:

```text
s = "(]"
```

Output:

```text
false
```

### Example 4

Input:

```text
s = "([])"
```

Output:

```text
true
```

### Example 5

Input:

```text
s = "([)]"
```

Output:

```text
false
```

## Constraints

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
