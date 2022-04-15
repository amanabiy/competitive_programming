class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        memo = defaultdict(int)

        for i in range(len(prices) - 2, -1, -1):
            if prices[i] == prices[i + 1] + 1:
                memo[i] += memo[i+1] + 1
                
        return len(prices) + sum(memo.values())
