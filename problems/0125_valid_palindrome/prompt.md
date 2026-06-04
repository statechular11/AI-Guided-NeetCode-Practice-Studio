# 125. Valid Palindrome

Problem: https://leetcode.com/problems/valid-palindrome/

## Study Lists

- LeetCode Top Interview 150; order 25; section: Two Pointers
- NeetCode 150; order 10; section: Two Pointers

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Signature

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
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
s = "A man, a plan, a canal: Panama"
```

Output:

```text
true
```

Explanation:

"amanaplanacanalpanama" is a palindrome.

### Example 2

Input:

```text
s = "race a car"
```

Output:

```text
false
```

Explanation:

"raceacar" is not a palindrome.

### Example 3

Input:

```text
s = " "
```

Output:

```text
true
```

Explanation:

```text
s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Constraints

- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
