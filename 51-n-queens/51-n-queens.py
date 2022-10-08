class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        
        
          0 1 2 3
        0 q     
        1   
        2   q....
        3   .   
        
        """
        ans = []
        leftDiag, rightDiag = set(), set()
        cols = set()
        
        def makeRow(col):
            row = []
            for i in range(n):
                if i == col:
                    row.append('Q')
                else:
                    row.append('.')
            return ''.join(row)
        def check(row, col):
            if row - col in leftDiag or col in cols or row + col in rightDiag:
                return False
            return True
        
        def backtrack(collected):
            if len(collected) == n:
                # print(collected)
                ans.append(collected[::])
            r = len(collected) - 1
            
            for j in range(n):
                if check(r, j):
                    collected.append(makeRow(j))
                    cols.add(j)
                    leftDiag.add(r - j)
                    rightDiag.add(r + j)
                    backtrack(collected)
                    collected.pop()
                    leftDiag.remove(r - j)
                    # print(rightDiag)
                    rightDiag.remove(r + j)
                    cols.remove(j)
            
        backtrack([])
        return ans