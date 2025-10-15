class Twitter:

    def __init__(self):
        self.graph = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        self.graph[userId].add(userId)
        self.tweets[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = list()
        ans = []
        for i in self.graph[userId]:
            if i in self.tweets: heappush(heap,[self.tweets[i][-1][0],self.tweets[i][-1][1],i,len(self.tweets[i])-1])
        print(heap)
        while heap and len(ans)<10:
            cnt,twid,fr,idx = heappop(heap)
            ans.append(twid)
            if idx-1>=0: heappush(heap,[self.tweets[fr][idx-1][0],self.tweets[fr][idx-1][1], fr, idx-1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.graph[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.graph[followerId]: self.graph[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)