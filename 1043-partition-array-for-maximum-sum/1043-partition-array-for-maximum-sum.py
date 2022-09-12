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
        
        memo = [0] * (len(arr) + 1)

        for i in range(1, len(arr) + 1):
            for j in range(1, k + 1):
                if i - j < 0:
                    break
                sliced = arr[i - j: i] 
                curr_max = max(sliced)
                memo[i] = max(memo[i], memo[i - j] + curr_max * j)
            
        return memo[-1]