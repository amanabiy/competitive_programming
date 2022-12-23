class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache
        def dfs(i, isBuy):
            if i >= len(prices):
                return 0

            take = not_take = 0
            if not isBuy:
                take = dfs(i + 2, True) + prices[i]
                not_take = dfs(i + 1, False)
            else:
                take = dfs(i + 1, False) - prices[i]
                not_take = dfs(i + 1, True)

            return max(take, not_take)
        
        return dfs(0, True)