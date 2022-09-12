class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        Two options
        either take the number I am at or the maximus among the k
        
         [1,4,1,5, 7,3,6,1, 9,9,3]
       0  1,4,1,5, 7,3,6,1, 9,9,3
       1  
       2
       3
        [5,5,5,5, 7,7,7,7, 9,9,9]
        [11, 11, 11, 2]
        [10, 10, 11, 11]
        
        """
        
        memo = {}

        def dfs(i):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            ans = arr[i]

            for j in range(i + 1, min(i + k + 1, len(arr) + 1)):
                arrs = (max(arr[i:j]) * len(arr[i:j])) + dfs(j) 
                ans = max(ans, arrs)

            memo[i] = ans
            return memo[i]
            
        return dfs(0)