
# importing libraries
from sortedcontainers import SortedList, SortedSet, SortedDict

class TweetCounts:

    def __init__(self):
        self.data = defaultdict(lambda: SortedList())
        self.times = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = [0] * ((endTime - startTime) // (self.times[freq]) + 1)
        for i in self.data[tweetName]:
            if startTime <= i <= endTime:
                j = (i - startTime) // self.times[freq]
                ans[j] += 1

        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)