class Solution:
    def isValid(self, newR, newC, n, m):
        if 0 <= newR < n and 0 <= newC < m:
            return True
        return False

    def bfs(self, start, end, forest):
        queue = deque([start])
        visited = set([start])
        steps = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(forest)
        m = len(forest[0])

        while queue:

            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == end:
                    return steps
                for x, y in directions:
                    newR = r + x
                    newC = c + y
                    if  not self.isValid(newR, newC, n, m):
                        continue
                    if (newR, newC) in visited:
                        continue
                    if forest[newR][newC] == 0:
                        continue
                    queue.append((newR, newC))
                    visited.add((newR, newC))

            steps += 1
        
        return -1
            
        
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        [
          [1,1,1],
          [0,0,4],
          [7,6,5]
        ]

        starting = (2, 2), 
        steps = 4
        [ (5, 2, 2) ]
        n**2 -> the minimum
        """
        heap = []
        steps = 0
        starting = (0, 0)
        n = len(forest)
        m = len(forest[0])

        for i in range(n):
            for j in range(m):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    heapq.heappush(heap, (forest[i][j], i, j))
        
        while heap:
            node, row, col = heapq.heappop(heap)
            stepsToReachNode = self.bfs(starting, (row, col), forest)
            if stepsToReachNode == -1:
                return -1
            steps += stepsToReachNode
            starting = (row, col)
            
        return steps
        