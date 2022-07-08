class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0 for i in range(n)] for j in range(m)]
        board[0][0] = 1
        isValid = lambda x, y: 0 <= x < m and 0 <= y < n
        for i in range(m):
            for j in range(n):
                left = j - 1
                up = i - 1
                if isValid(i, left):
                    board[i][j] += board[i][left]
                if isValid(up, j):
                    board[i][j] += board[up][j]
        print(board[-1][-1])
        return board[-1][-1]