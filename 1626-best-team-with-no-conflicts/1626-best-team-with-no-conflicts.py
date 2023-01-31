class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data = list(zip(ages, scores))
        data.sort()
        dp = [0] * (len(data))
        dp[0] = data[0][1]
        # print(data)
        for i in range(1, len(data)):
            dp[i] = data[i][1]
            for j in range(i):
                if data[j][0] < data[i][0] and data[j][1] > data[i][1]:
                    continue
                dp[i] = max(dp[i], dp[j] + data[i][1])
            # print(dp, i)
            
        return max(dp)