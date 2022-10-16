class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """
        
            0
          3
        1 3 2
          3   4
        """
        n = len(parent)
        visited = set()
        graph = defaultdict(list)
        self.maxAns = 1

        for i in range(1, n):
            graph[parent[i]].append(i)

        def dfs(i):
            if i > len(parent):
                return 0
        
            candi = [0,0]
            for child in graph[i]:
                score = dfs(child)
                if s[i] != s[child]:
                    candi.append(score)
    
            candi.sort()
            self.maxAns = max(candi[-1] + candi[-2]+ 1, self.maxAns)
            return candi[-1] + 1
        
        dfs(0)

        return self.maxAns
            