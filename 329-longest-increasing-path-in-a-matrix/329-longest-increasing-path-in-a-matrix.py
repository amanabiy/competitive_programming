class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        isValid = lambda x,y: 0 <= x < n and 0<= y < m
        visited = set()
        memo = {}
        answer = 0
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            visited.add((i, j))
            ans = [0]
            for x, y in directions:
                r, c = i + x, y + j
                if isValid(r, c) and matrix[i][j] < matrix[r][c]:
                    ans.append(dfs(r, c))
            memo[(i,j)] = max(ans) + 1
            return memo[(i, j)]
        
        for i in range(n):
            for j in range(m):
                answer = max(answer, dfs(i, j))
        return answer
            