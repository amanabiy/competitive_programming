class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        sell = -1
        for i in range(len(prices) - 1, 0 , -1):
            buy = prices[i - 1]
            sell = max(sell, prices[i])
            profit = max(sell - buy, profit)

        return profit                