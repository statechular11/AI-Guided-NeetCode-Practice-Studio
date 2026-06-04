# 271. Encode and Decode Strings

Problem: https://neetcode.io/problems/string-encode-and-decode/question
LeetCode: https://leetcode.com/problems/encode-and-decode-strings/

## Study Lists

- NeetCode 150; order 6; section: Arrays & Hashing

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {

// ... your code

return encoded_string;

}

Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {

// ... your code

return decoded_strs;

}

So Machine 1 does:

String encoded_string = encode(strs);

and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);

decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

## Signature

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| dummy_input | list<string> |

Return type: `list<string>`

## Examples

### Example 1

Input:

```text
strs = ["Hello","World"]
```

Output:

```text
["Hello","World"]
```

Explanation:

```text
Solution solution = new Solution();
String encoded_string = solution.encode(strs);
// Machine 1 ---encoded_string---> Machine 2
List<String> decoded_strs = solution.decode(encoded_string);
```

### Example 2

Input:

```text
strs = [""]
```

Output:

```text
[""]
```

## Constraints

- 0 <= strs.length < 100
- 0 <= strs[i].length < 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

## Follow-up

Could you write a generalized algorithm to work on any possible set of characters?
