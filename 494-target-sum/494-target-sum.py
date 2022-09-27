class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        either the number can be positive or negative at one point:
        therefore If I can know what the value of it when it negative I can use it
         -3   -2  -1   0   1   2   3
          0    1   2   3   4   5   6 
          
          
        
        """
        total = sum(nums)
        
        if abs(target) > total:
            return 0

        dp = [ [ 0 for i in range(total * 2 + 1)] for _ in range(len(nums))]
        dp[0][total + nums[0]] = 1
        dp[0][total - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(-total, total+1):
                index = j + total
                if index + nums[i] <= total * 2:
                    dp[i][index + nums[i]] += dp[i - 1][index]
                if index - nums[i] >= 0:
                    dp[i][index - nums[i]] += dp[i - 1][index]
        # print(dp)
        
        return dp[-1][total - target]