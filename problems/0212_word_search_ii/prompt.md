# 212. Word Search II

Problem: https://leetcode.com/problems/word-search-ii/

## Study Lists

- LeetCode Top Interview 150; order 100; section: Trie
- NeetCode 150; order 79; section: Tries

## Problem Description

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Signature

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| board | character[][] |
| words | string[] |

Return type: `list<string>`

## Examples

### Example 1

Input:

```text
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
```

Output:

```text
["eat","oath"]
```

### Example 2

Input:

```text
board = [["a","b"],["c","d"]], words = ["abcb"]
```

Output:

```text
[]
```

## Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
