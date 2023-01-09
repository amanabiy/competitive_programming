class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k == 0:
            return max(vals)

        queue = deque([0])
        visited = set([0])
        graph = defaultdict(list)
        n = len(edges)
        ans = -inf

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        for node in range(len(vals)):
            valuesChild = [0]
            
            # collect childs
            for child in graph[node]:
                valuesChild.append(max(vals[child], 0))
            
            valuesChild.sort()
            ans = max(ans, sum(valuesChild[-k:]) + vals[node])
        
        return ans