"""
355. Design Twitter - k-way heap merge over visible users

Variant role:
    Primary interview-ready design solution. It avoids sorting every visible
    tweet by treating each user's tweet history as one already-sorted list and
    merging only as far as the feed needs.

Core idea:
    A user's news feed is the 10 most recent tweets from this author set:

        {requesting user} union {users they follow}

    Each individual author posts in chronological order, so that author's tweet
    list is already sorted by time. `getNewsFeed` is therefore a k-way merge of
    sorted lists, where k is the number of visible authors with at least one
    tweet.

Key invariant:
    The heap contains at most one candidate tweet per visible author: the newest
    not-yet-returned tweet from that author. Because the heap root is the newest
    candidate overall, popping it returns the next correct feed item. Then we
    expose the same author's previous tweet, if one exists.

Mechanics:
    1. `postTweet` appends `(time, tweetId)` to that user's list.
    2. `getNewsFeed` builds the visible author set.
    3. For each visible author, push their newest tweet into the heap.
    4. Pop up to 10 times.
    5. After popping author A's tweet at index i, push A's tweet at index i - 1.

Concrete trace:
    Suppose user 1 follows users 2 and 3, and the per-user lists are:

        user 1: [(1, 101), (4, 104)]
        user 2: [(2, 202), (5, 205)]
        user 3: [(3, 303)]

    Initial heap candidates are tweet 104, 205, and 303. The heap pops 205
    first because time 5 is newest, then pushes user 2's previous tweet 202.
    The next candidates are 104, 303, and 202, so the feed continues 104, 303,
    202, 101.

Why it works:
    This is the same idea as merging sorted arrays. The newest remaining tweet
    from each visible author is enough information to know the global newest
    remaining tweet. Older tweets from an author cannot beat that author's
    current heap candidate, so they stay hidden until the candidate is popped.

Important details:
    - Tweet IDs are unique, but they are not recency timestamps. Use a separate
      monotonic counter.
    - Python `heapq` is a min heap. Store `-time` so the newest timestamp sorts
      first.
    - Include the requesting user's own tweets when building the feed; do not
      rely on a user following themself.
    - Store a set of followees so repeated `follow` calls do not duplicate feed
      authors.

Common pitfalls:
    - Sorting all visible tweets when only the top 10 are needed.
    - Forgetting to push the previous tweet from the same author after a pop.
    - Using `tweetId` as the order key.
    - Mutating stored tweet lists while building a feed.

Complexity:
    Let U be the number of visible authors with tweets.

    postTweet: O(1)
    follow/unfollow: O(1) average
    getNewsFeed: O(U log U + 10 log U), plus O(U) heap space
    total storage: O(T + F), where T is tweets and F is follow edges

When to choose this variant:
    Use this as the main interview answer. It shows the right heap pattern and
    scales with visible authors plus the fixed feed size, not with every visible
    tweet.
"""

from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        visible_users = set(self.following[userId])
        visible_users.add(userId)
        heap: list[tuple[int, int, int, int]] = []

        for author in visible_users:
            tweets = self.tweets[author]
            if not tweets:
                continue
            index = len(tweets) - 1
            time, tweet_id = tweets[index]
            # Keep the author and index so the next older tweet can be exposed.
            heapq.heappush(heap, (-time, author, index, tweet_id))

        feed: list[int] = []
        while heap and len(feed) < 10:
            _neg_time, author, index, tweet_id = heapq.heappop(heap)
            feed.append(tweet_id)

            if index > 0:
                previous_time, previous_tweet_id = self.tweets[author][index - 1]
                heapq.heappush(
                    heap,
                    (-previous_time, author, index - 1, previous_tweet_id),
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
