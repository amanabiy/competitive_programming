class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        """
        dp = [0] * (amount + 1)
        if amount == 0:
            return 1
        
        for coin in coins:
            if coin < amount + 1:
                dp[coin] += 1
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        
        # print(dp)
        return dp[-1]