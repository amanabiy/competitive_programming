class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        m, s = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,1), (1,-1), (-1,1), (-1,-1),(-1,0), (0,-1), (1,0), (0, 1)]
        isValid = lambda x, y: 0 <= x < m  and 0 <= y < s
        distance = 0
        ans = -1

        if grid[0][0] == 0:
            queue.append((0,0))
            visited.add((0,0))
            
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node[0] == m -1 and node[1] == s -1:
                    ans = distance + 1
                    break
                for x, y in directions:
                    r, c = node[0] + x, node[1] + y
                    if isValid(r,c) and (r, c) not in visited and grid[r][c] == 0:
                        queue.append((r, c))
                        visited.add((r, c))
            distance += 1
        
        return ans