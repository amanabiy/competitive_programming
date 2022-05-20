class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        memo = {}
        isValid = lambda x, y: 0<=x<len(obstacleGrid) and 0<= y < len(obstacleGrid[0])
        visited = set()
        
        def dfs(i, j):
            # if obstacleGrid
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                if obstacleGrid[i][j] == 0:
                    return 1
                return 0
            if (i, j) in memo:
                return memo[(i,j)]
            visited.add((i, j))
            answer = [0]
            
            for x, y in [(0,1),(1,0)]:
                r, c = x + i, y + j
                if isValid(r, c) and (r, c) not in visited:
                    if obstacleGrid[r][c] == 0:
                        answer.append(dfs(r, c))
            
            memo[(i,j)] = sum(answer)
            visited.remove((i,j))
            return memo[(i,j)]
        
        return dfs(0,0) if obstacleGrid[0][0] == 0 else 0