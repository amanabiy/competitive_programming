class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        [0,1,3,5,6,8,12,17]
                         |
        k = 5
        so at each position I can jump k, k + 1, k - 1
        at the begining my k is 1
        
        
        """
        if stones[1] != 1:
            return False
        ending = stones[-1]
        stones = set(stones)
        memo = {}
        def dfs(stone, k):
            if stone == ending:
                return True
            if stone not in stones:
                return False
            
            if (stone, k) in memo:
                return memo[(stone, k)]
    
            ans = False
            
            # with the same k
            ans = ans or dfs(stone + k, k)
        
            # increase with the k            
            ans = ans or dfs(stone + k + 1, k + 1)

            # decrease with k
            if k - 1 > 0:
                ans = ans or dfs(stone + k - 1, k - 1)
            
            memo[(stone, k)] = ans
            return ans
        
        return dfs(1, 1)
            
            