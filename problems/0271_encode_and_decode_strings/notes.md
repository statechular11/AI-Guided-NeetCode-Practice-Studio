# Notes - 271. Encode and Decode Strings

## Core Idea

Use a length prefix so decoding knows exactly how many characters belong to each string:

```text
<length>#<payload>
```

The separator only separates the length from the payload. It does not need to be absent from the payload.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_length_prefix.py` | primary robust codec | Time: O(total characters); Space: O(total characters) |
| `solution_escape_delimiter.py` | alternative robust codec reference | Time: O(total characters); Space: O(total characters) |

## Pitfalls To Watch

- A simple delimiter join fails if strings can contain that delimiter.
- Empty strings must round-trip.
- During decode, advance by the parsed length, not by searching for the next separator inside the payload.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
