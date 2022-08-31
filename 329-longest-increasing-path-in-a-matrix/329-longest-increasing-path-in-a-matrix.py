class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        indegree = [ [ 0 for i in range(len(matrix[0])) ] for _ in range(len(matrix))]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        isValid = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[r])
        maxLength = [ [ 1 for i in range(len(matrix[0])) ] for _ in range(len(matrix))]
        graph = defaultdict(list)
        queue = deque()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for x, y in directions:
                    newR, newC = x + i, y + j
                    if isValid(newR, newC) and matrix[newR][newC] > matrix[i][j]:
                        graph[(i, j)].append((newR, newC))
                        indegree[newR][newC] += 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            
            for newR, newC in graph[(row, col)]:
                indegree[newR][newC] -= 1                    
                if matrix[newR][newC] > matrix[row][col]:
                    maxLength[newR][newC] = max(maxLength[newR][newC], 1 + maxLength[row][col])

                if indegree[newR][newC] == 0:
                    queue.append([newR, newC])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans = max(ans, maxLength[i][j])

        return ans
        
                    
            
            