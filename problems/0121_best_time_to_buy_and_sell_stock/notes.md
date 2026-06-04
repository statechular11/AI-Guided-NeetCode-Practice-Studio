# Notes - 121. Best Time to Buy and Sell Stock

## Core Idea

For each sell day, only the minimum price before it matters:

```text
candidate_profit = prices[today] - cheapest_price_before_today
```

The O(n) solution scans once, maintains the cheapest buy price seen so far, and
updates the best profit for each possible sell day.

This is a Sliding Window starter problem because the "left side" of the window
does not need a full data structure. The only left-side state that matters is
the cheapest buy candidate.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_brute_force.py` | Educational pair-search baseline. | Time: O(n^2); Space: O(1) |
| `solution_min_price.py` | Primary one-pass running-min solution. | Time: O(n); Space: O(1) |

## Preferred Interview Path

Start from the brute-force question:

```text
For each sell day, which earlier buy day gives the largest profit?
```

For a fixed sell day, maximizing:

```text
sell_price - buy_price
```

means minimizing `buy_price`. So the inner loop over previous buy days can be
compressed into one running value:

```text
min_price = cheapest price before today
```

At each day:

1. Treat today's price as the sell price.
2. Compare `today - min_price` against `best`.
3. Update `min_price` so today's price can be the buy candidate for future days.

## Example Walkthrough

For `prices = [7, 1, 5, 3, 6, 4]`:

```text
start: min_price = 7, best = 0

price = 1: candidate = 1 - 7 = -6, best = 0, min_price = 1
price = 5: candidate = 5 - 1 = 4,  best = 4, min_price = 1
price = 3: candidate = 3 - 1 = 2,  best = 4, min_price = 1
price = 6: candidate = 6 - 1 = 5,  best = 5, min_price = 1
price = 4: candidate = 4 - 1 = 3,  best = 5, min_price = 1
```

Return `5`.

## Pitfalls To Watch

- Buy day must be before sell day.
- Do not compute global min and global max independently; the max might occur
  before the min.
- Keep `best` initialized to 0 so descending prices return 0.
- State whether `min_price` means "cheapest price before today" or "cheapest
  price seen including today"; then order the update consistently.

## Reference Enrichment Log

2026-06-01:

- Expanded `solution_min_price.py` into a first-principles running-min reference
  with sliding-window interpretation, invariant, walkthrough, descending-price
  behavior, and pitfalls.
- Added `solution_brute_force.py` as an educational baseline to show why the
  optimized solution only needs the cheapest earlier buy price.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
