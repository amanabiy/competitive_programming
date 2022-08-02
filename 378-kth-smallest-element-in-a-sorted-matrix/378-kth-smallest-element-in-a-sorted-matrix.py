class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        
        """
        row = 0
        h = 0
        inBound = lambda x, y: 0 <= x < len(matrix) and 0 <= y < len(matrix[x])
        heaps = []
        stop_flag = False


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(heaps) < k:
                    heappush(heaps, -matrix[i][j])
                elif heaps[0] < -matrix[i][j]:
                    popped = heappop(heaps)
                    heappush(heaps, -matrix[i][j])



        return -heaps[0]
                
                
            