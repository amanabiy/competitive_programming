class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        
        """
        twos = colsum.count(2)
        if upper + lower != sum(colsum) or twos > upper or twos > lower:
            return []

        ans = [[0 for i in range(len(colsum))], [0 for i in range(len(colsum))]]

        for i in range(len(colsum)):
            if colsum[i] == 2:
                ans[0][i], ans[1][i] = 1, 1
                upper -= 1
                lower -= 1
                                                                  
                                                                  
        for i in range(len(colsum)):
            if ans[0][i] == ans[1][i] == 1:
                continue

            if upper > 0 and colsum[i] == 1:
                ans[0][i] = 1
                colsum[i] -= 1
                upper -= 1
            else:
                ans[0][i] = 0

            if colsum[i] > 0 and lower > 0:
                ans[1][i] = 1
                colsum[i] -= 1
                lower -= 1
            else:
                ans[1][i] = 0

        
        return ans    