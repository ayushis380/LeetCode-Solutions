class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId : [count, tweetId]
        self.followMap = defaultdict(set) # userId : set of followeeIds (whom user follows)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxheap = []

        self.followMap[userId].add(userId) # in the requirement, user follow themself


#  defaultdict(<class 'list'>, {1: [[0, 5], [-1, 7]]})
# defaultdict(<class 'list'>, {1: [[0, 5], [-1, 7]], 2: [[-2, 6]]})
# defaultdict(<class 'list'>, {1: [[0, 5], [-1, 7]], 2: [[-2, 6]]})

    # making it like a merge k sorted list
    # from each list we get the length, to find index of last element as elements are appended
    # just like we do for k sorted list, then move the index back by 1 
        for followeeId in self.followMap[userId]: # check for tweets for each followee that user follows
            if followeeId in self.tweetMap: # maybe that followee doesnt have any tweets
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxheap, (count, tweetId, followeeId, index - 1))

    # add tweets to the result 
    # count is for building maxheap, followeeId and index to get the value from the same list
        while maxheap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxheap)
            result.append(tweetId)
            if index >=0: # list should have values
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxheap, (count, tweetId, followeeId, index - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)