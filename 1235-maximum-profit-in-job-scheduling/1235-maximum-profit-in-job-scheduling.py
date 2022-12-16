class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        value = list(sorted(zip(startTime, endTime, profit)))
        startTime = [s for s, e, v in value]
        
        @lru_cache(None)
        def dfs(i):
            if i >= len(startTime):
                return 0
            
            # take this 
            nextIndex = bisect.bisect_left(startTime, value[i][1])
            take = dfs(nextIndex) + value[i][2]

            # not take this
            not_take = dfs(i + 1)

            return max(take, not_take)
        
        print(value)
        return dfs(0)