"""
678. Valid Parenthesis String - Range Of Possible Open Counts

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Track a range of possible open counts, not one exact count.

    This specific variant uses: range of possible open counts.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "()"}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    678. Valid Parenthesis String - balance range reference Core idea: `*` can be `(`, `)`, or empty, so track the possible range of unmatched open parentheses: [low, high]. Updates: '(' increases both bounds. ')' decreases both bounds. '*' can decrease low or increase high. If high becomes negative, there are too many closing parentheses. Clamp low to 0 because unmatched opens cannot be negative. Complexity: Time: O(n) Space: O(1)
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for ch in s:
            if ch == "(":
                low += 1
                high += 1
            elif ch == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False
            low = max(low, 0)

        return low == 0
