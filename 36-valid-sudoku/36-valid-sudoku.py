class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [         0             1             2
            [".",".",".",  ".","5",".",  ".","1","."]
         0  [".","4",".",  "3",".",".",  ".",".","."],
            [".",".",".",  ".",".","3",  ".",".","1"],
            
            ["8",".",".",  ".",".",".",  ".","2","."],
         1  [".",".","2",  ".","7",".",  ".",".","."],
            [".","1","5",  ".",".",".",  ".",".","."],
            
            [".",".",".",  ".",".","2",  ".",".","."],
         2  [".","2",".",  "9",".",".",  ".",".","."],
            [".",".","4",  ".",".",".",  ".",".","."]
        ]
        
        I have only 3 rows so I can categorize them
        row 0 - 2 -> 0 
        row 3 - 5 -> 1
        row 6 - 8 -> 2
        
        
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                row, col = i // 3, j // 3
                if board[i][j] == '.':
                    continue
                    
                if  board[i][j] not in rows[i] \
                and board[i][j] not in cols[j] \
                and board[i][j] not in box[(row, col)]:
                
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    box[(row, col)].add(board[i][j])

                else:
                    print(i, j, board[i][j])
                    return False

        return True
                
        