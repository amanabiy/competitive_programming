class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
               0  1  2  3 4  5 6 7 8 9 10  11
          1    T  T  F  F     
          5    T  F  F       T T           
          11   T             T T            T
          5    T             T T            T
        
        """
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        
        half = totalSum // 2
        dp = [[ 0 for _ in range(half + 1)] for i in range(len(nums) + 1)]
        
        for i in range(len(dp)):
            dp[i][0] = True
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
                
        return dp[-1][-1]
        
        
        