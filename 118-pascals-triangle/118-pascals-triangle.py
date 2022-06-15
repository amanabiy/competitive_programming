class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        pascal = [[1], [1,1]]
        for i in range(1, numRows-1):
            ans = [1]
            for j in range(len(pascal[i]) -1):
                ans.append(pascal[i][j]+pascal[i][j+1])
            ans.append(1)
            pascal.append(ans)
            
        return pascal