class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = [[1]]

        for i in range(1, numRows):
            ans = [1]
            for j in range(len(grid[-1]) - 1):
                ans.append(grid[-1][j] + grid[-1][j + 1])
            ans.append(1)
            grid.append(ans)
        
        return grid