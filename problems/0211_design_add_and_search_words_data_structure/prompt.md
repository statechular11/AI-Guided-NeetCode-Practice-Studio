# 211. Design Add and Search Words Data Structure

Problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Study Lists

- LeetCode Top Interview 150; order 99; section: Trie
- NeetCode 150; order 78; section: Tries

## Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

## Signature

```python
class WordDictionary:

    def __init__(self):


    def addWord(self, word: str) -> None:


    def search(self, word: str) -> bool:



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

## Class Contract

Implement `WordDictionary` with its constructor and public methods.

- `addWord(word: string) -> void`
- `search(word: string) -> boolean`

## Examples

### Example 1

Input:

```text
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
```

Output:

```text
[null,null,null,null,false,true,true,true]
```

Explanation:

```text
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Constraints

- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.
