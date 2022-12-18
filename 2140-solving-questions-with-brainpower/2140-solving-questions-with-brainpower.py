class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        
        """
        
        def dp(index, memo={}):
            if index >= len(questions):
                return 0
            
            if index in memo:
                return memo[index]
    
            # taking this question
            take = dp(index + questions[index][1] + 1) + questions[index][0]
            
            # skiping this question
            not_take = dp(index + 1)
            
            memo[index] = max(not_take, take)
            return memo[index]


        return dp(0)