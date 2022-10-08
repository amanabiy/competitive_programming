class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        I am going to maintain minBoard = [3][3] -> modify this to know if I have an element in that box or not
        and also I will use row and col to know if I have the number in that row or col
        
        and then bruteforce and check if i can put that number in that position
        """
        # initialize variables
        rows, cols = defaultdict(set), defaultdict(set)
        miniBoard = [ [set() for _ in range(3)] for i in range(3) ]
        
        # check if value is satisfiying the rules
        canAdd = lambda val, i, j: val not in rows[i] and val not in cols[j] and val not in miniBoard[i // 3][j // 3]

        # fill data from the board
        for i in range(len(board)):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    miniBoard[i // 3][j // 3].add(board[i][j])
        # print(rows, cols, miniBoard)
        # check if the board is complete
        def getNextEmpty(row, col):
            while board[row][col] != '.':
                col += 1
                if col == 9:
                    row += 1
                    col = 0
                if row == 9:
                    return (-1, -1)
            return (row, col)
        # def nextEmptyPos(i, j):
            
        
        def backtrack(row, col):
            r, c = getNextEmpty(row, col)
            if r == c == -1:
                return True
            
            for i in range(1, 10):
                val = str(i)

                if canAdd(val, r, c):
                    rows[r].add(val)
                    cols[c].add(val)
                    miniBoard[r // 3][c // 3].add(val)
                    board[r][c] = val
                    
                    x = backtrack(r, c)

                    if x:
                        return True

                    rows[r].remove(val)
                    cols[c].remove(val)
                    miniBoard[r // 3][c // 3].remove(val)
                    board[r][c] = '.'
                    
                    
        
        backtrack(0, 0)