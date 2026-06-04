"""
355. Design Twitter - reverse global timeline scan

Variant role:
    Simple design baseline. This version is often the easiest one to derive
    first because it stores exactly what happened globally, then scans backward
    for the newest visible tweets.

Core idea:
    Keep one append-only global timeline:

        [(author, tweetId), (author, tweetId), ...]

    Newer tweets are near the end. To get a feed, scan the timeline in reverse
    and collect tweets whose author is either the requesting user or someone
    they follow. Stop after 10 results.

Key invariant:
    The reversed global timeline is already in newest-to-oldest order. Once we
    filter it by visible authors, the remaining sequence is still in correct
    newest-to-oldest feed order.

Step-by-step trace:
    Operations:

        postTweet(1, 10)
        postTweet(2, 20)
        postTweet(1, 11)
        follow(3, 1)
        follow(3, 2)
        getNewsFeed(3)

    The global timeline is:

        [(1, 10), (2, 20), (1, 11)]

    Scanning backward sees 11 from user 1, then 20 from user 2, then 10 from
    user 1. Since users 1 and 2 are visible to user 3, the feed is:

        [11, 20, 10]

Why it works:
    Recency is global, not per author. A single timeline preserves that global
    order directly. Filtering a sequence does not change the relative order of
    the items that remain.

Tradeoff:
    This approach can be slow when many old tweets are invisible to the
    requester, because `getNewsFeed` may scan much of the global timeline. It is
    still a valuable baseline: the state is minimal, the correctness argument is
    straightforward, and the fixed output size lets many practical calls stop
    early.

Common pitfalls:
    - Scanning forward and then reversing; scanning backward is simpler.
    - Forgetting to stop after 10 visible tweets.
    - Forgetting that the requester always sees their own tweets.
    - Storing followees in a list, which can duplicate authors after repeated
      `follow` calls.

Complexity:
    postTweet: O(1)
    follow/unfollow: O(1) average
    getNewsFeed: O(T) worst case, where T is total tweets
    space: O(T + F), where F is follow edges

When to choose this variant:
    Use it as a first-principles baseline or when explaining why a later heap
    solution exists. Prefer the heap merge when feed calls must scale better.
"""

from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timeline: list[tuple[int, int]] = []
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeline.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        visible_users = set(self.following[userId])
        visible_users.add(userId)

        feed: list[int] = []
        for author, tweet_id in reversed(self.timeline):
            if author in visible_users:
                feed.append(tweet_id)
                if len(feed) == 10:
                    break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
