class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        
        """
        matrix = list(zip(*matrix))
        
        for row in range(len(matrix)):
            matrix[row] = list(matrix[row])
        
        return matrix