class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def dfs(n, memo):
            
            if n in memo:
                return memo[n]
            if n > target:
                return 0
            if n == target:
                return 1
            
            ans = 0
            for i in nums:
                ans += dfs(n+i, memo)
            
            memo[n] = ans
            return ans
        
        return dfs(0, {})