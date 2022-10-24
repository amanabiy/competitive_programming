class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,3] -> a % b == 0
                          b % a == 0
        for each element:
        I have two choices ->
            taking this element and the second one is not take it
            my next dividor is going to be this number
        
          [1  2  3]
        1  1  2  2
        2     1  1
        3  
        """
        nums.sort()

        dp = [set([nums[i]]) for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if len(dp[j]) < len(dp[i]) + 1:
                        dp[j] = dp[i] | { nums[j] } 
        
        ans = None
        for val in dp:
            if not ans or len(ans) < len(val):
                ans = val
        
        return ans