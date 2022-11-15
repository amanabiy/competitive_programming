class Solution:
    def isValid(self, r, c, n, m):
        return 0 <= r < n and 0 <= c < m

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        
        for i in range(n):
            for j in range(m):
                countOnes = 0
                for x, y in directions:
                    nr = i + x
                    nc = j + y
                    if self.isValid(nr, nc, n, m) and (board[nr][nc] & 1):
                        countOnes += 1

                # set the second bit to 1 for those who are alive next generation
                if (countOnes == 3 or (countOnes == 2 and board[i][j])):
                    board[i][j] |= 2

        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
