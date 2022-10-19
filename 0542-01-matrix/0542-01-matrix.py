class Solution:
    def inBound(self, n, m, row, col):
        return 0 <= row < n and 0 <= col < m
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        n, m = len(mat), len(mat[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ans = [[ inf for _ in range(m) ] for _ in range(n)]
        visited = [ [ 0 for _ in range(m) ] for _ in range(n)]

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited[row][col] = 1
        
        distance = 0
        while queue:
            
            for i in range(len(queue)):
                row, col = queue.popleft()
                ans[row][col] = distance
                
                for x, y in DIRECTIONS:
                    newR = row + x
                    newC = col + y
                    if self.inBound(n, m, newR, newC) and not visited[newR][newC]:
                        visited[newR][newC] = 1
                        queue.append((newR, newC))
            
            distance += 1
        
        return ans