class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """

        i, j ->
        n -> 
        newRow = i + n
        newCol = j + n
        
        topPartToRemove = [i - 1][j + n]
        leftPartToRemove = [i + n][j - 1]
        commonPart = [i - 1][j - 1]
        
       
        
         6 - 2 = 
        
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1] + matrix[i][j]
        
        
        ((n * m) * min(m, n) - 1) * n
        
        Time: ((n * m) * min(m, n))
        Space: (n * m)
        
        maxSquareArea = 1
        
         a valid square has only 1's and width == height and inBound
         [
             ["1","0","1","0","0"],
             ["1","0","1","1","1"],
             ["1","1","1","1","1"],
             ["1","0","0","1","0"],
         ]
         
        """
        n = len(matrix)
        m = len(matrix[0])
        maxSquareArea = 0
        
        dp = [ [0] * (m + 1) for _ in range(n + 1) ]
        
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    minnSize = min(dp[i][j + 1], dp[i + 1][j])
                    dp[i + 1][j + 1] = (sqrt(min(dp[i][j], minnSize)) + 1) ** 2
                    

        return int(max([ max(row) for row in dp]))
                    
                    
            