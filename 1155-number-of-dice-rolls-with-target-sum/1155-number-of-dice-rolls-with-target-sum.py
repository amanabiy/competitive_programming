class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        for one die with the max k I will only be able to reach the targets from 1 to 30
          1 2 3 ... 30 0 0 0 ... 1000
        k = 6 and n = 1 and taret = 3
         1 2 3 4 5 6 7   Faces: 1 2 3 4 5 6     n = 2  target = 1 - 1
                                                       target = 2 -> 1 + 1 and 2
                                                       target = 3 -> 1 + 2 and 2 + 1
           0  1   2   3   4   5   6
        0  0  0   0   0   0   0   0
        1  0  1   1   1   1   1   1
        2  0  2  
        
        dp[i] = 
        
        get -> 1 (target - get) = lookup
                     2 - 1 = 1 -> 
       1 1 1 1 1 1 1 0
       2 1 2 
       
        """
        
        memo = {}
        def dfs(n, k, collected):
            if n == 0 or k == 0:
                return 1 if collected == target else 0
            
            if (n, collected) in memo:
                return memo[(n, collected)]
            
            take = 0
            
            for i in range(1, k + 1):
                take += dfs(n - 1, k, collected + i)
            
            memo[(n, collected)] = take
            return take % (10 ** 9 + 7)
        
        return dfs(n, k, 0)