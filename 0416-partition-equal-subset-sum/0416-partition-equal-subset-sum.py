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
        dp = [ 0 for _ in range(half + 1)  ]
        dp[0] = True
        
        for i in range(len(nums)):
            for j in range(len(dp) - 1, -1, -1):
                if dp[j] and (j + nums[i] <= half):
                    dp[j + nums[i]] = dp[j]

        return dp[-1]
        
        
        