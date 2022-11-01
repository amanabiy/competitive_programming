class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    isShip = True
                    if i - 1 >= 0:
                        isShip = isShip and board[i - 1][j] != 'X'
                    if j - 1 >= 0:
                        isShip = isShip and board[i][j - 1] != 'X'
                    count += isShip
        
        return count
                    