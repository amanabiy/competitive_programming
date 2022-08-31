class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        either the number can be positive or negative at one point:
        therefore If I can know what the value of it when it negative I can use it
        """
        memo = {}
        
        def dfs(i, sums):
            if i == len(nums):
                if sums == target:
                    return 1
                return 0
        
            if (i, sums) in memo:
                return memo[(i, sums)]
            
            pos = dfs(i+1, sums + nums[i])
            neg = dfs(i+1, sums - nums[i])

            memo[(i, sums)] = pos + neg
            
            return memo[(i, sums)]
        
        return dfs(0, 0)