class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        1
        """
        dp = [[1, 1] for i in range(len(nums)) ] # length until now and quantity
        
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    curr = dp[j][0] + 1
                    if curr > dp[i][0]:
                        dp[i] = [curr, dp[j][1]]
                    elif curr == dp[i][0]:
                        dp[i][1] += dp[j][1]

        total = 0
        maxim = float('-inf')
        for val, size in dp:
            if val == maxim:
                total += size
            elif val > maxim:
                total = size
                maxim = val

        return total