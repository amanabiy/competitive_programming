class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        
        """
        n = len(questions)
        dp = [0] * (n + 1)
    
        for i in range(n - 1, -1, -1):
            nextHoop = questions[i][1] + i + 1
            valHoop = questions[i][0]
            if nextHoop < n:
                valHoop += dp[nextHoop]
            dp[i] = max(valHoop, dp[i + 1])
        
        return dp[0]
        
        


        return 