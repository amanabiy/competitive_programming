class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [ [0] for i in range(len(matrix)) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.prefix_sum[i].append(self.prefix_sum[i][j] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        row = row1
        while row <= row2:
            ans += self.prefix_sum[row][col2+1] - self.prefix_sum[row][col1]
            row += 1
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)                                                                                                                                                                              