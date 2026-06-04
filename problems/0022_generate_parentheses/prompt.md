# 22. Generate Parentheses

Problem: https://leetcode.com/problems/generate-parentheses/

## Study Lists

- LeetCode Top Interview 150; order 106; section: Backtracking
- NeetCode 150; order 72; section: Backtracking

## Problem Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Signature

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |

Return type: `list<string>`

## Examples

### Example 1

Input:

```text
n = 3
```

Output:

```text
["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2

Input:

```text
n = 1
```

Output:

```text
["()"]
```

## Constraints

- 1 <= n <= 8
