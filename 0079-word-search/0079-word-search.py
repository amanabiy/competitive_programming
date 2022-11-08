class Solution:
    def inBound(self, row, col, n, m):
        return 0 <= row < n and 0 <= col < m

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        """
        
        def backtrack(row, col, i, visited):

            if board[row][col] != word[i] or i >= len(word):
                return False
            
            if i == len(word) - 1 and board[row][col] == word[i]:
                return True

            for x, y in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                newRow = row + x
                newCol = col + y
                
                if (newRow, newCol) in visited or not self.inBound(newRow, newCol, len(board), len(board[0])):
                    continue

                visited.add((newRow, newCol))
                if backtrack(newRow, newCol, i + 1, visited):
                    return True
                visited.remove((newRow, newCol))

            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0, {(i, j)}):
                    return True
        
        return False