class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [ (1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(board), len(board[0])
        if n * m < len(word):
            return False
        w = Counter(word)
        letters = defaultdict(int)
        for i in range(n):
            for j in range(m):
                if board[i][j] in w and letters[board[i][j]] < w[board[i][j]]:
                    letters[board[i][j]] += 1

        if w != letters:
            return False
        
        def isValid(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def backtrack(row, col, nextLetter, visited):
            if nextLetter >= len(word)-1:
                return True
            
            visited.add((row, col))
            for x, y in directions:
                r, c = row + x, col + y
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r, c) not in visited and word[nextLetter+1] == board[r][c]:
                    if backtrack(r, c, nextLetter + 1, visited):
                        return True
            visited.remove((row, col))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(i, j, 0, set()):
                    return True
        
        return False