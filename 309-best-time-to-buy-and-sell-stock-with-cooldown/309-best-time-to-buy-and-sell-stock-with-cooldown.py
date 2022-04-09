class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        
        for i in range(len(prices)-1, -1, -1):
            max_r = 0
            for j in range(i+1, len(prices)):
                result = max(prices[j] - prices[i] + memo[j + 2],0)
                max_r = max(result, max_r)
            # print(i, max_r)
            memo[i] = max(memo[i+1], max_r)
        
        # print(memo)
        return memo[0]
#         memo = {}
#         ans = 0
        
#         def dfs(buy):
#             """ buy and sell for a given stock
#             """
#             # check buy is in index
#             if buy >= len(prices):
#                 return 0
            
#             if buy in memo:
#                 # print(buy, memo[buy])
#                 return memo[buy]
            
#             ans = profit = 0 
#             for sell in range(buy + 1, len(prices)):
#                 profit = max(prices[sell] - prices[buy], profit)
#                 ans = max(profit + dfs(sell + 2), ans)
#                 # print(buy, sell, profit, ans, dfs(sell + 2))
            
#             memo[buy] = ans
#             return ans
        
#         for i in range(len(prices)):
#             ans = max(ans, dfs(i))
        
#         return ans
        