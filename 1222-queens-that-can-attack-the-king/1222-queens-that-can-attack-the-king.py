class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        directions = [(1,0), (0,1), (0,-1), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
        isValid = lambda r, c: 0 <= r < 8 and 0 <= c < 8
        queens = set([tuple(item) for item in queens])
        ans = []
        
        for x, y in directions:
            nr, nc = king
            while (nr, nc) not in queens and isValid(nr, nc):
                nr, nc = nr + x, nc + y
            if isValid(nr, nc):
                ans.append([nr, nc])
        
        return ans
                