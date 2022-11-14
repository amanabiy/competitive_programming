class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            if i != headID:
                graph[manager[i]].append(i)
        
        def dfs(node, timeToReach):
            
            if not graph[node]:
                return timeToReach
            
            ans = 0
            for child in graph[node]:
                ans = max(ans, dfs(child, informTime[node] + timeToReach))
            
            return ans
        
        return dfs(headID, 0)
        