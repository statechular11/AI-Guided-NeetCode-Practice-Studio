# 79. Word Search

Problem: https://leetcode.com/problems/word-search/

## Study Lists

- LeetCode Top Interview 150; order 107; section: Backtracking
- NeetCode 150; order 73; section: Backtracking

## Problem Description

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Signature

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| board | character[][] |
| word | string |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
```

Output:

```text
true
```

### Example 2

Input:

```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
```

Output:

```text
true
```

### Example 3

Input:

```text
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
```

Output:

```text
false
```

## Constraints

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

## Follow-up

Could you use search pruning to make your solution faster with a larger board?
