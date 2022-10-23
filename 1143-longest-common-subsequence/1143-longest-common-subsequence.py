class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
           b  l
        y  0  0
        b  0
        y     1
        """
        
        memo = [ [ 0 for _ in range(len(text2) + 1) ] for _ in range(len(text1) + 1) ]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                memo[i + 1][j] = max(memo[i + 1][j], memo[i][j])
                memo[i][j + 1] = max(memo[i][j + 1], memo[i][j])
                val = memo[i][j]
                if text1[i] == text2[j]:
                    val = memo[i][j] + 1
                memo[i + 1][j + 1] = max(val, memo[i + 1][j + 1], memo[i + 1][j], memo[i][j + 1])

        return memo[-1][-1]