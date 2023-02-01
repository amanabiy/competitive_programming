class Solution:
    def getSum(self, mat, r1, r2, c1, c2):
        val = 0
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                val += mat[i][j]
        return val

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        ans = [[0] * m for _ in range(n)]        
        
        for i in range(n):
            for j in range(m):
                row1 = i - k if i - k >= 0 else 0
                row2 = i + k if i + k < n else n - 1
                col1 = j - k if j - k >= 0 else 0
                col2 = j + k if j + k < m else m - 1

                ans[i][j] = self.getSum(mat, row1, row2, col1, col2)
        
        return ans