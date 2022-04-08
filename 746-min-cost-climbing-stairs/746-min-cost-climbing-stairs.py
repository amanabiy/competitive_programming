class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, memo):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1, memo), dfs(i+2, memo))
            return memo[i]
        
        return min(dfs(0,{}), dfs(1,{}))