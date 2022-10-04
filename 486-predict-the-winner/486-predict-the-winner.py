class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def dp(isPlayer1, p1, p2, i, j):
            if i > j:
                return p1 >= p2
            
            # print(nums[i:j+1])
            if isPlayer1:
                isPlayer1 = not isPlayer1
                return dp(isPlayer1, p1 + nums[i], p2, i + 1, j) or \
                       dp(isPlayer1, p1 + nums[j], p2, i, j - 1)
            isPlayer1 = not isPlayer1
            
            return dp(isPlayer1, p1, p2 + nums[i], i + 1, j) and \
                   dp(isPlayer1, p1, p2 + nums[j], i, j - 1)
        
        return dp(True, 0, 0, 0, len(nums) - 1)