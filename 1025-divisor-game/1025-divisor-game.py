class Solution:
    def divisorGame(self, n: int) -> bool:
        def dp(n, isAlice, memo):
            if n == 1:
                return not isAlice
            if n in memo:
                return memo[n]

            ans = False
            for i in range(1, n):
                if n % i == 0:
                    ans = ans or dp(n - i, not isAlice, memo)

            memo[n] = ans
            return ans

        return dp(n, True, {})        