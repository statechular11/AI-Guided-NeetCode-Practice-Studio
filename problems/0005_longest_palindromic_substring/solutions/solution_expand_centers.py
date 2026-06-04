"""
5. Longest Palindromic Substring - Expand Every Odd/Even Palindrome Center

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    A palindrome is determined by its center; expand around both odd and even centers.

    This specific variant uses: expand every odd/even palindrome center.

Key invariant:
    Each DP value has a clear subproblem meaning for a prefix, index, amount, or state, and updates only use already-computed smaller subproblems.

Mechanics:
    1. Define the one-dimensional state in words before coding.
    2. Initialize base cases that represent the smallest prefixes or amounts.
    3. Fill later states from earlier states in an order that preserves dependencies.
    4. Return the state that matches the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "babad"}` and the expected result is `"bab"`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define the DP state in words before coding the recurrence. Check base cases, especially empty prefixes, zeros, and one-element arrays. When optimizing space, update rolling variables in an order that preserves old values. For subsequence/subset problems, distinguish contiguous subarray, subsequence, and subset semantics.

Complexity:
    Time: O(n^2); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    5. Longest Palindromic Substring - expand around centers reference Core idea: Every palindrome has a center: either one character for odd length or the gap between two characters for even length. Expand from every possible center and keep the longest valid window. Why this is usually preferred: It is O(n^2) like the classic DP table, but uses O(1) extra space and is much easier to implement correctly in interviews. Complexity: Time: O(n^2) Space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = best_right = 0

        def expand(left: int, right: int) -> None:
            nonlocal best_left, best_right
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > best_right - best_left:
                best_left, best_right = left, right

        for center in range(len(s)):
            expand(center, center)
            expand(center, center + 1)
        return s[best_left:best_right + 1]
